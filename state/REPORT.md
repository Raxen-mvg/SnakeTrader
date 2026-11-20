# Paper trading report

Updated 2026-11-20 13:13 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,250 | +13.12% | 0 | - | 236 |
| benchmark | 224,388 | +12.19% | 0 | - | 237 |
| intraweek | 215,216 | +7.61% | 35 | 54% | 3,851 |
| intramonth | 215,186 | +7.59% | 0 | - | 235 |
| oracle | 212,581 | +6.29% | 0 | - | 233 |
| random_hold | 209,670 | +4.83% | 11 | 73% | 979 |
| snake_abs_exit | 209,292 | +4.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,274 | +3.64% | 2 | 50% | 345 |
| snake_abs | 206,387 | +3.19% | 1 | 100% | 255 |
| snake_abs_conv | 206,252 | +3.13% | 1 | 100% | 255 |
| snake_viper_wild | 205,703 | +2.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,194 | +1.10% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,964 | +0.48% | 0 | - | 237 |
| snake_anaconda | 200,512 | +0.26% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,109 | -16.95% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,087 (-3.96%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,327 | +1.09% |
| benchmark | +2,012 | +0.91% |
| unified | +1,635 | +0.73% |
| random_hold | +1,217 | +0.58% |
| intramonth | +1,178 | +0.55% |
| oracle | +492 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -504 | -0.25% |
| snake_viper_tick | -1,783 | -0.87% |
| snake_viper_wild | -1,819 | -0.88% |
| snake_abs | -2,593 | -1.24% |
| snake_abs_conv | -2,608 | -1.25% |
| snake_anaconda | -2,952 | -1.45% |
| snake_abs_exit_conv | -3,790 | -1.80% |
| snake_abs_exit | -4,059 | -1.90% |
| gold | -8,664 | -4.96% |

Average per day so far: unified Rs +691, benchmark Rs +642, intraweek Rs +400, intramonth Rs +400, oracle Rs +331, snake_abs_exit Rs +265, random_hold Rs +254, snake_abs_exit_conv Rs +208, snake_viper_wild Rs +190, snake_abs_conv Rs +179, snake_abs Rs +177, snake_viper_tick Rs +81, nifty_calls Rs +48, benchmark_smallcap Rs +28, snake_anaconda Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -892

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.