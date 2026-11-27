# Paper trading report

Updated 2026-11-27 14:43 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,883 | +11.94% | 0 | - | 237 |
| unified | 223,705 | +11.85% | 0 | - | 236 |
| oracle | 211,856 | +5.93% | 0 | - | 233 |
| random_hold | 211,252 | +5.63% | 13 | 69% | 1,037 |
| intramonth | 211,042 | +5.52% | 0 | - | 235 |
| intraweek | 207,884 | +3.94% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,384 | +3.19% | 2 | 50% | 345 |
| snake_abs_exit | 204,046 | +2.02% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,558 | +0.78% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,645 | -0.18% | 1 | 100% | 255 |
| snake_abs_conv | 199,461 | -0.27% | 1 | 100% | 255 |
| snake_anaconda | 192,933 | -3.53% | 3 | 33% | 374 |
| snake_viper_wild | 192,217 | -3.89% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,953 | -5.52% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 171,107 | -14.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,010 (-5.50%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,987 | +2.99% |
| gold | +5,113 | +3.08% |
| snake_abs_exit | +2,969 | +1.48% |
| random_hold | +2,658 | +1.27% |
| snake_abs_conv | +1,094 | +0.55% |
| snake_abs | +1,093 | +0.55% |
| intraweek | +836 | +0.40% |
| benchmark_smallcap | +717 | +0.36% |
| snake_anaconda | +637 | +0.33% |
| unified | +627 | +0.28% |
| intramonth | +509 | +0.24% |
| snake_viper_tick | +12 | +0.01% |
| snake_viper_wild | +11 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -380 | -0.18% |
| benchmark | -2,104 | -0.93% |

Average per day so far: benchmark Rs +569, unified Rs +564, oracle Rs +282, random_hold Rs +268, intramonth Rs +263, intraweek Rs +188, snake_abs_exit_conv Rs +164, snake_abs_exit Rs +104, nifty_calls Rs +44, benchmark_smallcap Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -9, snake_abs_conv Rs -14, snake_anaconda Rs -191, snake_viper_wild Rs -229, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -356, gold Rs -688

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.