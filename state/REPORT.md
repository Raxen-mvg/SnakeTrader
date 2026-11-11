# Paper trading report

Updated 2026-11-11 11:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,404 | +10.70% | 0 | - | 237 |
| unified | 220,679 | +10.34% | 0 | - | 236 |
| snake_abs_exit_conv | 216,425 | +8.21% | 2 | 50% | 345 |
| snake_abs_exit | 215,115 | +7.56% | 2 | 50% | 345 |
| intraweek | 214,125 | +7.06% | 30 | 53% | 3,302 |
| snake_abs | 212,855 | +6.43% | 1 | 100% | 255 |
| snake_abs_conv | 212,703 | +6.35% | 1 | 100% | 255 |
| oracle | 212,184 | +6.09% | 0 | - | 233 |
| intramonth | 211,627 | +5.81% | 0 | - | 235 |
| random_hold | 206,986 | +3.49% | 9 | 67% | 709 |
| snake_anaconda | 203,043 | +1.52% | 3 | 33% | 374 |
| benchmark_smallcap | 201,872 | +0.94% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,402 | +0.70% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,979 | -1.01% | 9 | 44% | 1,639 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,392 (-4.30%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,516 | +2.13% |
| snake_viper_wild | +3,972 | +2.01% |
| snake_viper_tick | +3,903 | +2.01% |
| benchmark_smallcap | +3,699 | +1.87% |
| snake_anaconda | +3,576 | +1.79% |
| benchmark | +3,312 | +1.52% |
| snake_abs_conv | +3,226 | +1.54% |
| snake_abs | +3,208 | +1.53% |
| snake_abs_exit | +3,131 | +1.48% |
| oracle | +2,265 | +1.08% |
| random_hold | +2,025 | +0.99% |
| intramonth | +1,017 | +0.48% |
| unified | +932 | +0.42% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -417 | -0.19% |
| gold | -2,318 | -1.21% |

Average per day so far: benchmark Rs +690, unified Rs +667, snake_abs_exit_conv Rs +587, snake_abs_exit Rs +540, intraweek Rs +456, snake_abs_conv Rs +454, snake_abs Rs +443, oracle Rs +393, intramonth Rs +375, random_hold Rs +225, snake_anaconda Rs +117, benchmark_smallcap Rs +69, snake_viper_wild Rs +61, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -101, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.