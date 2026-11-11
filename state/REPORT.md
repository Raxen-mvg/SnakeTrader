# Paper trading report

Updated 2026-11-11 12:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,647 | +10.32% | 0 | - | 237 |
| unified | 220,563 | +10.28% | 0 | - | 236 |
| snake_abs_exit_conv | 216,402 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit | 215,210 | +7.61% | 2 | 50% | 345 |
| intraweek | 214,015 | +7.01% | 30 | 53% | 3,302 |
| snake_abs | 212,810 | +6.41% | 1 | 100% | 255 |
| snake_abs_conv | 212,653 | +6.33% | 1 | 100% | 255 |
| oracle | 211,964 | +5.98% | 0 | - | 233 |
| intramonth | 211,554 | +5.78% | 0 | - | 235 |
| random_hold | 207,047 | +3.52% | 9 | 67% | 709 |
| snake_anaconda | 203,160 | +1.58% | 3 | 33% | 374 |
| snake_viper_wild | 203,146 | +1.57% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,636 | +0.82% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,687 | -0.16% | 9 | 44% | 1,639 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,312 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +5,716 | +2.90% |
| snake_viper_tick | +5,611 | +2.89% |
| snake_abs_exit_conv | +4,494 | +2.12% |
| snake_anaconda | +3,694 | +1.85% |
| benchmark_smallcap | +3,464 | +1.75% |
| snake_abs_exit | +3,226 | +1.52% |
| snake_abs_conv | +3,176 | +1.52% |
| snake_abs | +3,164 | +1.51% |
| benchmark | +2,555 | +1.17% |
| random_hold | +2,086 | +1.02% |
| oracle | +2,045 | +0.97% |
| intramonth | +944 | +0.45% |
| unified | +817 | +0.37% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -527 | -0.25% |
| gold | -2,203 | -1.15% |

Average per day so far: benchmark Rs +666, unified Rs +663, snake_abs_exit_conv Rs +586, snake_abs_exit Rs +543, intraweek Rs +452, snake_abs_conv Rs +452, snake_abs Rs +442, oracle Rs +386, intramonth Rs +373, random_hold Rs +227, snake_viper_wild Rs +137, snake_anaconda Rs +122, benchmark_smallcap Rs +61, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -16, gold Rs -325, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.