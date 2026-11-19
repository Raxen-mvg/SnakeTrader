# Paper trading report

Updated 2026-11-19 11:46 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,688 | +11.84% | 0 | - | 236 |
| benchmark | 221,106 | +10.55% | 0 | - | 237 |
| snake_abs_exit | 213,331 | +6.67% | 2 | 50% | 345 |
| intramonth | 213,213 | +6.61% | 0 | - | 235 |
| intraweek | 211,790 | +5.89% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,480 | +5.74% | 2 | 50% | 345 |
| oracle | 210,990 | +5.50% | 0 | - | 233 |
| snake_abs | 208,827 | +4.41% | 1 | 100% | 255 |
| snake_abs_conv | 208,704 | +4.35% | 1 | 100% | 255 |
| random_hold | 207,618 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,220 | +3.61% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,681 | +1.84% | 15 | 47% | 2,625 |
| snake_anaconda | 203,088 | +1.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,594 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,217 | -12.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,157 (-4.42%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,267 | +0.64% |
| unified | +1,077 | +0.48% |
| intramonth | +940 | +0.44% |
| benchmark | +811 | +0.37% |
| random_hold | +686 | +0.33% |
| oracle | +194 | +0.09% |
| snake_viper_wild | +181 | +0.09% |
| snake_viper_tick | +178 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -50 | -0.02% |
| snake_abs | -609 | -0.29% |
| snake_abs_conv | -621 | -0.30% |
| snake_abs_exit | -701 | -0.33% |
| snake_abs_exit_conv | -903 | -0.42% |
| snake_anaconda | -1,313 | -0.64% |
| gold | -2,104 | -1.19% |

Average per day so far: unified Rs +640, benchmark Rs +570, snake_abs_exit Rs +392, intramonth Rs +357, snake_abs_exit_conv Rs +338, intraweek Rs +319, oracle Rs +297, snake_abs_conv Rs +256, snake_abs Rs +252, snake_viper_wild Rs +249, random_hold Rs +206, snake_viper_tick Rs +142, snake_anaconda Rs +97, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -670

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.