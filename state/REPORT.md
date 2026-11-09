# Paper trading report

Updated 2026-11-09 15:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,061 | +10.03% | 0 | - | 236 |
| benchmark | 218,276 | +9.14% | 0 | - | 237 |
| intraweek | 214,501 | +7.25% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,634 | +6.32% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,606 | +6.30% | 2 | 50% | 330 |
| intramonth | 210,684 | +5.34% | 0 | - | 235 |
| snake_abs | 210,625 | +5.31% | 1 | 100% | 255 |
| snake_abs_conv | 210,471 | +5.24% | 1 | 100% | 255 |
| oracle | 210,104 | +5.05% | 0 | - | 233 |
| random_hold | 205,256 | +2.63% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,145 | +0.07% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,318 | -0.84% | 0 | - | 237 |
| snake_viper_wild | 197,365 | -1.32% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,012 | -2.99% | 6 | 50% | 1,154 |
| gold | 192,166 | -3.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,574 (-4.71%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +5,244 | +2.56% |
| snake_abs | +5,205 | +2.53% |
| unified | +4,452 | +2.06% |
| snake_abs_exit | +4,322 | +2.08% |
| snake_anaconda | +4,318 | +2.21% |
| oracle | +4,278 | +2.08% |
| snake_abs_exit_conv | +4,184 | +2.01% |
| intraweek | +4,139 | +1.97% |
| intramonth | +3,081 | +1.48% |
| benchmark_smallcap | +1,525 | +0.78% |
| random_hold | +1,349 | +0.66% |
| snake_viper_wild | +1,328 | +0.68% |
| snake_viper_tick | +1,302 | +0.68% |
| gold | +1,118 | +0.58% |
| benchmark | +788 | +0.36% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +669, benchmark Rs +609, intraweek Rs +483, snake_abs_exit Rs +468, snake_abs_exit_conv Rs +467, snake_abs_conv Rs +388, snake_abs Rs +379, intramonth Rs +356, oracle Rs +337, random_hold Rs +175, nifty_calls Rs +61, snake_anaconda Rs +6, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -65, snake_viper_wild Rs -120, gold Rs -261, snake_viper_tick Rs -315, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.