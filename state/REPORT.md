# Paper trading report

Updated 2026-11-19 12:11 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,738 | +11.87% | 0 | - | 236 |
| benchmark | 221,328 | +10.66% | 0 | - | 237 |
| intramonth | 213,368 | +6.68% | 0 | - | 235 |
| snake_abs_exit | 212,963 | +6.48% | 2 | 50% | 345 |
| intraweek | 211,603 | +5.80% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,081 | +5.54% | 2 | 50% | 345 |
| oracle | 210,978 | +5.49% | 0 | - | 233 |
| snake_abs | 208,633 | +4.32% | 1 | 100% | 255 |
| snake_abs_conv | 208,500 | +4.25% | 1 | 100% | 255 |
| random_hold | 207,601 | +3.80% | 10 | 70% | 733 |
| snake_viper_wild | 207,571 | +3.79% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,024 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 202,891 | +1.45% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,594 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,904 | -12.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,157 (-4.42%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,267 | +0.64% |
| unified | +1,127 | +0.51% |
| intramonth | +1,095 | +0.52% |
| benchmark | +1,033 | +0.47% |
| random_hold | +668 | +0.32% |
| snake_viper_wild | +531 | +0.26% |
| snake_viper_tick | +521 | +0.26% |
| oracle | +182 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -236 | -0.11% |
| snake_abs | -804 | -0.38% |
| snake_abs_conv | -825 | -0.39% |
| snake_abs_exit | -1,069 | -0.50% |
| snake_abs_exit_conv | -1,302 | -0.61% |
| snake_anaconda | -1,510 | -0.74% |
| gold | -2,417 | -1.36% |

Average per day so far: unified Rs +642, benchmark Rs +576, snake_abs_exit Rs +381, intramonth Rs +361, snake_abs_exit_conv Rs +326, intraweek Rs +314, oracle Rs +297, snake_viper_wild Rs +261, snake_abs_conv Rs +250, snake_abs Rs +247, random_hold Rs +205, snake_viper_tick Rs +155, snake_anaconda Rs +90, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.