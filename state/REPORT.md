# Paper trading report

Updated 2026-11-26 14:55 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,926 | +12.96% | 0 | - | 237 |
| unified | 223,015 | +11.51% | 0 | - | 236 |
| oracle | 212,518 | +6.26% | 0 | - | 233 |
| intramonth | 210,358 | +5.18% | 0 | - | 235 |
| random_hold | 208,806 | +4.40% | 13 | 69% | 1,037 |
| intraweek | 207,368 | +3.68% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,896 | +0.45% | 0 | - | 237 |
| snake_abs_exit | 200,246 | +0.12% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,532 | -0.23% | 2 | 50% | 345 |
| snake_abs | 197,763 | -1.12% | 1 | 100% | 255 |
| snake_abs_conv | 197,554 | -1.22% | 1 | 100% | 255 |
| snake_viper_wild | 192,177 | -3.91% | 16 | 50% | 2,827 |
| snake_anaconda | 191,433 | -4.28% | 3 | 33% | 374 |
| snake_viper_tick | 188,913 | -5.54% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,240 | -16.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,328 (-5.84%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,085 | +1.05% |
| gold | +1,644 | +1.00% |
| benchmark | +903 | +0.40% |
| intraweek | +625 | +0.30% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -686 | -0.33% |
| unified | -1,085 | -0.48% |
| oracle | -1,278 | -0.60% |
| intramonth | -1,335 | -0.63% |
| snake_abs_exit | -2,010 | -0.99% |
| snake_abs | -2,387 | -1.19% |
| snake_abs_conv | -2,418 | -1.21% |
| snake_abs_exit_conv | -2,443 | -1.21% |
| snake_anaconda | -3,120 | -1.60% |
| snake_viper_tick | -5,264 | -2.71% |
| snake_viper_wild | -5,367 | -2.72% |

Average per day so far: benchmark Rs +632, unified Rs +561, oracle Rs +305, intramonth Rs +253, random_hold Rs +215, intraweek Rs +180, nifty_calls Rs +45, benchmark_smallcap Rs +24, snake_abs_exit Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -12, snake_abs Rs -57, snake_abs_conv Rs -64, snake_viper_wild Rs -237, snake_anaconda Rs -238, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -370, gold Rs -823

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.