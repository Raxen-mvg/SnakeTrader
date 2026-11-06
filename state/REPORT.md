# Paper trading report

Updated 2026-11-06 10:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,589 | +7.29% | 0 | - | 236 |
| benchmark | 214,397 | +7.20% | 0 | - | 237 |
| intraweek | 210,662 | +5.33% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,295 | +4.65% | 1 | 100% | 255 |
| snake_abs_exit | 209,081 | +4.54% | 1 | 100% | 260 |
| intramonth | 206,615 | +3.31% | 0 | - | 235 |
| snake_abs | 206,248 | +3.12% | 1 | 100% | 255 |
| snake_abs_conv | 206,081 | +3.04% | 1 | 100% | 255 |
| oracle | 204,723 | +2.36% | 0 | - | 233 |
| random_hold | 203,136 | +1.57% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,213 | -1.39% | 3 | 33% | 702 |
| snake_anaconda | 196,601 | -1.70% | 3 | 33% | 374 |
| benchmark_smallcap | 194,585 | -2.71% | 0 | - | 237 |
| snake_viper_tick | 193,871 | -3.06% | 2 | 0% | 532 |
| gold | 189,865 | -5.07% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,254 (-6.37%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,244 | +0.59% |
| oracle | +651 | +0.32% |
| benchmark | +627 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,187 | -0.58% |
| intramonth | -1,333 | -0.64% |
| unified | -1,395 | -0.65% |
| benchmark_smallcap | -4,103 | -2.06% |
| gold | -4,357 | -2.24% |
| snake_abs | -5,440 | -2.57% |
| snake_abs_conv | -5,464 | -2.58% |
| snake_abs_exit_conv | -5,509 | -2.56% |
| snake_abs_exit | -5,577 | -2.60% |
| snake_anaconda | -5,879 | -2.90% |
| snake_viper_tick | -7,267 | -3.61% |
| snake_viper_wild | -7,443 | -3.64% |

Average per day so far: unified Rs +503, benchmark Rs +496, intraweek Rs +368, snake_abs_exit_conv Rs +357, snake_abs_exit Rs +349, snake_abs_conv Rs +234, snake_abs Rs +231, intramonth Rs +228, oracle Rs +163, random_hold Rs +108, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -133, snake_anaconda Rs -142, benchmark_smallcap Rs -217, snake_viper_tick Rs -341, gold Rs -349, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.