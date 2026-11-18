# Paper trading report

Updated 2026-11-18 09:31 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,826 | +10.91% | 0 | - | 236 |
| benchmark | 220,930 | +10.46% | 0 | - | 237 |
| snake_abs_exit | 213,521 | +6.76% | 2 | 50% | 345 |
| intraweek | 212,923 | +6.46% | 35 | 54% | 3,851 |
| oracle | 212,674 | +6.34% | 0 | - | 233 |
| snake_abs_exit_conv | 211,853 | +5.93% | 2 | 50% | 345 |
| intramonth | 211,661 | +5.83% | 0 | - | 235 |
| snake_abs | 209,047 | +4.52% | 1 | 100% | 255 |
| snake_abs_conv | 208,911 | +4.46% | 1 | 100% | 255 |
| snake_viper_wild | 207,588 | +3.79% | 16 | 50% | 2,827 |
| random_hold | 207,305 | +3.65% | 10 | 70% | 733 |
| snake_anaconda | 204,228 | +2.11% | 3 | 33% | 374 |
| snake_viper_tick | 204,040 | +2.02% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,992 | -11.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,070 (-4.47%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +492 | +0.24% |
| snake_abs | +488 | +0.23% |
| unified | +388 | +0.17% |
| snake_abs_exit | +379 | +0.18% |
| snake_abs_exit_conv | +279 | +0.13% |
| oracle | +188 | +0.09% |
| snake_anaconda | +173 | +0.09% |
| intramonth | +119 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| benchmark_smallcap | -348 | -0.17% |
| intraweek | -400 | -0.19% |
| benchmark | -673 | -0.30% |
| random_hold | -1,127 | -0.54% |
| snake_viper_tick | -1,796 | -0.87% |
| snake_viper_wild | -1,827 | -0.87% |
| gold | -3,732 | -2.06% |

Average per day so far: unified Rs +606, benchmark Rs +581, snake_abs_exit Rs +410, snake_abs_exit_conv Rs +359, intraweek Rs +359, oracle Rs +352, intramonth Rs +324, snake_viper_wild Rs +271, snake_abs_conv Rs +270, snake_abs Rs +266, random_hold Rs +203, snake_viper_tick Rs +162, snake_anaconda Rs +136, nifty_calls Rs +51, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -639

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.