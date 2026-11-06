# Paper trading report

Updated 2026-11-06 13:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,743 | +7.87% | 0 | - | 237 |
| unified | 214,702 | +7.35% | 0 | - | 236 |
| snake_abs_exit_conv | 208,638 | +4.32% | 1 | 100% | 255 |
| snake_abs_exit | 208,545 | +4.27% | 1 | 100% | 260 |
| intraweek | 208,212 | +4.11% | 25 | 48% | 2,757 |
| intramonth | 207,001 | +3.50% | 0 | - | 235 |
| snake_abs | 205,619 | +2.81% | 1 | 100% | 255 |
| snake_abs_conv | 205,438 | +2.72% | 1 | 100% | 255 |
| oracle | 205,285 | +2.64% | 0 | - | 233 |
| random_hold | 203,271 | +1.64% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,127 | -1.94% | 3 | 33% | 702 |
| snake_anaconda | 196,044 | -1.98% | 3 | 33% | 374 |
| benchmark_smallcap | 195,112 | -2.44% | 0 | - | 237 |
| snake_viper_tick | 192,804 | -3.60% | 2 | 0% | 532 |
| gold | 190,391 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,877 (-6.56%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,974 | +0.92% |
| oracle | +1,213 | +0.59% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -947 | -0.46% |
| random_hold | -1,052 | -0.52% |
| intraweek | -1,207 | -0.58% |
| unified | -1,281 | -0.59% |
| benchmark_smallcap | -3,576 | -1.80% |
| gold | -3,831 | -1.97% |
| snake_abs | -6,069 | -2.87% |
| snake_abs_conv | -6,107 | -2.89% |
| snake_abs_exit | -6,114 | -2.85% |
| snake_abs_exit_conv | -6,166 | -2.87% |
| snake_anaconda | -6,435 | -3.18% |
| snake_viper_tick | -8,334 | -4.14% |
| snake_viper_wild | -8,529 | -4.17% |

Average per day so far: benchmark Rs +543, unified Rs +507, snake_abs_exit_conv Rs +332, snake_abs_exit Rs +329, intraweek Rs +283, intramonth Rs +241, snake_abs_conv Rs +209, snake_abs Rs +208, oracle Rs +182, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -184, benchmark_smallcap Rs -196, gold Rs -331, snake_viper_tick Rs -400, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.