# Paper trading report

Updated 2026-11-09 14:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,245 | +10.12% | 0 | - | 236 |
| benchmark | 217,947 | +8.97% | 0 | - | 237 |
| intraweek | 214,524 | +7.26% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,274 | +6.64% | 2 | 50% | 330 |
| snake_abs_exit | 212,656 | +6.33% | 2 | 50% | 308 |
| intramonth | 210,213 | +5.11% | 0 | - | 235 |
| snake_abs | 209,912 | +4.96% | 1 | 100% | 255 |
| snake_abs_conv | 209,746 | +4.87% | 1 | 100% | 255 |
| oracle | 209,521 | +4.76% | 0 | - | 233 |
| random_hold | 204,450 | +2.23% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,059 | +0.03% | 3 | 33% | 374 |
| snake_viper_wild | 200,012 | +0.01% | 7 | 57% | 1,332 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,284 | -0.86% | 0 | - | 237 |
| snake_viper_tick | 196,614 | -1.69% | 6 | 50% | 1,154 |
| gold | 192,035 | -3.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,385 (-4.81%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,853 | +2.33% |
| unified | +4,636 | +2.15% |
| snake_abs_conv | +4,519 | +2.20% |
| snake_abs | +4,493 | +2.19% |
| snake_abs_exit | +4,344 | +2.08% |
| snake_anaconda | +4,231 | +2.16% |
| intraweek | +4,162 | +1.98% |
| snake_viper_wild | +3,974 | +2.03% |
| snake_viper_tick | +3,904 | +2.03% |
| oracle | +3,694 | +1.79% |
| intramonth | +2,610 | +1.26% |
| benchmark_smallcap | +1,491 | +0.76% |
| gold | +986 | +0.52% |
| random_hold | +543 | +0.27% |
| benchmark | +459 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +675, benchmark Rs +598, snake_abs_exit_conv Rs +492, intraweek Rs +484, snake_abs_exit Rs +469, snake_abs_conv Rs +361, snake_abs Rs +354, intramonth Rs +340, oracle Rs +317, random_hold Rs +148, nifty_calls Rs +61, snake_anaconda Rs +2, snake_viper_wild Rs +1, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -66, snake_viper_tick Rs -178, gold Rs -266, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.