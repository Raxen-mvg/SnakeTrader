# Paper trading report

Updated 2026-11-06 14:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,707 | +8.35% | 0 | - | 237 |
| unified | 214,998 | +7.50% | 0 | - | 236 |
| intraweek | 209,299 | +4.65% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,639 | +4.32% | 1 | 100% | 255 |
| snake_abs_exit | 208,559 | +4.28% | 1 | 100% | 260 |
| intramonth | 207,249 | +3.62% | 0 | - | 235 |
| snake_abs | 205,625 | +2.81% | 1 | 100% | 255 |
| snake_abs_conv | 205,440 | +2.72% | 1 | 100% | 255 |
| oracle | 205,253 | +2.63% | 0 | - | 233 |
| random_hold | 203,402 | +1.70% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,094 | -1.95% | 4 | 25% | 842 |
| snake_anaconda | 195,998 | -2.00% | 3 | 33% | 374 |
| benchmark_smallcap | 195,773 | -2.11% | 0 | - | 237 |
| snake_viper_tick | 192,766 | -3.62% | 3 | 0% | 672 |
| gold | 191,607 | -4.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,092 (-6.45%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,938 | +1.37% |
| oracle | +1,181 | +0.58% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -119 | -0.06% |
| intramonth | -700 | -0.34% |
| random_hold | -922 | -0.45% |
| unified | -985 | -0.46% |
| gold | -2,614 | -1.35% |
| benchmark_smallcap | -2,915 | -1.47% |
| snake_abs | -6,064 | -2.86% |
| snake_abs_exit | -6,099 | -2.84% |
| snake_abs_conv | -6,105 | -2.89% |
| snake_abs_exit_conv | -6,164 | -2.87% |
| snake_anaconda | -6,481 | -3.20% |
| snake_viper_tick | -8,372 | -4.16% |
| snake_viper_wild | -8,561 | -4.18% |

Average per day so far: benchmark Rs +576, unified Rs +517, snake_abs_exit_conv Rs +332, snake_abs_exit Rs +329, intraweek Rs +321, intramonth Rs +250, snake_abs_conv Rs +209, snake_abs Rs +208, oracle Rs +181, random_hold Rs +117, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -167, benchmark_smallcap Rs -169, snake_viper_wild Rs -186, gold Rs -289, snake_viper_tick Rs -402, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.