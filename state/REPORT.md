# Paper trading report

Updated 2026-11-09 11:29 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,323 | +10.16% | 0 | - | 236 |
| benchmark | 217,304 | +8.65% | 0 | - | 237 |
| intraweek | 215,105 | +7.55% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,132 | +6.07% | 2 | 50% | 330 |
| snake_abs_exit | 211,861 | +5.93% | 2 | 50% | 308 |
| intramonth | 210,323 | +5.16% | 0 | - | 235 |
| snake_abs | 209,647 | +4.82% | 1 | 100% | 255 |
| snake_abs_conv | 209,471 | +4.74% | 1 | 100% | 255 |
| oracle | 209,110 | +4.55% | 0 | - | 233 |
| random_hold | 204,215 | +2.11% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,328 | -0.34% | 3 | 33% | 374 |
| snake_viper_wild | 198,412 | -0.79% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,408 | -0.80% | 0 | - | 237 |
| snake_viper_tick | 195,041 | -2.48% | 6 | 50% | 1,154 |
| gold | 193,120 | -3.44% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,377 (-4.81%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,742 | +2.25% |
| unified | +4,713 | +2.19% |
| snake_abs_conv | +4,244 | +2.07% |
| snake_abs | +4,228 | +2.06% |
| snake_abs_exit_conv | +3,710 | +1.78% |
| snake_abs_exit | +3,549 | +1.70% |
| snake_anaconda | +3,501 | +1.79% |
| oracle | +3,283 | +1.59% |
| intramonth | +2,720 | +1.31% |
| snake_viper_wild | +2,375 | +1.21% |
| snake_viper_tick | +2,331 | +1.21% |
| gold | +2,071 | +1.08% |
| benchmark_smallcap | +1,614 | +0.82% |
| random_hold | +308 | +0.15% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -184 | -0.08% |

Average per day so far: unified Rs +677, benchmark Rs +577, intraweek Rs +503, snake_abs_exit_conv Rs +449, snake_abs_exit Rs +439, snake_abs_conv Rs +351, snake_abs Rs +345, intramonth Rs +344, oracle Rs +304, random_hold Rs +140, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -27, benchmark_smallcap Rs -61, snake_viper_wild Rs -72, gold Rs -229, snake_viper_tick Rs -261, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.