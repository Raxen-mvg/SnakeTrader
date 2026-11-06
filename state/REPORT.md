# Paper trading report

Updated 2026-11-06 10:06 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,037 | +7.52% | 0 | - | 236 |
| benchmark | 214,718 | +7.36% | 0 | - | 237 |
| intraweek | 211,613 | +5.81% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 210,246 | +5.12% | 1 | 100% | 255 |
| snake_abs_exit | 210,022 | +5.01% | 1 | 100% | 260 |
| snake_abs | 207,195 | +3.60% | 1 | 100% | 255 |
| snake_abs_conv | 207,020 | +3.51% | 1 | 100% | 255 |
| intramonth | 206,983 | +3.49% | 0 | - | 235 |
| oracle | 204,500 | +2.25% | 0 | - | 233 |
| random_hold | 204,053 | +2.03% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,604 | -1.20% | 3 | 33% | 702 |
| snake_anaconda | 196,955 | -1.52% | 3 | 33% | 374 |
| benchmark_smallcap | 194,809 | -2.60% | 0 | - | 237 |
| snake_viper_tick | 194,248 | -2.88% | 2 | 0% | 532 |
| gold | 190,539 | -4.73% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,783 (-6.11%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,195 | +1.05% |
| benchmark | +949 | +0.44% |
| oracle | +428 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -270 | -0.13% |
| unified | -946 | -0.44% |
| intramonth | -965 | -0.46% |
| gold | -3,683 | -1.90% |
| benchmark_smallcap | -3,879 | -1.95% |
| snake_abs | -4,493 | -2.12% |
| snake_abs_conv | -4,524 | -2.14% |
| snake_abs_exit_conv | -4,557 | -2.12% |
| snake_abs_exit | -4,637 | -2.16% |
| snake_anaconda | -5,524 | -2.73% |
| snake_viper_tick | -6,890 | -3.43% |
| snake_viper_wild | -7,052 | -3.45% |

Average per day so far: unified Rs +519, benchmark Rs +508, intraweek Rs +400, snake_abs_exit_conv Rs +394, snake_abs_exit Rs +385, snake_abs_conv Rs +270, snake_abs Rs +266, intramonth Rs +241, oracle Rs +155, random_hold Rs +140, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -114, snake_anaconda Rs -127, benchmark_smallcap Rs -208, snake_viper_tick Rs -320, gold Rs -326, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.