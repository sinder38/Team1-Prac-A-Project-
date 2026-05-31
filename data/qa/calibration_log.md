# Calibration Log - Week 2

Role: R10 QA and Learning Log Lead  
Checked by: QA Lead  
Date checked: 31 May 2026  
Main evidence file: `data/evidence/actuals_W2.md`

## Why I am scoring it this way

The teacher's scoring table gives different points depending on confidence:

| Confidence | Direction correct? | Score |
| --- | --- | ---: |
| High | Correct | +3 |
| Medium | Correct | +2 |
| Low / Uncertain | Correct | +1 |
| High | Wrong | -2 |
| Medium | Wrong | 0 |
| Low / Uncertain | Wrong | +1 |

I found the actual results in the repo. At the time of this QA check, the available GitHub evidence also showed the team direction as Up for SPX, NDX, and IWM. However, I could not find the locked prediction file with the original confidence levels and percentage ranges. Because of that, I should not claim High or Medium confidence after the result is already known. I am using the lowest score bucket as a safe QA decision.

## Current Week 2 score

| Asset | Team direction available during QA check | Actual result | Direction result | Confidence proof found? | Score used |
| --- | --- | ---: | --- | --- | ---: |
| SPX | Up | +1.40% | Hit | No | +1 |
| NDX | Up | +2.86% | Hit | No | +1 |
| IWM | Up | +1.82% | Hit | No | +1 |

## Result

Direction result: 3 / 3  
Conservative calibration score: +3 / +9

## QA note

This score can change only if the team finds a prediction file that was committed before the deadline and clearly shows:

- SPX, NDX, and IWM direction,
- percentage range,
- confidence level.

Until then, I will present the score as a conservative QA score, not a full final score.
