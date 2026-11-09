# Paper trading report

Updated 2026-11-09 13:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,920 | +9.96% | 0 | - | 236 |
| benchmark | 217,388 | +8.69% | 0 | - | 237 |
| intraweek | 215,213 | +7.61% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,974 | +6.49% | 2 | 50% | 330 |
| snake_abs_exit | 212,546 | +6.27% | 2 | 50% | 308 |
| intramonth | 210,025 | +5.01% | 0 | - | 235 |
| snake_abs | 210,014 | +5.01% | 1 | 100% | 255 |
| snake_abs_conv | 209,845 | +4.92% | 1 | 100% | 255 |
| oracle | 209,532 | +4.77% | 0 | - | 233 |
| random_hold | 204,433 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,968 | -0.02% | 3 | 33% | 374 |
| snake_viper_wild | 199,530 | -0.23% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,766 | -0.62% | 0 | - | 237 |
| snake_viper_tick | 196,141 | -1.93% | 6 | 50% | 1,154 |
| gold | 192,347 | -3.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,432 (-4.78%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,850 | +2.31% |
| snake_abs_conv | +4,618 | +2.25% |
| snake_abs | +4,595 | +2.24% |
| snake_abs_exit_conv | +4,553 | +2.18% |
| unified | +4,311 | +2.00% |
| snake_abs_exit | +4,234 | +2.03% |
| snake_anaconda | +4,141 | +2.12% |
| oracle | +3,705 | +1.80% |
| snake_viper_wild | +3,492 | +1.78% |
| snake_viper_tick | +3,431 | +1.78% |
| intramonth | +2,422 | +1.17% |
| benchmark_smallcap | +1,973 | +1.00% |
| gold | +1,299 | +0.68% |
| random_hold | +527 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -99 | -0.05% |

Average per day so far: unified Rs +664, benchmark Rs +580, intraweek Rs +507, snake_abs_exit_conv Rs +481, snake_abs_exit Rs +465, snake_abs_conv Rs +365, snake_abs Rs +358, intramonth Rs +334, oracle Rs +318, random_hold Rs +148, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -1, snake_viper_wild Rs -21, benchmark_smallcap Rs -47, snake_viper_tick Rs -203, gold Rs -255, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.