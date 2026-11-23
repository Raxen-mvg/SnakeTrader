# Paper trading report

Updated 2026-11-23 10:10 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,289 | +12.64% | 0 | - | 236 |
| benchmark | 223,699 | +11.85% | 0 | - | 237 |
| intramonth | 213,268 | +6.63% | 0 | - | 235 |
| intraweek | 212,840 | +6.42% | 40 | 55% | 4,400 |
| oracle | 211,319 | +5.66% | 0 | - | 233 |
| random_hold | 209,971 | +4.99% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,990 | +4.00% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,444 | +3.22% | 2 | 50% | 345 |
| snake_abs | 205,205 | +2.60% | 1 | 100% | 255 |
| snake_abs_conv | 205,059 | +2.53% | 1 | 100% | 255 |
| snake_viper_wild | 203,578 | +1.79% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,105 | +0.05% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,719 | -0.14% | 0 | - | 237 |
| snake_anaconda | 199,177 | -0.41% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,265 | -15.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,819 (-4.59%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,217 | +0.72% |
| snake_viper_wild | +749 | +0.37% |
| snake_viper_tick | +733 | +0.37% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -172 | -0.08% |
| snake_abs_exit | -572 | -0.27% |
| snake_abs | -715 | -0.35% |
| snake_abs_conv | -724 | -0.35% |
| snake_anaconda | -729 | -0.36% |
| random_hold | -789 | -0.37% |
| unified | -893 | -0.40% |
| oracle | -1,159 | -0.55% |
| benchmark_smallcap | -1,188 | -0.59% |
| benchmark | -1,438 | -0.64% |
| intramonth | -1,736 | -0.81% |
| intraweek | -2,872 | -1.33% |

Average per day so far: unified Rs +648, benchmark Rs +608, intramonth Rs +340, intraweek Rs +329, oracle Rs +290, random_hold Rs +256, snake_abs_exit Rs +222, snake_abs_exit_conv Rs +179, snake_abs Rs +141, snake_abs_conv Rs +141, snake_viper_wild Rs +115, nifty_calls Rs +47, snake_viper_tick Rs +4, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -8, snake_anaconda Rs -24, snake_nonews Rs -300, snake Rs -320, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.