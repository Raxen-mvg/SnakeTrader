# Paper trading report

Updated 2026-11-20 13:48 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,581 | +13.29% | 0 | - | 236 |
| benchmark | 224,472 | +12.24% | 0 | - | 237 |
| intraweek | 215,703 | +7.85% | 35 | 54% | 3,851 |
| intramonth | 215,387 | +7.69% | 0 | - | 235 |
| oracle | 212,969 | +6.49% | 0 | - | 233 |
| random_hold | 209,929 | +4.96% | 11 | 73% | 979 |
| snake_abs_exit | 209,145 | +4.57% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,162 | +3.58% | 2 | 50% | 345 |
| snake_abs | 206,245 | +3.12% | 1 | 100% | 255 |
| snake_abs_conv | 206,115 | +3.06% | 1 | 100% | 255 |
| snake_viper_wild | 203,551 | +1.77% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,277 | +0.64% | 0 | - | 237 |
| snake_anaconda | 200,401 | +0.20% | 3 | 33% | 374 |
| snake_viper_tick | 200,080 | +0.04% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,210 | -16.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,207 (-3.90%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,814 | +1.32% |
| benchmark | +2,096 | +0.94% |
| unified | +1,965 | +0.88% |
| random_hold | +1,476 | +0.71% |
| intramonth | +1,379 | +0.65% |
| oracle | +880 | +0.41% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -191 | -0.10% |
| snake_abs | -2,735 | -1.31% |
| snake_abs_conv | -2,745 | -1.31% |
| snake_anaconda | -3,062 | -1.50% |
| snake_viper_tick | -3,897 | -1.91% |
| snake_abs_exit_conv | -3,903 | -1.85% |
| snake_viper_wild | -3,972 | -1.91% |
| snake_abs_exit | -4,206 | -1.97% |
| gold | -7,562 | -4.33% |

Average per day so far: unified Rs +699, benchmark Rs +644, intraweek Rs +413, intramonth Rs +405, oracle Rs +341, snake_abs_exit Rs +261, random_hold Rs +261, snake_abs_exit_conv Rs +205, snake_abs_conv Rs +175, snake_abs Rs +173, snake_viper_wild Rs +118, nifty_calls Rs +48, benchmark_smallcap Rs +38, snake_anaconda Rs +12, snake_viper_tick Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -863

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.