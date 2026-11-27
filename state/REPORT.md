# Paper trading report

Updated 2026-11-27 14:52 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,776 | +11.89% | 0 | - | 237 |
| unified | 223,632 | +11.82% | 0 | - | 236 |
| oracle | 211,995 | +6.00% | 0 | - | 233 |
| random_hold | 211,003 | +5.50% | 13 | 69% | 1,037 |
| intramonth | 210,980 | +5.49% | 0 | - | 235 |
| intraweek | 207,093 | +3.55% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,641 | +3.32% | 2 | 50% | 345 |
| snake_abs_exit | 204,345 | +2.17% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,614 | +0.81% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,859 | -0.07% | 1 | 100% | 255 |
| snake_abs_conv | 199,675 | -0.16% | 1 | 100% | 255 |
| snake_anaconda | 193,306 | -3.35% | 3 | 33% | 374 |
| snake_viper_wild | 192,447 | -3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,178 | -5.41% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,926 | -14.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,898 (-5.55%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,244 | +3.12% |
| gold | +4,932 | +2.97% |
| snake_abs_exit | +3,268 | +1.62% |
| random_hold | +2,409 | +1.16% |
| snake_abs_conv | +1,308 | +0.66% |
| snake_abs | +1,307 | +0.66% |
| snake_anaconda | +1,010 | +0.53% |
| benchmark_smallcap | +773 | +0.39% |
| unified | +554 | +0.25% |
| intramonth | +446 | +0.21% |
| snake_viper_wild | +242 | +0.13% |
| snake_viper_tick | +237 | +0.13% |
| intraweek | +44 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -241 | -0.11% |
| benchmark | -2,211 | -0.98% |

Average per day so far: benchmark Rs +566, unified Rs +563, oracle Rs +286, random_hold Rs +262, intramonth Rs +261, snake_abs_exit_conv Rs +170, intraweek Rs +169, snake_abs_exit Rs +111, nifty_calls Rs +44, benchmark_smallcap Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -4, snake_abs_conv Rs -8, snake_anaconda Rs -181, snake_viper_wild Rs -222, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -349, gold Rs -692

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.