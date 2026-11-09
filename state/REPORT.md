# Paper trading report

Updated 2026-11-09 10:03 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,205 | +10.10% | 0 | - | 236 |
| benchmark | 217,419 | +8.71% | 0 | - | 237 |
| intraweek | 215,180 | +7.59% | 30 | 53% | 3,302 |
| snake_abs_exit | 211,041 | +5.52% | 2 | 50% | 308 |
| snake_abs_exit_conv | 211,015 | +5.51% | 2 | 50% | 330 |
| intramonth | 210,408 | +5.20% | 0 | - | 235 |
| oracle | 209,252 | +4.63% | 0 | - | 233 |
| snake_abs | 208,727 | +4.36% | 1 | 100% | 255 |
| snake_abs_conv | 208,544 | +4.27% | 1 | 100% | 255 |
| random_hold | 203,972 | +1.99% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,498 | -0.75% | 3 | 33% | 374 |
| benchmark_smallcap | 198,318 | -0.84% | 0 | - | 237 |
| snake_viper_wild | 197,401 | -1.30% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,048 | -2.98% | 6 | 50% | 1,154 |
| gold | 193,399 | -3.30% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,257 (-4.87%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,817 | +2.29% |
| unified | +4,595 | +2.13% |
| oracle | +3,425 | +1.66% |
| snake_abs_conv | +3,317 | +1.62% |
| snake_abs | +3,307 | +1.61% |
| intramonth | +2,805 | +1.35% |
| snake_abs_exit | +2,729 | +1.31% |
| snake_anaconda | +2,671 | +1.36% |
| snake_abs_exit_conv | +2,594 | +1.24% |
| gold | +2,351 | +1.23% |
| benchmark_smallcap | +1,525 | +0.78% |
| snake_viper_wild | +1,363 | +0.69% |
| snake_viper_tick | +1,338 | +0.69% |
| random_hold | +65 | +0.03% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -69 | -0.03% |

Average per day so far: unified Rs +673, benchmark Rs +581, intraweek Rs +506, snake_abs_exit Rs +409, snake_abs_exit_conv Rs +408, intramonth Rs +347, snake_abs_conv Rs +316, snake_abs Rs +312, oracle Rs +308, random_hold Rs +132, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -60, benchmark_smallcap Rs -65, snake_viper_wild Rs -118, gold Rs -220, snake_viper_tick Rs -313, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.