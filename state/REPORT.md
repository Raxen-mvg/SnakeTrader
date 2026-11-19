# Paper trading report

Updated 2026-11-19 12:04 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,601 | +11.80% | 0 | - | 236 |
| benchmark | 221,458 | +10.73% | 0 | - | 237 |
| snake_abs_exit | 213,302 | +6.65% | 2 | 50% | 345 |
| intramonth | 213,241 | +6.62% | 0 | - | 235 |
| intraweek | 211,565 | +5.78% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,449 | +5.72% | 2 | 50% | 345 |
| oracle | 210,958 | +5.48% | 0 | - | 233 |
| snake_abs | 208,926 | +4.46% | 1 | 100% | 255 |
| snake_abs_conv | 208,798 | +4.40% | 1 | 100% | 255 |
| snake_viper_wild | 207,600 | +3.80% | 16 | 50% | 2,827 |
| random_hold | 207,592 | +3.80% | 10 | 70% | 733 |
| snake_viper_tick | 204,052 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,188 | +1.59% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,638 | +0.32% | 0 | - | 237 |
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
| benchmark_smallcap | +1,312 | +0.66% |
| benchmark | +1,163 | +0.53% |
| unified | +989 | +0.44% |
| intramonth | +968 | +0.46% |
| random_hold | +660 | +0.32% |
| snake_viper_wild | +560 | +0.27% |
| snake_viper_tick | +549 | +0.27% |
| oracle | +162 | +0.08% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -274 | -0.13% |
| snake_abs | -511 | -0.24% |
| snake_abs_conv | -527 | -0.25% |
| snake_abs_exit | -730 | -0.34% |
| snake_abs_exit_conv | -934 | -0.44% |
| snake_anaconda | -1,213 | -0.59% |
| gold | -2,154 | -1.22% |

Average per day so far: unified Rs +638, benchmark Rs +580, snake_abs_exit Rs +391, intramonth Rs +358, snake_abs_exit_conv Rs +337, intraweek Rs +313, oracle Rs +296, snake_viper_wild Rs +262, snake_abs_conv Rs +259, snake_abs Rs +255, random_hold Rs +205, snake_viper_tick Rs +156, snake_anaconda Rs +100, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -671

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.