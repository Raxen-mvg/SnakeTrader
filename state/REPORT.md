# Paper trading report

Updated 2026-11-25 14:37 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,694 | +12.35% | 0 | - | 237 |
| unified | 224,425 | +12.21% | 0 | - | 236 |
| oracle | 212,923 | +6.46% | 0 | - | 233 |
| intramonth | 211,887 | +5.94% | 0 | - | 235 |
| random_hold | 209,850 | +4.92% | 12 | 75% | 1,009 |
| intraweek | 207,432 | +3.72% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,438 | +0.72% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,117 | +0.56% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,784 | -0.11% | 1 | 100% | 255 |
| snake_abs_conv | 199,580 | -0.21% | 1 | 100% | 255 |
| benchmark_smallcap | 199,080 | -0.46% | 0 | - | 237 |
| snake_viper_wild | 197,481 | -1.26% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,116 | -2.94% | 15 | 47% | 2,625 |
| snake_anaconda | 193,221 | -3.39% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,221 | -17.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,012 (-5.49%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,221 | +1.45% |
| random_hold | +1,424 | +0.68% |
| oracle | +581 | +0.27% |
| unified | +140 | +0.06% |
| benchmark_smallcap | +101 | +0.05% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -864 | -0.41% |
| snake_viper_tick | -3,577 | -1.81% |
| snake_viper_wild | -3,643 | -1.81% |
| intraweek | -4,187 | -1.98% |
| gold | -4,209 | -2.48% |
| snake_anaconda | -5,483 | -2.76% |
| snake_abs | -5,676 | -2.76% |
| snake_abs_conv | -5,722 | -2.79% |
| snake_abs_exit_conv | -5,929 | -2.86% |
| snake_abs_exit | -6,057 | -2.92% |

Average per day so far: benchmark Rs +617, unified Rs +611, oracle Rs +323, intramonth Rs +297, random_hold Rs +246, intraweek Rs +186, nifty_calls Rs +46, snake_abs_exit Rs +39, snake_abs_exit_conv Rs +30, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, benchmark_smallcap Rs -26, snake_viper_wild Rs -79, snake_anaconda Rs -194, snake_viper_tick Rs -203, snake_nonews Rs -292, snake Rs -311, gold Rs -869

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.