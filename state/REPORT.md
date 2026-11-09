# Paper trading report

Updated 2026-11-09 15:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,748 | +9.37% | 0 | - | 236 |
| benchmark | 217,947 | +8.97% | 0 | - | 237 |
| intraweek | 214,429 | +7.21% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,175 | +6.09% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,002 | +6.00% | 2 | 50% | 330 |
| intramonth | 209,741 | +4.87% | 0 | - | 235 |
| snake_abs | 209,482 | +4.74% | 1 | 100% | 255 |
| oracle | 209,347 | +4.67% | 0 | - | 233 |
| snake_abs_conv | 209,315 | +4.66% | 1 | 100% | 255 |
| random_hold | 204,590 | +2.29% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,685 | -0.16% | 3 | 33% | 374 |
| benchmark_smallcap | 198,139 | -0.93% | 0 | - | 237 |
| snake_viper_wild | 197,606 | -1.20% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,250 | -2.88% | 6 | 50% | 1,154 |
| gold | 192,249 | -3.88% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,949 (-5.03%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,088 | +1.99% |
| intraweek | +4,066 | +1.93% |
| snake_abs | +4,062 | +1.98% |
| snake_abs_exit | +3,863 | +1.85% |
| snake_anaconda | +3,858 | +1.97% |
| snake_abs_exit_conv | +3,580 | +1.72% |
| oracle | +3,520 | +1.71% |
| unified | +3,138 | +1.46% |
| intramonth | +2,138 | +1.03% |
| snake_viper_wild | +1,569 | +0.80% |
| snake_viper_tick | +1,541 | +0.80% |
| benchmark_smallcap | +1,345 | +0.68% |
| gold | +1,200 | +0.63% |
| random_hold | +683 | +0.34% |
| benchmark | +459 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +625, benchmark Rs +598, intraweek Rs +481, snake_abs_exit Rs +451, snake_abs_exit_conv Rs +445, snake_abs_conv Rs +345, snake_abs Rs +339, intramonth Rs +325, oracle Rs +312, random_hold Rs +153, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -13, benchmark_smallcap Rs -72, snake_viper_wild Rs -109, gold Rs -258, snake_viper_tick Rs -303, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.