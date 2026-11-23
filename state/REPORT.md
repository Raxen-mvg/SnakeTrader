# Paper trading report

Updated 2026-11-23 11:13 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,352 | +12.18% | 0 | - | 236 |
| benchmark | 223,363 | +11.68% | 0 | - | 237 |
| intraweek | 212,819 | +6.41% | 40 | 55% | 4,400 |
| intramonth | 212,547 | +6.27% | 0 | - | 235 |
| oracle | 211,301 | +5.65% | 0 | - | 233 |
| random_hold | 209,843 | +4.92% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,680 | +3.34% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,802 | +2.90% | 2 | 50% | 345 |
| snake_abs | 204,056 | +2.03% | 1 | 100% | 255 |
| snake_abs_conv | 203,892 | +1.95% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,879 | +0.44% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,417 | -0.29% | 0 | - | 237 |
| snake_anaconda | 197,687 | -1.16% | 3 | 33% | 374 |
| snake_viper_tick | 197,453 | -1.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,005 | -15.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,322 (-4.84%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,956 | +1.16% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -815 | -0.39% |
| random_hold | -917 | -0.43% |
| oracle | -1,177 | -0.55% |
| benchmark_smallcap | -1,491 | -0.74% |
| benchmark | -1,775 | -0.79% |
| unified | -1,830 | -0.81% |
| snake_abs | -1,864 | -0.91% |
| snake_abs_exit | -1,882 | -0.90% |
| snake_abs_conv | -1,891 | -0.92% |
| snake_viper_tick | -1,919 | -0.96% |
| snake_viper_wild | -1,950 | -0.96% |
| snake_anaconda | -2,218 | -1.11% |
| intramonth | -2,457 | -1.14% |
| intraweek | -2,893 | -1.34% |

Average per day so far: unified Rs +624, benchmark Rs +599, intraweek Rs +329, intramonth Rs +322, oracle Rs +290, random_hold Rs +252, snake_abs_exit Rs +186, snake_abs_exit_conv Rs +161, snake_abs Rs +110, snake_abs_conv Rs +108, nifty_calls Rs +47, snake_viper_wild Rs +28, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -17, snake_anaconda Rs -68, snake_viper_tick Rs -91, snake_nonews Rs -300, snake Rs -320, gold Rs -769

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.