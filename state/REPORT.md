# Paper trading report

Updated 2026-11-06 14:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,876 | +8.44% | 0 | - | 237 |
| unified | 215,028 | +7.51% | 0 | - | 236 |
| snake_abs_exit_conv | 209,237 | +4.62% | 1 | 100% | 255 |
| intraweek | 209,205 | +4.60% | 25 | 48% | 2,757 |
| snake_abs_exit | 209,138 | +4.57% | 1 | 100% | 260 |
| intramonth | 207,284 | +3.64% | 0 | - | 235 |
| snake_abs | 206,214 | +3.11% | 1 | 100% | 255 |
| snake_abs_conv | 206,032 | +3.02% | 1 | 100% | 255 |
| oracle | 205,465 | +2.73% | 0 | - | 233 |
| random_hold | 203,445 | +1.72% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,582 | -1.71% | 3 | 33% | 374 |
| snake_viper_wild | 196,338 | -1.83% | 4 | 25% | 842 |
| benchmark_smallcap | 196,300 | -1.85% | 0 | - | 237 |
| snake_viper_tick | 193,009 | -3.50% | 3 | 0% | 672 |
| gold | 191,624 | -4.19% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,285 (-6.36%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,106 | +1.45% |
| oracle | +1,393 | +0.68% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -214 | -0.10% |
| intramonth | -665 | -0.32% |
| random_hold | -879 | -0.43% |
| unified | -955 | -0.44% |
| benchmark_smallcap | -2,388 | -1.20% |
| gold | -2,598 | -1.34% |
| snake_abs | -5,475 | -2.59% |
| snake_abs_conv | -5,513 | -2.61% |
| snake_abs_exit | -5,521 | -2.57% |
| snake_abs_exit_conv | -5,567 | -2.59% |
| snake_anaconda | -5,898 | -2.91% |
| snake_viper_tick | -8,129 | -4.04% |
| snake_viper_wild | -8,318 | -4.06% |

Average per day so far: benchmark Rs +582, unified Rs +518, snake_abs_exit_conv Rs +355, snake_abs_exit Rs +351, intraweek Rs +317, intramonth Rs +251, snake_abs_conv Rs +232, snake_abs Rs +230, oracle Rs +188, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -142, benchmark_smallcap Rs -148, snake_viper_wild Rs -174, gold Rs -289, snake_viper_tick Rs -388, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.