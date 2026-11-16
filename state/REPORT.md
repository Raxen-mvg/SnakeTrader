# Paper trading report

Updated 2026-11-16 09:17 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,027 | +10.01% | 0 | - | 237 |
| unified | 217,859 | +8.93% | 0 | - | 236 |
| intraweek | 216,769 | +8.38% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,716 | +7.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,168 | +6.58% | 2 | 50% | 345 |
| oracle | 212,454 | +6.23% | 0 | - | 233 |
| snake_abs | 210,118 | +5.06% | 1 | 100% | 255 |
| snake_abs_conv | 209,944 | +4.97% | 1 | 100% | 255 |
| intramonth | 208,974 | +4.49% | 0 | - | 235 |
| random_hold | 206,674 | +3.34% | 10 | 70% | 733 |
| snake_anaconda | 203,747 | +1.87% | 3 | 33% | 374 |
| snake_viper_wild | 203,742 | +1.87% | 14 | 50% | 2,496 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,502 | +0.75% | 0 | - | 237 |
| snake_viper_tick | 200,256 | +0.13% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,500 | -8.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,011 (-4.49%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +688 | +0.31% |
| intraweek | +624 | +0.29% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| random_hold | -551 | -0.27% |
| oracle | -644 | -0.30% |
| snake_viper_tick | -999 | -0.50% |
| snake_viper_wild | -1,016 | -0.50% |
| intramonth | -1,082 | -0.52% |
| snake_anaconda | -1,145 | -0.56% |
| unified | -1,161 | -0.53% |
| benchmark_smallcap | -1,368 | -0.67% |
| gold | -1,496 | -0.81% |
| snake_abs_exit | -2,269 | -1.05% |
| snake_abs | -2,422 | -1.14% |
| snake_abs_conv | -2,423 | -1.14% |
| snake_abs_exit_conv | -3,213 | -1.49% |

Average per day so far: benchmark Rs +589, unified Rs +525, intraweek Rs +493, snake_abs_exit Rs +475, snake_abs_exit_conv Rs +425, oracle Rs +366, snake_abs_conv Rs +321, snake_abs Rs +316, intramonth Rs +264, random_hold Rs +196, snake_viper_wild Rs +144, snake_anaconda Rs +129, nifty_calls Rs +54, benchmark_smallcap Rs +50, snake_viper_tick Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -515

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.