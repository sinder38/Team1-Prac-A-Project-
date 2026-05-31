# Learning Log - Week 2

Role: R10 QA and Learning Log Lead  
Sprint: Week 2 / 2026-W22  
Audit date: 31 May 2026

## What did we predict?

The current `data/evidence/actuals_W2.md` file records the team's direction calls as:

- SPX: Up
- NDX: Up
- IWM: Up

The team had a bullish technical picture from the Technical Agent: SPX, NDX, and IWM were all described as Zone 1 / bullish, with price above the 8 EMA and 21 EMA. The Almanac branch was more cautious, describing the seasonal bias as cautiously bearish-neutral. The Macro branch was neutral, with lower oil, lower yields, and a weaker dollar helping risk assets but payrolls still the main event.

## What actually happened?

According to `data/evidence/actuals_W2.md`:

- SPX finished +1.40%.
- NDX finished +2.86%.
- IWM finished +1.82%.
- WTI crude oil fell -9.57%.
- VIX fell -9.95%.
- Technology was the leading sector at +1.98%.

The team's recorded Up direction was correct for all three scored assets.

## What surprised us?

NDX led strongly while IWM also stayed positive. That suggests the week was not only a broad small-cap rebound; it was mainly a tech-led risk-on week. The sharp fall in oil and VIX helped the bullish outcome by reducing inflation and fear pressure.

The quality surprise was not market-related. It was process-related: several useful files exist, but the final audit trail is incomplete on `main`. The actuals file refers to predictions, but the locked prediction file with confidence levels and percentage ranges is not present. That makes the calibration score less defensible than it should be.

## What did the team learn?

Good market direction is not enough for this assignment. The grade depends on evidence discipline: the team must prove what was known before the outcome and what was recorded after the outcome. A correct prediction without a locked confidence record cannot earn full calibration credit.

## What will we do differently next sprint?

We will add an R10 QA gate before submission. Before the GitHub lead creates any release tag, R10 will check that the following are present:

- locked prediction file with SPX, NDX, and IWM direction, range, and confidence,
- raw LLM outputs and comparison table,
- Human Score with override paragraph,
- agent outputs for Almanac, Macro, and Technical,
- actuals file and evidence screenshots,
- calibration log and learning log,
- presentation slide notes.

The exact next-sprint change is: no final release until R10 marks the evidence checklist complete.
