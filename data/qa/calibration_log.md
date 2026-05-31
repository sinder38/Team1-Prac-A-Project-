# Calibration Log - Week 2

Role: R10 QA and Learning Log Lead  
Checked by: QA Lead  
Date checked: 31 May 2026  
Main evidence file: `data/evidence/actuals_W2.md`

## Why I am holding the score

The teacher's scoring table gives different points depending on confidence:

| Confidence | Direction correct? | Score |
| --- | --- | ---: |
| High | Correct | +3 |
| Medium | Correct | +2 |
| Low / Uncertain | Correct | +1 |
| High | Wrong | -2 |
| Medium | Wrong | 0 |
| Low / Uncertain | Wrong | +1 |

I found the actual results in the repo. However, I could not find a valid locked prediction file that was committed before the Week 2 result was known. Some later GitHub evidence shows bullish direction calls, but I should not treat those as the official team prediction unless the locked prediction file is present.

Because of that, I am holding the final calibration score for now. I can calculate it only after the team provides the original prediction with direction, percentage range, and confidence level.

## Current Week 2 QA status

| Asset | Locked team prediction found? | Actual result | Direction result | Confidence proof found? | Score used |
| --- | --- | ---: | --- | --- | ---: |
| SPX | No | +1.40% | Not fully scoreable | No | N/A |
| NDX | No | +2.86% | Not fully scoreable | No | N/A |
| IWM | No | +1.82% | Not fully scoreable | No | N/A |

## Result

Direction result: not confirmed from a locked file  
Calibration score: pending valid locked prediction evidence

## QA note

This log can be updated if the team finds a prediction file that was committed before the deadline and clearly shows:

- SPX, NDX, and IWM direction,
- percentage range,
- confidence level.

Until then, I should present Week 2 calibration as not fully scoreable instead of giving points from evidence that may not be the locked prediction.
