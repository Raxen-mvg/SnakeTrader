# Paper trading report

Updated 2026-11-05 14:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,087 | +8.04% | 0 | - | 236 |
| snake_abs_exit_conv | 214,585 | +7.29% | 1 | 100% | 255 |
| snake_abs_exit | 214,299 | +7.15% | 1 | 100% | 260 |
| benchmark | 213,907 | +6.95% | 0 | - | 237 |
| snake_abs | 211,468 | +5.73% | 1 | 100% | 255 |
| snake_abs_conv | 211,328 | +5.66% | 1 | 100% | 255 |
| intraweek | 209,777 | +4.89% | 25 | 48% | 2,757 |
| intramonth | 207,783 | +3.89% | 0 | - | 235 |
| snake_viper_wild | 205,549 | +2.77% | 3 | 33% | 702 |
| random_hold | 204,661 | +2.33% | 8 | 62% | 649 |
| oracle | 204,058 | +2.03% | 0 | - | 233 |
| snake_anaconda | 202,366 | +1.18% | 3 | 33% | 374 |
| snake_viper_tick | 202,015 | +1.01% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,159 | -0.42% | 0 | - | 237 |
| gold | 194,369 | -2.81% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,537 (-5.23%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,148 | +2.47% |
| gold | +2,976 | +1.55% |
| benchmark_smallcap | +2,489 | +1.26% |
| oracle | +2,266 | +1.12% |
| unified | +1,647 | +0.77% |
| random_hold | +1,352 | +0.67% |
| intramonth | +767 | +0.37% |
| intraweek | +79 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -430 | -0.20% |
| snake_abs_conv | -431 | -0.20% |
| snake_abs | -435 | -0.20% |
| snake_abs_exit | -601 | -0.28% |
| snake_anaconda | -1,454 | -0.71% |
| snake_viper_tick | -3,386 | -1.65% |
| snake_viper_wild | -3,481 | -1.67% |

Average per day so far: snake_abs_exit_conv Rs +583, unified Rs +575, snake_abs_exit Rs +572, benchmark Rs +497, snake_abs_conv Rs +453, snake_abs Rs +441, intraweek Rs +349, intramonth Rs +278, snake_viper_wild Rs +277, random_hold Rs +166, oracle Rs +145, snake_viper_tick Rs +119, snake_anaconda Rs +103, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -35, gold Rs -201, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.