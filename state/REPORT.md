# Paper trading report

Updated 2026-11-19 11:11 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,652 | +11.83% | 0 | - | 236 |
| benchmark | 220,754 | +10.38% | 0 | - | 237 |
| snake_abs_exit | 213,875 | +6.94% | 2 | 50% | 345 |
| intramonth | 213,139 | +6.57% | 0 | - | 235 |
| snake_abs_exit_conv | 211,912 | +5.96% | 2 | 50% | 345 |
| intraweek | 211,689 | +5.84% | 35 | 54% | 3,851 |
| oracle | 210,856 | +5.43% | 0 | - | 233 |
| snake_abs | 209,378 | +4.69% | 1 | 100% | 255 |
| snake_abs_conv | 209,256 | +4.63% | 1 | 100% | 255 |
| random_hold | 207,633 | +3.82% | 10 | 70% | 733 |
| snake_viper_wild | 207,600 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,052 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,550 | +1.77% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,167 | -12.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,109 (-4.45%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,065 | +0.53% |
| unified | +1,041 | +0.47% |
| intramonth | +865 | +0.41% |
| random_hold | +700 | +0.34% |
| snake_viper_wild | +560 | +0.27% |
| snake_viper_tick | +549 | +0.27% |
| benchmark | +459 | +0.21% |
| oracle | +60 | +0.03% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -59 | -0.03% |
| snake_abs_conv | -69 | -0.03% |
| intraweek | -151 | -0.07% |
| snake_abs_exit | -157 | -0.07% |
| snake_abs_exit_conv | -471 | -0.22% |
| snake_anaconda | -851 | -0.42% |
| gold | -2,154 | -1.22% |

Average per day so far: unified Rs +639, benchmark Rs +561, snake_abs_exit Rs +408, intramonth Rs +355, snake_abs_exit_conv Rs +350, intraweek Rs +316, oracle Rs +293, snake_abs_conv Rs +272, snake_abs Rs +268, snake_viper_wild Rs +262, random_hold Rs +206, snake_viper_tick Rs +156, snake_anaconda Rs +111, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -671

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.