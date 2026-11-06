# Paper trading report

Updated 2026-11-06 09:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,091 | +7.55% | 0 | - | 236 |
| benchmark | 214,978 | +7.49% | 0 | - | 237 |
| intraweek | 210,955 | +5.48% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 210,471 | +5.24% | 1 | 100% | 255 |
| snake_abs_exit | 210,235 | +5.12% | 1 | 100% | 260 |
| snake_abs | 207,409 | +3.71% | 1 | 100% | 255 |
| snake_abs_conv | 207,243 | +3.62% | 1 | 100% | 255 |
| intramonth | 206,814 | +3.41% | 0 | - | 235 |
| oracle | 204,597 | +2.30% | 0 | - | 233 |
| random_hold | 204,265 | +2.13% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,561 | -0.72% | 3 | 33% | 702 |
| snake_anaconda | 197,443 | -1.28% | 3 | 33% | 374 |
| snake_viper_tick | 195,194 | -2.40% | 2 | 0% | 532 |
| benchmark_smallcap | 195,067 | -2.47% | 0 | - | 237 |
| gold | 190,374 | -4.81% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,818 (-6.09%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,537 | +0.73% |
| benchmark | +1,209 | +0.56% |
| oracle | +525 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -58 | -0.03% |
| unified | -892 | -0.41% |
| intramonth | -1,134 | -0.55% |
| benchmark_smallcap | -3,621 | -1.82% |
| gold | -3,847 | -1.98% |
| snake_abs | -4,279 | -2.02% |
| snake_abs_conv | -4,302 | -2.03% |
| snake_abs_exit_conv | -4,332 | -2.02% |
| snake_abs_exit | -4,424 | -2.06% |
| snake_anaconda | -5,036 | -2.49% |
| snake_viper_tick | -5,944 | -2.96% |
| snake_viper_wild | -6,095 | -2.98% |

Average per day so far: unified Rs +520, benchmark Rs +516, snake_abs_exit_conv Rs +403, snake_abs_exit Rs +394, intraweek Rs +378, snake_abs_conv Rs +279, snake_abs Rs +274, intramonth Rs +235, oracle Rs +159, random_hold Rs +147, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -69, snake_anaconda Rs -107, benchmark_smallcap Rs -197, snake_viper_tick Rs -267, gold Rs -332, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.