# Paper trading report

Updated 2026-11-23 11:45 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,402 | +12.20% | 0 | - | 236 |
| benchmark | 223,210 | +11.61% | 0 | - | 237 |
| intraweek | 212,813 | +6.41% | 40 | 55% | 4,400 |
| intramonth | 212,538 | +6.27% | 0 | - | 235 |
| oracle | 211,475 | +5.74% | 0 | - | 233 |
| random_hold | 209,910 | +4.96% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,523 | +3.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,508 | +3.25% | 2 | 50% | 345 |
| snake_abs | 204,957 | +2.48% | 1 | 100% | 255 |
| snake_abs_conv | 204,793 | +2.40% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,599 | +0.80% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,764 | -0.12% | 0 | - | 237 |
| snake_anaconda | 198,425 | -0.79% | 3 | 33% | 374 |
| snake_viper_tick | 198,158 | -0.92% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,742 | -15.13% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,510 (-4.75%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,693 | +1.01% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -108 | -0.05% |
| random_hold | -849 | -0.40% |
| snake_abs | -963 | -0.47% |
| snake_abs_conv | -990 | -0.48% |
| oracle | -1,003 | -0.47% |
| snake_abs_exit | -1,039 | -0.50% |
| benchmark_smallcap | -1,143 | -0.57% |
| snake_viper_tick | -1,214 | -0.61% |
| snake_viper_wild | -1,230 | -0.61% |
| snake_anaconda | -1,480 | -0.74% |
| unified | -1,780 | -0.79% |
| benchmark | -1,928 | -0.86% |
| intramonth | -2,467 | -1.15% |
| intraweek | -2,899 | -1.34% |

Average per day so far: unified Rs +626, benchmark Rs +595, intraweek Rs +329, intramonth Rs +321, oracle Rs +294, random_hold Rs +254, snake_abs_exit Rs +209, snake_abs_exit_conv Rs +181, snake_abs Rs +134, snake_abs_conv Rs +133, snake_viper_wild Rs +52, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -7, snake_anaconda Rs -46, snake_viper_tick Rs -66, snake_nonews Rs -300, snake Rs -320, gold Rs -776

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.