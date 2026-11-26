# Paper trading report

Updated 2026-11-26 11:36 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,658 | +12.83% | 0 | - | 237 |
| unified | 223,174 | +11.59% | 0 | - | 236 |
| oracle | 213,033 | +6.52% | 0 | - | 233 |
| intramonth | 210,439 | +5.22% | 0 | - | 235 |
| random_hold | 209,739 | +4.87% | 13 | 69% | 1,037 |
| intraweek | 208,708 | +4.35% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 200,667 | +0.33% | 2 | 50% | 345 |
| benchmark_smallcap | 200,425 | +0.21% | 0 | - | 237 |
| snake_abs_exit_conv | 200,131 | +0.07% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,432 | -0.78% | 1 | 100% | 255 |
| snake_abs_conv | 198,241 | -0.88% | 1 | 100% | 255 |
| snake_anaconda | 192,289 | -3.85% | 3 | 33% | 374 |
| snake_viper_wild | 191,942 | -4.03% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,683 | -5.66% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,717 | -16.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,750 (-5.62%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,121 | +1.29% |
| intraweek | +1,965 | +0.95% |
| benchmark_smallcap | +1,614 | +0.81% |
| benchmark | +635 | +0.28% |
| random_hold | +246 | +0.12% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -763 | -0.36% |
| unified | -926 | -0.41% |
| intramonth | -1,255 | -0.59% |
| snake_abs_exit | -1,589 | -0.79% |
| snake_abs | -1,718 | -0.86% |
| snake_abs_conv | -1,731 | -0.87% |
| snake_abs_exit_conv | -1,845 | -0.91% |
| snake_anaconda | -2,264 | -1.16% |
| snake_viper_tick | -5,494 | -2.83% |
| snake_viper_wild | -5,602 | -2.84% |

Average per day so far: benchmark Rs +626, unified Rs +565, oracle Rs +318, intramonth Rs +255, random_hold Rs +238, intraweek Rs +212, nifty_calls Rs +45, snake_abs_exit Rs +18, benchmark_smallcap Rs +11, snake_abs_exit_conv Rs +3, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -40, snake_abs_conv Rs -46, snake_anaconda Rs -214, snake_viper_wild Rs -244, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -377, gold Rs -812

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.