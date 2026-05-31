# Calibration Log - Week 2

Role: R10 QA and Learning Log Lead  
Checked by: QA Lead  
Date checked: 31 May 2026

## Evidence checked

- `data/evidence/actuals_W2.md`
- `data/llm/llm_comparison_W2.md`
- `human/human_score_W2.md` from the R7 branch
- `data/final prediction/prediction_2026-W02_Team1.md` from the R7 branch

## Scoring rule

The teacher's calibration score depends on direction and confidence:

| Confidence | Direction correct? | Score |
| --- | --- | ---: |
| High | Correct | +3 |
| Medium | Correct | +2 |
| Low / Uncertain | Correct | +1 |
| High | Wrong | -2 |
| Medium | Wrong | 0 |
| Low / Uncertain | Wrong | +1 |

## Latest actuals available

From `data/evidence/actuals_W2.md`, the completed market week ended on Friday 29 May 2026:

| Asset | Actual result |
| --- | ---: |
| SPX | +1.40% |
| NDX | +2.86% |
| IWM | +1.82% |

## Prediction evidence available

The R7 branch currently has a final prediction file. It was filed on 31 May 2026 and predicts the 1-5 June market week:

| Asset | Direction | Predicted range | Confidence |
| --- | --- | ---: | --- |
| SPX | Up | +0.2% to +1.0% | Medium |
| NDX | Up | +0.5% to +1.5% | Medium |
| IWM | Up | 0.0% to +1.2% | Low-Medium |

## QA decision

I am not assigning a final calibration score yet. The actuals file currently available is for the week ending 29 May, while the latest final prediction file appears to forecast 1-5 June.

Because the prediction week and actuals week do not clearly match, scoring it now would be misleading. The right QA action is to hold calibration until the matching actual results are available.

## Current calibration status

| Asset | Prediction to track | Matching actual available? | Score |
| --- | --- | --- | ---: |
| SPX | Up, +0.2% to +1.0%, Medium confidence | No | N/A |
| NDX | Up, +0.5% to +1.5%, Medium confidence | No | N/A |
| IWM | Up, 0.0% to +1.2%, Low-Medium confidence | No | N/A |

## Result

Calibration score: pending  
Reason: the locked prediction and the available actuals do not refer to the same market week yet.

## QA note

For the next calibration update, R10 should compare the 1-5 June actual results against the locked prediction file and then apply the scoring table above.
