# Paper trading report

Updated 2026-11-11 11:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,336 | +10.67% | 0 | - | 237 |
| unified | 220,559 | +10.28% | 0 | - | 236 |
| snake_abs_exit_conv | 216,496 | +8.25% | 2 | 50% | 345 |
| snake_abs_exit | 215,164 | +7.58% | 2 | 50% | 345 |
| intraweek | 214,165 | +7.08% | 30 | 53% | 3,302 |
| snake_abs | 213,308 | +6.65% | 1 | 100% | 255 |
| snake_abs_conv | 213,150 | +6.58% | 1 | 100% | 255 |
| oracle | 211,787 | +5.89% | 0 | - | 233 |
| intramonth | 211,453 | +5.73% | 0 | - | 235 |
| random_hold | 206,812 | +3.41% | 9 | 67% | 709 |
| snake_anaconda | 203,041 | +1.52% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,771 | +0.89% | 0 | - | 237 |
| snake_viper_wild | 201,770 | +0.89% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,340 | -0.83% | 9 | 44% | 1,639 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,315 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,587 | +2.17% |
| snake_viper_wild | +4,340 | +2.20% |
| snake_viper_tick | +4,264 | +2.20% |
| snake_abs_conv | +3,672 | +1.75% |
| snake_abs | +3,662 | +1.75% |
| benchmark_smallcap | +3,598 | +1.82% |
| snake_anaconda | +3,574 | +1.79% |
| benchmark | +3,244 | +1.49% |
| snake_abs_exit | +3,180 | +1.50% |
| oracle | +1,869 | +0.89% |
| random_hold | +1,851 | +0.90% |
| intramonth | +844 | +0.40% |
| unified | +812 | +0.37% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -377 | -0.18% |
| gold | -2,236 | -1.16% |

Average per day so far: benchmark Rs +688, unified Rs +663, snake_abs_exit_conv Rs +589, snake_abs_exit Rs +542, snake_abs_conv Rs +470, snake_abs Rs +459, intraweek Rs +457, oracle Rs +380, intramonth Rs +369, random_hold Rs +220, snake_anaconda Rs +117, snake_viper_wild Rs +77, benchmark_smallcap Rs +66, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -83, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.