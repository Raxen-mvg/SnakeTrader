# Paper trading report

Updated 2026-11-09 12:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,133 | +10.07% | 0 | - | 236 |
| benchmark | 217,166 | +8.58% | 0 | - | 237 |
| intraweek | 215,043 | +7.52% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,150 | +6.08% | 2 | 50% | 330 |
| snake_abs_exit | 211,828 | +5.91% | 2 | 50% | 308 |
| intramonth | 210,178 | +5.09% | 0 | - | 235 |
| oracle | 209,679 | +4.84% | 0 | - | 233 |
| snake_abs | 209,543 | +4.77% | 1 | 100% | 255 |
| snake_abs_conv | 209,365 | +4.68% | 1 | 100% | 255 |
| random_hold | 204,472 | +2.24% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,537 | -0.23% | 7 | 57% | 1,332 |
| snake_anaconda | 199,329 | -0.34% | 3 | 33% | 374 |
| benchmark_smallcap | 198,542 | -0.73% | 0 | - | 237 |
| snake_viper_tick | 196,148 | -1.93% | 6 | 50% | 1,154 |
| gold | 192,314 | -3.84% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,394 (-4.80%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,680 | +2.23% |
| unified | +4,524 | +2.10% |
| snake_abs_conv | +4,138 | +2.02% |
| snake_abs | +4,123 | +2.01% |
| oracle | +3,852 | +1.87% |
| snake_abs_exit_conv | +3,729 | +1.79% |
| snake_abs_exit | +3,516 | +1.69% |
| snake_anaconda | +3,501 | +1.79% |
| snake_viper_wild | +3,499 | +1.78% |
| snake_viper_tick | +3,438 | +1.78% |
| intramonth | +2,575 | +1.24% |
| benchmark_smallcap | +1,749 | +0.89% |
| gold | +1,266 | +0.66% |
| random_hold | +566 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -321 | -0.15% |

Average per day so far: unified Rs +671, benchmark Rs +572, intraweek Rs +501, snake_abs_exit_conv Rs +450, snake_abs_exit Rs +438, snake_abs_conv Rs +347, snake_abs Rs +341, intramonth Rs +339, oracle Rs +323, random_hold Rs +149, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -21, snake_anaconda Rs -27, benchmark_smallcap Rs -56, snake_viper_tick Rs -203, gold Rs -256, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.