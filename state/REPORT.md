# Paper trading report

Updated 2026-11-11 13:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,716 | +10.36% | 0 | - | 237 |
| unified | 220,626 | +10.31% | 0 | - | 236 |
| snake_abs_exit_conv | 218,156 | +9.08% | 2 | 50% | 345 |
| snake_abs_exit | 217,078 | +8.54% | 2 | 50% | 345 |
| snake_abs | 214,645 | +7.32% | 1 | 100% | 255 |
| snake_abs_conv | 214,491 | +7.25% | 1 | 100% | 255 |
| intraweek | 213,702 | +6.85% | 30 | 53% | 3,302 |
| oracle | 212,063 | +6.03% | 0 | - | 233 |
| intramonth | 211,581 | +5.79% | 0 | - | 235 |
| random_hold | 207,042 | +3.52% | 9 | 67% | 709 |
| snake_anaconda | 204,950 | +2.48% | 3 | 33% | 374 |
| snake_viper_wild | 204,924 | +2.46% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,429 | +0.71% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,345 | +0.67% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,144 | -4.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,468 (-4.27%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,494 | +3.80% |
| snake_viper_tick | +7,353 | +3.79% |
| snake_abs_exit_conv | +6,247 | +2.95% |
| snake_anaconda | +5,484 | +2.75% |
| snake_abs_exit | +5,094 | +2.40% |
| snake_abs_conv | +5,013 | +2.39% |
| snake_abs | +4,998 | +2.38% |
| benchmark_smallcap | +3,172 | +1.60% |
| benchmark | +2,624 | +1.20% |
| oracle | +2,144 | +1.02% |
| random_hold | +2,081 | +1.01% |
| intramonth | +972 | +0.46% |
| unified | +879 | +0.40% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -840 | -0.39% |
| gold | -1,989 | -1.03% |

Average per day so far: benchmark Rs +668, unified Rs +665, snake_abs_exit_conv Rs +648, snake_abs_exit Rs +610, snake_abs_conv Rs +518, snake_abs Rs +505, intraweek Rs +442, oracle Rs +389, intramonth Rs +374, random_hold Rs +227, snake_viper_wild Rs +214, snake_anaconda Rs +190, snake_viper_tick Rs +71, nifty_calls Rs +59, benchmark_smallcap Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -318, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.