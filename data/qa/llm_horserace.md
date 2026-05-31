# LLM Horse Race - Week 2

Role: R10 QA and Learning Log Lead  
Date checked: 31 May 2026

## What this file is for

The LLM horse race is meant to track which AI model was closest to the actual S&P 500 weekly move. Over the sprint weeks, this should show whether ChatGPT, Claude, Gemini, or DeepSeek gives the most useful market forecast.

## Current status

Status: Not scoreable yet

I checked the current `main` branch and I could not find the raw outputs for the four LLMs. I also could not find a comparison table showing each model's SPX forecast.

Because of that, I cannot honestly pick a winning model for Week 2.

## What is needed from the LLM operator

| Model | What I need for QA |
| --- | --- |
| ChatGPT | SPX direction, range, confidence, and reason |
| Claude | SPX direction, range, confidence, and reason |
| Gemini | SPX direction, range, confidence, and reason |
| DeepSeek | SPX direction, range, confidence, and reason |

## Week 2 record

| Sprint | Actual SPX result | Winner | Reason |
| --- | ---: | --- | --- |
| Week 2 | +1.40% | N/A | Raw LLM outputs are not in the repo yet |

## Next sprint improvement

Next sprint, the raw LLM outputs should be committed before the final prediction is locked. Then R10 can compare each model fairly.
