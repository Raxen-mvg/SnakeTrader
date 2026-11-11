# Paper trading report

Updated 2026-11-11 14:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,408 | +10.20% | 0 | - | 236 |
| benchmark | 219,767 | +9.88% | 0 | - | 237 |
| snake_abs_exit_conv | 216,792 | +8.40% | 2 | 50% | 345 |
| snake_abs_exit | 216,115 | +8.06% | 2 | 50% | 345 |
| snake_abs | 213,737 | +6.87% | 1 | 100% | 255 |
| snake_abs_conv | 213,574 | +6.79% | 1 | 100% | 255 |
| intraweek | 213,277 | +6.64% | 30 | 53% | 3,302 |
| oracle | 211,652 | +5.83% | 0 | - | 233 |
| intramonth | 211,380 | +5.69% | 0 | - | 235 |
| random_hold | 207,113 | +3.56% | 9 | 67% | 709 |
| snake_viper_wild | 205,417 | +2.71% | 10 | 50% | 1,825 |
| snake_anaconda | 203,906 | +1.95% | 3 | 33% | 374 |
| snake_viper_tick | 201,911 | +0.96% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,952 | +0.48% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,569 | -5.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,157 (-4.42%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,987 | +4.04% |
| snake_viper_tick | +7,834 | +4.04% |
| snake_abs_exit_conv | +4,883 | +2.30% |
| snake_anaconda | +4,440 | +2.23% |
| snake_abs_exit | +4,132 | +1.95% |
| snake_abs_conv | +4,097 | +1.96% |
| snake_abs | +4,090 | +1.95% |
| benchmark_smallcap | +2,780 | +1.40% |
| random_hold | +2,152 | +1.05% |
| oracle | +1,733 | +0.83% |
| benchmark | +1,675 | +0.77% |
| intramonth | +771 | +0.37% |
| unified | +661 | +0.30% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,265 | -0.59% |
| gold | -2,565 | -1.33% |

Average per day so far: unified Rs +658, benchmark Rs +638, snake_abs_exit_conv Rs +600, snake_abs_exit Rs +576, snake_abs_conv Rs +485, snake_abs Rs +474, intraweek Rs +428, oracle Rs +376, intramonth Rs +367, snake_viper_wild Rs +236, random_hold Rs +229, snake_anaconda Rs +150, snake_viper_tick Rs +96, nifty_calls Rs +59, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -336, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.