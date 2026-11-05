# Paper trading report

Updated 2026-11-05 09:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,114 | +9.06% | 0 | - | 236 |
| snake_abs_exit_conv | 216,571 | +8.29% | 1 | 100% | 255 |
| snake_abs_exit | 216,284 | +8.14% | 1 | 100% | 260 |
| snake_abs | 213,435 | +6.72% | 1 | 100% | 255 |
| snake_abs_conv | 213,287 | +6.64% | 1 | 100% | 255 |
| benchmark | 212,645 | +6.32% | 0 | - | 237 |
| intraweek | 210,634 | +5.32% | 25 | 48% | 2,757 |
| intramonth | 210,006 | +5.00% | 0 | - | 235 |
| snake_viper_wild | 206,418 | +3.21% | 3 | 33% | 702 |
| random_hold | 205,528 | +2.76% | 8 | 62% | 649 |
| oracle | 204,251 | +2.12% | 0 | - | 233 |
| snake_anaconda | 203,557 | +1.78% | 3 | 33% | 374 |
| snake_viper_tick | 202,890 | +1.45% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,473 | -0.26% | 0 | - | 237 |
| gold | 195,224 | -2.39% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,818 (-4.59%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,886 | +1.86% |
| gold | +3,831 | +2.00% |
| unified | +3,675 | +1.71% |
| intramonth | +2,990 | +1.44% |
| benchmark_smallcap | +2,802 | +1.43% |
| oracle | +2,458 | +1.22% |
| random_hold | +2,219 | +1.09% |
| snake_abs_exit_conv | +1,556 | +0.72% |
| snake_abs | +1,532 | +0.72% |
| snake_abs_conv | +1,528 | +0.72% |
| snake_abs_exit | +1,383 | +0.64% |
| intraweek | +936 | +0.45% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -264 | -0.13% |
| snake_viper_tick | -2,510 | -1.22% |
| snake_viper_wild | -2,612 | -1.25% |

Average per day so far: snake_abs_exit_conv Rs +663, snake_abs_exit Rs +651, unified Rs +647, snake_abs_conv Rs +531, snake_abs Rs +517, benchmark Rs +452, intraweek Rs +380, intramonth Rs +357, snake_viper_wild Rs +321, random_hold Rs +197, snake_viper_tick Rs +170, snake_anaconda Rs +155, oracle Rs +152, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -22, gold Rs -171, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.