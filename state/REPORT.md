# Paper trading report

Updated 2026-11-26 14:22 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,283 | +12.64% | 0 | - | 237 |
| unified | 223,239 | +11.62% | 0 | - | 236 |
| oracle | 213,067 | +6.53% | 0 | - | 233 |
| intramonth | 210,503 | +5.25% | 0 | - | 235 |
| random_hold | 209,332 | +4.67% | 13 | 69% | 1,037 |
| intraweek | 207,846 | +3.92% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,437 | +0.22% | 0 | - | 237 |
| snake_abs_exit | 200,050 | +0.03% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,437 | -0.28% | 2 | 50% | 345 |
| snake_abs | 197,724 | -1.14% | 1 | 100% | 255 |
| snake_abs_conv | 197,517 | -1.24% | 1 | 100% | 255 |
| snake_viper_wild | 192,417 | -3.79% | 16 | 50% | 2,827 |
| snake_anaconda | 191,479 | -4.26% | 3 | 33% | 374 |
| snake_viper_tick | 189,148 | -5.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,520 | -16.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,572 (-5.71%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,923 | +1.17% |
| benchmark_smallcap | +1,625 | +0.82% |
| intraweek | +1,102 | +0.53% |
| benchmark | +260 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -161 | -0.08% |
| oracle | -729 | -0.34% |
| unified | -861 | -0.38% |
| intramonth | -1,190 | -0.56% |
| snake_abs_exit | -2,206 | -1.09% |
| snake_abs | -2,426 | -1.21% |
| snake_abs_conv | -2,455 | -1.23% |
| snake_abs_exit_conv | -2,539 | -1.26% |
| snake_anaconda | -3,074 | -1.58% |
| snake_viper_tick | -5,029 | -2.59% |
| snake_viper_wild | -5,127 | -2.60% |

Average per day so far: benchmark Rs +617, unified Rs +567, oracle Rs +319, intramonth Rs +256, random_hold Rs +228, intraweek Rs +191, nifty_calls Rs +45, benchmark_smallcap Rs +12, snake_abs_exit Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -15, snake_abs Rs -58, snake_abs_conv Rs -65, snake_viper_wild Rs -230, snake_anaconda Rs -237, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -362, gold Rs -817

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.