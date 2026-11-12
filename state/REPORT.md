# Paper trading report

Updated 2026-11-12 12:52 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,533 | +10.77% | 0 | - | 236 |
| benchmark | 220,165 | +10.08% | 0 | - | 237 |
| snake_abs_exit_conv | 218,925 | +9.46% | 2 | 50% | 345 |
| snake_abs_exit | 217,915 | +8.96% | 2 | 50% | 345 |
| snake_abs | 215,837 | +7.92% | 1 | 100% | 255 |
| snake_abs_conv | 215,669 | +7.83% | 1 | 100% | 255 |
| intraweek | 214,642 | +7.32% | 30 | 53% | 3,302 |
| oracle | 213,435 | +6.72% | 0 | - | 233 |
| intramonth | 211,891 | +5.95% | 0 | - | 235 |
| random_hold | 208,190 | +4.09% | 10 | 70% | 733 |
| snake_viper_wild | 207,241 | +3.62% | 10 | 50% | 1,825 |
| snake_anaconda | 206,540 | +3.27% | 3 | 33% | 374 |
| snake_viper_tick | 203,696 | +1.85% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,194 | +1.60% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,116 | -6.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,273 (-3.86%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,417 | +1.18% |
| benchmark_smallcap | +2,388 | +1.19% |
| snake_abs | +2,212 | +1.04% |
| snake_abs_conv | +2,211 | +1.04% |
| snake_abs_exit_conv | +1,774 | +0.82% |
| snake_abs_exit | +1,753 | +0.81% |
| unified | +1,719 | +0.78% |
| intraweek | +1,509 | +0.71% |
| oracle | +1,432 | +0.68% |
| random_hold | +1,079 | +0.52% |
| benchmark | +903 | +0.41% |
| intramonth | +895 | +0.42% |
| snake_viper_wild | +499 | +0.24% |
| snake_viper_tick | +487 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,469 | -1.83% |

Average per day so far: unified Rs +673, snake_abs_exit_conv Rs +653, benchmark Rs +630, snake_abs_exit Rs +618, snake_abs_conv Rs +540, snake_abs Rs +528, intraweek Rs +458, oracle Rs +420, intramonth Rs +372, snake_viper_wild Rs +302, random_hold Rs +256, snake_anaconda Rs +242, snake_viper_tick Rs +176, benchmark_smallcap Rs +114, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.