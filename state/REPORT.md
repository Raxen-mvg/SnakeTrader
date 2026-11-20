# Paper trading report

Updated 2026-11-20 13:45 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,585 | +13.29% | 0 | - | 236 |
| benchmark | 224,434 | +12.22% | 0 | - | 237 |
| intraweek | 215,847 | +7.92% | 35 | 54% | 3,851 |
| intramonth | 215,405 | +7.70% | 0 | - | 235 |
| oracle | 212,922 | +6.46% | 0 | - | 233 |
| random_hold | 209,996 | +5.00% | 11 | 73% | 979 |
| snake_abs_exit | 209,146 | +4.57% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,117 | +3.56% | 2 | 50% | 345 |
| snake_abs | 206,279 | +3.14% | 1 | 100% | 255 |
| snake_abs_conv | 206,146 | +3.07% | 1 | 100% | 255 |
| snake_viper_wild | 203,839 | +1.92% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,233 | +0.62% | 0 | - | 237 |
| snake_anaconda | 200,439 | +0.22% | 3 | 33% | 374 |
| snake_viper_tick | 200,362 | +0.18% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,293 | -16.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,237 (-3.88%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,958 | +1.39% |
| benchmark | +2,058 | +0.93% |
| unified | +1,970 | +0.88% |
| random_hold | +1,543 | +0.74% |
| intramonth | +1,397 | +0.65% |
| oracle | +833 | +0.39% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -235 | -0.12% |
| snake_abs | -2,701 | -1.29% |
| snake_abs_conv | -2,714 | -1.30% |
| snake_anaconda | -3,024 | -1.49% |
| snake_viper_tick | -3,615 | -1.77% |
| snake_viper_wild | -3,684 | -1.77% |
| snake_abs_exit_conv | -3,947 | -1.87% |
| snake_abs_exit | -4,206 | -1.97% |
| gold | -7,480 | -4.28% |

Average per day so far: unified Rs +700, benchmark Rs +643, intraweek Rs +417, intramonth Rs +405, oracle Rs +340, random_hold Rs +263, snake_abs_exit Rs +261, snake_abs_exit_conv Rs +203, snake_abs_conv Rs +176, snake_abs Rs +174, snake_viper_wild Rs +128, nifty_calls Rs +48, benchmark_smallcap Rs +36, snake_viper_tick Rs +13, snake_anaconda Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -861

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.