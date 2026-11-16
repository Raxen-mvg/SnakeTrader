# Paper trading report

Updated 2026-11-16 14:22 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,359 | +10.18% | 0 | - | 236 |
| benchmark | 219,920 | +9.96% | 0 | - | 237 |
| snake_abs_exit | 213,408 | +6.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,170 | +6.08% | 2 | 50% | 345 |
| oracle | 211,111 | +5.55% | 0 | - | 233 |
| intramonth | 210,902 | +5.45% | 0 | - | 235 |
| intraweek | 210,589 | +5.29% | 35 | 54% | 3,851 |
| snake_abs | 209,417 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,255 | +4.63% | 1 | 100% | 255 |
| random_hold | 207,644 | +3.82% | 10 | 70% | 733 |
| snake_viper_wild | 205,452 | +2.73% | 14 | 50% | 2,496 |
| snake_anaconda | 203,822 | +1.91% | 3 | 33% | 374 |
| snake_viper_tick | 201,938 | +0.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,325 | +0.16% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,316 | -9.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,108 (-4.95%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,338 | +0.61% |
| intramonth | +846 | +0.40% |
| snake_viper_wild | +695 | +0.34% |
| snake_viper_tick | +683 | +0.34% |
| benchmark | +581 | +0.27% |
| random_hold | +418 | +0.20% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -1,070 | -0.52% |
| oracle | -1,987 | -0.93% |
| benchmark_smallcap | -2,545 | -1.25% |
| gold | -2,680 | -1.46% |
| snake_abs_conv | -3,112 | -1.47% |
| snake_abs | -3,123 | -1.47% |
| snake_abs_exit | -3,577 | -1.65% |
| snake_abs_exit_conv | -4,212 | -1.95% |
| intraweek | -5,556 | -2.57% |

Average per day so far: unified Rs +599, benchmark Rs +586, snake_abs_exit Rs +433, snake_abs_exit_conv Rs +393, oracle Rs +327, intramonth Rs +321, intraweek Rs +311, snake_abs_conv Rs +299, snake_abs Rs +294, random_hold Rs +225, snake_viper_wild Rs +210, snake_anaconda Rs +132, snake_viper_tick Rs +84, nifty_calls Rs +54, benchmark_smallcap Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -550

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.