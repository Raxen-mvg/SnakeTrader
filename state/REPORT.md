# Paper trading report

Updated 2026-11-18 14:31 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,258 | +11.13% | 0 | - | 236 |
| benchmark | 220,349 | +10.17% | 0 | - | 237 |
| snake_abs_exit | 214,307 | +7.15% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,573 | +6.29% | 2 | 50% | 345 |
| intraweek | 212,120 | +6.06% | 35 | 54% | 3,851 |
| intramonth | 211,933 | +5.97% | 0 | - | 235 |
| oracle | 211,872 | +5.94% | 0 | - | 233 |
| snake_abs | 209,393 | +4.70% | 1 | 100% | 255 |
| snake_abs_conv | 209,288 | +4.64% | 1 | 100% | 255 |
| snake_viper_wild | 206,934 | +3.47% | 16 | 50% | 2,827 |
| random_hold | 206,920 | +3.46% | 10 | 70% | 733 |
| snake_anaconda | 204,672 | +2.34% | 3 | 33% | 374 |
| snake_viper_tick | 203,400 | +1.70% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,484 | -0.26% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,140 | -11.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,848 (-4.58%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +1,165 | +0.55% |
| snake_abs_exit_conv | +999 | +0.47% |
| snake_abs_conv | +868 | +0.42% |
| snake_abs | +835 | +0.40% |
| unified | +820 | +0.37% |
| snake_anaconda | +617 | +0.30% |
| intramonth | +391 | +0.18% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -615 | -0.29% |
| benchmark_smallcap | -1,087 | -0.54% |
| intraweek | -1,202 | -0.56% |
| benchmark | -1,255 | -0.57% |
| random_hold | -1,512 | -0.73% |
| snake_viper_tick | -2,437 | -1.18% |
| snake_viper_wild | -2,481 | -1.19% |
| gold | -3,584 | -1.98% |

Average per day so far: unified Rs +618, benchmark Rs +565, snake_abs_exit Rs +434, snake_abs_exit_conv Rs +381, intraweek Rs +337, intramonth Rs +331, oracle Rs +330, snake_abs_conv Rs +281, snake_abs Rs +276, snake_viper_wild Rs +248, random_hold Rs +192, snake_anaconda Rs +151, snake_viper_tick Rs +136, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -16, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.