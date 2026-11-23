# Paper trading report

Updated 2026-11-23 11:52 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,329 | +12.16% | 0 | - | 236 |
| benchmark | 222,980 | +11.49% | 0 | - | 237 |
| intraweek | 212,965 | +6.48% | 40 | 55% | 4,400 |
| intramonth | 212,388 | +6.19% | 0 | - | 235 |
| oracle | 211,547 | +5.77% | 0 | - | 233 |
| random_hold | 209,862 | +4.93% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,304 | +3.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,388 | +3.19% | 2 | 50% | 345 |
| snake_abs | 204,847 | +2.42% | 1 | 100% | 255 |
| snake_abs_conv | 204,679 | +2.34% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,604 | +0.80% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,450 | -0.28% | 0 | - | 237 |
| snake_anaconda | 198,311 | -0.84% | 3 | 33% | 374 |
| snake_viper_tick | 198,163 | -0.92% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,841 | -15.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,462 (-4.77%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,792 | +1.07% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -228 | -0.11% |
| random_hold | -898 | -0.43% |
| oracle | -931 | -0.44% |
| snake_abs | -1,072 | -0.52% |
| snake_abs_conv | -1,103 | -0.54% |
| snake_viper_tick | -1,209 | -0.61% |
| snake_viper_wild | -1,225 | -0.60% |
| snake_abs_exit | -1,258 | -0.60% |
| benchmark_smallcap | -1,457 | -0.72% |
| snake_anaconda | -1,594 | -0.80% |
| unified | -1,852 | -0.82% |
| benchmark | -2,157 | -0.96% |
| intramonth | -2,616 | -1.22% |
| intraweek | -2,747 | -1.27% |

Average per day so far: unified Rs +624, benchmark Rs +589, intraweek Rs +332, intramonth Rs +318, oracle Rs +296, random_hold Rs +253, snake_abs_exit Rs +203, snake_abs_exit_conv Rs +177, snake_abs Rs +131, snake_abs_conv Rs +130, snake_viper_wild Rs +52, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -50, snake_viper_tick Rs -66, snake_nonews Rs -300, snake Rs -320, gold Rs -773

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.