# Paper trading report

Updated 2026-11-09 15:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,333 | +10.17% | 0 | - | 236 |
| benchmark | 218,123 | +9.06% | 0 | - | 237 |
| intraweek | 214,347 | +7.17% | 30 | 53% | 3,302 |
| snake_abs_exit | 211,766 | +5.88% | 2 | 50% | 308 |
| snake_abs_exit_conv | 211,649 | +5.82% | 2 | 50% | 330 |
| intramonth | 211,388 | +5.69% | 0 | - | 235 |
| oracle | 210,097 | +5.05% | 0 | - | 233 |
| snake_abs | 209,237 | +4.62% | 1 | 100% | 255 |
| snake_abs_conv | 209,067 | +4.53% | 1 | 100% | 255 |
| random_hold | 204,659 | +2.33% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,249 | -0.38% | 3 | 33% | 374 |
| benchmark_smallcap | 198,352 | -0.82% | 0 | - | 237 |
| snake_viper_wild | 197,432 | -1.28% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,079 | -2.96% | 6 | 50% | 1,154 |
| gold | 192,101 | -3.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,491 (-4.75%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,724 | +2.19% |
| oracle | +4,270 | +2.08% |
| intraweek | +3,985 | +1.89% |
| snake_abs_conv | +3,840 | +1.87% |
| snake_abs | +3,817 | +1.86% |
| intramonth | +3,785 | +1.82% |
| snake_abs_exit | +3,454 | +1.66% |
| snake_anaconda | +3,422 | +1.75% |
| snake_abs_exit_conv | +3,227 | +1.55% |
| benchmark_smallcap | +1,558 | +0.79% |
| snake_viper_wild | +1,394 | +0.71% |
| snake_viper_tick | +1,369 | +0.71% |
| gold | +1,052 | +0.55% |
| random_hold | +752 | +0.37% |
| benchmark | +635 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +678, benchmark Rs +604, intraweek Rs +478, snake_abs_exit Rs +436, snake_abs_exit_conv Rs +431, intramonth Rs +380, oracle Rs +337, snake_abs_conv Rs +336, snake_abs Rs +330, random_hold Rs +155, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -30, benchmark_smallcap Rs -63, snake_viper_wild Rs -117, gold Rs -263, snake_viper_tick Rs -312, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.