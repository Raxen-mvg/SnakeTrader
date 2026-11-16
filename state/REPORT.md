# Paper trading report

Updated 2026-11-16 14:01 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,691 | +10.35% | 0 | - | 236 |
| benchmark | 219,828 | +9.91% | 0 | - | 237 |
| snake_abs_exit | 213,681 | +6.84% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,497 | +6.25% | 2 | 50% | 345 |
| oracle | 211,639 | +5.82% | 0 | - | 233 |
| intramonth | 211,329 | +5.67% | 0 | - | 235 |
| intraweek | 211,229 | +5.62% | 35 | 54% | 3,851 |
| snake_abs | 209,804 | +4.90% | 1 | 100% | 255 |
| snake_abs_conv | 209,645 | +4.82% | 1 | 100% | 255 |
| random_hold | 207,668 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 205,577 | +2.79% | 14 | 50% | 2,496 |
| snake_anaconda | 204,216 | +2.11% | 3 | 33% | 374 |
| snake_viper_tick | 202,062 | +1.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,381 | +0.19% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,234 | -9.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,482 (-4.76%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,670 | +0.76% |
| intramonth | +1,272 | +0.61% |
| snake_viper_wild | +820 | +0.40% |
| snake_viper_tick | +807 | +0.40% |
| benchmark | +490 | +0.22% |
| random_hold | +442 | +0.21% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -675 | -0.33% |
| oracle | -1,459 | -0.69% |
| benchmark_smallcap | -2,489 | -1.23% |
| snake_abs_conv | -2,722 | -1.28% |
| snake_abs | -2,736 | -1.29% |
| gold | -2,762 | -1.50% |
| snake_abs_exit | -3,304 | -1.52% |
| snake_abs_exit_conv | -3,884 | -1.79% |
| intraweek | -4,916 | -2.27% |

Average per day so far: unified Rs +609, benchmark Rs +583, snake_abs_exit Rs +441, snake_abs_exit_conv Rs +403, oracle Rs +342, intramonth Rs +333, intraweek Rs +330, snake_abs_conv Rs +311, snake_abs Rs +306, random_hold Rs +226, snake_viper_wild Rs +215, snake_anaconda Rs +145, snake_viper_tick Rs +90, nifty_calls Rs +54, benchmark_smallcap Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -552

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.