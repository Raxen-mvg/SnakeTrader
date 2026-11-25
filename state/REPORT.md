# Paper trading report

Updated 2026-11-25 12:37 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,323 | +12.66% | 0 | - | 236 |
| benchmark | 225,237 | +12.62% | 0 | - | 237 |
| intramonth | 213,431 | +6.72% | 0 | - | 235 |
| oracle | 212,922 | +6.46% | 0 | - | 233 |
| random_hold | 210,073 | +5.04% | 12 | 75% | 1,009 |
| intraweek | 208,391 | +4.20% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,396 | +1.20% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,154 | +1.08% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,866 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,682 | +0.34% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_viper_wild | 196,958 | -1.52% | 16 | 50% | 2,827 |
| snake_anaconda | 194,120 | -2.94% | 3 | 33% | 374 |
| snake_viper_tick | 193,603 | -3.20% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,481 | -17.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,661 (-5.17%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,764 | +1.70% |
| random_hold | +1,646 | +0.79% |
| unified | +1,038 | +0.46% |
| intramonth | +680 | +0.32% |
| oracle | +580 | +0.27% |
| benchmark_smallcap | +572 | +0.29% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,228 | -1.52% |
| snake_viper_tick | -4,089 | -2.07% |
| snake_viper_wild | -4,167 | -2.07% |
| snake_anaconda | -4,584 | -2.31% |
| snake_abs | -4,595 | -2.24% |
| snake_abs_conv | -4,620 | -2.25% |
| snake_abs_exit_conv | -4,891 | -2.36% |
| gold | -4,948 | -2.92% |
| snake_abs_exit | -5,099 | -2.46% |

Average per day so far: unified Rs +633, benchmark Rs +631, intramonth Rs +336, oracle Rs +323, random_hold Rs +252, intraweek Rs +210, snake_abs_exit Rs +65, snake_abs_exit_conv Rs +58, nifty_calls Rs +46, snake_abs Rs +23, snake_abs_conv Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_viper_wild Rs -95, snake_anaconda Rs -168, snake_viper_tick Rs -221, snake_nonews Rs -292, snake Rs -311, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.