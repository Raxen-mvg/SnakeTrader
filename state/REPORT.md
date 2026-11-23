# Paper trading report

Updated 2026-11-23 10:28 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,617 | +12.31% | 0 | - | 236 |
| benchmark | 223,439 | +11.72% | 0 | - | 237 |
| intraweek | 212,960 | +6.48% | 40 | 55% | 4,400 |
| intramonth | 212,504 | +6.25% | 0 | - | 235 |
| oracle | 211,224 | +5.61% | 0 | - | 233 |
| random_hold | 209,835 | +4.92% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,845 | +3.92% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,852 | +3.43% | 2 | 50% | 345 |
| snake_abs | 205,018 | +2.51% | 1 | 100% | 255 |
| snake_abs_conv | 204,870 | +2.44% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,062 | +0.53% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,730 | -0.14% | 0 | - | 237 |
| snake_anaconda | 198,822 | -0.59% | 3 | 33% | 374 |
| snake_viper_tick | 197,632 | -1.18% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,397 | -15.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,538 (-4.73%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,348 | +0.80% |
| snake_abs_exit_conv | +236 | +0.11% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -717 | -0.34% |
| snake_abs | -902 | -0.44% |
| snake_abs_conv | -913 | -0.44% |
| random_hold | -925 | -0.44% |
| snake_anaconda | -1,083 | -0.54% |
| benchmark_smallcap | -1,177 | -0.59% |
| oracle | -1,255 | -0.59% |
| unified | -1,565 | -0.69% |
| benchmark | -1,698 | -0.75% |
| snake_viper_tick | -1,740 | -0.87% |
| snake_viper_wild | -1,767 | -0.87% |
| intramonth | -2,500 | -1.16% |
| intraweek | -2,752 | -1.28% |

Average per day so far: unified Rs +631, benchmark Rs +601, intraweek Rs +332, intramonth Rs +321, oracle Rs +288, random_hold Rs +252, snake_abs_exit Rs +218, snake_abs_exit_conv Rs +190, snake_abs Rs +136, snake_abs_conv Rs +135, nifty_calls Rs +47, snake_viper_wild Rs +34, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -8, snake_anaconda Rs -35, snake_viper_tick Rs -85, snake_nonews Rs -300, snake Rs -320, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.