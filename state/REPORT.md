# Paper trading report

Updated 2026-11-09 14:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,315 | +9.66% | 0 | - | 236 |
| benchmark | 217,862 | +8.93% | 0 | - | 237 |
| intraweek | 214,536 | +7.27% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,212 | +6.11% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,118 | +6.06% | 2 | 50% | 330 |
| intramonth | 209,882 | +4.94% | 0 | - | 235 |
| snake_abs | 209,579 | +4.79% | 1 | 100% | 255 |
| snake_abs_conv | 209,412 | +4.71% | 1 | 100% | 255 |
| oracle | 209,293 | +4.65% | 0 | - | 233 |
| random_hold | 204,500 | +2.25% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,692 | -0.15% | 3 | 33% | 374 |
| snake_viper_wild | 198,324 | -0.84% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,172 | -0.91% | 0 | - | 237 |
| snake_viper_tick | 194,957 | -2.52% | 6 | 50% | 1,154 |
| gold | 191,887 | -4.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,084 (-4.96%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,185 | +2.04% |
| intraweek | +4,173 | +1.98% |
| snake_abs | +4,160 | +2.02% |
| snake_abs_exit | +3,900 | +1.87% |
| snake_anaconda | +3,865 | +1.97% |
| unified | +3,706 | +1.72% |
| snake_abs_exit_conv | +3,696 | +1.77% |
| oracle | +3,466 | +1.68% |
| snake_viper_wild | +2,286 | +1.17% |
| intramonth | +2,279 | +1.10% |
| snake_viper_tick | +2,247 | +1.17% |
| benchmark_smallcap | +1,379 | +0.70% |
| gold | +838 | +0.44% |
| random_hold | +594 | +0.29% |
| benchmark | +375 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +644, benchmark Rs +595, intraweek Rs +485, snake_abs_exit Rs +452, snake_abs_exit_conv Rs +449, snake_abs_conv Rs +349, snake_abs Rs +342, intramonth Rs +329, oracle Rs +310, random_hold Rs +150, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -12, benchmark_smallcap Rs -70, snake_viper_wild Rs -76, snake_viper_tick Rs -265, gold Rs -270, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.