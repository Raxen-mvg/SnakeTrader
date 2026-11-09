# Paper trading report

Updated 2026-11-09 13:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,877 | +9.94% | 0 | - | 236 |
| benchmark | 217,273 | +8.64% | 0 | - | 237 |
| intraweek | 214,836 | +7.42% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,940 | +6.47% | 2 | 50% | 330 |
| snake_abs_exit | 212,491 | +6.25% | 2 | 50% | 308 |
| intramonth | 209,957 | +4.98% | 0 | - | 235 |
| snake_abs | 209,704 | +4.85% | 1 | 100% | 255 |
| oracle | 209,593 | +4.80% | 0 | - | 233 |
| snake_abs_conv | 209,537 | +4.77% | 1 | 100% | 255 |
| random_hold | 204,274 | +2.14% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 200,000 | +0.00% | 3 | 33% | 374 |
| snake_viper_wild | 199,661 | -0.17% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,262 | -0.87% | 0 | - | 237 |
| snake_viper_tick | 196,269 | -1.87% | 6 | 50% | 1,154 |
| gold | 192,216 | -3.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,314 (-4.84%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,519 | +2.17% |
| intraweek | +4,473 | +2.13% |
| snake_abs_conv | +4,310 | +2.10% |
| snake_abs | +4,285 | +2.09% |
| unified | +4,268 | +1.98% |
| snake_abs_exit | +4,179 | +2.01% |
| snake_anaconda | +4,173 | +2.13% |
| oracle | +3,766 | +1.83% |
| snake_viper_wild | +3,624 | +1.85% |
| snake_viper_tick | +3,559 | +1.85% |
| intramonth | +2,354 | +1.13% |
| benchmark_smallcap | +1,469 | +0.75% |
| gold | +1,167 | +0.61% |
| random_hold | +367 | +0.18% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -214 | -0.10% |

Average per day so far: unified Rs +663, benchmark Rs +576, intraweek Rs +495, snake_abs_exit_conv Rs +479, snake_abs_exit Rs +463, snake_abs_conv Rs +353, snake_abs Rs +347, intramonth Rs +332, oracle Rs +320, random_hold Rs +142, nifty_calls Rs +61, snake_anaconda Rs +0, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -15, benchmark_smallcap Rs -67, snake_viper_tick Rs -196, gold Rs -259, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.