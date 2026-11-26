# Paper trading report

Updated 2026-11-26 12:18 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,147 | +13.07% | 0 | - | 237 |
| unified | 223,443 | +11.72% | 0 | - | 236 |
| oracle | 213,106 | +6.55% | 0 | - | 233 |
| intramonth | 210,601 | +5.30% | 0 | - | 235 |
| random_hold | 209,742 | +4.87% | 13 | 69% | 1,037 |
| intraweek | 208,282 | +4.14% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,851 | +0.43% | 0 | - | 237 |
| snake_abs_exit | 200,701 | +0.35% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,119 | +0.06% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,411 | -0.79% | 1 | 100% | 255 |
| snake_abs_conv | 198,216 | -0.89% | 1 | 100% | 255 |
| snake_anaconda | 192,297 | -3.85% | 3 | 33% | 374 |
| snake_viper_wild | 192,105 | -3.95% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,842 | -5.58% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,824 (-5.59%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,040 | +1.03% |
| intraweek | +1,539 | +0.74% |
| gold | +1,463 | +0.89% |
| benchmark | +1,125 | +0.50% |
| random_hold | +249 | +0.12% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -657 | -0.29% |
| oracle | -690 | -0.32% |
| intramonth | -1,092 | -0.52% |
| snake_abs_exit | -1,555 | -0.77% |
| snake_abs | -1,738 | -0.87% |
| snake_abs_conv | -1,756 | -0.88% |
| snake_abs_exit_conv | -1,857 | -0.92% |
| snake_anaconda | -2,256 | -1.16% |
| snake_viper_tick | -5,334 | -2.75% |
| snake_viper_wild | -5,439 | -2.75% |

Average per day so far: benchmark Rs +638, unified Rs +572, oracle Rs +320, intramonth Rs +259, random_hold Rs +238, intraweek Rs +202, nifty_calls Rs +45, benchmark_smallcap Rs +23, snake_abs_exit Rs +18, snake_abs_exit_conv Rs +3, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -41, snake_abs_conv Rs -47, snake_anaconda Rs -214, snake_viper_wild Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -372, gold Rs -828

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.