# Paper trading report

Updated 2026-11-26 14:36 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,543 | +12.77% | 0 | - | 237 |
| unified | 223,172 | +11.59% | 0 | - | 236 |
| oracle | 212,751 | +6.38% | 0 | - | 233 |
| intramonth | 210,531 | +5.26% | 0 | - | 235 |
| random_hold | 208,886 | +4.44% | 13 | 69% | 1,037 |
| intraweek | 207,514 | +3.76% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,773 | +0.39% | 0 | - | 237 |
| snake_abs_exit | 200,212 | +0.11% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,588 | -0.21% | 2 | 50% | 345 |
| snake_abs | 197,928 | -1.04% | 1 | 100% | 255 |
| snake_abs_conv | 197,723 | -1.14% | 1 | 100% | 255 |
| snake_viper_wild | 192,321 | -3.84% | 16 | 50% | 2,827 |
| snake_anaconda | 191,605 | -4.20% | 3 | 33% | 374 |
| snake_viper_tick | 189,054 | -5.47% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,421 | -16.79% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,446 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,962 | +0.99% |
| gold | +1,825 | +1.11% |
| intraweek | +771 | +0.37% |
| benchmark | +520 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -606 | -0.29% |
| unified | -928 | -0.41% |
| oracle | -1,044 | -0.49% |
| intramonth | -1,163 | -0.55% |
| snake_abs_exit | -2,044 | -1.01% |
| snake_abs | -2,221 | -1.11% |
| snake_abs_conv | -2,249 | -1.12% |
| snake_abs_exit_conv | -2,388 | -1.18% |
| snake_anaconda | -2,948 | -1.51% |
| snake_viper_tick | -5,123 | -2.64% |
| snake_viper_wild | -5,223 | -2.64% |

Average per day so far: benchmark Rs +623, unified Rs +565, oracle Rs +311, intramonth Rs +257, random_hold Rs +217, intraweek Rs +183, nifty_calls Rs +45, benchmark_smallcap Rs +21, snake_abs_exit Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -11, snake_abs Rs -53, snake_abs_conv Rs -60, snake_viper_wild Rs -233, snake_anaconda Rs -233, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -365, gold Rs -819

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.