# Paper trading report

Updated 2026-11-06 14:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,225 | +8.11% | 0 | - | 237 |
| unified | 215,320 | +7.66% | 0 | - | 236 |
| intraweek | 208,737 | +4.37% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,489 | +4.24% | 1 | 100% | 255 |
| snake_abs_exit | 208,381 | +4.19% | 1 | 100% | 260 |
| intramonth | 207,572 | +3.79% | 0 | - | 235 |
| oracle | 205,552 | +2.78% | 0 | - | 233 |
| snake_abs | 205,474 | +2.74% | 1 | 100% | 255 |
| snake_abs_conv | 205,287 | +2.64% | 1 | 100% | 255 |
| random_hold | 203,437 | +1.72% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,215 | -1.89% | 3 | 33% | 702 |
| snake_anaconda | 195,717 | -2.14% | 3 | 33% | 374 |
| benchmark_smallcap | 195,314 | -2.34% | 0 | - | 237 |
| snake_viper_tick | 192,888 | -3.56% | 2 | 0% | 532 |
| gold | 190,933 | -4.53% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,093 (-6.45%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,456 | +1.15% |
| oracle | +1,480 | +0.72% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -377 | -0.18% |
| unified | -663 | -0.31% |
| intraweek | -682 | -0.33% |
| random_hold | -886 | -0.43% |
| gold | -3,288 | -1.69% |
| benchmark_smallcap | -3,374 | -1.70% |
| snake_abs | -6,215 | -2.94% |
| snake_abs_conv | -6,258 | -2.96% |
| snake_abs_exit | -6,278 | -2.92% |
| snake_abs_exit_conv | -6,315 | -2.94% |
| snake_anaconda | -6,762 | -3.34% |
| snake_viper_tick | -8,250 | -4.10% |
| snake_viper_wild | -8,440 | -4.12% |

Average per day so far: benchmark Rs +559, unified Rs +528, snake_abs_exit_conv Rs +326, snake_abs_exit Rs +322, intraweek Rs +301, intramonth Rs +261, snake_abs_conv Rs +203, snake_abs Rs +203, oracle Rs +191, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -178, snake_viper_wild Rs -180, benchmark_smallcap Rs -187, gold Rs -313, snake_viper_tick Rs -395, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.