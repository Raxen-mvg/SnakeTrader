# Paper trading report

Updated 2026-11-17 15:19 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,688 | +10.84% | 0 | - | 236 |
| benchmark | 221,664 | +10.83% | 0 | - | 237 |
| snake_abs_exit | 213,529 | +6.76% | 2 | 50% | 345 |
| intraweek | 213,488 | +6.74% | 35 | 54% | 3,851 |
| oracle | 212,692 | +6.35% | 0 | - | 233 |
| snake_abs_exit_conv | 211,954 | +5.98% | 2 | 50% | 345 |
| intramonth | 211,823 | +5.91% | 0 | - | 235 |
| snake_viper_wild | 209,610 | +4.80% | 14 | 50% | 2,496 |
| snake_abs | 208,769 | +4.38% | 1 | 100% | 255 |
| snake_abs_conv | 208,634 | +4.32% | 1 | 100% | 255 |
| random_hold | 208,317 | +4.16% | 10 | 70% | 733 |
| snake_viper_tick | 206,028 | +3.01% | 13 | 46% | 2,299 |
| snake_anaconda | 204,451 | +2.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,773 | -9.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,334 (-4.33%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,465 | +1.68% |
| snake_viper_tick | +3,408 | +1.68% |
| intraweek | +2,222 | +1.05% |
| benchmark | +1,584 | +0.72% |
| oracle | +669 | +0.32% |
| random_hold | +524 | +0.25% |
| unified | +251 | +0.11% |
| intramonth | +204 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -181 | -0.10% |
| benchmark_smallcap | -269 | -0.13% |
| snake_anaconda | -652 | -0.32% |
| snake_abs_exit | -880 | -0.41% |
| snake_abs_exit_conv | -1,263 | -0.59% |
| snake_abs_conv | -1,355 | -0.65% |
| snake_abs | -1,365 | -0.65% |

Average per day so far: unified Rs +620, benchmark Rs +619, snake_abs_exit Rs +423, intraweek Rs +385, snake_abs_exit_conv Rs +374, oracle Rs +363, snake_viper_wild Rs +356, intramonth Rs +338, snake_abs_conv Rs +270, snake_abs Rs +266, snake_viper_tick Rs +251, random_hold Rs +238, snake_anaconda Rs +148, nifty_calls Rs +52, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -549

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.