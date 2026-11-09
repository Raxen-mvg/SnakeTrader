# Paper trading report

Updated 2026-11-09 13:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,220 | +10.11% | 0 | - | 236 |
| benchmark | 217,319 | +8.66% | 0 | - | 237 |
| intraweek | 215,118 | +7.56% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,653 | +6.33% | 2 | 50% | 330 |
| snake_abs_exit | 212,289 | +6.14% | 2 | 50% | 308 |
| intramonth | 210,317 | +5.16% | 0 | - | 235 |
| snake_abs | 209,830 | +4.92% | 1 | 100% | 255 |
| oracle | 209,736 | +4.87% | 0 | - | 233 |
| snake_abs_conv | 209,656 | +4.83% | 1 | 100% | 255 |
| random_hold | 204,531 | +2.27% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,719 | -0.14% | 3 | 33% | 374 |
| snake_viper_wild | 199,217 | -0.39% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,565 | -0.72% | 0 | - | 237 |
| snake_viper_tick | 195,834 | -2.08% | 6 | 50% | 1,154 |
| gold | 192,495 | -3.75% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,506 (-4.75%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,756 | +2.26% |
| unified | +4,610 | +2.14% |
| snake_abs_conv | +4,429 | +2.16% |
| snake_abs | +4,410 | +2.15% |
| snake_abs_exit_conv | +4,231 | +2.03% |
| snake_abs_exit | +3,977 | +1.91% |
| oracle | +3,909 | +1.90% |
| snake_anaconda | +3,892 | +1.99% |
| snake_viper_wild | +3,180 | +1.62% |
| snake_viper_tick | +3,124 | +1.62% |
| intramonth | +2,714 | +1.31% |
| benchmark_smallcap | +1,771 | +0.90% |
| gold | +1,447 | +0.76% |
| random_hold | +625 | +0.31% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -168 | -0.08% |

Average per day so far: unified Rs +674, benchmark Rs +577, intraweek Rs +504, snake_abs_exit_conv Rs +469, snake_abs_exit Rs +455, snake_abs_conv Rs +358, snake_abs Rs +351, intramonth Rs +344, oracle Rs +325, random_hold Rs +151, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -11, snake_viper_wild Rs -36, benchmark_smallcap Rs -55, snake_viper_tick Rs -219, gold Rs -250, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.