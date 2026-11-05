# Paper trading report

Updated 2026-11-05 13:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,636 | +8.82% | 0 | - | 236 |
| snake_abs_exit_conv | 214,338 | +7.17% | 1 | 100% | 255 |
| snake_abs_exit | 214,046 | +7.02% | 1 | 100% | 260 |
| benchmark | 213,334 | +6.67% | 0 | - | 237 |
| snake_abs | 211,219 | +5.61% | 1 | 100% | 255 |
| snake_abs_conv | 211,081 | +5.54% | 1 | 100% | 255 |
| intraweek | 210,681 | +5.34% | 25 | 48% | 2,757 |
| intramonth | 209,543 | +4.77% | 0 | - | 235 |
| snake_viper_wild | 206,667 | +3.33% | 3 | 33% | 702 |
| random_hold | 206,128 | +3.06% | 8 | 62% | 649 |
| oracle | 204,043 | +2.02% | 0 | - | 233 |
| snake_viper_tick | 203,119 | +1.56% | 2 | 0% | 532 |
| snake_anaconda | 202,373 | +1.19% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,991 | -0.51% | 0 | - | 237 |
| gold | 194,024 | -2.99% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,098 (-4.95%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,575 | +2.19% |
| unified | +3,197 | +1.49% |
| random_hold | +2,820 | +1.39% |
| gold | +2,630 | +1.37% |
| intramonth | +2,527 | +1.22% |
| benchmark_smallcap | +2,320 | +1.18% |
| oracle | +2,251 | +1.11% |
| intraweek | +983 | +0.47% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -677 | -0.32% |
| snake_abs_conv | -677 | -0.32% |
| snake_abs | -684 | -0.32% |
| snake_abs_exit | -854 | -0.40% |
| snake_anaconda | -1,447 | -0.71% |
| snake_viper_tick | -2,281 | -1.11% |
| snake_viper_wild | -2,363 | -1.13% |

Average per day so far: unified Rs +630, snake_abs_exit_conv Rs +574, snake_abs_exit Rs +562, benchmark Rs +476, snake_abs_conv Rs +443, snake_abs Rs +431, intraweek Rs +381, intramonth Rs +341, snake_viper_wild Rs +333, random_hold Rs +219, snake_viper_tick Rs +183, oracle Rs +144, snake_anaconda Rs +103, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -42, gold Rs -213, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.