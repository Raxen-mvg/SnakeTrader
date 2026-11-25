# Paper trading report

Updated 2026-11-25 13:58 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,531 | +12.27% | 0 | - | 236 |
| benchmark | 224,174 | +12.09% | 0 | - | 237 |
| oracle | 212,336 | +6.17% | 0 | - | 233 |
| intramonth | 212,081 | +6.04% | 0 | - | 235 |
| random_hold | 209,549 | +4.77% | 12 | 75% | 1,009 |
| intraweek | 207,373 | +3.69% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,512 | +0.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,228 | +0.61% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,771 | -0.11% | 1 | 100% | 255 |
| snake_abs_conv | 199,577 | -0.21% | 1 | 100% | 255 |
| benchmark_smallcap | 198,598 | -0.70% | 0 | - | 237 |
| snake_viper_wild | 197,183 | -1.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,824 | -3.09% | 15 | 47% | 2,625 |
| snake_anaconda | 193,309 | -3.35% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,810 | -17.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,889 (-5.56%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,700 | +1.22% |
| random_hold | +1,122 | +0.54% |
| unified | +246 | +0.11% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -6 | -0.00% |
| benchmark_smallcap | -381 | -0.19% |
| intramonth | -670 | -0.32% |
| snake_viper_tick | -3,868 | -1.96% |
| snake_viper_wild | -3,941 | -1.96% |
| intraweek | -4,246 | -2.01% |
| gold | -4,620 | -2.73% |
| snake_anaconda | -5,395 | -2.71% |
| snake_abs | -5,690 | -2.77% |
| snake_abs_conv | -5,725 | -2.79% |
| snake_abs_exit_conv | -5,818 | -2.81% |
| snake_abs_exit | -5,982 | -2.88% |

Average per day so far: unified Rs +613, benchmark Rs +604, oracle Rs +308, intramonth Rs +302, random_hold Rs +239, intraweek Rs +184, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +33, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, benchmark_smallcap Rs -39, snake_viper_wild Rs -88, snake_anaconda Rs -191, snake_viper_tick Rs -213, snake_nonews Rs -292, snake Rs -311, gold Rs -880

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.