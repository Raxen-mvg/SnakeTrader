# Paper trading report

Updated 2026-11-05 09:21 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,619 | +8.31% | 0 | - | 236 |
| snake_abs_exit_conv | 216,255 | +8.13% | 1 | 100% | 255 |
| snake_abs_exit | 216,172 | +8.09% | 1 | 100% | 260 |
| snake_abs | 213,100 | +6.55% | 1 | 100% | 255 |
| snake_abs_conv | 212,972 | +6.49% | 1 | 100% | 255 |
| benchmark | 212,148 | +6.07% | 0 | - | 237 |
| intraweek | 211,366 | +5.68% | 25 | 48% | 2,757 |
| intramonth | 209,295 | +4.65% | 0 | - | 235 |
| snake_viper_wild | 206,519 | +3.26% | 3 | 33% | 702 |
| random_hold | 205,105 | +2.55% | 8 | 62% | 649 |
| oracle | 204,401 | +2.20% | 0 | - | 233 |
| snake_anaconda | 203,776 | +1.89% | 3 | 33% | 361 |
| snake_viper_tick | 202,991 | +1.50% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,204 | -0.40% | 0 | - | 237 |
| gold | 194,945 | -2.53% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,654 (-4.67%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,551 | +1.85% |
| benchmark | +3,389 | +1.62% |
| oracle | +2,609 | +1.29% |
| benchmark_smallcap | +2,533 | +1.29% |
| intramonth | +2,280 | +1.10% |
| unified | +2,179 | +1.02% |
| random_hold | +1,796 | +0.88% |
| intraweek | +1,668 | +0.80% |
| snake_abs_exit | +1,272 | +0.59% |
| snake_abs_exit_conv | +1,240 | +0.58% |
| snake_abs_conv | +1,213 | +0.57% |
| snake_abs | +1,197 | +0.56% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -44 | -0.02% |
| snake_viper_tick | -2,410 | -1.17% |
| snake_viper_wild | -2,510 | -1.20% |

Average per day so far: snake_abs_exit_conv Rs +650, snake_abs_exit Rs +647, unified Rs +594, snake_abs_conv Rs +519, snake_abs Rs +504, benchmark Rs +434, intraweek Rs +406, intramonth Rs +332, snake_viper_wild Rs +326, random_hold Rs +182, snake_viper_tick Rs +176, snake_anaconda Rs +164, oracle Rs +157, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -181, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.