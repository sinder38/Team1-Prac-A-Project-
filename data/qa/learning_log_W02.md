# Learning Log - Week 2

Role: R10 QA and Learning Log Lead  
Date checked: 31 May 2026

## What did we predict?

At the time of this QA check, I could not verify the official locked team prediction file for Week 2. Some technical notes showed bullish direction calls, but I should not treat them as the final team prediction because they are not the locked prediction file and may not use the correct pre-week data.

For R10, this means I can record the actual result, but I should not give a full calibration score yet.

## What actually happened?

Based on `data/evidence/actuals_W2.md`:

- SPX was +1.40%.
- NDX was +2.86%.
- IWM was +1.82%.
- WTI crude oil was -9.57%.
- VIX was -9.95%.
- Technology was the strongest sector at +5.89%.

If the team had a valid locked Up prediction, the direction would have been correct for SPX, NDX, and IWM. However, I cannot mark that as fully scored until the locked prediction evidence is found.

## What surprised me?

NDX was much stronger than the other two. That means the week was mainly led by technology. IWM also went up, but not as much as NDX.

The other surprise is about our process. We have some good files in GitHub, but the prediction evidence is not fully clean. I could not find the original locked prediction file with confidence and percentage range on `main`.

After the R6 LLM evidence was merged, I could compare the model ranges. DeepSeek was the closest model for SPX because its range included the actual +1.40% result and its midpoint was closest.

## What did we learn?

Being right on direction is good, but it is not enough for this assignment. We also need to prove what we predicted before the result happened. If the locked file or confidence level is missing, R10 cannot give the full calibration score properly. The LLM horse race was easier to update once the comparison table was merged, so keeping all model outputs in one clear folder helps a lot.

## What will we do differently next sprint?

Next sprint, I will add a QA check before submission. Before the team says the sprint is done, R10 should check that these files exist:

- prediction file with direction, range, and confidence,
- raw LLM outputs,
- Human Score,
- agent outputs,
- actuals file and screenshots,
- calibration log,
- learning log,
- presentation notes.

My main improvement for next sprint: no final submission until the QA checklist is complete.
