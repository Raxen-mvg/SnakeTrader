# Paper trading report

Updated 2026-11-11 14:06 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,298 | +10.15% | 0 | - | 236 |
| benchmark | 220,134 | +10.07% | 0 | - | 237 |
| snake_abs_exit_conv | 216,500 | +8.25% | 2 | 50% | 345 |
| snake_abs_exit | 215,740 | +7.87% | 2 | 50% | 345 |
| snake_abs | 213,684 | +6.84% | 1 | 100% | 255 |
| snake_abs_conv | 213,513 | +6.76% | 1 | 100% | 255 |
| intraweek | 213,496 | +6.75% | 30 | 53% | 3,302 |
| oracle | 211,812 | +5.91% | 0 | - | 233 |
| intramonth | 211,306 | +5.65% | 0 | - | 235 |
| random_hold | 207,026 | +3.51% | 9 | 67% | 709 |
| snake_viper_wild | 205,188 | +2.59% | 10 | 50% | 1,825 |
| snake_anaconda | 203,509 | +1.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,686 | +0.84% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,165 | +0.58% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,799 | -5.10% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,167 (-4.42%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,758 | +3.93% |
| snake_viper_tick | +7,610 | +3.92% |
| snake_abs_exit_conv | +4,591 | +2.17% |
| snake_anaconda | +4,042 | +2.03% |
| snake_abs | +4,037 | +1.93% |
| snake_abs_conv | +4,036 | +1.93% |
| snake_abs_exit | +3,757 | +1.77% |
| benchmark_smallcap | +2,993 | +1.51% |
| random_hold | +2,066 | +1.01% |
| benchmark | +2,043 | +0.94% |
| oracle | +1,894 | +0.90% |
| intramonth | +697 | +0.33% |
| unified | +551 | +0.25% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,045 | -0.49% |
| gold | -2,334 | -1.22% |

Average per day so far: unified Rs +655, benchmark Rs +649, snake_abs_exit_conv Rs +589, snake_abs_exit Rs +562, snake_abs_conv Rs +483, snake_abs Rs +472, intraweek Rs +435, oracle Rs +381, intramonth Rs +365, random_hold Rs +227, snake_viper_wild Rs +226, snake_anaconda Rs +135, snake_viper_tick Rs +84, nifty_calls Rs +59, benchmark_smallcap Rs +43, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.