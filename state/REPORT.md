# Paper trading report

Updated 2026-11-25 10:52 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,436 | +12.72% | 0 | - | 237 |
| unified | 225,208 | +12.60% | 0 | - | 236 |
| intramonth | 212,961 | +6.48% | 0 | - | 235 |
| oracle | 212,138 | +6.07% | 0 | - | 233 |
| random_hold | 209,766 | +4.88% | 12 | 75% | 1,009 |
| intraweek | 208,328 | +4.16% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,004 | +1.00% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,523 | +0.76% | 2 | 50% | 345 |
| snake_abs | 200,932 | +0.47% | 1 | 100% | 255 |
| snake_abs_conv | 200,743 | +0.37% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_viper_wild | 195,546 | -2.23% | 16 | 50% | 2,827 |
| snake_anaconda | 193,449 | -3.27% | 3 | 33% | 374 |
| snake_viper_tick | 192,222 | -3.89% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,731 | -17.14% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,360 (-5.32%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,963 | +1.79% |
| random_hold | +1,339 | +0.64% |
| unified | +923 | +0.41% |
| benchmark_smallcap | +572 | +0.29% |
| intramonth | +209 | +0.10% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -204 | -0.10% |
| intraweek | -3,291 | -1.55% |
| gold | -3,699 | -2.18% |
| snake_abs | -4,529 | -2.20% |
| snake_abs_conv | -4,560 | -2.22% |
| snake_anaconda | -5,254 | -2.64% |
| snake_viper_tick | -5,471 | -2.77% |
| snake_abs_exit | -5,491 | -2.65% |
| snake_abs_exit_conv | -5,523 | -2.67% |
| snake_viper_wild | -5,578 | -2.77% |

Average per day so far: benchmark Rs +636, unified Rs +630, intramonth Rs +324, oracle Rs +303, random_hold Rs +244, intraweek Rs +208, snake_abs_exit Rs +54, nifty_calls Rs +46, snake_abs_exit_conv Rs +41, snake_abs Rs +25, snake_abs_conv Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_viper_wild Rs -139, snake_anaconda Rs -187, snake_viper_tick Rs -268, snake_nonews Rs -292, snake Rs -311, gold Rs -857

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.