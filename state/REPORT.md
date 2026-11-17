# Paper trading report

Updated 2026-11-17 14:11 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,131 | +11.07% | 0 | - | 237 |
| unified | 221,676 | +10.84% | 0 | - | 236 |
| snake_abs_exit | 213,911 | +6.96% | 2 | 50% | 345 |
| intraweek | 213,631 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,426 | +6.21% | 0 | - | 233 |
| snake_abs_exit_conv | 212,344 | +6.17% | 2 | 50% | 345 |
| intramonth | 211,546 | +5.77% | 0 | - | 235 |
| snake_viper_wild | 209,735 | +4.87% | 14 | 50% | 2,496 |
| snake_abs | 209,028 | +4.51% | 1 | 100% | 255 |
| snake_abs_conv | 208,893 | +4.45% | 1 | 100% | 255 |
| random_hold | 207,675 | +3.84% | 10 | 70% | 733 |
| snake_viper_tick | 206,151 | +3.08% | 13 | 46% | 2,299 |
| snake_anaconda | 204,597 | +2.30% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,244 | +0.62% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,889 | -9.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,210 (-4.40%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,591 | +1.74% |
| snake_viper_tick | +3,531 | +1.74% |
| intraweek | +2,365 | +1.12% |
| benchmark | +2,050 | +0.93% |
| benchmark_smallcap | +415 | +0.21% |
| oracle | +403 | +0.19% |
| unified | +238 | +0.11% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| gold | -66 | -0.04% |
| intramonth | -73 | -0.03% |
| random_hold | -118 | -0.06% |
| snake_abs_exit | -499 | -0.23% |
| snake_anaconda | -505 | -0.25% |
| snake_abs_exit_conv | -873 | -0.41% |
| snake_abs_conv | -1,097 | -0.52% |
| snake_abs | -1,106 | -0.53% |

Average per day so far: benchmark Rs +632, unified Rs +619, snake_abs_exit Rs +435, intraweek Rs +389, snake_abs_exit_conv Rs +386, snake_viper_wild Rs +361, oracle Rs +355, intramonth Rs +330, snake_abs_conv Rs +278, snake_abs Rs +274, snake_viper_tick Rs +256, random_hold Rs +219, snake_anaconda Rs +153, nifty_calls Rs +52, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -546

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.