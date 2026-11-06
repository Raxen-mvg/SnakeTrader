# Paper trading report

Updated 2026-11-06 15:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,824 | +8.91% | 0 | - | 237 |
| unified | 215,885 | +7.94% | 0 | - | 236 |
| intraweek | 210,642 | +5.32% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,195 | +4.60% | 1 | 100% | 255 |
| snake_abs_exit | 209,100 | +4.55% | 1 | 100% | 260 |
| intramonth | 207,743 | +3.87% | 0 | - | 235 |
| snake_abs | 206,170 | +3.08% | 1 | 100% | 255 |
| snake_abs_conv | 205,989 | +2.99% | 1 | 100% | 255 |
| oracle | 205,700 | +2.85% | 0 | - | 233 |
| random_hold | 204,067 | +2.03% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 197,197 | -1.40% | 0 | - | 237 |
| snake_anaconda | 196,481 | -1.76% | 3 | 33% | 374 |
| snake_viper_wild | 196,078 | -1.96% | 4 | 25% | 842 |
| snake_viper_tick | 192,752 | -3.62% | 3 | 0% | 672 |
| gold | 191,279 | -4.36% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,686 (-6.16%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,055 | +1.90% |
| oracle | +1,628 | +0.80% |
| intraweek | +1,224 | +0.58% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -99 | -0.05% |
| intramonth | -206 | -0.10% |
| random_hold | -256 | -0.12% |
| benchmark_smallcap | -1,491 | -0.75% |
| gold | -2,943 | -1.51% |
| snake_abs | -5,518 | -2.61% |
| snake_abs_conv | -5,556 | -2.63% |
| snake_abs_exit | -5,559 | -2.59% |
| snake_abs_exit_conv | -5,609 | -2.61% |
| snake_anaconda | -5,998 | -2.96% |
| snake_viper_tick | -8,386 | -4.17% |
| snake_viper_wild | -8,577 | -4.19% |

Average per day so far: benchmark Rs +615, unified Rs +548, intraweek Rs +367, snake_abs_exit_conv Rs +354, snake_abs_exit Rs +350, intramonth Rs +267, snake_abs_conv Rs +230, snake_abs Rs +229, oracle Rs +197, random_hold Rs +140, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -112, snake_anaconda Rs -147, snake_viper_wild Rs -187, gold Rs -301, snake_viper_tick Rs -403, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.