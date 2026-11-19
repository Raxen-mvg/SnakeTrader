# Paper trading report

Updated 2026-11-19 11:14 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,567 | +11.78% | 0 | - | 236 |
| benchmark | 220,854 | +10.43% | 0 | - | 237 |
| snake_abs_exit | 213,872 | +6.94% | 2 | 50% | 345 |
| intramonth | 213,086 | +6.54% | 0 | - | 235 |
| snake_abs_exit_conv | 211,891 | +5.95% | 2 | 50% | 345 |
| intraweek | 211,687 | +5.84% | 35 | 54% | 3,851 |
| oracle | 210,846 | +5.42% | 0 | - | 233 |
| snake_abs | 209,423 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,302 | +4.65% | 1 | 100% | 255 |
| random_hold | 207,633 | +3.82% | 10 | 70% | 733 |
| snake_viper_wild | 207,600 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,052 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,595 | +1.80% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,414 | -12.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,081 (-4.46%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,065 | +0.53% |
| unified | +956 | +0.43% |
| intramonth | +812 | +0.38% |
| random_hold | +700 | +0.34% |
| snake_viper_wild | +560 | +0.27% |
| benchmark | +558 | +0.25% |
| snake_viper_tick | +549 | +0.27% |
| oracle | +50 | +0.02% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -13 | -0.01% |
| snake_abs_conv | -23 | -0.01% |
| intraweek | -152 | -0.07% |
| snake_abs_exit | -160 | -0.07% |
| snake_abs_exit_conv | -492 | -0.23% |
| snake_anaconda | -806 | -0.39% |
| gold | -1,907 | -1.07% |

Average per day so far: unified Rs +637, benchmark Rs +564, snake_abs_exit Rs +408, intramonth Rs +354, snake_abs_exit_conv Rs +350, intraweek Rs +316, oracle Rs +293, snake_abs_conv Rs +274, snake_abs Rs +269, snake_viper_wild Rs +262, random_hold Rs +206, snake_viper_tick Rs +156, snake_anaconda Rs +112, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -664

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.