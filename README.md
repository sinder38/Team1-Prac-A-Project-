# CP3405 Design Thinking 3: Market Intelligence — Team 1

**A 10-week sprint exercise in structured market analysis, AI collaboration, and calibrated prediction.**

---

## Project Overview

This is Team 1's repository for CP3405 Design Thinking 3 (DT3), an educational market intelligence sprint taught by Prof. Dr. Tan at TR2 2026 (Singapore). Each week, our team:

1. **Reads real market data** — S&P 500, Nasdaq 100, Russell 2000, and 8 macro assets
2. **Builds structured analysis** — Almanac (seasonal), Macro (fundamentals), and Technical (chart) agents
3. **Queries four AI models** — Claude, ChatGPT, Gemini, DeepSeek with identical prompts
4. **Applies human judgment** — Our team's reasoning overrides or validates AI consensus
5. **Makes a prediction** — SPX, NDX, IWM direction + % range + confidence level
6. **Measures calibration** — Were we right *and* confident, or wrong *but* honest about uncertainty?

By Week 10, we will have a 10-sprint track record of predictions vs. actuals, a public GitHub history showing our reasoning, and a live web application ([IRIS 2.0](#iris-20-the-product)) that any user can access to see our analysis.

---

## The Nine Tracked Assets

| Asset | Ticker | Why We Track It |
|-------|--------|-----------------|
| **S&P 500** | SPX | The benchmark. 500 largest US companies. |
| **Nasdaq 100** | NDX | Tech-heavy. Fastest-moving index. |
| **Russell 2000** | IWM | Small caps. Most rate-sensitive. |
| **Gold** | GC | Safe haven. Inflation & fear gauge. |
| **Crude Oil** | CL | Inflation driver. Geopolitical signal. |
| **10-Year Treasury Yield** | ZN | The gravity on all asset valuations. |
| **US Bonds** | TLT | Stocks + bonds both down = fear signal. |
| **VIX** | VIX | Volatility index. Fear measure. 15 = calm, 30+ = panic. |
| **Bitcoin** | BTC | Risk appetite proxy. 24/7 trading. |

---

## The Three-Agent Framework

### 1. **Almanac Agent** (R3)
Seasonal patterns from 75 years of market history. This week's month rank, day-of-week effects, sector seasonality, and presidential cycle context. Confidence is deliberately lower than charts because patterns break.

### 2. **Macro Agent** (R4)
The fundamental drivers: Fed rate probabilities, yield curve, dollar, oil, economic calendar surprises, confirmed news events. Separated into three layers — confirmed facts, market expectations, and our interpretation.

### 3. **Technical Agent** (R5)
Chart reading: 8-day EMA, 21-day EMA, trendlines, support/resistance levels. Specific invalidation levels. No vague calls like "looks bullish" — only measured statements like "bullish while above 7,350."

---

## Multi-LLM Synthesis

After the three agents are built, we paste them into an identical prompt and query all four models:

- **Claude** — Anthropic
- **ChatGPT** — OpenAI
- **Gemini** — Google
- **DeepSeek** — DeepSeek

We save all four raw responses and fill a comparison table:
- Where do they agree? (high confidence)
- Where do they diverge? (flag as uncertainty)
- Which model's reasoning is strongest this week?

---


## The Ten Scrum Roles

| Role | Responsibility | GitHub Artifact |
|------|-----------------|-----------------|
| **R1 — Product Owner** | Sprint goal. Definition of done. | `sprint_goal_WXX.md` |
| **R2 — Scrum Master** | Stand-ups. Retrospective. Blockers. | `retrospective_WXX.md` |
| **R3 — Almanac Agent Lead** | Seasonal pattern analysis. | `data/almanac/almanac_agent_WXX.md` |
| **R4 — Macro Agent Lead** | Fed, rates, oil, calendar. | `data/macro/macro_agent_WXX.md` |
| **R5 — Technical Agent Lead** | Charts. EMA zones. Key levels. | `data/technical/technical_agent_WXX.md` + charts/ |
| **R6 — LLM Synthesis Operator** | Query all four models. Comparison table. | `data/synthesis/synthesis_*_WXX.txt` |
| **R7 — Human Score Analyst** | Five-dimension scoring. Override paragraph. Final prediction. | `data/synthesis/human_score_WXX.md` |
| **R8 — Data & Evidence Lead** | Data sourcing. Screenshots. Actuals recording. | `data/evidence/` folder |
| **R9 — GitHub & Integration Lead** | Repository organization. Commits. Release tags. | All files merged + README updated |
| **R10 — QA & Learning Log Lead** | Calibration scoring. LLM horse race. Learning log. | `calibration_log.md`, `learning_log_WXX.md` |

---

## Repository Structure
May be not up to date

```
team1-prac-a-project/
├── README.md                          # This file
├── CONTRIBUTING.md                    # Git workflow & coding standards
│
├── /sprints/                          # Sprint metadata
│   ├── sprint_goal_W2.md
│   ├── acceptance_criteria_W2.md
│   └── retrospective_W2.md (after sprint closes)
│
├── /data/
│   ├── /evidence/                     # Data & screenshots 
│   ├── /almanac/                      # Seasonal analysis
│   │   └── almanac_agent_W2.md        # Week 2 output
│   ├── /macro/                        # Fundamental analysis
│   │   └── macro_agent_W2.md          # Week 2 output
│   ├── /technical/                    # Chart analysis
│   │   ├── technical_agent_W2.md      # Week 2 output
│   │   └── charts/
│   │       └── (annotated screenshots)
│   ├── /formats/                      # Formats for each agent
│
└── /presentations/                    # Class presentations
```

---

## The Monday Presentation (20–25 minutes)

**Every role holder speaks.** No silent passengers.

| Time | Role | Content |
|------|------|---------|
| 0:00–1:30 | R1 Product Owner | Sprint goal + last week's calibration score |
| 1:30–3:00 | R8 Data Lead | Week 1 actuals: what we predicted vs. what happened |
| 3:00–5:00 | R3 Almanac Lead | This week's seasonal context & bias |
| 5:00–7:00 | R4 Macro Lead | This week's single most important event |
| 7:00–9:00 | R5 Technical Lead | **Live chart demo** — annotated S&P 500 screenshot |
| 9:00–11:00 | R6 LLM Operator | AI comparison table — where models agreed & diverged |
| 11:00–15:00 | **R7 Human Score** (★ most important) | **Our thinking** — the wild card insight no AI raised |
| 15:00–17:00 | R9 GitHub Lead | Live GitHub repo — commits, evidence, release tag |
| 17:00–19:00 | R10 QA Lead | Calibration score update + LLM horse race + one change for next sprint |

---

## Resources & References

### Official Course Materials
- **Task Brief:** [DT3 Market Intelligence](https://dt3-tr2-26-market-intelligence.pages.dev/)
- **Discord:** [CP3405 Server](https://discord.com/channels/1505861202444816455/1505883026771677366)
- **Professor:** Dr. Tan · TR2 2026 Singapore

### Essential Bookmarks
1. [Finviz Futures Performance](https://finviz.com/futures_performance.ashx) — All 9 assets, 1W view
2. [Yahoo Finance Sectors](https://finance.yahoo.com/sectors/) — 11 sectors, 5D view
3. [TradingEconomics Calendar](https://tradingeconomics.com/calendar) — Week-ahead events
4. [CME FedWatch Tool](https://cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html) — Fed rate probabilities
5. [Stock Trader's Almanac 2026](file:///example) — Seasonal patterns (PDF)

---

## Contributing Guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Git workflow (feature branches, PRs, reviews)
- Commit message format
- Code style conventions
- Issue & task management

**Key rule:** All changes to `main` require a pull request. No direct pushes.
