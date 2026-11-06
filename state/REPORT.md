# Paper trading report

Updated 2026-11-06 14:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,233 | +8.12% | 0 | - | 237 |
| unified | 215,180 | +7.59% | 0 | - | 236 |
| snake_abs_exit_conv | 208,944 | +4.47% | 1 | 100% | 255 |
| snake_abs_exit | 208,848 | +4.42% | 1 | 100% | 260 |
| intraweek | 208,180 | +4.09% | 25 | 48% | 2,757 |
| intramonth | 207,471 | +3.73% | 0 | - | 235 |
| snake_abs | 205,922 | +2.96% | 1 | 100% | 255 |
| snake_abs_conv | 205,737 | +2.87% | 1 | 100% | 255 |
| oracle | 205,482 | +2.74% | 0 | - | 233 |
| random_hold | 203,452 | +1.73% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,210 | -1.90% | 3 | 33% | 702 |
| snake_anaconda | 196,044 | -1.98% | 3 | 33% | 374 |
| benchmark_smallcap | 195,347 | -2.33% | 0 | - | 237 |
| snake_viper_tick | 192,882 | -3.56% | 2 | 0% | 532 |
| gold | 190,966 | -4.52% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,109 (-6.45%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,463 | +1.15% |
| oracle | +1,410 | +0.69% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -478 | -0.23% |
| unified | -803 | -0.37% |
| random_hold | -871 | -0.43% |
| intraweek | -1,239 | -0.59% |
| gold | -3,255 | -1.68% |
| benchmark_smallcap | -3,341 | -1.68% |
| snake_abs | -5,767 | -2.72% |
| snake_abs_conv | -5,808 | -2.75% |
| snake_abs_exit | -5,811 | -2.71% |
| snake_abs_exit_conv | -5,859 | -2.73% |
| snake_anaconda | -6,435 | -3.18% |
| snake_viper_tick | -8,256 | -4.11% |
| snake_viper_wild | -8,446 | -4.13% |

Average per day so far: benchmark Rs +560, unified Rs +523, snake_abs_exit_conv Rs +344, snake_abs_exit Rs +340, intraweek Rs +282, intramonth Rs +258, snake_abs_conv Rs +221, snake_abs Rs +219, oracle Rs +189, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -180, benchmark_smallcap Rs -186, gold Rs -312, snake_viper_tick Rs -395, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.