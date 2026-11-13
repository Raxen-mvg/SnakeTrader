# Paper trading report

Updated 2026-11-13 13:31 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,256 | +10.13% | 0 | - | 236 |
| benchmark | 219,270 | +9.63% | 0 | - | 237 |
| snake_abs_exit | 216,644 | +8.32% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,386 | +8.19% | 2 | 50% | 345 |
| intraweek | 215,856 | +7.93% | 30 | 53% | 3,302 |
| oracle | 212,985 | +6.49% | 0 | - | 233 |
| snake_abs | 212,324 | +6.16% | 1 | 100% | 255 |
| snake_abs_conv | 212,153 | +6.08% | 1 | 100% | 255 |
| intramonth | 210,921 | +5.46% | 0 | - | 235 |
| random_hold | 207,282 | +3.64% | 10 | 70% | 733 |
| snake_viper_wild | 205,337 | +2.67% | 14 | 50% | 2,496 |
| snake_anaconda | 204,595 | +2.30% | 3 | 33% | 374 |
| benchmark_smallcap | 202,634 | +1.32% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,825 | +0.91% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,773 (-4.11%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,198 | +0.56% |
| snake_viper_wild | +44 | +0.02% |
| snake_viper_tick | +43 | +0.02% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -130 | -0.06% |
| unified | -441 | -0.20% |
| benchmark_smallcap | -572 | -0.28% |
| intramonth | -672 | -0.32% |
| random_hold | -772 | -0.37% |
| snake_abs_exit | -798 | -0.37% |
| benchmark | -1,278 | -0.58% |
| snake_anaconda | -1,332 | -0.65% |
| gold | -1,480 | -0.80% |
| snake_abs_exit_conv | -2,288 | -1.05% |
| snake_abs_conv | -3,382 | -1.57% |
| snake_abs | -3,387 | -1.57% |

Average per day so far: unified Rs +614, benchmark Rs +584, snake_abs_exit Rs +555, snake_abs_exit_conv Rs +546, intraweek Rs +480, snake_abs_conv Rs +405, snake_abs Rs +398, oracle Rs +393, intramonth Rs +331, random_hold Rs +221, snake_viper_wild Rs +213, snake_anaconda Rs +164, benchmark_smallcap Rs +91, snake_viper_tick Rs +83, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.