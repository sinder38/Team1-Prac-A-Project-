#!/usr/bin/env python3
"""
validate_output.py — enforce agent output formats defined in data/formats/

Usage:
  python scripts/validate_output.py <agent_type> <output_file>
  python scripts/validate_output.py --list

Exit codes:
  0  all required checks pass (warnings may be present)
  1  one or more required checks failed
  2  usage error (unknown agent type, file not found, etc.)

Examples:
  python scripts/validate_output.py almanac_agent reports/week_22.txt
  python scripts/validate_output.py technical_agent reports/spx_tech.txt
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running from the repo root without installing the package
sys.path.insert(0, str(Path(__file__).parent))

from rules import REGISTRY
from rules.base import Finding


def _supports_color() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


COLOR = _supports_color()
RED = "\033[31m" if COLOR else ""
YELLOW = "\033[33m" if COLOR else ""
GREEN = "\033[32m" if COLOR else ""
BOLD = "\033[1m" if COLOR else ""
RESET = "\033[0m" if COLOR else ""


def _sev_color(sev: str) -> str:
    return {
        "FAIL": f"{BOLD}{RED}FAIL{RESET}",
        "WARN": f"{YELLOW}WARN{RESET}",
        "PASS": f"{GREEN}PASS{RESET}",
    }.get(sev, sev)


def _format_finding(f: Finding, agent: str) -> str:
    sev, rule_name, lineno, msg = f
    location = f"line {lineno}" if lineno > 0 else "not found"
    return (
        f"  {_sev_color(sev)}"
        f"  {BOLD}{agent}{RESET} › {rule_name}"
        f"  [{location}]"
        f"\n        {msg}"
    )


def _format_pass(rule_name: str, agent: str) -> str:
    return f"  {_sev_color('PASS')}  {agent} › {rule_name}"


def validate(agent_type: str, text: str) -> list[Finding]:
    rules = REGISTRY[agent_type]
    lines = text.splitlines()
    findings: list[Finding] = []
    for rule in rules:
        findings.extend(rule.check(lines))
    return findings


def run(agent_type: str, filepath: Path, verbose: bool = False) -> int:
    if agent_type not in REGISTRY:
        known = ", ".join(sorted(REGISTRY))
        print(
            f"Error: unknown agent type '{agent_type}'. Known: {known}", file=sys.stderr
        )
        return 2

    if not filepath.exists():
        print(f"Error: file not found: {filepath}", file=sys.stderr)
        return 2

    text = filepath.read_text(encoding="utf-8")
    findings = validate(agent_type, text)

    rules = REGISTRY[agent_type]
    failed_names = {f[1] for f in findings if f[0] == "FAIL"}
    warned_names = {f[1] for f in findings if f[0] == "WARN"}

    print(f"\n{BOLD}Validating:{RESET} {filepath}  ({agent_type})\n")

    for rule in rules:
        rule_findings = [f for f in findings if f[1] == rule.name]
        if rule_findings:
            for f in rule_findings:
                print(_format_finding(f, agent_type))
        elif verbose:
            print(_format_pass(rule.name, agent_type))

    fail_count = len(failed_names)
    warn_count = len(warned_names)
    pass_count = len(rules) - len(failed_names) - len(warned_names)

    print(f"\n{'─' * 60}")
    print(
        f"  {GREEN}{pass_count} passed{RESET}"
        f"  {YELLOW}{warn_count} warnings{RESET}"
        f"  {RED}{fail_count} failed{RESET}"
        f"  ({len(rules)} rules total)"
    )

    if fail_count > 0:
        print(
            f"\n{RED}RESULT: FAIL{RESET} — {fail_count} required check(s) did not pass.\n"
        )
        return 1

    print(f"\n{GREEN}RESULT: PASS{RESET}\n")
    return 0


# ── CLI ───────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate agent output files against their format specs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "agent_type",
        nargs="?",
        help="Agent type to validate against (e.g. almanac_agent)",
    )
    parser.add_argument(
        "output_file",
        nargs="?",
        type=Path,
        help="Path to the agent output file to validate",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all known agent types and exit",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Also print passing checks",
    )

    args = parser.parse_args()

    if args.list:
        print("Known agent types:")
        for name in sorted(REGISTRY):
            rule_count = len(REGISTRY[name])
            print(f"  {name}  ({rule_count} rules)")
        sys.exit(0)

    if not args.agent_type or not args.output_file:
        parser.print_help()
        sys.exit(2)

    sys.exit(run(args.agent_type, args.output_file, verbose=args.verbose))


if __name__ == "__main__":
    main()
