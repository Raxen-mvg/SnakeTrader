# Paper trading report

Updated 2026-11-20 10:31 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,774 | +12.89% | 0 | - | 236 |
| benchmark | 222,774 | +11.39% | 0 | - | 237 |
| intramonth | 214,695 | +7.35% | 0 | - | 235 |
| intraweek | 213,818 | +6.91% | 35 | 54% | 3,851 |
| oracle | 212,808 | +6.40% | 0 | - | 233 |
| snake_abs_exit | 210,444 | +5.22% | 2 | 50% | 345 |
| random_hold | 208,924 | +4.46% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,961 | +3.98% | 2 | 50% | 345 |
| snake_abs | 206,944 | +3.47% | 1 | 100% | 255 |
| snake_abs_conv | 206,808 | +3.40% | 1 | 100% | 255 |
| snake_viper_wild | 205,931 | +2.97% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,419 | +1.21% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,881 | +0.44% | 3 | 33% | 374 |
| benchmark_smallcap | 200,190 | +0.10% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,271 | -17.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,833 (-4.08%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,159 | +0.52% |
| intraweek | +929 | +0.44% |
| oracle | +719 | +0.34% |
| intramonth | +687 | +0.32% |
| random_hold | +471 | +0.23% |
| benchmark | +398 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,278 | -0.63% |
| snake_viper_tick | -1,558 | -0.76% |
| snake_viper_wild | -1,592 | -0.77% |
| snake_abs | -2,035 | -0.97% |
| snake_abs_conv | -2,052 | -0.98% |
| snake_anaconda | -2,583 | -1.27% |
| snake_abs_exit | -2,908 | -1.36% |
| snake_abs_exit_conv | -3,104 | -1.47% |
| gold | -9,502 | -5.44% |

Average per day so far: unified Rs +678, benchmark Rs +599, intramonth Rs +387, intraweek Rs +364, oracle Rs +337, snake_abs_exit Rs +298, random_hold Rs +235, snake_abs_exit_conv Rs +227, snake_viper_wild Rs +198, snake_abs_conv Rs +195, snake_abs Rs +193, snake_viper_tick Rs +90, nifty_calls Rs +48, snake_anaconda Rs +27, benchmark_smallcap Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -914

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.