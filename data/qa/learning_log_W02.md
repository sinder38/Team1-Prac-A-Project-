# Learning Log - Week 2

Role: R10 QA and Learning Log Lead  
Date checked: 31 May 2026

## What did we predict?

At the time of this QA check, the available GitHub evidence showed the team's direction calls as:

- SPX: Up
- NDX: Up
- IWM: Up

The technical analysis was bullish for all three because the prices were above the 8 EMA and 21 EMA. The Almanac branch was more cautious, and the Macro branch looked more neutral. So the team had bullish chart evidence, but not every signal was fully bullish.

## What actually happened?

Based on `data/evidence/actuals_W2.md`:

- SPX was +1.40%.
- NDX was +2.86%.
- IWM was +1.82%.
- WTI crude oil was -9.57%.
- VIX was -9.95%.
- Technology was the strongest sector at +1.98%.

The direction call was correct for SPX, NDX, and IWM.

## What surprised me?

NDX was much stronger than the other two. That means the week was mainly led by technology. IWM also went up, but not as much as NDX.

The other surprise is about our process. We have some good files in GitHub, but the prediction evidence is not fully clean. I could see the team direction call, but I could not find the original locked prediction file with confidence and percentage range on `main`.

## What did we learn?

Being right on direction is good, but it is not enough for this assignment. We also need to prove what we predicted before the result happened. If the confidence level is missing, R10 cannot give the full calibration score properly.

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
