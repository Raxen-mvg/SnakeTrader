# Paper trading report

Updated 2026-11-06 12:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,292 | +7.65% | 0 | - | 237 |
| unified | 214,784 | +7.39% | 0 | - | 236 |
| snake_abs_exit_conv | 208,891 | +4.45% | 1 | 100% | 255 |
| intraweek | 208,877 | +4.44% | 25 | 48% | 2,757 |
| snake_abs_exit | 208,699 | +4.35% | 1 | 100% | 260 |
| intramonth | 207,015 | +3.51% | 0 | - | 235 |
| snake_abs | 205,858 | +2.93% | 1 | 100% | 255 |
| snake_abs_conv | 205,684 | +2.84% | 1 | 100% | 255 |
| oracle | 205,001 | +2.50% | 0 | - | 233 |
| random_hold | 203,175 | +1.59% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,157 | -1.92% | 3 | 33% | 374 |
| snake_viper_wild | 195,568 | -2.22% | 3 | 33% | 702 |
| benchmark_smallcap | 195,000 | -2.50% | 0 | - | 237 |
| snake_viper_tick | 192,257 | -3.87% | 2 | 0% | 532 |
| gold | 190,309 | -4.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,973 (-6.51%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,522 | +0.71% |
| oracle | +929 | +0.46% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -541 | -0.26% |
| intramonth | -934 | -0.45% |
| random_hold | -1,148 | -0.56% |
| unified | -1,199 | -0.56% |
| benchmark_smallcap | -3,688 | -1.86% |
| gold | -3,913 | -2.02% |
| snake_abs | -5,830 | -2.75% |
| snake_abs_conv | -5,861 | -2.77% |
| snake_abs_exit_conv | -5,912 | -2.75% |
| snake_abs_exit | -5,960 | -2.78% |
| snake_anaconda | -6,322 | -3.12% |
| snake_viper_tick | -8,881 | -4.42% |
| snake_viper_wild | -9,088 | -4.44% |

Average per day so far: benchmark Rs +527, unified Rs +510, snake_abs_exit_conv Rs +342, snake_abs_exit Rs +335, intraweek Rs +306, intramonth Rs +242, snake_abs_conv Rs +219, snake_abs Rs +217, oracle Rs +172, random_hold Rs +109, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -160, benchmark_smallcap Rs -200, snake_viper_wild Rs -211, gold Rs -334, snake_nonews Rs -411, snake_viper_tick Rs -430, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.