# Paper trading report

Updated 2026-11-09 15:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,425 | +9.71% | 0 | - | 236 |
| benchmark | 218,008 | +9.00% | 0 | - | 237 |
| intraweek | 214,338 | +7.17% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,193 | +6.10% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,050 | +6.03% | 2 | 50% | 330 |
| intramonth | 210,008 | +5.00% | 0 | - | 235 |
| snake_abs | 209,653 | +4.83% | 1 | 100% | 255 |
| snake_abs_conv | 209,491 | +4.75% | 1 | 100% | 255 |
| oracle | 209,447 | +4.72% | 0 | - | 233 |
| random_hold | 204,639 | +2.32% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,666 | -0.17% | 3 | 33% | 374 |
| benchmark_smallcap | 198,307 | -0.85% | 0 | - | 237 |
| snake_viper_wild | 197,324 | -1.34% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,973 | -3.01% | 6 | 50% | 1,154 |
| gold | 192,117 | -3.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,113 (-4.94%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,263 | +2.08% |
| snake_abs | +4,234 | +2.06% |
| intraweek | +3,975 | +1.89% |
| snake_abs_exit | +3,881 | +1.86% |
| snake_anaconda | +3,839 | +1.96% |
| unified | +3,815 | +1.77% |
| snake_abs_exit_conv | +3,628 | +1.74% |
| oracle | +3,620 | +1.76% |
| intramonth | +2,405 | +1.16% |
| benchmark_smallcap | +1,513 | +0.77% |
| snake_viper_wild | +1,287 | +0.66% |
| snake_viper_tick | +1,263 | +0.66% |
| gold | +1,069 | +0.56% |
| random_hold | +732 | +0.36% |
| benchmark | +520 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +647, benchmark Rs +600, intraweek Rs +478, snake_abs_exit Rs +452, snake_abs_exit_conv Rs +446, snake_abs_conv Rs +352, snake_abs Rs +345, intramonth Rs +334, oracle Rs +315, random_hold Rs +155, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -13, benchmark_smallcap Rs -65, snake_viper_wild Rs -122, gold Rs -263, snake_viper_tick Rs -317, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.