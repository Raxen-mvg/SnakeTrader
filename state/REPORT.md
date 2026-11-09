# Paper trading report

Updated 2026-11-09 11:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,306 | +10.15% | 0 | - | 236 |
| benchmark | 217,970 | +8.98% | 0 | - | 237 |
| intraweek | 215,125 | +7.56% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,610 | +6.30% | 2 | 50% | 330 |
| snake_abs_exit | 212,130 | +6.07% | 2 | 50% | 308 |
| intramonth | 210,352 | +5.18% | 0 | - | 235 |
| snake_abs | 209,786 | +4.89% | 1 | 100% | 255 |
| snake_abs_conv | 209,612 | +4.81% | 1 | 100% | 255 |
| oracle | 209,380 | +4.69% | 0 | - | 233 |
| random_hold | 204,347 | +2.17% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,645 | -0.18% | 3 | 33% | 374 |
| snake_viper_wild | 199,632 | -0.18% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,845 | -0.58% | 0 | - | 237 |
| snake_viper_tick | 196,240 | -1.88% | 6 | 50% | 1,154 |
| gold | 192,840 | -3.58% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,460 (-4.77%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,763 | +2.26% |
| unified | +4,696 | +2.18% |
| snake_abs_conv | +4,385 | +2.14% |
| snake_abs | +4,367 | +2.13% |
| snake_abs_exit_conv | +4,188 | +2.01% |
| snake_anaconda | +3,818 | +1.95% |
| snake_abs_exit | +3,818 | +1.83% |
| snake_viper_wild | +3,595 | +1.83% |
| oracle | +3,554 | +1.73% |
| snake_viper_tick | +3,530 | +1.83% |
| intramonth | +2,749 | +1.32% |
| benchmark_smallcap | +2,051 | +1.04% |
| gold | +1,792 | +0.94% |
| benchmark | +482 | +0.22% |
| random_hold | +440 | +0.22% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +677, benchmark Rs +599, intraweek Rs +504, snake_abs_exit_conv Rs +467, snake_abs_exit Rs +449, snake_abs_conv Rs +356, snake_abs Rs +349, intramonth Rs +345, oracle Rs +313, random_hold Rs +145, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -14, snake_viper_wild Rs -17, benchmark_smallcap Rs -44, snake_viper_tick Rs -198, gold Rs -239, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.