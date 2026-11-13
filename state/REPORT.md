# Paper trading report

Updated 2026-11-13 15:10 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,339 | +9.67% | 0 | - | 237 |
| unified | 218,886 | +9.44% | 0 | - | 236 |
| snake_abs_exit | 217,118 | +8.56% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,532 | +8.27% | 2 | 50% | 345 |
| intraweek | 216,133 | +8.07% | 30 | 53% | 3,302 |
| oracle | 212,937 | +6.47% | 0 | - | 233 |
| snake_abs | 212,692 | +6.35% | 1 | 100% | 255 |
| snake_abs_conv | 212,522 | +6.26% | 1 | 100% | 255 |
| intramonth | 209,990 | +5.00% | 0 | - | 235 |
| random_hold | 207,254 | +3.63% | 10 | 70% | 733 |
| snake_viper_wild | 205,350 | +2.67% | 14 | 50% | 2,496 |
| snake_anaconda | 204,975 | +2.49% | 3 | 33% | 374 |
| benchmark_smallcap | 203,138 | +1.57% | 0 | - | 237 |
| snake_viper_tick | 201,838 | +0.92% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,045 | -7.98% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,522 (-4.24%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,475 | +0.69% |
| snake_viper_wild | +57 | +0.03% |
| snake_viper_tick | +56 | +0.03% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -67 | -0.03% |
| oracle | -179 | -0.08% |
| snake_abs_exit | -325 | -0.15% |
| random_hold | -800 | -0.38% |
| snake_anaconda | -952 | -0.46% |
| benchmark | -1,209 | -0.55% |
| gold | -1,266 | -0.68% |
| intramonth | -1,603 | -0.76% |
| unified | -1,810 | -0.82% |
| snake_abs_exit_conv | -2,142 | -0.98% |
| snake_abs_conv | -3,013 | -1.40% |
| snake_abs | -3,019 | -1.40% |

Average per day so far: benchmark Rs +586, unified Rs +572, snake_abs_exit Rs +571, snake_abs_exit_conv Rs +551, intraweek Rs +489, snake_abs_conv Rs +417, snake_abs Rs +409, oracle Rs +392, intramonth Rs +303, random_hold Rs +220, snake_viper_wild Rs +214, snake_anaconda Rs +178, benchmark_smallcap Rs +108, snake_viper_tick Rs +84, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -483

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.