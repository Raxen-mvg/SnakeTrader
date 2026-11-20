# Paper trading report

Updated 2026-11-20 09:52 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,307 | +12.65% | 0 | - | 236 |
| benchmark | 222,636 | +11.32% | 0 | - | 237 |
| intramonth | 214,515 | +7.26% | 0 | - | 235 |
| intraweek | 214,305 | +7.15% | 35 | 54% | 3,851 |
| oracle | 213,193 | +6.60% | 0 | - | 233 |
| snake_abs_exit | 210,668 | +5.33% | 2 | 50% | 345 |
| random_hold | 209,575 | +4.79% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,386 | +4.19% | 2 | 50% | 345 |
| snake_abs | 207,006 | +3.50% | 1 | 100% | 255 |
| snake_abs_conv | 206,869 | +3.43% | 1 | 100% | 255 |
| snake_viper_wild | 205,622 | +2.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,116 | +1.06% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,373 | +0.69% | 3 | 33% | 374 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,961 | -17.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,962 (-4.02%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,416 | +0.67% |
| random_hold | +1,122 | +0.54% |
| oracle | +1,104 | +0.52% |
| unified | +692 | +0.31% |
| intramonth | +507 | +0.24% |
| benchmark | +260 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -852 | -0.42% |
| snake_viper_tick | -1,861 | -0.91% |
| snake_viper_wild | -1,901 | -0.92% |
| snake_abs | -1,974 | -0.94% |
| snake_abs_conv | -1,991 | -0.95% |
| snake_anaconda | -2,090 | -1.03% |
| snake_abs_exit_conv | -2,678 | -1.27% |
| snake_abs_exit | -2,683 | -1.26% |
| gold | -8,812 | -5.04% |

Average per day so far: unified Rs +666, benchmark Rs +596, intramonth Rs +382, intraweek Rs +376, oracle Rs +347, snake_abs_exit Rs +305, random_hold Rs +252, snake_abs_exit_conv Rs +240, snake_abs_conv Rs +196, snake_abs Rs +195, snake_viper_wild Rs +187, snake_viper_tick Rs +78, nifty_calls Rs +48, snake_anaconda Rs +42, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -896

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.