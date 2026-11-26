# Paper trading report

Updated 2026-11-26 15:30 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,987 | +12.99% | 0 | - | 237 |
| unified | 223,079 | +11.54% | 0 | - | 236 |
| oracle | 212,236 | +6.12% | 0 | - | 233 |
| intramonth | 210,533 | +5.27% | 0 | - | 235 |
| random_hold | 208,594 | +4.30% | 13 | 69% | 1,037 |
| intraweek | 207,049 | +3.52% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,077 | +0.54% | 2 | 50% | 345 |
| benchmark_smallcap | 200,840 | +0.42% | 0 | - | 237 |
| snake_abs_exit_conv | 200,397 | +0.20% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,552 | -0.72% | 1 | 100% | 255 |
| snake_abs_conv | 198,367 | -0.82% | 1 | 100% | 255 |
| snake_anaconda | 192,296 | -3.85% | 3 | 33% | 374 |
| snake_viper_wild | 192,206 | -3.90% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,941 | -5.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,994 | -17.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,312 (-5.84%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,029 | +1.02% |
| gold | +1,397 | +0.85% |
| benchmark | +964 | +0.43% |
| intraweek | +305 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -899 | -0.43% |
| unified | -1,021 | -0.46% |
| intramonth | -1,160 | -0.55% |
| snake_abs_exit | -1,178 | -0.58% |
| oracle | -1,560 | -0.73% |
| snake_abs_exit_conv | -1,579 | -0.78% |
| snake_abs | -1,598 | -0.80% |
| snake_abs_conv | -1,606 | -0.80% |
| snake_anaconda | -2,257 | -1.16% |
| snake_viper_tick | -5,236 | -2.70% |
| snake_viper_wild | -5,338 | -2.70% |

Average per day so far: benchmark Rs +634, unified Rs +563, oracle Rs +298, intramonth Rs +257, random_hold Rs +210, intraweek Rs +172, nifty_calls Rs +45, snake_abs_exit Rs +28, benchmark_smallcap Rs +23, snake_abs_exit_conv Rs +10, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -37, snake_abs_conv Rs -43, snake_anaconda Rs -214, snake_viper_wild Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -369, gold Rs -829

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.