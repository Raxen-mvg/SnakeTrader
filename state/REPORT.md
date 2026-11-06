# Paper trading report

Updated 2026-11-06 12:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,017 | +7.51% | 0 | - | 237 |
| unified | 214,982 | +7.49% | 0 | - | 236 |
| intraweek | 209,252 | +4.63% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,777 | +4.39% | 1 | 100% | 255 |
| snake_abs_exit | 208,601 | +4.30% | 1 | 100% | 260 |
| intramonth | 207,317 | +3.66% | 0 | - | 235 |
| snake_abs | 205,743 | +2.87% | 1 | 100% | 255 |
| snake_abs_conv | 205,570 | +2.79% | 1 | 100% | 255 |
| oracle | 204,990 | +2.50% | 0 | - | 233 |
| random_hold | 203,321 | +1.66% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,017 | -1.99% | 3 | 33% | 374 |
| snake_viper_wild | 195,621 | -2.19% | 3 | 33% | 702 |
| benchmark_smallcap | 194,596 | -2.70% | 0 | - | 237 |
| snake_viper_tick | 192,307 | -3.85% | 2 | 0% | 532 |
| gold | 190,243 | -4.88% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,059 (-6.47%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,247 | +0.58% |
| oracle | +918 | +0.45% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -167 | -0.08% |
| intramonth | -631 | -0.30% |
| unified | -1,002 | -0.46% |
| random_hold | -1,003 | -0.49% |
| gold | -3,978 | -2.05% |
| benchmark_smallcap | -4,092 | -2.06% |
| snake_abs | -5,945 | -2.81% |
| snake_abs_conv | -5,975 | -2.83% |
| snake_abs_exit_conv | -6,026 | -2.81% |
| snake_abs_exit | -6,058 | -2.82% |
| snake_anaconda | -6,462 | -3.19% |
| snake_viper_tick | -8,831 | -4.39% |
| snake_viper_wild | -9,035 | -4.42% |

Average per day so far: benchmark Rs +518, unified Rs +517, snake_abs_exit_conv Rs +338, snake_abs_exit Rs +331, intraweek Rs +319, intramonth Rs +252, snake_abs_conv Rs +214, snake_abs Rs +213, oracle Rs +172, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -166, snake_viper_wild Rs -209, benchmark_smallcap Rs -216, gold Rs -336, snake_nonews Rs -411, snake_viper_tick Rs -427, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.