# Paper trading report

Updated 2026-11-09 11:39 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,396 | +10.20% | 0 | - | 236 |
| benchmark | 218,153 | +9.08% | 0 | - | 237 |
| intraweek | 215,241 | +7.62% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,482 | +6.24% | 2 | 50% | 330 |
| snake_abs_exit | 211,948 | +5.97% | 2 | 50% | 308 |
| intramonth | 210,482 | +5.24% | 0 | - | 235 |
| snake_abs | 209,723 | +4.86% | 1 | 100% | 255 |
| snake_abs_conv | 209,547 | +4.77% | 1 | 100% | 255 |
| oracle | 209,412 | +4.71% | 0 | - | 233 |
| random_hold | 204,378 | +2.19% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,758 | -0.12% | 7 | 57% | 1,332 |
| snake_anaconda | 199,470 | -0.27% | 3 | 33% | 374 |
| benchmark_smallcap | 198,856 | -0.57% | 0 | - | 237 |
| snake_viper_tick | 196,363 | -1.82% | 6 | 50% | 1,154 |
| gold | 192,840 | -3.58% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,508 (-4.75%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,878 | +2.32% |
| unified | +4,787 | +2.22% |
| snake_abs_conv | +4,320 | +2.10% |
| snake_abs | +4,304 | +2.10% |
| snake_abs_exit_conv | +4,061 | +1.95% |
| snake_viper_wild | +3,721 | +1.90% |
| snake_viper_tick | +3,653 | +1.90% |
| snake_anaconda | +3,643 | +1.86% |
| snake_abs_exit | +3,636 | +1.75% |
| oracle | +3,585 | +1.74% |
| intramonth | +2,879 | +1.39% |
| benchmark_smallcap | +2,063 | +1.05% |
| gold | +1,792 | +0.94% |
| benchmark | +666 | +0.31% |
| random_hold | +472 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +680, benchmark Rs +605, intraweek Rs +508, snake_abs_exit_conv Rs +462, snake_abs_exit Rs +443, snake_abs_conv Rs +354, intramonth Rs +349, snake_abs Rs +347, oracle Rs +314, random_hold Rs +146, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -11, snake_anaconda Rs -21, benchmark_smallcap Rs -44, snake_viper_tick Rs -191, gold Rs -239, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.