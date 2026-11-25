# Paper trading report

Updated 2026-11-25 15:19 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,900 | +12.45% | 0 | - | 237 |
| unified | 224,017 | +12.01% | 0 | - | 236 |
| oracle | 213,726 | +6.86% | 0 | - | 233 |
| intramonth | 211,640 | +5.82% | 0 | - | 235 |
| random_hold | 209,599 | +4.80% | 12 | 75% | 1,009 |
| intraweek | 206,543 | +3.27% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,221 | +1.11% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,914 | +0.96% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,235 | +0.12% | 1 | 100% | 255 |
| snake_abs_conv | 200,054 | +0.03% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,878 | -0.56% | 0 | - | 237 |
| snake_viper_wild | 197,399 | -1.30% | 16 | 50% | 2,827 |
| snake_anaconda | 194,600 | -2.70% | 3 | 33% | 374 |
| snake_viper_tick | 194,036 | -2.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,794 | -17.60% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,029 (-5.49%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,427 | +1.55% |
| oracle | +1,384 | +0.65% |
| random_hold | +1,173 | +0.56% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| benchmark_smallcap | -101 | -0.05% |
| unified | -268 | -0.12% |
| intramonth | -1,111 | -0.52% |
| snake_viper_tick | -3,657 | -1.85% |
| snake_viper_wild | -3,725 | -1.85% |
| snake_anaconda | -4,104 | -2.06% |
| gold | -4,636 | -2.74% |
| intraweek | -5,076 | -2.40% |
| snake_abs_exit_conv | -5,132 | -2.48% |
| snake_abs | -5,226 | -2.54% |
| snake_abs_conv | -5,248 | -2.56% |
| snake_abs_exit | -5,274 | -2.54% |

Average per day so far: benchmark Rs +623, unified Rs +600, oracle Rs +343, intramonth Rs +291, random_hold Rs +240, intraweek Rs +164, snake_abs_exit Rs +60, snake_abs_exit_conv Rs +52, nifty_calls Rs +46, snake_abs Rs +6, snake_abs_conv Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -31, snake_viper_wild Rs -81, snake_anaconda Rs -154, snake_viper_tick Rs -206, snake_nonews Rs -292, snake Rs -311, gold Rs -880

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.