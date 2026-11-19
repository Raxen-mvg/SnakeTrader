# Paper trading report

Updated 2026-11-19 13:15 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,650 | +11.82% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| intramonth | 213,280 | +6.64% | 0 | - | 235 |
| snake_abs_exit | 212,770 | +6.38% | 2 | 50% | 345 |
| intraweek | 211,907 | +5.95% | 35 | 54% | 3,851 |
| oracle | 211,768 | +5.88% | 0 | - | 233 |
| snake_abs_exit_conv | 210,849 | +5.42% | 2 | 50% | 345 |
| snake_abs | 208,400 | +4.20% | 1 | 100% | 255 |
| snake_abs_conv | 208,267 | +4.13% | 1 | 100% | 255 |
| snake_viper_wild | 207,720 | +3.86% | 16 | 50% | 2,827 |
| random_hold | 207,653 | +3.83% | 10 | 70% | 733 |
| snake_viper_tick | 204,170 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,218 | +1.61% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,019 | -12.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,326 (-4.34%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,233 | +0.62% |
| benchmark | +1,232 | +0.56% |
| unified | +1,039 | +0.47% |
| intramonth | +1,006 | +0.47% |
| oracle | +972 | +0.46% |
| random_hold | +721 | +0.35% |
| snake_viper_wild | +680 | +0.33% |
| snake_viper_tick | +666 | +0.33% |
| intraweek | +68 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -1,036 | -0.49% |
| snake_abs_conv | -1,058 | -0.51% |
| snake_anaconda | -1,183 | -0.58% |
| snake_abs_exit | -1,262 | -0.59% |
| snake_abs_exit_conv | -1,535 | -0.72% |
| gold | -2,302 | -1.30% |

Average per day so far: unified Rs +639, benchmark Rs +582, snake_abs_exit Rs +376, intramonth Rs +359, intraweek Rs +322, snake_abs_exit_conv Rs +319, oracle Rs +318, snake_viper_wild Rs +266, snake_abs_conv Rs +243, snake_abs Rs +240, random_hold Rs +207, snake_viper_tick Rs +160, snake_anaconda Rs +101, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -675

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.