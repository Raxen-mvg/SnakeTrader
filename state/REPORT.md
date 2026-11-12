# Paper trading report

Updated 2026-11-12 15:10 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,484 | +10.24% | 0 | - | 236 |
| benchmark | 220,448 | +10.22% | 0 | - | 237 |
| snake_abs_exit_conv | 219,501 | +9.75% | 2 | 50% | 345 |
| snake_abs_exit | 218,212 | +9.11% | 2 | 50% | 345 |
| snake_abs | 216,464 | +8.23% | 1 | 100% | 255 |
| snake_abs_conv | 216,294 | +8.15% | 1 | 100% | 255 |
| intraweek | 214,560 | +7.28% | 30 | 53% | 3,302 |
| oracle | 212,848 | +6.42% | 0 | - | 233 |
| intramonth | 211,459 | +5.73% | 0 | - | 235 |
| random_hold | 207,842 | +3.92% | 10 | 70% | 733 |
| snake_anaconda | 206,414 | +3.21% | 3 | 33% | 374 |
| snake_viper_wild | 205,548 | +2.77% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,105 | +1.55% | 0 | - | 237 |
| snake_viper_tick | 202,033 | +1.02% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,196 | -7.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,992 (-4.00%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs | +2,840 | +1.33% |
| snake_abs_conv | +2,837 | +1.33% |
| snake_abs_exit_conv | +2,350 | +1.08% |
| benchmark_smallcap | +2,298 | +1.14% |
| snake_anaconda | +2,291 | +1.12% |
| snake_abs_exit | +2,050 | +0.95% |
| intraweek | +1,427 | +0.67% |
| benchmark | +1,186 | +0.54% |
| oracle | +845 | +0.40% |
| random_hold | +732 | +0.35% |
| unified | +670 | +0.30% |
| intramonth | +462 | +0.22% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,176 | -0.58% |
| snake_viper_wild | -1,194 | -0.58% |
| gold | -4,389 | -2.31% |

Average per day so far: snake_abs_exit_conv Rs +672, unified Rs +640, benchmark Rs +639, snake_abs_exit Rs +628, snake_abs_conv Rs +562, snake_abs Rs +549, intraweek Rs +455, oracle Rs +401, intramonth Rs +358, random_hold Rs +245, snake_anaconda Rs +238, snake_viper_wild Rs +231, benchmark_smallcap Rs +111, snake_viper_tick Rs +97, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -463

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.