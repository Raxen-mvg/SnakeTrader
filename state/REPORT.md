# Paper trading report

Updated 2026-11-09 13:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,308 | +10.15% | 0 | - | 236 |
| benchmark | 217,388 | +8.69% | 0 | - | 237 |
| intraweek | 215,093 | +7.55% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,011 | +6.51% | 2 | 50% | 330 |
| snake_abs_exit | 212,598 | +6.30% | 2 | 50% | 308 |
| intramonth | 210,459 | +5.23% | 0 | - | 235 |
| snake_abs | 210,125 | +5.06% | 1 | 100% | 255 |
| snake_abs_conv | 209,956 | +4.98% | 1 | 100% | 255 |
| oracle | 209,763 | +4.88% | 0 | - | 233 |
| random_hold | 204,501 | +2.25% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,017 | +0.01% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,458 | -0.27% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,688 | -0.66% | 0 | - | 237 |
| snake_viper_tick | 196,070 | -1.97% | 6 | 50% | 1,154 |
| gold | 192,380 | -3.81% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,580 (-4.71%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,730 | +2.25% |
| snake_abs_conv | +4,728 | +2.30% |
| snake_abs | +4,706 | +2.29% |
| unified | +4,699 | +2.18% |
| snake_abs_exit_conv | +4,590 | +2.20% |
| snake_abs_exit | +4,286 | +2.06% |
| snake_anaconda | +4,190 | +2.14% |
| oracle | +3,936 | +1.91% |
| snake_viper_wild | +3,421 | +1.75% |
| snake_viper_tick | +3,361 | +1.74% |
| intramonth | +2,856 | +1.38% |
| benchmark_smallcap | +1,894 | +0.96% |
| gold | +1,332 | +0.70% |
| random_hold | +594 | +0.29% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -99 | -0.05% |

Average per day so far: unified Rs +677, benchmark Rs +580, intraweek Rs +503, snake_abs_exit_conv Rs +482, snake_abs_exit Rs +467, snake_abs_conv Rs +369, snake_abs Rs +362, intramonth Rs +349, oracle Rs +325, random_hold Rs +150, nifty_calls Rs +61, snake_anaconda Rs +1, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -25, benchmark_smallcap Rs -50, snake_viper_tick Rs -207, gold Rs -254, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.