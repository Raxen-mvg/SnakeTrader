# Paper trading report

Updated 2026-11-19 11:54 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,627 | +11.81% | 0 | - | 236 |
| benchmark | 221,297 | +10.65% | 0 | - | 237 |
| intramonth | 213,228 | +6.61% | 0 | - | 235 |
| snake_abs_exit | 213,210 | +6.61% | 2 | 50% | 345 |
| intraweek | 211,793 | +5.90% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,419 | +5.71% | 2 | 50% | 345 |
| oracle | 210,975 | +5.49% | 0 | - | 233 |
| snake_abs | 208,827 | +4.41% | 1 | 100% | 255 |
| snake_abs_conv | 208,699 | +4.35% | 1 | 100% | 255 |
| random_hold | 207,672 | +3.84% | 10 | 70% | 733 |
| snake_viper_wild | 207,220 | +3.61% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,681 | +1.84% | 15 | 47% | 2,625 |
| snake_anaconda | 203,078 | +1.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,151 | -12.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,149 (-4.43%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,289 | +0.65% |
| unified | +1,016 | +0.46% |
| benchmark | +1,002 | +0.46% |
| intramonth | +955 | +0.45% |
| random_hold | +740 | +0.36% |
| snake_viper_wild | +181 | +0.09% |
| oracle | +179 | +0.09% |
| snake_viper_tick | +178 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -47 | -0.02% |
| snake_abs | -610 | -0.29% |
| snake_abs_conv | -626 | -0.30% |
| snake_abs_exit | -822 | -0.38% |
| snake_abs_exit_conv | -964 | -0.45% |
| snake_anaconda | -1,323 | -0.65% |
| gold | -2,170 | -1.22% |

Average per day so far: unified Rs +639, benchmark Rs +576, snake_abs_exit Rs +389, intramonth Rs +358, snake_abs_exit_conv Rs +336, intraweek Rs +319, oracle Rs +297, snake_abs_conv Rs +256, snake_abs Rs +252, snake_viper_wild Rs +249, random_hold Rs +207, snake_viper_tick Rs +142, snake_anaconda Rs +96, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.