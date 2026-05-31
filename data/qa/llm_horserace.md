# LLM Horse Race

Role: R10 QA and Learning Log Lead  
Sprint: Week 2 / 2026-W22  
Audit date: 31 May 2026

## Purpose

The LLM horse race tracks which model was closest to the actual S&P 500 weekly move across the sprint sequence. The assignment asks R10 to update this weekly so the team can learn which model is most calibrated over time.

## Week 2 status

Current status: Not scoreable from `main`

Reason: No raw LLM output files or per-model SPX forecasts were found on the current `main` branch during QA review. Without each model's predicted SPX direction and percentage range, R10 cannot fairly choose a winner.

## Required data for next sprint

Each LLM output should be committed before the final team prediction is locked.

| Model | Required forecast fields | Raw output file required |
| --- | --- | --- |
| ChatGPT | SPX direction, SPX percentage range, confidence, key reason | Yes |
| Claude | SPX direction, SPX percentage range, confidence, key reason | Yes |
| Gemini | SPX direction, SPX percentage range, confidence, key reason | Yes |
| DeepSeek | SPX direction, SPX percentage range, confidence, key reason | Yes |

## Week 2 leaderboard

| Sprint | Actual SPX weekly change | Winning model | Reason |
| --- | ---: | --- | --- |
| Week 2 / 2026-W22 | +1.40% | N/A | Raw LLM forecasts not committed, so no auditable winner |

## QA action for next sprint

R10 will not mark the LLM horse race as complete until the LLM operator commits the raw model responses and a comparison table before the final prediction is submitted.
