# QA Evidence Checklist - Week 2

Role: R10 QA and Learning Log Lead  
Sprint: Week 2 / 2026-W22  
Audit date: 31 May 2026

## Checklist

| Requirement | Status | Evidence / note | R10 action |
| --- | --- | --- | --- |
| README present | Done | `README.md` exists but is very brief | Add R10 links to README |
| Actuals file | Done | `data/evidence/actuals_W2.md` | Used for calibration |
| Finviz / sector evidence screenshots | Done | `data/evidence/finviz_1W_2026-W2_Sat.png.png`, `data/evidence/finviz_sectors_5D_2026_W2_Sat.png.png` | Verified file presence |
| Technical Agent output | Done | `data/charts/technical_agent_W2.md` and chart screenshots | Used in learning log |
| Almanac Agent output | In branch | `origin/almanac-agent-week-2:data/almanac/almanac_agent_W02.md` | Should be merged before final submission |
| Macro Agent output | In branch | `origin/macro-agent-week02:data/macro/macro_agent_W02.md` | Should be merged before final submission |
| Product Owner sprint goal / acceptance criteria | In branch | `origin/product-owner-week2:sprint_goal_W01.md`, `acceptance_criteria.md` | Should be merged before final submission |
| Locked prediction file | Missing on main | No file found with SPX, NDX, IWM direction, range, and confidence | Required before final calibration can be fully trusted |
| Four raw LLM outputs | Missing on main | No ChatGPT / Claude / Gemini / DeepSeek raw responses found | Horse race cannot be scored |
| LLM comparison table | Missing on main | No model comparison file found | Required from R6 |
| Human Score table and override paragraph | Missing on main | No Human Score file found | Required from R7 |
| Calibration log | Added by R10 | `data/qa/calibration_log.md` | Complete with conservative score |
| LLM horse race update | Added by R10 | `data/qa/llm_horserace.md` | Marked not scoreable due missing evidence |
| Learning log | Added by R10 | `data/qa/learning_log_W02.md` | Complete |
| Slide 9 QA notes | Added by R10 | `data/qa/slide_9_QA_lead_notes_W02.md` | Ready for Canva |
| Release tag | Not R10 job | Team Discord says tags should not be created until evidence is committed and handled by the responsible lead | R10 should only confirm readiness |
| PowerPoint / Canva slide | External | Canva link is outside GitHub at audit time | R10 slide text prepared for copying |

## QA verdict

The team has enough evidence to present a partial Week 2 QA update, but the submission is not yet a clean, fully auditable package. The biggest risks are missing prediction evidence, missing raw LLM outputs, and missing Human Score.

## Minimum fix before final submission

If time is limited, prioritize these four items:

1. Commit or locate the locked prediction file.
2. Commit raw LLM outputs or at least the comparison table.
3. Commit the Human Score table and override paragraph.
4. Merge the R3, R4, and R1 branches or reference them clearly in the final PR.
