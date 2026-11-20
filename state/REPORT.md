# Paper trading report

Updated 2026-11-20 10:09 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,761 | +12.38% | 0 | - | 236 |
| benchmark | 222,651 | +11.33% | 0 | - | 237 |
| intramonth | 213,969 | +6.98% | 0 | - | 235 |
| intraweek | 213,492 | +6.75% | 35 | 54% | 3,851 |
| oracle | 212,700 | +6.35% | 0 | - | 233 |
| snake_abs_exit | 210,506 | +5.25% | 2 | 50% | 345 |
| random_hold | 208,923 | +4.46% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,254 | +4.13% | 2 | 50% | 345 |
| snake_abs | 206,856 | +3.43% | 1 | 100% | 255 |
| snake_abs_conv | 206,723 | +3.36% | 1 | 100% | 255 |
| snake_viper_wild | 205,363 | +2.68% | 16 | 50% | 2,827 |
| snake_viper_tick | 201,862 | +0.93% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,299 | +0.65% | 3 | 33% | 374 |
| benchmark_smallcap | 200,538 | +0.27% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,221 | -17.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,547 (-4.23%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +611 | +0.29% |
| intraweek | +603 | +0.28% |
| random_hold | +470 | +0.23% |
| benchmark | +275 | +0.12% |
| unified | +146 | +0.07% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intramonth | -39 | -0.02% |
| benchmark_smallcap | -930 | -0.46% |
| snake_viper_tick | -2,115 | -1.04% |
| snake_abs | -2,124 | -1.02% |
| snake_abs_conv | -2,137 | -1.02% |
| snake_viper_wild | -2,160 | -1.04% |
| snake_anaconda | -2,165 | -1.06% |
| snake_abs_exit_conv | -2,811 | -1.33% |
| snake_abs_exit | -2,845 | -1.33% |
| gold | -9,552 | -5.46% |

Average per day so far: unified Rs +652, benchmark Rs +596, intramonth Rs +368, intraweek Rs +355, oracle Rs +334, snake_abs_exit Rs +300, snake_abs_exit_conv Rs +236, random_hold Rs +235, snake_abs_conv Rs +192, snake_abs Rs +190, snake_viper_wild Rs +179, snake_viper_tick Rs +69, nifty_calls Rs +48, snake_anaconda Rs +39, benchmark_smallcap Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -915

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.