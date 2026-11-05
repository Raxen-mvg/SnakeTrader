# Paper trading report

Updated 2026-11-05 12:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,207 | +9.10% | 0 | - | 236 |
| snake_abs_exit_conv | 213,838 | +6.92% | 1 | 100% | 255 |
| snake_abs_exit | 213,551 | +6.78% | 1 | 100% | 260 |
| benchmark | 212,760 | +6.38% | 0 | - | 237 |
| snake_abs | 210,724 | +5.36% | 1 | 100% | 255 |
| snake_abs_conv | 210,589 | +5.29% | 1 | 100% | 255 |
| intraweek | 210,422 | +5.21% | 25 | 48% | 2,757 |
| intramonth | 209,998 | +5.00% | 0 | - | 235 |
| snake_viper_wild | 206,915 | +3.46% | 3 | 33% | 702 |
| random_hold | 206,663 | +3.33% | 8 | 62% | 649 |
| oracle | 204,125 | +2.06% | 0 | - | 233 |
| snake_viper_tick | 203,357 | +1.68% | 2 | 0% | 532 |
| snake_anaconda | 202,099 | +1.05% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| gold | 193,925 | -3.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,042 (-4.98%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,001 | +1.92% |
| unified | +3,767 | +1.76% |
| random_hold | +3,354 | +1.65% |
| intramonth | +2,982 | +1.44% |
| benchmark_smallcap | +2,545 | +1.29% |
| gold | +2,532 | +1.32% |
| oracle | +2,333 | +1.16% |
| intraweek | +724 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,169 | -0.55% |
| snake_abs_exit_conv | -1,177 | -0.55% |
| snake_abs | -1,179 | -0.56% |
| snake_abs_exit | -1,349 | -0.63% |
| snake_anaconda | -1,721 | -0.84% |
| snake_viper_tick | -2,043 | -0.99% |
| snake_viper_wild | -2,115 | -1.01% |

Average per day so far: unified Rs +650, snake_abs_exit_conv Rs +554, snake_abs_exit Rs +542, benchmark Rs +456, snake_abs_conv Rs +424, snake_abs Rs +412, intraweek Rs +372, intramonth Rs +357, snake_viper_wild Rs +346, random_hold Rs +238, snake_viper_tick Rs +197, oracle Rs +147, snake_anaconda Rs +91, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -217, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.