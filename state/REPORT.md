# Paper trading report

Updated 2026-11-12 12:31 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,558 | +10.78% | 0 | - | 236 |
| benchmark | 219,989 | +9.99% | 0 | - | 237 |
| snake_abs_exit_conv | 218,932 | +9.47% | 2 | 50% | 345 |
| snake_abs_exit | 217,971 | +8.98% | 2 | 50% | 345 |
| snake_abs | 215,973 | +7.99% | 1 | 100% | 255 |
| snake_abs_conv | 215,807 | +7.90% | 1 | 100% | 255 |
| intraweek | 214,802 | +7.40% | 30 | 53% | 3,302 |
| oracle | 213,305 | +6.65% | 0 | - | 233 |
| intramonth | 211,819 | +5.91% | 0 | - | 235 |
| random_hold | 208,025 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 207,039 | +3.52% | 10 | 50% | 1,825 |
| snake_anaconda | 206,710 | +3.35% | 3 | 33% | 374 |
| snake_viper_tick | 203,498 | +1.75% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,183 | +1.59% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,116 | -6.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,272 (-3.86%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,587 | +1.27% |
| benchmark_smallcap | +2,377 | +1.18% |
| snake_abs_conv | +2,349 | +1.10% |
| snake_abs | +2,348 | +1.10% |
| snake_abs_exit | +1,808 | +0.84% |
| snake_abs_exit_conv | +1,781 | +0.82% |
| unified | +1,744 | +0.79% |
| intraweek | +1,669 | +0.78% |
| oracle | +1,302 | +0.61% |
| random_hold | +914 | +0.44% |
| intramonth | +823 | +0.39% |
| benchmark | +727 | +0.33% |
| snake_viper_wild | +297 | +0.14% |
| snake_viper_tick | +289 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,469 | -1.83% |

Average per day so far: unified Rs +674, snake_abs_exit_conv Rs +653, benchmark Rs +625, snake_abs_exit Rs +620, snake_abs_conv Rs +545, snake_abs Rs +532, intraweek Rs +463, oracle Rs +416, intramonth Rs +369, snake_viper_wild Rs +293, random_hold Rs +251, snake_anaconda Rs +249, snake_viper_tick Rs +167, benchmark_smallcap Rs +114, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.