# Paper trading report

Updated 2026-11-05 11:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,698 | +9.35% | 0 | - | 236 |
| snake_abs_exit_conv | 215,711 | +7.86% | 1 | 100% | 255 |
| snake_abs_exit | 215,410 | +7.71% | 1 | 100% | 260 |
| snake_abs | 212,586 | +6.29% | 1 | 100% | 255 |
| snake_abs_conv | 212,449 | +6.22% | 1 | 100% | 255 |
| benchmark | 212,431 | +6.21% | 0 | - | 237 |
| intraweek | 211,049 | +5.53% | 25 | 48% | 2,757 |
| intramonth | 210,478 | +5.24% | 0 | - | 235 |
| snake_viper_wild | 207,392 | +3.70% | 3 | 33% | 702 |
| random_hold | 206,972 | +3.49% | 8 | 62% | 649 |
| oracle | 204,371 | +2.19% | 0 | - | 233 |
| snake_viper_tick | 203,834 | +1.92% | 2 | 0% | 532 |
| snake_anaconda | 203,708 | +1.85% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| gold | 193,827 | -3.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,887 (-4.56%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,258 | +1.99% |
| benchmark | +3,672 | +1.76% |
| random_hold | +3,663 | +1.80% |
| intramonth | +3,463 | +1.67% |
| oracle | +2,579 | +1.28% |
| benchmark_smallcap | +2,545 | +1.29% |
| gold | +2,433 | +1.27% |
| intraweek | +1,352 | +0.65% |
| snake_abs_exit_conv | +696 | +0.32% |
| snake_abs_conv | +691 | +0.33% |
| snake_abs | +683 | +0.32% |
| snake_abs_exit | +510 | +0.24% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -112 | -0.06% |
| snake_viper_tick | -1,567 | -0.76% |
| snake_viper_wild | -1,638 | -0.78% |

Average per day so far: unified Rs +668, snake_abs_exit_conv Rs +628, snake_abs_exit Rs +616, snake_abs_conv Rs +498, snake_abs Rs +484, benchmark Rs +444, intraweek Rs +395, intramonth Rs +374, snake_viper_wild Rs +370, random_hold Rs +249, snake_viper_tick Rs +226, snake_anaconda Rs +161, oracle Rs +156, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -220, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.