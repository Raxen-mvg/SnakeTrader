# Paper trading report

Updated 2026-11-26 13:03 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,849 | +12.93% | 0 | - | 237 |
| unified | 223,468 | +11.73% | 0 | - | 236 |
| oracle | 213,131 | +6.57% | 0 | - | 233 |
| intramonth | 210,575 | +5.29% | 0 | - | 235 |
| random_hold | 209,931 | +4.96% | 13 | 69% | 1,037 |
| intraweek | 208,130 | +4.07% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,661 | +0.33% | 0 | - | 237 |
| snake_abs_exit | 200,338 | +0.17% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,803 | -0.10% | 2 | 50% | 345 |
| snake_abs | 198,125 | -0.94% | 1 | 100% | 255 |
| snake_abs_conv | 197,924 | -1.04% | 1 | 100% | 255 |
| snake_viper_wild | 191,937 | -4.03% | 16 | 50% | 2,827 |
| snake_anaconda | 191,809 | -4.09% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,678 | -5.66% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,158 | -16.92% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,801 (-5.60%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,850 | +0.93% |
| gold | +1,562 | +0.95% |
| intraweek | +1,386 | +0.67% |
| benchmark | +826 | +0.37% |
| random_hold | +438 | +0.21% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -631 | -0.28% |
| oracle | -665 | -0.31% |
| intramonth | -1,118 | -0.53% |
| snake_abs_exit | -1,918 | -0.95% |
| snake_abs | -2,025 | -1.01% |
| snake_abs_conv | -2,048 | -1.02% |
| snake_abs_exit_conv | -2,173 | -1.08% |
| snake_anaconda | -2,744 | -1.41% |
| snake_viper_tick | -5,499 | -2.83% |
| snake_viper_wild | -5,607 | -2.84% |

Average per day so far: benchmark Rs +630, unified Rs +572, oracle Rs +320, intramonth Rs +258, random_hold Rs +242, intraweek Rs +198, nifty_calls Rs +45, benchmark_smallcap Rs +18, snake_abs_exit Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -5, snake_abs Rs -48, snake_abs_conv Rs -55, snake_anaconda Rs -228, snake_viper_wild Rs -244, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -377, gold Rs -825

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.