"""
Rules for technical_agent output format.

Format reference: data/formats/technical_agent.md
Canonical example has real data — rules are derived from that exact structure.
One output file covers one instrument; running multiple instruments means
multiple files (or extend this to support multi-instrument blocks later).
"""

import re
from typing import List

from .base import BulletCount, FieldValue, Rule, SectionPresent

CONFIDENCE_VALUES = {"LOW", "MEDIUM", "HIGH"}
# EMA zone labels from the canonical example
EMA_ZONE_PATTERN = re.compile(r"EMA condition:\s+Zone\s+\d+\s+\(", re.IGNORECASE)


RULES: List[Rule] = [
    # ── Instrument header ─────────────────────────────────────────────────
    FieldValue(
        name="Title line",
        pattern=re.compile(r"^Technical Agent Output"),
        required=True,
    ),
    FieldValue(
        name="INSTRUMENT field",
        pattern=re.compile(r"^INSTRUMENT:\s+\S"),
        required=True,
    ),
    FieldValue(
        name="LAST CLOSE field (number + date)",
        pattern=re.compile(r"^LAST CLOSE:\s+[\d,\.]+\s+\("),
        required=True,
    ),
    # ── EMA sections ──────────────────────────────────────────────────────
    SectionPresent(
        name="8 EMA vs PRICE section",
        header=re.compile(r"^8 EMA vs PRICE:"),
        required=True,
    ),
    BulletCount(
        name="8 EMA vs PRICE — ABOVE or BELOW statement",
        section_header=re.compile(r"^8 EMA vs PRICE:"),
        bullet_pattern=re.compile(r"^\s+-\s+Price is (ABOVE|BELOW) the 8 EMA"),
        min_count=1,
        max_count=1,
        required=True,
    ),
    SectionPresent(
        name="8 EMA vs 21 EMA section",
        header=re.compile(r"^8 EMA vs 21 EMA:"),
        required=True,
    ),
    BulletCount(
        name="8 EMA vs 21 EMA — ABOVE or BELOW statement",
        section_header=re.compile(r"^8 EMA vs 21 EMA:"),
        bullet_pattern=re.compile(r"^\s+-\s+8 EMA is (ABOVE|BELOW) 21 EMA"),
        min_count=1,
        max_count=1,
        required=True,
    ),
    BulletCount(
        name="8 EMA vs 21 EMA — EMA condition Zone label",
        section_header=re.compile(r"^8 EMA vs 21 EMA:"),
        bullet_pattern=re.compile(r"^\s+-\s+EMA condition:\s+Zone\s+\d+\s+\("),
        min_count=1,
        max_count=1,
        required=True,
    ),
    # ── TRENDLINE ─────────────────────────────────────────────────────────
    SectionPresent(
        name="TRENDLINE section",
        header=re.compile(r"^TRENDLINE:"),
        required=True,
    ),
    # ── KEY LEVELS ────────────────────────────────────────────────────────
    SectionPresent(
        name="KEY LEVELS section",
        header=re.compile(r"^KEY LEVELS:"),
        required=True,
    ),
    BulletCount(
        name="KEY LEVELS — Resistance 1",
        section_header=re.compile(r"^KEY LEVELS:"),
        bullet_pattern=re.compile(r"^\s+-\s+Resistance 1:"),
        min_count=1,
        max_count=1,
        required=True,
    ),
    BulletCount(
        name="KEY LEVELS — Resistance 2",
        section_header=re.compile(r"^KEY LEVELS:"),
        bullet_pattern=re.compile(r"^\s+-\s+Resistance 2:"),
        min_count=1,
        max_count=1,
        required=True,
    ),
    BulletCount(
        name="KEY LEVELS — Support 1",
        section_header=re.compile(r"^KEY LEVELS:"),
        bullet_pattern=re.compile(r"^\s+-\s+Support 1:"),
        min_count=1,
        max_count=1,
        required=True,
    ),
    BulletCount(
        name="KEY LEVELS — Support 2",
        section_header=re.compile(r"^KEY LEVELS:"),
        bullet_pattern=re.compile(r"^\s+-\s+Support 2:"),
        min_count=1,
        max_count=1,
        required=True,
    ),
    # ── BREADTH NOTE ──────────────────────────────────────────────────────
    SectionPresent(
        name="BREADTH NOTE section",
        header=re.compile(r"^BREADTH NOTE:"),
        required=True,
    ),
    # ── Closing fields ────────────────────────────────────────────────────
    FieldValue(
        name="TECHNICAL BIAS field",
        pattern=re.compile(r"^TECHNICAL BIAS:\s+\S"),
        label_pattern=re.compile(r"^TECHNICAL BIAS:\s*$"),
        required=True,
    ),
    FieldValue(
        name="CONFIDENCE field (Low/Medium/High)",
        pattern=re.compile(r"^CONFIDENCE:\s+(?P<val>Low|Medium|High)", re.IGNORECASE),
        label_pattern=re.compile(r"^CONFIDENCE:\s*$"),
        required=True,
        value_validator=lambda m: m.group("val").upper() in CONFIDENCE_VALUES,
        value_hint=f"must be one of: {', '.join(sorted(CONFIDENCE_VALUES))}",
    ),
    FieldValue(
        name="INVALIDATION field",
        pattern=re.compile(r"^INVALIDATION:\s+\S"),
        label_pattern=re.compile(r"^INVALIDATION:\s*$"),
        required=True,
    ),
    FieldValue(
        name="WATCH THIS WEEK field",
        pattern=re.compile(r"^WATCH THIS WEEK:\s+\S"),
        label_pattern=re.compile(r"^WATCH THIS WEEK:\s*$"),
        required=True,
    ),
]
