# Paper trading report

Updated 2026-11-09 13:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,898 | +9.95% | 0 | - | 236 |
| benchmark | 217,457 | +8.73% | 0 | - | 237 |
| intraweek | 214,761 | +7.38% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,234 | +6.62% | 2 | 50% | 330 |
| snake_abs_exit | 212,746 | +6.37% | 2 | 50% | 308 |
| intramonth | 209,947 | +4.97% | 0 | - | 235 |
| snake_abs | 209,930 | +4.96% | 1 | 100% | 255 |
| snake_abs_conv | 209,767 | +4.88% | 1 | 100% | 255 |
| oracle | 209,349 | +4.67% | 0 | - | 233 |
| random_hold | 204,274 | +2.14% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,154 | +0.08% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,698 | -0.15% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,542 | -0.73% | 0 | - | 237 |
| snake_viper_tick | 196,307 | -1.85% | 6 | 50% | 1,154 |
| gold | 192,199 | -3.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,304 (-4.85%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,812 | +2.31% |
| snake_abs_conv | +4,540 | +2.21% |
| snake_abs | +4,511 | +2.20% |
| snake_abs_exit | +4,434 | +2.13% |
| intraweek | +4,399 | +2.09% |
| snake_anaconda | +4,327 | +2.21% |
| unified | +4,289 | +1.99% |
| snake_viper_wild | +3,661 | +1.87% |
| snake_viper_tick | +3,597 | +1.87% |
| oracle | +3,522 | +1.71% |
| intramonth | +2,344 | +1.13% |
| benchmark_smallcap | +1,749 | +0.89% |
| gold | +1,151 | +0.60% |
| random_hold | +367 | +0.18% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -31 | -0.01% |

Average per day so far: unified Rs +663, benchmark Rs +582, intraweek Rs +492, snake_abs_exit_conv Rs +490, snake_abs_exit Rs +472, snake_abs_conv Rs +362, snake_abs Rs +355, intramonth Rs +332, oracle Rs +312, random_hold Rs +142, nifty_calls Rs +61, snake_anaconda Rs +6, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -14, benchmark_smallcap Rs -56, snake_viper_tick Rs -194, gold Rs -260, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.