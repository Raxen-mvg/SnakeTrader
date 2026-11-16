# Paper trading report

Updated 2026-11-16 13:14 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,361 | +10.68% | 0 | - | 236 |
| benchmark | 220,287 | +10.14% | 0 | - | 237 |
| snake_abs_exit | 213,553 | +6.78% | 2 | 50% | 345 |
| oracle | 212,908 | +6.45% | 0 | - | 233 |
| snake_abs_exit_conv | 212,397 | +6.20% | 2 | 50% | 345 |
| intraweek | 212,313 | +6.16% | 35 | 54% | 3,851 |
| intramonth | 211,986 | +5.99% | 0 | - | 235 |
| snake_abs | 209,675 | +4.84% | 1 | 100% | 255 |
| snake_abs_conv | 209,517 | +4.76% | 1 | 100% | 255 |
| random_hold | 207,896 | +3.95% | 10 | 70% | 733 |
| snake_viper_wild | 205,662 | +2.83% | 14 | 50% | 2,496 |
| snake_anaconda | 204,023 | +2.01% | 3 | 33% | 374 |
| snake_viper_tick | 202,145 | +1.07% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,076 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,135 | -9.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,251 (-4.37%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,340 | +1.07% |
| intramonth | +1,929 | +0.92% |
| benchmark | +949 | +0.43% |
| snake_viper_wild | +905 | +0.44% |
| snake_viper_tick | +891 | +0.44% |
| random_hold | +670 | +0.32% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -190 | -0.09% |
| snake_anaconda | -869 | -0.42% |
| benchmark_smallcap | -1,794 | -0.88% |
| snake_abs_conv | -2,850 | -1.34% |
| gold | -2,861 | -1.55% |
| snake_abs | -2,865 | -1.35% |
| snake_abs_exit | -3,432 | -1.58% |
| intraweek | -3,832 | -1.77% |
| snake_abs_exit_conv | -3,984 | -1.84% |

Average per day so far: unified Rs +628, benchmark Rs +597, snake_abs_exit Rs +437, snake_abs_exit_conv Rs +400, oracle Rs +380, intraweek Rs +362, intramonth Rs +353, snake_abs_conv Rs +307, snake_abs Rs +302, random_hold Rs +232, snake_viper_wild Rs +218, snake_anaconda Rs +139, snake_viper_tick Rs +93, nifty_calls Rs +54, benchmark_smallcap Rs +36, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -555

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.