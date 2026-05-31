# Learning Log - Week 2

Role: R10 QA and Learning Log Lead  
Date checked: 31 May 2026

## What did we predict?

Based on the current R7 GitHub evidence, the team final prediction file says:

| Asset | Direction | Range | Confidence |
| --- | --- | ---: | --- |
| S&P 500 (SPX) | Up | +0.2% to +1.0% | Medium |
| Nasdaq 100 (NDX) | Up | +0.5% to +1.5% | Medium |
| Russell 2000 (IWM) | Up | 0.0% to +1.2% | Low-Medium |

The Human Score total is 0, so the team adjusted the AI consensus from bullish to neutral-bullish. The main human concern was narrow market breadth: only 57% of S&P 500 stocks were above their 200-day moving average, based on the R5 Technical Agent output.

## What actually happened?

The latest actuals file currently in the repo is `data/evidence/actuals_W2.md`. It records the market week ending Friday 29 May 2026:

- SPX was +1.40%.
- NDX was +2.86%.
- IWM was +1.82%.
- WTI crude oil was -9.57%.
- VIX was -9.95%.
- Technology was the strongest sector at +5.89%.

I am not using these actuals to score the 31 May final prediction yet, because the final prediction appears to forecast the 1-5 June market week.

## LLM horse race update

The R6 LLM comparison table is now available in `data/llm/llm_comparison_W2.md`. For SPX, ChatGPT and DeepSeek both included the actual +1.40% result inside their predicted ranges. I recorded DeepSeek as the Week 2 winner because its midpoint was closest to the actual SPX move.

## What surprised me?

NDX was much stronger than SPX and IWM. This shows that the week was mainly led by technology, not by broad strength across every part of the market.

The process also showed why clean evidence matters. The team now has stronger files than before, but R10 still needs the prediction week and actuals week to match before giving a final calibration score.

## What did we learn?

Being right on direction is useful, but it is not enough for this assignment. The team also needs to show the exact locked prediction, confidence level, and prediction week. Otherwise, QA cannot score the result fairly.

The LLM horse race was easier to update once the R6 comparison table was merged. The final prediction was also easier to check once R7 separated the Human Score and prediction file.

## What will we do differently next sprint?

Next sprint, I will do a quick QA check before the team calls the work done. I will check that these are clear:

- final prediction file,
- SPX, NDX, and IWM direction, range, and confidence,
- raw LLM outputs and comparison table,
- Human Score and override,
- actuals file and screenshots,
- calibration log and learning log.

My main improvement for next sprint is to check the prediction week before scoring anything.
