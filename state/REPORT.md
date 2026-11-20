# Paper trading report

Updated 2026-11-20 11:34 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,705 | +12.85% | 0 | - | 236 |
| benchmark | 222,881 | +11.44% | 0 | - | 237 |
| intramonth | 214,715 | +7.36% | 0 | - | 235 |
| intraweek | 214,478 | +7.24% | 35 | 54% | 3,851 |
| oracle | 212,997 | +6.50% | 0 | - | 233 |
| snake_abs_exit | 210,020 | +5.01% | 2 | 50% | 345 |
| random_hold | 209,338 | +4.67% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,891 | +3.95% | 2 | 50% | 345 |
| snake_abs | 207,590 | +3.79% | 1 | 100% | 255 |
| snake_abs_conv | 207,448 | +3.72% | 1 | 100% | 255 |
| snake_viper_wild | 205,786 | +2.89% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,274 | +1.14% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,391 | +0.69% | 3 | 33% | 374 |
| benchmark_smallcap | 200,538 | +0.27% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,022 (-3.99%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,589 | +0.75% |
| unified | +1,090 | +0.48% |
| oracle | +908 | +0.43% |
| random_hold | +885 | +0.42% |
| intramonth | +707 | +0.33% |
| benchmark | +505 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -930 | -0.46% |
| snake_abs | -1,390 | -0.67% |
| snake_abs_conv | -1,412 | -0.68% |
| snake_viper_tick | -1,702 | -0.83% |
| snake_viper_wild | -1,737 | -0.84% |
| snake_anaconda | -2,073 | -1.02% |
| snake_abs_exit_conv | -3,173 | -1.50% |
| snake_abs_exit | -3,331 | -1.56% |
| gold | -8,713 | -4.99% |

Average per day so far: unified Rs +676, benchmark Rs +602, intramonth Rs +387, intraweek Rs +381, oracle Rs +342, snake_abs_exit Rs +286, random_hold Rs +246, snake_abs_exit_conv Rs +225, snake_abs_conv Rs +213, snake_abs Rs +211, snake_viper_wild Rs +193, snake_viper_tick Rs +84, nifty_calls Rs +48, snake_anaconda Rs +42, benchmark_smallcap Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -893

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.