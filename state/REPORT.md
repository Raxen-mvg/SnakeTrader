# Paper trading report

Updated 2026-11-27 13:31 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,837 | +11.92% | 0 | - | 237 |
| unified | 223,230 | +11.62% | 0 | - | 236 |
| oracle | 211,670 | +5.83% | 0 | - | 233 |
| intramonth | 210,804 | +5.40% | 0 | - | 235 |
| random_hold | 210,713 | +5.36% | 13 | 69% | 1,037 |
| intraweek | 208,311 | +4.16% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,640 | +2.82% | 2 | 50% | 345 |
| snake_abs_exit | 204,472 | +2.24% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,233 | +0.62% | 0 | - | 237 |
| snake_abs | 200,246 | +0.12% | 1 | 100% | 255 |
| snake_abs_conv | 200,064 | +0.03% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,544 | -3.23% | 3 | 33% | 374 |
| snake_viper_wild | 192,030 | -3.98% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,769 | -5.62% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,857 | -15.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,766 (-5.62%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,243 | +2.62% |
| gold | +3,863 | +2.33% |
| snake_abs_exit | +3,394 | +1.69% |
| random_hold | +2,119 | +1.02% |
| snake_abs_conv | +1,697 | +0.86% |
| snake_abs | +1,694 | +0.85% |
| intraweek | +1,262 | +0.61% |
| snake_anaconda | +1,247 | +0.65% |
| benchmark_smallcap | +392 | +0.20% |
| intramonth | +271 | +0.13% |
| unified | +152 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -172 | -0.09% |
| snake_viper_wild | -176 | -0.09% |
| oracle | -565 | -0.27% |
| benchmark | -2,150 | -0.95% |

Average per day so far: benchmark Rs +568, unified Rs +553, oracle Rs +278, intramonth Rs +257, random_hold Rs +255, intraweek Rs +198, snake_abs_exit_conv Rs +145, snake_abs_exit Rs +115, nifty_calls Rs +44, benchmark_smallcap Rs +32, snake_abs Rs +6, snake_abs_conv Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -174, snake_viper_wild Rs -234, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -362, gold Rs -718

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.