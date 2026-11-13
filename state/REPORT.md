# Paper trading report

Updated 2026-11-13 14:37 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,505 | +10.25% | 0 | - | 236 |
| benchmark | 219,194 | +9.60% | 0 | - | 237 |
| snake_abs_exit | 216,204 | +8.10% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,041 | +8.02% | 2 | 50% | 345 |
| intraweek | 215,811 | +7.91% | 30 | 53% | 3,302 |
| oracle | 213,188 | +6.59% | 0 | - | 233 |
| snake_abs | 212,058 | +6.03% | 1 | 100% | 255 |
| snake_abs_conv | 211,888 | +5.94% | 1 | 100% | 255 |
| intramonth | 211,040 | +5.52% | 0 | - | 235 |
| random_hold | 207,230 | +3.62% | 10 | 70% | 733 |
| snake_viper_wild | 205,110 | +2.56% | 14 | 50% | 2,496 |
| snake_anaconda | 204,303 | +2.15% | 3 | 33% | 374 |
| benchmark_smallcap | 202,802 | +1.40% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,602 | +0.80% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,078 | -7.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,836 (-4.08%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,153 | +0.54% |
| oracle | +72 | +0.03% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_viper_tick | -179 | -0.09% |
| snake_viper_wild | -182 | -0.09% |
| unified | -191 | -0.09% |
| benchmark_smallcap | -404 | -0.20% |
| intramonth | -553 | -0.26% |
| random_hold | -823 | -0.40% |
| gold | -1,233 | -0.67% |
| snake_abs_exit | -1,238 | -0.57% |
| benchmark | -1,354 | -0.61% |
| snake_anaconda | -1,624 | -0.79% |
| snake_abs_exit_conv | -2,633 | -1.20% |
| snake_abs_conv | -3,647 | -1.69% |
| snake_abs | -3,654 | -1.69% |

Average per day so far: unified Rs +621, benchmark Rs +582, snake_abs_exit Rs +540, snake_abs_exit_conv Rs +535, intraweek Rs +479, oracle Rs +400, snake_abs_conv Rs +396, snake_abs Rs +389, intramonth Rs +335, random_hold Rs +219, snake_viper_wild Rs +204, snake_anaconda Rs +154, benchmark_smallcap Rs +97, snake_viper_tick Rs +73, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -482

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.