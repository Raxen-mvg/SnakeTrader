# Paper trading report

Updated 2026-11-11 15:11 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,224 | +9.61% | 0 | - | 236 |
| benchmark | 219,171 | +9.59% | 0 | - | 237 |
| snake_abs_exit_conv | 217,014 | +8.51% | 2 | 50% | 345 |
| snake_abs_exit | 216,095 | +8.05% | 2 | 50% | 345 |
| snake_abs | 213,751 | +6.88% | 1 | 100% | 255 |
| snake_abs_conv | 213,581 | +6.79% | 1 | 100% | 255 |
| intraweek | 212,863 | +6.43% | 30 | 53% | 3,302 |
| oracle | 211,568 | +5.78% | 0 | - | 233 |
| intramonth | 210,547 | +5.27% | 0 | - | 235 |
| random_hold | 206,862 | +3.43% | 9 | 67% | 709 |
| snake_viper_wild | 206,597 | +3.30% | 10 | 50% | 1,825 |
| snake_anaconda | 204,055 | +2.03% | 3 | 33% | 374 |
| snake_viper_tick | 203,066 | +1.53% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,635 | -5.18% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,718 (-4.64%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,167 | +4.64% |
| snake_viper_tick | +8,990 | +4.63% |
| snake_abs_exit_conv | +5,105 | +2.41% |
| snake_anaconda | +4,589 | +2.30% |
| snake_abs_exit | +4,111 | +1.94% |
| snake_abs | +4,104 | +1.96% |
| snake_abs_conv | +4,104 | +1.96% |
| benchmark_smallcap | +2,612 | +1.32% |
| random_hold | +1,902 | +0.93% |
| oracle | +1,649 | +0.79% |
| benchmark | +1,079 | +0.49% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intramonth | -62 | -0.03% |
| unified | -523 | -0.24% |
| intraweek | -1,678 | -0.78% |
| gold | -2,499 | -1.30% |

Average per day so far: unified Rs +620, benchmark Rs +618, snake_abs_exit_conv Rs +608, snake_abs_exit Rs +575, snake_abs_conv Rs +485, snake_abs Rs +474, intraweek Rs +415, oracle Rs +373, intramonth Rs +340, snake_viper_wild Rs +287, random_hold Rs +221, snake_anaconda Rs +156, snake_viper_tick Rs +153, nifty_calls Rs +59, benchmark_smallcap Rs +29, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -334, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.