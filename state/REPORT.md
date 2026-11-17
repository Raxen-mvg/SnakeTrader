# Paper trading report

Updated 2026-11-17 10:08 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,771 | +11.38% | 0 | - | 236 |
| benchmark | 221,313 | +10.66% | 0 | - | 237 |
| snake_abs_exit | 215,752 | +7.88% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,220 | +7.11% | 2 | 50% | 345 |
| intraweek | 213,064 | +6.53% | 35 | 54% | 3,851 |
| oracle | 212,983 | +6.49% | 0 | - | 233 |
| intramonth | 212,750 | +6.38% | 0 | - | 235 |
| snake_abs | 210,516 | +5.26% | 1 | 100% | 255 |
| snake_abs_conv | 210,367 | +5.18% | 1 | 100% | 255 |
| random_hold | 208,018 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 206,757 | +3.38% | 14 | 50% | 2,496 |
| snake_anaconda | 205,791 | +2.90% | 3 | 33% | 374 |
| snake_viper_tick | 203,222 | +1.61% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,230 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,152 | -9.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,778 (-4.11%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,798 | +0.85% |
| benchmark_smallcap | +1,401 | +0.70% |
| snake_abs_exit | +1,342 | +0.63% |
| unified | +1,333 | +0.60% |
| benchmark | +1,232 | +0.56% |
| intramonth | +1,132 | +0.54% |
| snake_abs_exit_conv | +1,003 | +0.47% |
| oracle | +960 | +0.45% |
| snake_anaconda | +688 | +0.34% |
| snake_viper_wild | +612 | +0.30% |
| snake_viper_tick | +602 | +0.30% |
| snake_abs | +382 | +0.18% |
| snake_abs_conv | +377 | +0.18% |
| random_hold | +224 | +0.11% |
| gold | +197 | +0.11% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +651, benchmark Rs +609, snake_abs_exit Rs +492, snake_abs_exit_conv Rs +444, intraweek Rs +373, oracle Rs +371, intramonth Rs +364, snake_abs_conv Rs +324, snake_abs Rs +319, snake_viper_wild Rs +250, random_hold Rs +229, snake_anaconda Rs +193, snake_viper_tick Rs +134, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -539

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.