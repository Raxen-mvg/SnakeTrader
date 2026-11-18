# Paper trading report

Updated 2026-11-18 14:24 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,321 | +11.16% | 0 | - | 236 |
| benchmark | 220,448 | +10.22% | 0 | - | 237 |
| snake_abs_exit | 214,678 | +7.34% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,887 | +6.44% | 2 | 50% | 345 |
| intraweek | 212,238 | +6.12% | 35 | 54% | 3,851 |
| oracle | 212,111 | +6.06% | 0 | - | 233 |
| intramonth | 211,940 | +5.97% | 0 | - | 235 |
| snake_abs | 209,670 | +4.83% | 1 | 100% | 255 |
| snake_abs_conv | 209,572 | +4.79% | 1 | 100% | 255 |
| snake_viper_wild | 206,996 | +3.50% | 16 | 50% | 2,827 |
| random_hold | 206,906 | +3.45% | 10 | 70% | 733 |
| snake_anaconda | 204,960 | +2.48% | 3 | 33% | 374 |
| snake_viper_tick | 203,461 | +1.73% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,652 | -0.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,009 | -11.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,945 (-4.53%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +1,536 | +0.72% |
| snake_abs_exit_conv | +1,313 | +0.62% |
| snake_abs_conv | +1,152 | +0.55% |
| snake_abs | +1,112 | +0.53% |
| snake_anaconda | +905 | +0.44% |
| unified | +882 | +0.40% |
| intramonth | +398 | +0.19% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -375 | -0.18% |
| benchmark_smallcap | -919 | -0.46% |
| intraweek | -1,085 | -0.51% |
| benchmark | -1,155 | -0.52% |
| random_hold | -1,527 | -0.73% |
| snake_viper_tick | -2,376 | -1.15% |
| snake_viper_wild | -2,419 | -1.16% |
| gold | -3,715 | -2.06% |

Average per day so far: unified Rs +620, benchmark Rs +568, snake_abs_exit Rs +445, snake_abs_exit_conv Rs +391, intraweek Rs +340, oracle Rs +336, intramonth Rs +332, snake_abs_conv Rs +290, snake_abs Rs +284, snake_viper_wild Rs +250, random_hold Rs +192, snake_anaconda Rs +160, snake_viper_tick Rs +138, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -11, snake_nonews Rs -326, snake Rs -347, gold Rs -639

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.