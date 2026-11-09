# Paper trading report

Updated 2026-11-09 14:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,976 | +9.99% | 0 | - | 236 |
| benchmark | 218,038 | +9.02% | 0 | - | 237 |
| intraweek | 214,308 | +7.15% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,579 | +6.29% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,401 | +6.20% | 2 | 50% | 330 |
| intramonth | 209,963 | +4.98% | 0 | - | 235 |
| snake_abs | 209,944 | +4.97% | 1 | 100% | 255 |
| snake_abs_conv | 209,778 | +4.89% | 1 | 100% | 255 |
| oracle | 209,228 | +4.61% | 0 | - | 233 |
| random_hold | 204,458 | +2.23% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,994 | -0.00% | 3 | 33% | 374 |
| benchmark_smallcap | 198,161 | -0.92% | 0 | - | 237 |
| snake_viper_wild | 197,702 | -1.15% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,346 | -2.83% | 6 | 50% | 1,154 |
| gold | 192,101 | -3.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,197 (-4.90%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,551 | +2.22% |
| snake_abs | +4,524 | +2.20% |
| unified | +4,367 | +2.02% |
| snake_abs_exit | +4,267 | +2.05% |
| snake_anaconda | +4,166 | +2.13% |
| snake_abs_exit_conv | +3,979 | +1.91% |
| intraweek | +3,945 | +1.88% |
| oracle | +3,401 | +1.65% |
| intramonth | +2,360 | +1.14% |
| snake_viper_wild | +1,664 | +0.85% |
| snake_viper_tick | +1,636 | +0.85% |
| benchmark_smallcap | +1,368 | +0.69% |
| gold | +1,052 | +0.55% |
| random_hold | +552 | +0.27% |
| benchmark | +551 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +666, benchmark Rs +601, intraweek Rs +477, snake_abs_exit Rs +466, snake_abs_exit_conv Rs +459, snake_abs_conv Rs +362, snake_abs Rs +355, intramonth Rs +332, oracle Rs +308, random_hold Rs +149, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -0, benchmark_smallcap Rs -71, snake_viper_wild Rs -104, gold Rs -263, snake_viper_tick Rs -298, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.