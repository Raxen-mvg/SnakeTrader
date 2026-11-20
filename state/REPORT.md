# Paper trading report

Updated 2026-11-20 11:12 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,655 | +12.83% | 0 | - | 236 |
| benchmark | 222,804 | +11.40% | 0 | - | 237 |
| intramonth | 214,646 | +7.32% | 0 | - | 235 |
| intraweek | 214,090 | +7.04% | 35 | 54% | 3,851 |
| oracle | 212,640 | +6.32% | 0 | - | 233 |
| snake_abs_exit | 210,631 | +5.32% | 2 | 50% | 345 |
| random_hold | 209,053 | +4.53% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,264 | +4.13% | 2 | 50% | 345 |
| snake_abs | 207,433 | +3.72% | 1 | 100% | 255 |
| snake_abs_conv | 207,295 | +3.65% | 1 | 100% | 255 |
| snake_viper_wild | 206,834 | +3.42% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,303 | +1.65% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,334 | +0.67% | 3 | 33% | 374 |
| benchmark_smallcap | 200,336 | +0.17% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,876 | -17.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,938 (-4.03%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,200 | +0.56% |
| unified | +1,040 | +0.46% |
| intramonth | +638 | +0.30% |
| random_hold | +600 | +0.29% |
| oracle | +551 | +0.26% |
| benchmark | +428 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -674 | -0.33% |
| snake_viper_wild | -689 | -0.33% |
| benchmark_smallcap | -1,132 | -0.56% |
| snake_abs | -1,546 | -0.74% |
| snake_abs_conv | -1,565 | -0.75% |
| snake_anaconda | -2,130 | -1.05% |
| snake_abs_exit | -2,720 | -1.27% |
| snake_abs_exit_conv | -2,801 | -1.33% |
| gold | -9,897 | -5.66% |

Average per day so far: unified Rs +675, benchmark Rs +600, intramonth Rs +385, intraweek Rs +371, oracle Rs +333, snake_abs_exit Rs +304, random_hold Rs +238, snake_abs_exit_conv Rs +236, snake_viper_wild Rs +228, snake_abs_conv Rs +208, snake_abs Rs +206, snake_viper_tick Rs +122, nifty_calls Rs +48, snake_anaconda Rs +40, benchmark_smallcap Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -924

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.