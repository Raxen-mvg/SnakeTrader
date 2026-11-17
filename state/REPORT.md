# Paper trading report

Updated 2026-11-17 12:33 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,276 | +11.14% | 0 | - | 237 |
| unified | 221,890 | +10.95% | 0 | - | 236 |
| snake_abs_exit | 214,253 | +7.13% | 2 | 50% | 345 |
| intraweek | 212,961 | +6.48% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,490 | +6.25% | 2 | 50% | 345 |
| oracle | 212,417 | +6.21% | 0 | - | 233 |
| intramonth | 211,784 | +5.89% | 0 | - | 235 |
| snake_abs | 209,402 | +4.70% | 1 | 100% | 255 |
| snake_abs_conv | 209,253 | +4.63% | 1 | 100% | 255 |
| random_hold | 207,615 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,504 | +3.75% | 14 | 50% | 2,496 |
| snake_anaconda | 204,991 | +2.50% | 3 | 33% | 374 |
| snake_viper_tick | 203,957 | +1.98% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,580 | +0.79% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,332 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,206 (-4.40%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,196 | +1.00% |
| intraweek | +1,695 | +0.80% |
| snake_viper_wild | +1,360 | +0.66% |
| snake_viper_tick | +1,337 | +0.66% |
| benchmark_smallcap | +751 | +0.37% |
| unified | +452 | +0.20% |
| oracle | +394 | +0.19% |
| gold | +378 | +0.21% |
| intramonth | +165 | +0.08% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -111 | -0.05% |
| snake_abs_exit | -157 | -0.07% |
| random_hold | -179 | -0.09% |
| snake_abs_exit_conv | -727 | -0.34% |
| snake_abs | -732 | -0.35% |
| snake_abs_conv | -737 | -0.35% |

Average per day so far: benchmark Rs +636, unified Rs +625, snake_abs_exit Rs +445, snake_abs_exit_conv Rs +390, intraweek Rs +370, oracle Rs +355, intramonth Rs +337, snake_abs_conv Rs +289, snake_abs Rs +285, snake_viper_wild Rs +278, random_hold Rs +218, snake_anaconda Rs +166, snake_viper_tick Rs +165, nifty_calls Rs +52, benchmark_smallcap Rs +51, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.