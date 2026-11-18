# Paper trading report

Updated 2026-11-18 12:04 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,091 | +11.54% | 0 | - | 236 |
| benchmark | 220,073 | +10.04% | 0 | - | 237 |
| intraweek | 213,767 | +6.88% | 35 | 54% | 3,851 |
| intramonth | 212,832 | +6.42% | 0 | - | 235 |
| snake_abs_exit | 212,720 | +6.36% | 2 | 50% | 345 |
| oracle | 212,334 | +6.17% | 0 | - | 233 |
| snake_abs_exit_conv | 211,031 | +5.51% | 2 | 50% | 345 |
| snake_abs | 207,932 | +3.97% | 1 | 100% | 255 |
| snake_abs_conv | 207,798 | +3.90% | 1 | 100% | 255 |
| random_hold | 207,311 | +3.65% | 10 | 70% | 733 |
| snake_viper_wild | 206,972 | +3.49% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,437 | +1.72% | 15 | 47% | 2,625 |
| snake_anaconda | 203,113 | +1.56% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,316 | -0.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,107 | -11.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,473 (-4.26%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,652 | +0.75% |
| intramonth | +1,289 | +0.61% |
| intraweek | +444 | +0.21% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -152 | -0.07% |
| snake_abs_exit | -422 | -0.20% |
| snake_abs_exit_conv | -543 | -0.26% |
| snake_abs_conv | -621 | -0.30% |
| snake_abs | -627 | -0.30% |
| snake_anaconda | -942 | -0.46% |
| random_hold | -1,122 | -0.54% |
| benchmark_smallcap | -1,256 | -0.63% |
| benchmark | -1,530 | -0.69% |
| snake_viper_tick | -2,399 | -1.17% |
| snake_viper_wild | -2,443 | -1.17% |
| gold | -3,617 | -2.00% |

Average per day so far: unified Rs +641, benchmark Rs +558, snake_abs_exit Rs +385, intraweek Rs +382, intramonth Rs +356, oracle Rs +343, snake_abs_exit_conv Rs +334, snake_viper_wild Rs +249, snake_abs_conv Rs +236, snake_abs Rs +233, random_hold Rs +203, snake_viper_tick Rs +137, snake_anaconda Rs +100, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -21, snake_nonews Rs -326, snake Rs -347, gold Rs -636

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.