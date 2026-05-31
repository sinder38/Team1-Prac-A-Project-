from __future__ import annotations
import re
from . import almanac_agent, llm_agent, macro_agent, technical_agent
from .base import Rule
from typing import Callable, List, Optional
from dataclasses import dataclass, field


@dataclass
class AgentSpec:
    rules: List[Rule]
    # If set, the file is split into named blocks before validation.
    # Returns list of (block_label, lines) pairs.
    split_blocks: Optional[Callable[[List[str]], List[tuple]]] = None


def _split_technical_blocks(lines: List[str]) -> List[tuple]:
    """
    Split a technical_agent file on '---' separators.
    Each block starting with 'INSTRUMENT:' is returned as
    (instrument_name, block_lines).  The file header (before the first
    INSTRUMENT line) is prepended to every block so title/date checks pass.
    """
    # Collect the preamble (title + any prose before the first instrument block)
    preamble: List[str] = []
    blocks: List[tuple] = []
    current_label: Optional[str] = None
    current_lines: List[str] = []
    in_block = False

    for line in lines:
        if re.match(r"^---\s*$", line):
            if in_block and current_label:
                blocks.append((current_label, list(current_lines)))
            current_label = None
            current_lines = []
            in_block = False
            continue

        instrument_match = re.match(r"^INSTRUMENT:\s*(.+)", line)
        if instrument_match:
            if in_block and current_label:
                blocks.append((current_label, list(current_lines)))
            current_label = instrument_match.group(1).strip()
            current_lines = preamble + [line]
            in_block = True
            continue

        if in_block:
            current_lines.append(line)
        else:
            preamble.append(line)

    if in_block and current_label:
        blocks.append((current_label, list(current_lines)))

    # If no separators found, treat the whole file as one unnamed block
    if not blocks:
        return [("(single block)", lines)]

    return blocks


REGISTRY: dict[str, AgentSpec] = {
    "almanac_agent": AgentSpec(rules=almanac_agent.RULES),
    "llm_agent":     AgentSpec(rules=llm_agent.RULES),
    "macro_agent":   AgentSpec(rules=macro_agent.RULES),
    "technical_agent": AgentSpec(
        rules=technical_agent.RULES,
        split_blocks=_split_technical_blocks,
    ),
}
