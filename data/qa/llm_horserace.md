# LLM Horse Race - Week 2

Role: R10 QA and Learning Log Lead  
Date checked: 31 May 2026

## What this file is for

The LLM horse race is meant to track which AI model was closest to the actual S&P 500 weekly move. Over the sprint weeks, this should show whether ChatGPT, Claude, Gemini, or DeepSeek gives the most useful market forecast.

## Current status

Status: Scoreable from merged R6 evidence

After PR #12 was merged, the current `main` branch includes raw LLM outputs and a comparison table in `data/llm/`. I used the merged R6 comparison table as the official LLM evidence for this QA check.

The actual SPX result was +1.40%. ChatGPT and DeepSeek both included +1.40% inside their predicted SPX range. I chose DeepSeek as the Week 2 winner because its range midpoint is slightly closer to the actual result.

## Week 2 comparison

| Model | SPX estimate | Compared with actual +1.40% |
| --- | ---: | --- |
| Claude | +0.3% to +1.2% | Slightly low |
| ChatGPT | +0.3% to +1.5% | Hit range |
| Gemini | +0.5% to +1.2% | Slightly low |
| DeepSeek | +0.5% to +1.5% | Hit range and closest midpoint |

## Week 2 record

| Sprint | Actual SPX result | Winner | Reason |
| --- | ---: | --- | --- |
| Week 2 | +1.40% | DeepSeek | Its SPX range included the actual result and had the closest midpoint |

## Next sprint improvement

Next sprint, the raw LLM outputs should be committed before the final prediction is locked and the comparison table should clearly state the prediction week. That will make the horse race easier to check.
