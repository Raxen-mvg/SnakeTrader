# Paper trading report

Updated 2026-11-09 13:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,709 | +9.85% | 0 | - | 236 |
| benchmark | 217,120 | +8.56% | 0 | - | 237 |
| intraweek | 214,676 | +7.34% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,168 | +6.58% | 2 | 50% | 330 |
| snake_abs_exit | 212,688 | +6.34% | 2 | 50% | 308 |
| snake_abs | 209,876 | +4.94% | 1 | 100% | 255 |
| intramonth | 209,829 | +4.91% | 0 | - | 235 |
| snake_abs_conv | 209,711 | +4.86% | 1 | 100% | 255 |
| oracle | 209,528 | +4.76% | 0 | - | 233 |
| random_hold | 204,222 | +2.11% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,178 | +0.09% | 3 | 33% | 374 |
| snake_viper_wild | 200,085 | +0.04% | 7 | 57% | 1,332 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,464 | -0.77% | 0 | - | 237 |
| snake_viper_tick | 196,686 | -1.66% | 6 | 50% | 1,154 |
| gold | 192,150 | -3.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,250 (-4.88%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,746 | +2.28% |
| snake_abs_conv | +4,484 | +2.19% |
| snake_abs | +4,456 | +2.17% |
| snake_abs_exit | +4,376 | +2.10% |
| snake_anaconda | +4,351 | +2.22% |
| intraweek | +4,314 | +2.05% |
| unified | +4,100 | +1.90% |
| snake_viper_wild | +4,048 | +2.06% |
| snake_viper_tick | +3,977 | +2.06% |
| oracle | +3,701 | +1.80% |
| intramonth | +2,226 | +1.07% |
| benchmark_smallcap | +1,670 | +0.85% |
| gold | +1,101 | +0.58% |
| random_hold | +315 | +0.15% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -367 | -0.17% |

Average per day so far: unified Rs +657, benchmark Rs +571, intraweek Rs +489, snake_abs_exit_conv Rs +488, snake_abs_exit Rs +470, snake_abs_conv Rs +360, snake_abs Rs +353, intramonth Rs +328, oracle Rs +318, random_hold Rs +141, nifty_calls Rs +61, snake_anaconda Rs +7, snake_viper_wild Rs +4, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -59, snake_viper_tick Rs -174, gold Rs -262, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.