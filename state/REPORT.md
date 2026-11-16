# Paper trading report

Updated 2026-11-16 11:04 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,147 | +10.57% | 0 | - | 236 |
| benchmark | 220,150 | +10.07% | 0 | - | 237 |
| oracle | 213,349 | +6.67% | 0 | - | 233 |
| intraweek | 213,291 | +6.65% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,172 | +6.59% | 2 | 50% | 345 |
| intramonth | 211,778 | +5.89% | 0 | - | 235 |
| snake_abs_exit_conv | 211,760 | +5.88% | 2 | 50% | 345 |
| snake_abs | 208,828 | +4.41% | 1 | 100% | 255 |
| snake_abs_conv | 208,662 | +4.33% | 1 | 100% | 255 |
| random_hold | 208,074 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 204,762 | +2.38% | 14 | 50% | 2,496 |
| snake_anaconda | 203,278 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,260 | +0.63% | 13 | 46% | 2,299 |
| benchmark_smallcap | 201,210 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,039 | -8.98% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,505 (-4.25%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,126 | +0.97% |
| intramonth | +1,721 | +0.82% |
| random_hold | +848 | +0.41% |
| benchmark | +811 | +0.37% |
| oracle | +251 | +0.12% |
| snake_viper_tick | +5 | +0.00% |
| snake_viper_wild | +5 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_anaconda | -1,614 | -0.79% |
| benchmark_smallcap | -1,659 | -0.82% |
| gold | -1,956 | -1.06% |
| intraweek | -2,854 | -1.32% |
| snake_abs_conv | -3,704 | -1.74% |
| snake_abs | -3,712 | -1.75% |
| snake_abs_exit | -3,813 | -1.76% |
| snake_abs_exit_conv | -4,621 | -2.13% |

Average per day so far: unified Rs +622, benchmark Rs +593, snake_abs_exit Rs +425, oracle Rs +393, intraweek Rs +391, snake_abs_exit_conv Rs +379, intramonth Rs +346, snake_abs_conv Rs +279, snake_abs Rs +276, random_hold Rs +237, snake_viper_wild Rs +183, snake_anaconda Rs +113, snake_viper_tick Rs +55, nifty_calls Rs +54, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -528

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.