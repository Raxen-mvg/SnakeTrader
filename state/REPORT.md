# Paper trading report

Updated 2026-11-20 14:16 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,487 | +13.24% | 0 | - | 236 |
| benchmark | 224,663 | +12.33% | 0 | - | 237 |
| intraweek | 215,863 | +7.93% | 35 | 54% | 3,851 |
| intramonth | 215,283 | +7.64% | 0 | - | 235 |
| oracle | 212,818 | +6.41% | 0 | - | 233 |
| random_hold | 210,364 | +5.18% | 11 | 73% | 979 |
| snake_abs_exit | 208,960 | +4.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,029 | +3.52% | 2 | 50% | 345 |
| snake_abs | 206,137 | +3.07% | 1 | 100% | 255 |
| snake_abs_conv | 206,007 | +3.00% | 1 | 100% | 255 |
| snake_viper_wild | 203,371 | +1.69% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,210 | +0.60% | 0 | - | 237 |
| snake_anaconda | 200,296 | +0.15% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,903 | -0.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,556 | -16.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,187 (-3.91%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,974 | +1.40% |
| benchmark | +2,287 | +1.03% |
| random_hold | +1,911 | +0.92% |
| unified | +1,872 | +0.83% |
| intramonth | +1,275 | +0.60% |
| oracle | +729 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -258 | -0.13% |
| snake_abs | -2,843 | -1.36% |
| snake_abs_conv | -2,853 | -1.37% |
| snake_anaconda | -3,168 | -1.56% |
| snake_abs_exit_conv | -4,035 | -1.91% |
| snake_viper_tick | -4,074 | -2.00% |
| snake_viper_wild | -4,152 | -2.00% |
| snake_abs_exit | -4,391 | -2.06% |
| gold | -7,217 | -4.13% |

Average per day so far: unified Rs +697, benchmark Rs +649, intraweek Rs +417, intramonth Rs +402, oracle Rs +337, random_hold Rs +273, snake_abs_exit Rs +256, snake_abs_exit_conv Rs +201, snake_abs_conv Rs +172, snake_abs Rs +170, snake_viper_wild Rs +112, nifty_calls Rs +48, benchmark_smallcap Rs +36, snake_anaconda Rs +9, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -4, snake_nonews Rs -308, snake Rs -328, gold Rs -854

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.