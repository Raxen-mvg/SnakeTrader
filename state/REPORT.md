# Paper trading report

Updated 2026-11-20 12:49 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,160 | +13.08% | 0 | - | 236 |
| benchmark | 224,327 | +12.16% | 0 | - | 237 |
| intramonth | 215,208 | +7.60% | 0 | - | 235 |
| intraweek | 214,632 | +7.32% | 35 | 54% | 3,851 |
| oracle | 212,625 | +6.31% | 0 | - | 233 |
| snake_abs_exit | 209,165 | +4.58% | 2 | 50% | 345 |
| random_hold | 209,005 | +4.50% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,228 | +3.61% | 2 | 50% | 345 |
| snake_abs | 206,355 | +3.18% | 1 | 100% | 255 |
| snake_abs_conv | 206,220 | +3.11% | 1 | 100% | 255 |
| snake_viper_wild | 205,348 | +2.67% | 16 | 50% | 2,827 |
| snake_viper_tick | 201,846 | +0.92% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,964 | +0.48% | 0 | - | 237 |
| snake_anaconda | 200,363 | +0.18% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,651 | -16.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,923 (-4.04%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,951 | +0.88% |
| intraweek | +1,743 | +0.82% |
| unified | +1,545 | +0.69% |
| intramonth | +1,200 | +0.56% |
| random_hold | +552 | +0.27% |
| oracle | +537 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -504 | -0.25% |
| snake_viper_tick | -2,131 | -1.04% |
| snake_viper_wild | -2,174 | -1.05% |
| snake_abs | -2,624 | -1.26% |
| snake_abs_conv | -2,640 | -1.26% |
| snake_anaconda | -3,100 | -1.52% |
| snake_abs_exit_conv | -3,837 | -1.82% |
| snake_abs_exit | -4,186 | -1.96% |
| gold | -8,121 | -4.65% |

Average per day so far: unified Rs +688, benchmark Rs +640, intramonth Rs +400, intraweek Rs +385, oracle Rs +332, snake_abs_exit Rs +262, random_hold Rs +237, snake_abs_exit_conv Rs +207, snake_viper_wild Rs +178, snake_abs_conv Rs +178, snake_abs Rs +177, snake_viper_tick Rs +68, nifty_calls Rs +48, benchmark_smallcap Rs +28, snake_anaconda Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -878

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.