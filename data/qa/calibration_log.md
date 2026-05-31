# Calibration Log

Role: R10 QA and Learning Log Lead  
Sprint: Week 2 / 2026-W22  
Audit date: 31 May 2026  
Source checked: `data/evidence/actuals_W2.md`

## Scoring rule used

The assignment scores SPX, NDX, and IWM calibration by combining direction correctness with stated confidence:

| Stated confidence | Direction call | Outcome | Score |
| --- | --- | --- | --- |
| High | Up or Down | Correct | +3 |
| Medium | Up or Down | Correct | +2 |
| Low / Uncertain | Up or Down | Correct | +1 |
| High | Up or Down | Wrong | -2 |
| Medium | Up or Down | Wrong | 0 |
| Low / Uncertain | Any | Wrong | +1 |

## Week 2 scored assets

The current actuals file records the team prediction as Up for all three primary instruments. It does not include the original locked prediction file, confidence levels, or percentage ranges. Because QA cannot verify stated confidence from GitHub, this log uses the conservative Low / Uncertain scoring bucket.

| Asset | Prediction recorded in actuals | Actual weekly change | Direction result | Confidence evidence found? | R10 score |
| --- | --- | ---: | --- | --- | ---: |
| SPX | Up | +1.40% | Hit | No locked confidence found | +1 |
| NDX | Up | +2.86% | Hit | No locked confidence found | +1 |
| IWM | Up | +1.82% | Hit | No locked confidence found | +1 |

## Week 2 calibration result

Conservative audited calibration score: +3 / +9

Directional accuracy: 3 / 3 primary assets

QA note: This score should only be upgraded if the team can provide a committed prediction file from before the deadline that includes direction, percentage range, and confidence level for SPX, NDX, and IWM. Without that file, R10 should not claim Medium or High confidence after the outcome is known.

## Evidence limitation

The actuals file is useful, but it is not a complete calibration artifact by itself. For a fully auditable sprint, the repo needs both:

- the locked prediction file created before the scored period or deadline, and
- the actuals file created after Friday market close.

Next sprint, QA will require both files before calculating a final score.
