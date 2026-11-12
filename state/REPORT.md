# Paper trading report

Updated 2026-11-12 13:10 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,765 | +10.88% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| snake_abs_exit_conv | 218,935 | +9.47% | 2 | 50% | 345 |
| snake_abs_exit | 217,892 | +8.95% | 2 | 50% | 345 |
| snake_abs | 215,879 | +7.94% | 1 | 100% | 255 |
| snake_abs_conv | 215,708 | +7.85% | 1 | 100% | 255 |
| intraweek | 214,783 | +7.39% | 30 | 53% | 3,302 |
| oracle | 213,687 | +6.84% | 0 | - | 233 |
| intramonth | 212,327 | +6.16% | 0 | - | 235 |
| random_hold | 208,082 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,392 | +3.70% | 10 | 50% | 1,825 |
| snake_anaconda | 206,632 | +3.32% | 3 | 33% | 374 |
| snake_viper_tick | 203,843 | +1.92% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,250 | +1.62% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,968 | -7.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,432 (-3.78%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,509 | +1.23% |
| benchmark_smallcap | +2,444 | +1.22% |
| snake_abs | +2,254 | +1.05% |
| snake_abs_conv | +2,250 | +1.05% |
| unified | +1,951 | +0.89% |
| snake_abs_exit_conv | +1,783 | +0.82% |
| snake_abs_exit | +1,730 | +0.80% |
| oracle | +1,684 | +0.79% |
| intraweek | +1,650 | +0.77% |
| intramonth | +1,331 | +0.63% |
| benchmark | +1,117 | +0.51% |
| random_hold | +972 | +0.47% |
| snake_viper_wild | +650 | +0.31% |
| snake_viper_tick | +634 | +0.31% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,617 | -1.91% |

Average per day so far: unified Rs +680, snake_abs_exit_conv Rs +653, benchmark Rs +637, snake_abs_exit Rs +617, snake_abs_conv Rs +542, snake_abs Rs +529, intraweek Rs +462, oracle Rs +428, intramonth Rs +385, snake_viper_wild Rs +308, random_hold Rs +253, snake_anaconda Rs +246, snake_viper_tick Rs +183, benchmark_smallcap Rs +116, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -438

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.