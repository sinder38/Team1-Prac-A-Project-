"""
Rules for llm_agent output format.

Format reference: data/formats/llm_agent.md
This file is a prompt template — these rules validate the LLM *response*,
i.e. what the LLM produces when given that prompt. The required output
structure is numbered 1–8 as defined in the template.
"""

import re
from typing import List

from .base import BulletRange, FieldValue, Rule

REGIME_VALUES = {"BULLISH", "BEARISH", "NEUTRAL", "UNCERTAIN"}
CONFIDENCE_VALUES = {"LOW", "MEDIUM", "HIGH"}

# e.g. "+1.2% to +3.4%" or "-0.5% to +1.0%"
PCT_RANGE_PATTERN = re.compile(r"\[?[+\-]\d+\.\d+%\s+to\s+[+\-]\d+\.\d+%\]?")


RULES: List[Rule] = [
    # ── Item 1: Weekly Regime ─────────────────────────────────────────────
    FieldValue(
        name="1. Weekly Regime",
        pattern=re.compile(
            r"^1\.\s+Weekly Regime:\s+(?P<val>Bullish|Bearish|Neutral|Uncertain)",
            re.IGNORECASE,
        ),
        required=True,
        value_validator=lambda m: m.group("val").upper() in REGIME_VALUES,
        value_hint=f"must be one of: {', '.join(sorted(REGIME_VALUES))}",
    ),
    # ── Item 2: Confidence Score ──────────────────────────────────────────
    FieldValue(
        name="2. Confidence Score",
        pattern=re.compile(
            r"^2\.\s+Confidence Score:\s+(?P<val>Low|Medium|High)",
            re.IGNORECASE,
        ),
        required=True,
        value_validator=lambda m: m.group("val").upper() in CONFIDENCE_VALUES,
        value_hint=f"must be one of: {', '.join(sorted(CONFIDENCE_VALUES))}",
    ),
    # ── Item 3: Key Supporting Evidence (≤3 points) ───────────────────────
    FieldValue(
        name="3. Key Supporting Evidence header",
        pattern=re.compile(r"^3\.\s+Key Supporting Evidence:"),
        required=True,
    ),
    BulletRange(
        name="3. Key Supporting Evidence — 1 to 3 bullets",
        section_header=re.compile(r"^3\.\s+Key Supporting Evidence:"),
        bullet_pattern=re.compile(r"^\s*[-·•]\s+\S"),
        min_count=1,
        max_count=3,
        required=True,
    ),
    # ── Item 4: Key Contradictions (≤2 points) ───────────────────────────
    FieldValue(
        name="4. Key Contradictions header",
        pattern=re.compile(r"^4\.\s+Key Contradictions:"),
        required=True,
    ),
    BulletRange(
        name="4. Key Contradictions — 1 to 2 bullets",
        section_header=re.compile(r"^4\.\s+Key Contradictions:"),
        bullet_pattern=re.compile(r"^\s*[-·•]\s+\S"),
        min_count=1,
        max_count=2,
        required=True,
    ),
    # ── Item 5: Invalidation Conditions ──────────────────────────────────
    FieldValue(
        name="5. Invalidation Conditions",
        pattern=re.compile(r"^5\.\s+Invalidation Conditions?:\s+\S"),
        label_pattern=re.compile(r"^5\.\s+Invalidation Conditions?:\s*$"),
        required=True,
    ),
    # ── Item 6: Predicted % moves ─────────────────────────────────────────
    FieldValue(
        name="6. Predicted % move — SPX",
        pattern=re.compile(
            r"^6\.\s+Predicted %\s*move\s*[—-]\s*SPX.*" + PCT_RANGE_PATTERN.pattern,
        ),
        required=True,
    ),
    FieldValue(
        name="6. Predicted % move — NDX",
        pattern=re.compile(
            r"^\s+Predicted %\s*move\s*[—-]\s*NDX.*" + PCT_RANGE_PATTERN.pattern,
        ),
        required=True,
    ),
    FieldValue(
        name="6. Predicted % move — IWM",
        pattern=re.compile(
            r"^\s+Predicted %\s*move\s*[—-]\s*IWM.*" + PCT_RANGE_PATTERN.pattern,
        ),
        required=True,
    ),
    # ── Item 7: Plain-English brief ───────────────────────────────────────
    FieldValue(
        name="7. Plain-English brief header",
        pattern=re.compile(r"^7\.\s+Plain-English brief:"),
        required=True,
    ),
    # ── Item 8: Disclaimer ────────────────────────────────────────────────
    FieldValue(
        name="8. Disclaimer",
        pattern=re.compile(r"^8\.\s+Disclaimer:", re.IGNORECASE),
        required=True,
    ),
]
