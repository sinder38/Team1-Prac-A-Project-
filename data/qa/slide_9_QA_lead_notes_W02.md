# Slide 9 - R10 QA Lead

Use this content for the R10 / QA Lead slide in Canva.

## Slide title

R10 QA Lead: Calibration, LLM Horse Race, and Next Sprint Change

## Slide bullets

- Direction result: SPX, NDX, and IWM were all Up; team recorded Up for all three.
- Conservative calibration score: +3 / +9 because confidence levels and percentage ranges are not auditable on `main`.
- LLM horse race: not scoreable this sprint because raw LLM outputs were not committed to `main`.
- QA finding: actuals, evidence screenshots, and technical charts exist; prediction file, LLM outputs, and Human Score are the main missing artifacts.
- Next sprint change: introduce a mandatory R10 QA gate before release/tagging.

## Speaker notes

As QA Lead, my job is to check whether our sprint evidence can be audited, not just whether the market call was right.

For Week 2, our actuals file shows that the team recorded Up predictions for SPX, NDX, and IWM. The actual results were SPX +1.40%, NDX +2.86%, and IWM +1.82%, so the directional result is 3 out of 3.

However, I am using a conservative calibration score of +3 out of +9. The reason is that the locked prediction file with confidence levels and percentage ranges is not currently present on main. Without that file, we should not claim Medium or High confidence after knowing the result.

The LLM horse race is also not scoreable this sprint because the raw model outputs are not committed. Next sprint, each model must have a saved output with SPX direction, range, confidence, and reasoning.

The main learning is that being correct is not enough. We need a clean evidence trail. Next sprint, I will run a QA gate before submission: no final release until the prediction file, LLM outputs, Human Score, actuals, calibration log, and learning log are all present.
