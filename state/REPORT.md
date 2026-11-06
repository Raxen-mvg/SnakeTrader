# Paper trading report

Updated 2026-11-06 12:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,223 | +7.61% | 0 | - | 237 |
| unified | 214,420 | +7.21% | 0 | - | 236 |
| intraweek | 209,527 | +4.76% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,942 | +4.47% | 1 | 100% | 255 |
| snake_abs_exit | 208,774 | +4.39% | 1 | 100% | 260 |
| intramonth | 206,617 | +3.31% | 0 | - | 235 |
| snake_abs | 205,915 | +2.96% | 1 | 100% | 255 |
| snake_abs_conv | 205,739 | +2.87% | 1 | 100% | 255 |
| oracle | 204,907 | +2.45% | 0 | - | 233 |
| random_hold | 203,219 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,414 | -1.79% | 3 | 33% | 702 |
| snake_anaconda | 196,375 | -1.81% | 3 | 33% | 374 |
| benchmark_smallcap | 194,787 | -2.61% | 0 | - | 237 |
| snake_viper_tick | 193,088 | -3.46% | 2 | 0% | 532 |
| gold | 190,144 | -4.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,998 (-6.50%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,454 | +0.68% |
| oracle | +835 | +0.41% |
| intraweek | +109 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,104 | -0.54% |
| intramonth | -1,332 | -0.64% |
| unified | -1,564 | -0.72% |
| benchmark_smallcap | -3,901 | -1.96% |
| gold | -4,077 | -2.10% |
| snake_abs | -5,774 | -2.73% |
| snake_abs_conv | -5,806 | -2.74% |
| snake_abs_exit_conv | -5,861 | -2.73% |
| snake_abs_exit | -5,884 | -2.74% |
| snake_anaconda | -6,104 | -3.02% |
| snake_viper_tick | -8,050 | -4.00% |
| snake_viper_wild | -8,242 | -4.03% |

Average per day so far: benchmark Rs +525, unified Rs +497, snake_abs_exit_conv Rs +344, snake_abs_exit Rs +337, intraweek Rs +329, intramonth Rs +228, snake_abs_conv Rs +221, snake_abs Rs +219, oracle Rs +169, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -151, snake_viper_wild Rs -171, benchmark_smallcap Rs -209, gold Rs -340, snake_viper_tick Rs -384, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.