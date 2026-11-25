# Paper trading report

Updated 2026-11-25 14:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,786 | +12.39% | 0 | - | 237 |
| unified | 224,552 | +12.28% | 0 | - | 236 |
| oracle | 212,678 | +6.34% | 0 | - | 233 |
| intramonth | 212,113 | +6.06% | 0 | - | 235 |
| random_hold | 209,470 | +4.74% | 12 | 75% | 1,009 |
| intraweek | 207,005 | +3.50% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,437 | +0.72% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,135 | +0.57% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,670 | -0.17% | 1 | 100% | 255 |
| snake_abs_conv | 199,471 | -0.26% | 1 | 100% | 255 |
| benchmark_smallcap | 198,845 | -0.58% | 0 | - | 237 |
| snake_viper_wild | 197,183 | -1.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,824 | -3.09% | 15 | 47% | 2,625 |
| snake_anaconda | 193,141 | -3.43% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,221 | -17.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,896 (-5.55%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,312 | +1.50% |
| random_hold | +1,044 | +0.50% |
| oracle | +336 | +0.16% |
| unified | +267 | +0.12% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -135 | -0.07% |
| intramonth | -638 | -0.30% |
| snake_viper_tick | -3,868 | -1.96% |
| snake_viper_wild | -3,941 | -1.96% |
| gold | -4,209 | -2.48% |
| intraweek | -4,614 | -2.18% |
| snake_anaconda | -5,562 | -2.80% |
| snake_abs | -5,791 | -2.82% |
| snake_abs_conv | -5,831 | -2.84% |
| snake_abs_exit_conv | -5,910 | -2.85% |
| snake_abs_exit | -6,058 | -2.92% |

Average per day so far: benchmark Rs +620, unified Rs +614, oracle Rs +317, intramonth Rs +303, random_hold Rs +237, intraweek Rs +175, nifty_calls Rs +46, snake_abs_exit Rs +39, snake_abs_exit_conv Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -9, snake_abs_conv Rs -14, benchmark_smallcap Rs -32, snake_viper_wild Rs -88, snake_anaconda Rs -196, snake_viper_tick Rs -213, snake_nonews Rs -292, snake Rs -311, gold Rs -869

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.