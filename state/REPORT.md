# Paper trading report

Updated 2026-11-27 11:43 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,090 | +12.04% | 0 | - | 237 |
| unified | 222,252 | +11.13% | 0 | - | 236 |
| oracle | 211,785 | +5.89% | 0 | - | 233 |
| intramonth | 210,411 | +5.21% | 0 | - | 235 |
| random_hold | 210,222 | +5.11% | 13 | 69% | 1,037 |
| intraweek | 207,636 | +3.82% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,622 | +2.81% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,218 | +2.11% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,726 | +0.86% | 0 | - | 237 |
| snake_abs | 200,936 | +0.47% | 1 | 100% | 255 |
| snake_abs_conv | 200,760 | +0.38% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,356 | -2.82% | 3 | 33% | 374 |
| snake_viper_wild | 193,100 | -3.45% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,817 | -5.09% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,200 | -15.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,441 (-5.78%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,545 | +2.26% |
| snake_abs_exit_conv | +3,821 | +1.91% |
| gold | +3,206 | +1.93% |
| snake_abs_conv | +2,394 | +1.21% |
| snake_abs | +2,384 | +1.20% |
| snake_anaconda | +2,060 | +1.07% |
| random_hold | +1,628 | +0.78% |
| snake_viper_wild | +894 | +0.47% |
| benchmark_smallcap | +886 | +0.44% |
| snake_viper_tick | +876 | +0.46% |
| intraweek | +587 | +0.28% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -122 | -0.06% |
| oracle | -450 | -0.21% |
| unified | -826 | -0.37% |
| benchmark | -1,897 | -0.84% |

Average per day so far: benchmark Rs +574, unified Rs +530, oracle Rs +281, intramonth Rs +248, random_hold Rs +243, intraweek Rs +182, snake_abs_exit Rs +144, snake_abs_exit_conv Rs +108, benchmark_smallcap Rs +45, nifty_calls Rs +44, snake_abs Rs +23, snake_abs_conv Rs +19, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -153, snake_viper_wild Rs -203, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -328, gold Rs -733

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.