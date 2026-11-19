# Paper trading report

Updated 2026-11-19 09:24 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,410 | +11.71% | 0 | - | 236 |
| benchmark | 219,500 | +9.75% | 0 | - | 237 |
| intramonth | 213,305 | +6.65% | 0 | - | 235 |
| snake_abs_exit | 212,530 | +6.26% | 2 | 50% | 345 |
| intraweek | 211,336 | +5.67% | 35 | 54% | 3,851 |
| oracle | 211,085 | +5.54% | 0 | - | 233 |
| snake_abs_exit_conv | 210,925 | +5.46% | 2 | 50% | 345 |
| snake_abs | 208,272 | +4.14% | 1 | 100% | 255 |
| snake_abs_conv | 208,146 | +4.07% | 1 | 100% | 255 |
| snake_viper_wild | 207,572 | +3.79% | 16 | 50% | 2,827 |
| random_hold | 206,913 | +3.46% | 10 | 70% | 733 |
| snake_viper_tick | 204,025 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 203,311 | +1.66% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,912 | -0.54% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,378 | -12.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,951 (-4.52%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,031 | +0.49% |
| unified | +798 | +0.36% |
| snake_viper_wild | +533 | +0.26% |
| snake_viper_tick | +522 | +0.26% |
| oracle | +289 | +0.14% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -20 | -0.01% |
| benchmark_smallcap | -415 | -0.21% |
| intraweek | -504 | -0.24% |
| benchmark | -796 | -0.36% |
| snake_anaconda | -1,090 | -0.53% |
| snake_abs | -1,164 | -0.56% |
| snake_abs_conv | -1,179 | -0.56% |
| snake_abs_exit_conv | -1,459 | -0.69% |
| snake_abs_exit | -1,501 | -0.70% |
| gold | -2,943 | -1.66% |

Average per day so far: unified Rs +633, benchmark Rs +527, snake_abs_exit Rs +369, intramonth Rs +360, snake_abs_exit_conv Rs +321, intraweek Rs +306, oracle Rs +300, snake_viper_wild Rs +261, snake_abs_conv Rs +240, snake_abs Rs +236, random_hold Rs +187, snake_viper_tick Rs +155, snake_anaconda Rs +103, nifty_calls Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, snake_nonews Rs -317, snake Rs -337, gold Rs -692

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.