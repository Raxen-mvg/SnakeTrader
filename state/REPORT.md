# Paper trading report

Updated 2026-11-17 10:05 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,678 | +11.34% | 0 | - | 236 |
| benchmark | 221,183 | +10.59% | 0 | - | 237 |
| snake_abs_exit | 215,352 | +7.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,978 | +6.99% | 2 | 50% | 345 |
| oracle | 212,806 | +6.40% | 0 | - | 233 |
| intramonth | 212,703 | +6.35% | 0 | - | 235 |
| intraweek | 212,690 | +6.34% | 35 | 54% | 3,851 |
| snake_abs | 210,378 | +5.19% | 1 | 100% | 255 |
| snake_abs_conv | 210,227 | +5.11% | 1 | 100% | 255 |
| random_hold | 207,822 | +3.91% | 10 | 70% | 733 |
| snake_viper_wild | 206,685 | +3.34% | 14 | 50% | 2,496 |
| snake_anaconda | 205,665 | +2.83% | 3 | 33% | 374 |
| snake_viper_tick | 203,151 | +1.58% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,051 | +1.02% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,069 | -9.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,631 (-4.18%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,424 | +0.67% |
| unified | +1,241 | +0.56% |
| benchmark_smallcap | +1,222 | +0.61% |
| benchmark | +1,102 | +0.50% |
| intramonth | +1,084 | +0.51% |
| snake_abs_exit | +943 | +0.44% |
| oracle | +783 | +0.37% |
| snake_abs_exit_conv | +761 | +0.36% |
| snake_anaconda | +562 | +0.27% |
| snake_viper_wild | +541 | +0.26% |
| snake_viper_tick | +532 | +0.26% |
| snake_abs | +244 | +0.12% |
| snake_abs_conv | +237 | +0.11% |
| gold | +115 | +0.06% |
| random_hold | +29 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +648, benchmark Rs +605, snake_abs_exit Rs +480, snake_abs_exit_conv Rs +437, oracle Rs +366, intramonth Rs +363, intraweek Rs +363, snake_abs_conv Rs +320, snake_abs Rs +314, snake_viper_wild Rs +248, random_hold Rs +223, snake_anaconda Rs +189, snake_viper_tick Rs +131, benchmark_smallcap Rs +66, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -541

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.