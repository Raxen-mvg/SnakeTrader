# Paper trading report

Updated 2026-11-09 10:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,934 | +9.97% | 0 | - | 236 |
| benchmark | 217,212 | +8.61% | 0 | - | 237 |
| intraweek | 216,293 | +8.15% | 30 | 53% | 3,302 |
| snake_abs_exit | 211,681 | +5.84% | 2 | 50% | 308 |
| snake_abs_exit_conv | 211,638 | +5.82% | 2 | 50% | 330 |
| intramonth | 209,864 | +4.93% | 0 | - | 235 |
| snake_abs | 209,617 | +4.81% | 1 | 100% | 255 |
| snake_abs_conv | 209,440 | +4.72% | 1 | 100% | 255 |
| oracle | 209,140 | +4.57% | 0 | - | 233 |
| random_hold | 203,925 | +1.96% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,166 | -0.42% | 3 | 33% | 374 |
| benchmark_smallcap | 198,509 | -0.75% | 0 | - | 237 |
| snake_viper_wild | 197,197 | -1.40% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,847 | -3.08% | 6 | 50% | 1,154 |
| gold | 193,005 | -3.50% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,438 (-4.78%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,930 | +2.82% |
| unified | +4,325 | +2.01% |
| snake_abs_conv | +4,213 | +2.05% |
| snake_abs | +4,198 | +2.04% |
| snake_abs_exit | +3,369 | +1.62% |
| snake_anaconda | +3,339 | +1.71% |
| oracle | +3,313 | +1.61% |
| snake_abs_exit_conv | +3,216 | +1.54% |
| intramonth | +2,261 | +1.09% |
| gold | +1,956 | +1.02% |
| benchmark_smallcap | +1,715 | +0.87% |
| snake_viper_wild | +1,160 | +0.59% |
| snake_viper_tick | +1,137 | +0.59% |
| random_hold | +18 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -275 | -0.13% |

Average per day so far: unified Rs +664, benchmark Rs +574, intraweek Rs +543, snake_abs_exit Rs +433, snake_abs_exit_conv Rs +431, snake_abs_conv Rs +350, snake_abs Rs +343, intramonth Rs +329, oracle Rs +305, random_hold Rs +131, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -33, benchmark_smallcap Rs -57, snake_viper_wild Rs -127, gold Rs -233, snake_viper_tick Rs -324, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.