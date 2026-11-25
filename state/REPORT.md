# Paper trading report

Updated 2026-11-25 11:48 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,209 | +13.10% | 0 | - | 237 |
| unified | 225,516 | +12.76% | 0 | - | 236 |
| intramonth | 213,178 | +6.59% | 0 | - | 235 |
| oracle | 212,432 | +6.22% | 0 | - | 233 |
| random_hold | 209,633 | +4.82% | 12 | 75% | 1,009 |
| intraweek | 207,622 | +3.81% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,728 | +1.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,153 | +1.08% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,730 | +0.86% | 1 | 100% | 255 |
| snake_abs_conv | 201,540 | +0.77% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,708 | -0.15% | 0 | - | 237 |
| snake_viper_wild | 196,818 | -1.59% | 16 | 50% | 2,827 |
| snake_anaconda | 194,205 | -2.90% | 3 | 33% | 374 |
| snake_viper_tick | 193,467 | -3.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,531 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,528 (-5.24%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,735 | +2.14% |
| unified | +1,231 | +0.55% |
| random_hold | +1,207 | +0.58% |
| benchmark_smallcap | +729 | +0.37% |
| intramonth | +426 | +0.20% |
| oracle | +90 | +0.04% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -3,731 | -1.82% |
| snake_abs_conv | -3,762 | -1.83% |
| intraweek | -3,997 | -1.89% |
| snake_viper_tick | -4,225 | -2.14% |
| snake_viper_wild | -4,306 | -2.14% |
| snake_anaconda | -4,498 | -2.26% |
| snake_abs_exit | -4,767 | -2.30% |
| snake_abs_exit_conv | -4,892 | -2.36% |
| gold | -4,899 | -2.89% |

Average per day so far: benchmark Rs +655, unified Rs +638, intramonth Rs +329, oracle Rs +311, random_hold Rs +241, intraweek Rs +191, snake_abs_exit Rs +74, snake_abs_exit_conv Rs +58, nifty_calls Rs +46, snake_abs Rs +46, snake_abs_conv Rs +42, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -8, snake_viper_wild Rs -99, snake_anaconda Rs -166, snake_viper_tick Rs -225, snake_nonews Rs -292, snake Rs -311, gold Rs -887

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.