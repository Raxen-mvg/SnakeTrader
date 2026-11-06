# Paper trading report

Updated 2026-11-06 14:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,547 | +8.27% | 0 | - | 237 |
| unified | 215,113 | +7.56% | 0 | - | 236 |
| snake_abs_exit_conv | 208,413 | +4.21% | 1 | 100% | 255 |
| snake_abs_exit | 208,319 | +4.16% | 1 | 100% | 260 |
| intraweek | 207,920 | +3.96% | 25 | 48% | 2,757 |
| intramonth | 207,411 | +3.71% | 0 | - | 235 |
| oracle | 205,594 | +2.80% | 0 | - | 233 |
| snake_abs | 205,398 | +2.70% | 1 | 100% | 255 |
| snake_abs_conv | 205,214 | +2.61% | 1 | 100% | 255 |
| random_hold | 203,451 | +1.73% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,223 | -1.89% | 3 | 33% | 702 |
| snake_anaconda | 195,762 | -2.12% | 3 | 33% | 374 |
| benchmark_smallcap | 195,370 | -2.31% | 0 | - | 237 |
| snake_viper_tick | 192,897 | -3.55% | 2 | 0% | 532 |
| gold | 190,753 | -4.62% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,934 (-6.53%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,777 | +1.30% |
| oracle | +1,522 | +0.75% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -537 | -0.26% |
| unified | -871 | -0.40% |
| random_hold | -872 | -0.43% |
| intraweek | -1,498 | -0.71% |
| benchmark_smallcap | -3,318 | -1.67% |
| gold | -3,469 | -1.79% |
| snake_abs | -6,290 | -2.97% |
| snake_abs_conv | -6,331 | -2.99% |
| snake_abs_exit | -6,340 | -2.95% |
| snake_abs_exit_conv | -6,390 | -2.98% |
| snake_anaconda | -6,718 | -3.32% |
| snake_viper_tick | -8,241 | -4.10% |
| snake_viper_wild | -8,433 | -4.12% |

Average per day so far: benchmark Rs +571, unified Rs +521, snake_abs_exit_conv Rs +324, snake_abs_exit Rs +320, intraweek Rs +273, intramonth Rs +256, snake_abs_conv Rs +201, snake_abs Rs +200, oracle Rs +193, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -177, snake_viper_wild Rs -180, benchmark_smallcap Rs -185, gold Rs -319, snake_viper_tick Rs -395, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.