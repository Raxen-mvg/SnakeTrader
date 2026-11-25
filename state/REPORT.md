# Paper trading report

Updated 2026-11-25 11:24 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,178 | +13.09% | 0 | - | 237 |
| unified | 225,036 | +12.52% | 0 | - | 236 |
| intramonth | 212,833 | +6.42% | 0 | - | 235 |
| oracle | 211,840 | +5.92% | 0 | - | 233 |
| random_hold | 210,257 | +5.13% | 12 | 75% | 1,009 |
| intraweek | 208,275 | +4.14% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,868 | +0.93% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,290 | +0.65% | 2 | 50% | 345 |
| snake_abs | 201,256 | +0.63% | 1 | 100% | 255 |
| snake_abs_conv | 201,061 | +0.53% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,517 | -0.24% | 0 | - | 237 |
| snake_viper_wild | 195,527 | -2.24% | 16 | 50% | 2,827 |
| snake_anaconda | 193,395 | -3.30% | 3 | 33% | 374 |
| snake_viper_tick | 192,203 | -3.90% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,564 | -17.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,340 (-5.33%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,705 | +2.12% |
| random_hold | +1,831 | +0.88% |
| unified | +751 | +0.34% |
| benchmark_smallcap | +538 | +0.27% |
| intramonth | +81 | +0.04% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -502 | -0.24% |
| intraweek | -3,344 | -1.58% |
| snake_abs | -4,205 | -2.05% |
| snake_abs_conv | -4,241 | -2.07% |
| gold | -4,866 | -2.87% |
| snake_anaconda | -5,309 | -2.67% |
| snake_viper_tick | -5,490 | -2.78% |
| snake_viper_wild | -5,597 | -2.78% |
| snake_abs_exit | -5,627 | -2.71% |
| snake_abs_exit_conv | -5,756 | -2.78% |

Average per day so far: benchmark Rs +654, unified Rs +626, intramonth Rs +321, oracle Rs +296, random_hold Rs +256, intraweek Rs +207, snake_abs_exit Rs +50, nifty_calls Rs +46, snake_abs_exit_conv Rs +35, snake_abs Rs +33, snake_abs_conv Rs +29, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_viper_wild Rs -140, snake_anaconda Rs -189, snake_viper_tick Rs -269, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.