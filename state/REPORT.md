# Paper trading report

Updated 2026-11-13 10:52 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,578 | +10.29% | 0 | - | 236 |
| benchmark | 220,127 | +10.06% | 0 | - | 237 |
| snake_abs_exit_conv | 217,296 | +8.65% | 2 | 50% | 345 |
| snake_abs_exit | 217,176 | +8.59% | 2 | 50% | 345 |
| intraweek | 216,153 | +8.08% | 30 | 53% | 3,302 |
| oracle | 213,809 | +6.90% | 0 | - | 233 |
| snake_abs | 213,216 | +6.61% | 1 | 100% | 255 |
| snake_abs_conv | 213,049 | +6.52% | 1 | 100% | 255 |
| intramonth | 211,344 | +5.67% | 0 | - | 235 |
| random_hold | 207,443 | +3.72% | 10 | 70% | 733 |
| snake_viper_wild | 206,636 | +3.32% | 14 | 50% | 2,496 |
| snake_anaconda | 205,199 | +2.60% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 203,102 | +1.55% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,522 | -7.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,211 (-3.89%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,495 | +0.70% |
| snake_viper_wild | +1,344 | +0.65% |
| snake_viper_tick | +1,321 | +0.65% |
| oracle | +694 | +0.33% |
| benchmark_smallcap | +493 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -119 | -0.05% |
| intramonth | -249 | -0.12% |
| snake_abs_exit | -266 | -0.12% |
| benchmark | -421 | -0.19% |
| random_hold | -611 | -0.29% |
| snake_anaconda | -728 | -0.35% |
| gold | -789 | -0.43% |
| snake_abs_exit_conv | -1,378 | -0.63% |
| snake_abs_conv | -2,486 | -1.15% |
| snake_abs | -2,496 | -1.16% |

Average per day so far: unified Rs +624, benchmark Rs +610, snake_abs_exit_conv Rs +577, snake_abs_exit Rs +573, intraweek Rs +489, snake_abs_conv Rs +435, snake_abs Rs +426, oracle Rs +418, intramonth Rs +344, snake_viper_wild Rs +265, random_hold Rs +226, snake_anaconda Rs +186, snake_viper_tick Rs +141, benchmark_smallcap Rs +128, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -469

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.