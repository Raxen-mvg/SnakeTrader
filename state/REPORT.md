# Paper trading report

Updated 2026-11-11 11:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,328 | +10.66% | 0 | - | 237 |
| unified | 220,546 | +10.27% | 0 | - | 236 |
| snake_abs_exit_conv | 216,525 | +8.26% | 2 | 50% | 345 |
| snake_abs_exit | 215,199 | +7.60% | 2 | 50% | 345 |
| intraweek | 214,256 | +7.13% | 30 | 53% | 3,302 |
| snake_abs | 213,005 | +6.50% | 1 | 100% | 255 |
| snake_abs_conv | 212,853 | +6.43% | 1 | 100% | 255 |
| oracle | 211,766 | +5.88% | 0 | - | 233 |
| intramonth | 211,384 | +5.69% | 0 | - | 235 |
| random_hold | 206,694 | +3.35% | 9 | 67% | 709 |
| snake_anaconda | 203,076 | +1.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,827 | +0.91% | 0 | - | 237 |
| snake_viper_wild | 201,797 | +0.90% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,366 | -0.82% | 9 | 44% | 1,639 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,293 (-4.35%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,616 | +2.18% |
| snake_viper_wild | +4,367 | +2.21% |
| snake_viper_tick | +4,289 | +2.21% |
| benchmark_smallcap | +3,654 | +1.84% |
| snake_anaconda | +3,610 | +1.81% |
| snake_abs_conv | +3,375 | +1.61% |
| snake_abs | +3,358 | +1.60% |
| benchmark | +3,236 | +1.48% |
| snake_abs_exit | +3,215 | +1.52% |
| oracle | +1,847 | +0.88% |
| random_hold | +1,734 | +0.85% |
| unified | +799 | +0.36% |
| intramonth | +774 | +0.37% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -286 | -0.13% |
| gold | -2,318 | -1.21% |

Average per day so far: benchmark Rs +688, unified Rs +663, snake_abs_exit_conv Rs +590, snake_abs_exit Rs +543, intraweek Rs +460, snake_abs_conv Rs +459, snake_abs Rs +448, oracle Rs +380, intramonth Rs +367, random_hold Rs +216, snake_anaconda Rs +118, snake_viper_wild Rs +78, benchmark_smallcap Rs +68, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -82, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.