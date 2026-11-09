# Paper trading report

Updated 2026-11-09 13:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,751 | +9.88% | 0 | - | 236 |
| benchmark | 217,212 | +8.61% | 0 | - | 237 |
| intraweek | 214,555 | +7.28% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,912 | +6.46% | 2 | 50% | 330 |
| snake_abs_exit | 212,544 | +6.27% | 2 | 50% | 308 |
| intramonth | 209,844 | +4.92% | 0 | - | 235 |
| snake_abs | 209,750 | +4.88% | 1 | 100% | 255 |
| snake_abs_conv | 209,586 | +4.79% | 1 | 100% | 255 |
| oracle | 209,454 | +4.73% | 0 | - | 233 |
| random_hold | 204,242 | +2.12% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,053 | +0.03% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,456 | -0.27% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,363 | -0.82% | 0 | - | 237 |
| snake_viper_tick | 196,067 | -1.97% | 6 | 50% | 1,154 |
| gold | 192,199 | -3.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,206 (-4.90%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,490 | +2.15% |
| snake_abs_conv | +4,359 | +2.12% |
| snake_abs | +4,331 | +2.11% |
| snake_abs_exit | +4,232 | +2.03% |
| snake_anaconda | +4,226 | +2.16% |
| intraweek | +4,192 | +1.99% |
| unified | +4,142 | +1.92% |
| oracle | +3,628 | +1.76% |
| snake_viper_wild | +3,418 | +1.74% |
| snake_viper_tick | +3,357 | +1.74% |
| intramonth | +2,241 | +1.08% |
| benchmark_smallcap | +1,569 | +0.80% |
| gold | +1,151 | +0.60% |
| random_hold | +335 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -275 | -0.13% |

Average per day so far: unified Rs +658, benchmark Rs +574, intraweek Rs +485, snake_abs_exit_conv Rs +478, snake_abs_exit Rs +465, snake_abs_conv Rs +355, snake_abs Rs +348, intramonth Rs +328, oracle Rs +315, random_hold Rs +141, nifty_calls Rs +61, snake_anaconda Rs +2, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -25, benchmark_smallcap Rs -63, snake_viper_tick Rs -207, gold Rs -260, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.