# Paper trading report

Updated 2026-11-19 11:29 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,732 | +11.87% | 0 | - | 236 |
| benchmark | 221,022 | +10.51% | 0 | - | 237 |
| snake_abs_exit | 213,591 | +6.80% | 2 | 50% | 345 |
| intramonth | 213,299 | +6.65% | 0 | - | 235 |
| intraweek | 211,922 | +5.96% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,686 | +5.84% | 2 | 50% | 345 |
| oracle | 211,031 | +5.52% | 0 | - | 233 |
| snake_abs | 209,100 | +4.55% | 1 | 100% | 255 |
| snake_abs_conv | 208,978 | +4.49% | 1 | 100% | 255 |
| random_hold | 207,744 | +3.87% | 10 | 70% | 733 |
| snake_viper_wild | 207,417 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,874 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,359 | +1.68% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,538 | +0.27% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,398 | -12.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,229 (-4.39%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,211 | +0.61% |
| unified | +1,121 | +0.50% |
| intramonth | +1,026 | +0.48% |
| random_hold | +812 | +0.39% |
| benchmark | +727 | +0.33% |
| snake_viper_wild | +378 | +0.18% |
| snake_viper_tick | +370 | +0.18% |
| oracle | +235 | +0.11% |
| intraweek | +82 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -337 | -0.16% |
| snake_abs_conv | -346 | -0.17% |
| snake_abs_exit | -441 | -0.21% |
| snake_abs_exit_conv | -698 | -0.33% |
| snake_anaconda | -1,042 | -0.51% |
| gold | -1,923 | -1.08% |

Average per day so far: unified Rs +641, benchmark Rs +568, snake_abs_exit Rs +400, intramonth Rs +359, snake_abs_exit_conv Rs +344, intraweek Rs +322, oracle Rs +298, snake_abs_conv Rs +264, snake_abs Rs +260, snake_viper_wild Rs +256, random_hold Rs +209, snake_viper_tick Rs +149, snake_anaconda Rs +105, nifty_calls Rs +50, benchmark_smallcap Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -665

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.