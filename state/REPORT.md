# Paper trading report

Updated 2026-11-26 13:24 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,543 | +12.77% | 0 | - | 237 |
| unified | 223,446 | +11.72% | 0 | - | 236 |
| oracle | 213,375 | +6.69% | 0 | - | 233 |
| intramonth | 210,670 | +5.33% | 0 | - | 235 |
| random_hold | 209,324 | +4.66% | 13 | 69% | 1,037 |
| intraweek | 207,917 | +3.96% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| snake_abs_exit | 200,195 | +0.10% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,597 | -0.20% | 2 | 50% | 345 |
| snake_abs | 197,948 | -1.03% | 1 | 100% | 255 |
| snake_abs_conv | 197,746 | -1.13% | 1 | 100% | 255 |
| snake_viper_wild | 192,110 | -3.94% | 16 | 50% | 2,827 |
| snake_anaconda | 191,698 | -4.15% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,847 | -5.58% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,977 | -17.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,721 (-5.64%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,805 | +0.91% |
| gold | +1,381 | +0.84% |
| intraweek | +1,174 | +0.57% |
| benchmark | +520 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -168 | -0.08% |
| oracle | -420 | -0.20% |
| unified | -654 | -0.29% |
| intramonth | -1,023 | -0.48% |
| snake_abs_exit | -2,060 | -1.02% |
| snake_abs | -2,202 | -1.10% |
| snake_abs_conv | -2,226 | -1.11% |
| snake_abs_exit_conv | -2,378 | -1.18% |
| snake_anaconda | -2,856 | -1.47% |
| snake_viper_tick | -5,330 | -2.75% |
| snake_viper_wild | -5,434 | -2.75% |

Average per day so far: benchmark Rs +623, unified Rs +572, oracle Rs +326, intramonth Rs +260, random_hold Rs +227, intraweek Rs +193, nifty_calls Rs +45, benchmark_smallcap Rs +17, snake_abs_exit Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -11, snake_abs Rs -53, snake_abs_conv Rs -59, snake_anaconda Rs -231, snake_viper_wild Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -372, gold Rs -830

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.