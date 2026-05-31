# R10 QA Lead - Week 2

This folder contains the R10 QA and Learning Log deliverables for Team 1A's Week 2 market intelligence sprint.

## R10 scope

- Check whether sprint evidence is present and auditable in GitHub.
- Calculate the SPX, NDX, and IWM calibration score using the published scoring table.
- Update the LLM horse race tracker.
- Record the learning log: what the team believed, what happened, what was confusing, and what changes next sprint.
- Prepare the Slide 9 content for the group presentation.

## Executive summary

- Direction result: SPX, NDX, and IWM all moved up. The existing actuals file records the team's direction prediction as Up for all three, so the directional result is 3/3.
- Conservative R10 calibration score: +3 total. Because no locked prediction file with confidence levels and percentage ranges is present on `main`, QA uses the lowest auditable confidence bucket instead of claiming Medium or High confidence.
- LLM horse race: not scoreable this sprint from the current `main` branch because raw LLM outputs and per-model SPX forecasts are not committed.
- Main quality issue: the team has useful work spread across branches, but the final evidence package is incomplete on `main`.
- Next sprint change: add a mandatory R10 QA gate before submission so prediction, confidence, LLM outputs, Human Score, actuals, and slide evidence are all checked before release.

## Files in this folder

- `calibration_log.md` - SPX, NDX, and IWM calibration record.
- `llm_horserace.md` - model comparison tracker and current scoring status.
- `learning_log_W02.md` - Week 2 learning log entry.
- `qa_checklist_W02.md` - evidence audit checklist against the assignment requirements.
- `slide_9_QA_lead_notes_W02.md` - ready-to-paste slide content and speaker notes.
