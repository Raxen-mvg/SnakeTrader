# Paper trading report

Updated 2026-11-20 14:06 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,319 | +13.16% | 0 | - | 236 |
| benchmark | 224,487 | +12.24% | 0 | - | 237 |
| intraweek | 215,689 | +7.84% | 35 | 54% | 3,851 |
| intramonth | 215,200 | +7.60% | 0 | - | 235 |
| oracle | 212,702 | +6.35% | 0 | - | 233 |
| random_hold | 210,200 | +5.10% | 11 | 73% | 979 |
| snake_abs_exit | 208,774 | +4.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,847 | +3.42% | 2 | 50% | 345 |
| snake_abs | 205,975 | +2.99% | 1 | 100% | 255 |
| snake_abs_conv | 205,844 | +2.92% | 1 | 100% | 255 |
| snake_viper_wild | 203,503 | +1.75% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,132 | +0.57% | 0 | - | 237 |
| snake_anaconda | 200,134 | +0.07% | 3 | 33% | 374 |
| snake_viper_tick | 200,033 | +0.02% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,082 | -15.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,070 (-3.97%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,800 | +1.31% |
| benchmark | +2,111 | +0.95% |
| random_hold | +1,747 | +0.84% |
| unified | +1,704 | +0.76% |
| intramonth | +1,192 | +0.56% |
| oracle | +613 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -336 | -0.17% |
| snake_abs | -3,005 | -1.44% |
| snake_abs_conv | -3,016 | -1.44% |
| snake_anaconda | -3,330 | -1.64% |
| snake_viper_tick | -3,944 | -1.93% |
| snake_viper_wild | -4,020 | -1.94% |
| snake_abs_exit_conv | -4,218 | -2.00% |
| snake_abs_exit | -4,577 | -2.15% |
| gold | -6,691 | -3.83% |

Average per day so far: unified Rs +693, benchmark Rs +644, intraweek Rs +413, intramonth Rs +400, oracle Rs +334, random_hold Rs +268, snake_abs_exit Rs +251, snake_abs_exit_conv Rs +196, snake_abs_conv Rs +167, snake_abs Rs +166, snake_viper_wild Rs +117, nifty_calls Rs +48, benchmark_smallcap Rs +33, snake_anaconda Rs +4, snake_viper_tick Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -840

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.