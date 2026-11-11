# Paper trading report

Updated 2026-11-11 11:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,328 | +10.66% | 0 | - | 237 |
| unified | 220,582 | +10.29% | 0 | - | 236 |
| snake_abs_exit_conv | 216,549 | +8.27% | 2 | 50% | 345 |
| snake_abs_exit | 215,193 | +7.60% | 2 | 50% | 345 |
| intraweek | 214,259 | +7.13% | 30 | 53% | 3,302 |
| snake_abs | 212,994 | +6.50% | 1 | 100% | 255 |
| snake_abs_conv | 212,842 | +6.42% | 1 | 100% | 255 |
| oracle | 211,999 | +6.00% | 0 | - | 233 |
| intramonth | 211,622 | +5.81% | 0 | - | 235 |
| random_hold | 206,860 | +3.43% | 9 | 67% | 709 |
| snake_anaconda | 203,206 | +1.60% | 3 | 33% | 374 |
| snake_viper_wild | 201,978 | +0.99% | 10 | 50% | 1,825 |
| benchmark_smallcap | 201,894 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,544 | -0.73% | 9 | 44% | 1,639 |
| gold | 189,848 | -5.08% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,380 (-4.31%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,640 | +2.19% |
| snake_viper_wild | +4,548 | +2.30% |
| snake_viper_tick | +4,467 | +2.30% |
| snake_anaconda | +3,740 | +1.88% |
| benchmark_smallcap | +3,722 | +1.88% |
| snake_abs_conv | +3,364 | +1.61% |
| snake_abs | +3,348 | +1.60% |
| benchmark | +3,236 | +1.48% |
| snake_abs_exit | +3,209 | +1.51% |
| oracle | +2,080 | +0.99% |
| random_hold | +1,900 | +0.93% |
| intramonth | +1,013 | +0.48% |
| unified | +835 | +0.38% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -283 | -0.13% |
| gold | -2,285 | -1.19% |

Average per day so far: benchmark Rs +688, unified Rs +664, snake_abs_exit_conv Rs +591, snake_abs_exit Rs +543, intraweek Rs +460, snake_abs_conv Rs +459, snake_abs Rs +448, oracle Rs +387, intramonth Rs +375, random_hold Rs +221, snake_anaconda Rs +123, snake_viper_wild Rs +86, benchmark_smallcap Rs +70, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -73, gold Rs -327, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.