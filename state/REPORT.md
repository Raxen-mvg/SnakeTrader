# Paper trading report

Updated 2026-11-11 11:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,221 | +10.61% | 0 | - | 237 |
| unified | 220,068 | +10.03% | 0 | - | 236 |
| snake_abs_exit_conv | 216,686 | +8.34% | 2 | 50% | 345 |
| snake_abs_exit | 215,267 | +7.63% | 2 | 50% | 345 |
| intraweek | 214,110 | +7.05% | 30 | 53% | 3,302 |
| snake_abs | 213,544 | +6.77% | 1 | 100% | 255 |
| snake_abs_conv | 213,386 | +6.69% | 1 | 100% | 255 |
| oracle | 211,816 | +5.91% | 0 | - | 233 |
| intramonth | 211,030 | +5.51% | 0 | - | 235 |
| random_hold | 206,788 | +3.39% | 9 | 67% | 709 |
| snake_anaconda | 203,346 | +1.67% | 3 | 33% | 374 |
| snake_viper_wild | 201,919 | +0.96% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,816 | +0.91% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,486 | -0.76% | 9 | 44% | 1,639 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,177 (-4.41%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,777 | +2.25% |
| snake_viper_wild | +4,489 | +2.27% |
| snake_viper_tick | +4,409 | +2.27% |
| snake_abs_conv | +3,909 | +1.87% |
| snake_abs | +3,898 | +1.86% |
| snake_anaconda | +3,880 | +1.95% |
| benchmark_smallcap | +3,643 | +1.84% |
| snake_abs_exit | +3,283 | +1.55% |
| benchmark | +3,129 | +1.44% |
| oracle | +1,897 | +0.90% |
| random_hold | +1,827 | +0.89% |
| intramonth | +420 | +0.20% |
| unified | +321 | +0.15% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -432 | -0.20% |
| gold | -2,236 | -1.16% |

Average per day so far: benchmark Rs +685, unified Rs +647, snake_abs_exit_conv Rs +596, snake_abs_exit Rs +545, snake_abs_conv Rs +478, snake_abs Rs +467, intraweek Rs +455, oracle Rs +381, intramonth Rs +356, random_hold Rs +219, snake_anaconda Rs +129, snake_viper_wild Rs +83, benchmark_smallcap Rs +67, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -76, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.