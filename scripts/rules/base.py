"""
Rule primitives used by all agent rule files.

Each Rule subclass implements check(lines) -> list[Finding].
A Finding is a (severity, rule_name, line_number, message) tuple.
line_number is 1-based; 0 means "not found / no specific line".
"""

from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Pattern, Tuple

Severity = str  # "FAIL" | "WARN"
Finding = Tuple[Severity, str, int, str]


@dataclass
class Rule:
    name: str
    required: bool = True

    def check(self, lines: List[str]) -> List[Finding]:
        raise NotImplementedError


# ── helpers ───────────────────────────────────────────────────────────────────

def _find_section_start(lines: List[str], header: Pattern) -> int:
    """Return 0-based index of the line matching header, or -1."""
    for i, line in enumerate(lines):
        if header.match(line):
            return i
    return -1


# Matches lines that open a new top-level section, e.g.:
#   "FED & RATES (..."  "COMMODITIES & DOLLAR ("  "MACRO BIAS:"  "1. Weekly Regime:"
# Explicitly excludes lines starting with bullet characters (-, ·, •).
_SECTION_HEADER_RE = re.compile(
    r"^(?![·\-•])(?:[A-Z0-9][A-Z0-9 &/\-]*[:(\d]|[1-9]\.\s)"
)


def _section_lines(lines: List[str], start: int) -> List[Tuple[int, str]]:
    """
    Return (1-based line number, text) pairs belonging to the section
    that starts at `start`.

    A section ends when a new top-level section header is encountered.
    Blank lines and continuation lines (prose that follows a bullet) are
    included so that multi-line field values don't prematurely close a
    section.
    """
    result = []
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if line.strip() == "":
            continue
        # Only break on lines that look like a new section header —
        # ALL-CAPS label or numbered item — not on arbitrary prose.
        if _SECTION_HEADER_RE.match(line):
            break
        result.append((i + 1, line))
    return result


# ── rule types ────────────────────────────────────────────────────────────────

@dataclass
class LineMatch(Rule):
    """The very first line must match `pattern`."""
    pattern: Pattern = field(default=None)
    line_hint: str = "Line 1"

    def check(self, lines: List[str]) -> List[Finding]:
        if not lines:
            return [("FAIL", self.name, 0, "file is empty")]
        if self.pattern.match(lines[0]):
            return []
        sev = "FAIL" if self.required else "WARN"
        return [(sev, self.name, 1, f"line 1 does not match expected pattern")]


@dataclass
class FieldValue(Rule):
    """
    At least one line in the file must match `pattern`.

    If `label_pattern` is also provided, a line matching `label_pattern`
    (the bare label, e.g. "^INVALIDATION:") followed by a non-blank
    continuation line also satisfies the check — accommodating values
    written on the next line.

    Optionally, the match object is passed to `value_validator`; if it
    returns False the check fails with `value_hint`.
    """
    pattern: Pattern = field(default=None)
    label_pattern: Optional[Pattern] = None
    value_validator: Optional[Callable] = None
    value_hint: str = ""

    def check(self, lines: List[str]) -> List[Finding]:
        sev = "FAIL" if self.required else "WARN"
        for i, line in enumerate(lines, start=1):
            m = self.pattern.match(line)
            if m:
                if self.value_validator and not self.value_validator(m):
                    return [(sev, self.name, i,
                             f"value invalid — {self.value_hint}: got {line.rstrip()}")]
                return []
            if self.label_pattern and self.label_pattern.match(line):
                # label-only line — check that the next non-blank line has content
                for next_line in lines[i:]:
                    if next_line.strip():
                        return []
        return [(sev, self.name, 0, "not found in output")]


@dataclass
class SectionPresent(Rule):
    """A section header line must exist somewhere in the file."""
    header: Pattern = field(default=None)

    def check(self, lines: List[str]) -> List[Finding]:
        sev = "FAIL" if self.required else "WARN"
        idx = _find_section_start(lines, self.header)
        if idx == -1:
            return [(sev, self.name, 0, "section header not found")]
        return []


@dataclass
class BulletCount(Rule):
    """
    Within a section, exactly `min_count`..`max_count` lines must match
    `bullet_pattern`.  max_count=None means no upper limit.
    """
    section_header: Pattern = field(default=None)
    bullet_pattern: Pattern = field(default=None)
    min_count: int = 1
    max_count: Optional[int] = None

    def check(self, lines: List[str]) -> List[Finding]:
        sev = "FAIL" if self.required else "WARN"
        start = _find_section_start(lines, self.section_header)
        if start == -1:
            return [(sev, self.name, 0, "parent section not found")]

        section = _section_lines(lines, start)
        matches = [(ln, txt) for ln, txt in section if self.bullet_pattern.match(txt)]
        count = len(matches)

        if count < self.min_count:
            return [(sev, self.name, start + 1,
                     f"expected ≥{self.min_count} matching bullet(s), found {count}")]
        if self.max_count is not None and count > self.max_count:
            first_extra_ln = matches[self.max_count][0]
            return [(sev, self.name, first_extra_ln,
                     f"expected ≤{self.max_count} matching bullet(s), found {count}")]
        return []


@dataclass
class BulletRange(Rule):
    """
    Alias of BulletCount with clearer intent for min/max range checks.
    Raises FAIL when count is outside [min_count, max_count].
    """
    section_header: Pattern = field(default=None)
    bullet_pattern: Pattern = field(default=None)
    min_count: int = 0
    max_count: Optional[int] = None

    def check(self, lines: List[str]) -> List[Finding]:
        sev = "FAIL" if self.required else "WARN"
        start = _find_section_start(lines, self.section_header)
        if start == -1:
            # If min_count is 0 the section might legitimately be absent
            if self.min_count == 0:
                return []
            return [(sev, self.name, 0, "parent section not found")]

        section = _section_lines(lines, start)
        matches = [(ln, txt) for ln, txt in section if self.bullet_pattern.match(txt)]
        count = len(matches)

        findings = []
        if count < self.min_count:
            findings.append((sev, self.name, start + 1,
                             f"expected ≥{self.min_count} entries, found {count}"))
        if self.max_count is not None and count > self.max_count:
            first_extra_ln = matches[self.max_count][0]
            findings.append((sev, self.name, first_extra_ln,
                             f"expected ≤{self.max_count} entries, found {count} "
                             f"(first excess at line {first_extra_ln})"))
        return findings
