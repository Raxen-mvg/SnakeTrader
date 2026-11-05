# Paper trading report

Updated 2026-11-05 14:23 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,092 | +8.05% | 0 | - | 236 |
| snake_abs_exit_conv | 214,266 | +7.13% | 1 | 100% | 255 |
| snake_abs_exit | 213,999 | +7.00% | 1 | 100% | 260 |
| benchmark | 213,647 | +6.82% | 0 | - | 237 |
| snake_abs | 211,153 | +5.58% | 1 | 100% | 255 |
| snake_abs_conv | 211,013 | +5.51% | 1 | 100% | 255 |
| intraweek | 210,538 | +5.27% | 25 | 48% | 2,757 |
| intramonth | 207,644 | +3.82% | 0 | - | 235 |
| snake_viper_wild | 205,394 | +2.70% | 3 | 33% | 702 |
| random_hold | 204,966 | +2.48% | 8 | 62% | 649 |
| oracle | 203,787 | +1.89% | 0 | - | 233 |
| snake_anaconda | 202,366 | +1.18% | 3 | 33% | 374 |
| snake_viper_tick | 201,863 | +0.93% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,935 | -0.53% | 0 | - | 237 |
| gold | 194,320 | -2.84% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,534 (-5.23%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,888 | +2.34% |
| gold | +2,926 | +1.53% |
| benchmark_smallcap | +2,264 | +1.15% |
| oracle | +1,995 | +0.99% |
| random_hold | +1,657 | +0.81% |
| unified | +1,652 | +0.77% |
| intraweek | +840 | +0.40% |
| intramonth | +628 | +0.30% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -745 | -0.35% |
| snake_abs_exit_conv | -749 | -0.35% |
| snake_abs | -750 | -0.35% |
| snake_abs_exit | -902 | -0.42% |
| snake_anaconda | -1,454 | -0.71% |
| snake_viper_tick | -3,537 | -1.72% |
| snake_viper_wild | -3,636 | -1.74% |

Average per day so far: unified Rs +575, snake_abs_exit_conv Rs +571, snake_abs_exit Rs +560, benchmark Rs +487, snake_abs_conv Rs +441, snake_abs Rs +429, intraweek Rs +376, intramonth Rs +273, snake_viper_wild Rs +270, random_hold Rs +177, oracle Rs +135, snake_viper_tick Rs +110, snake_anaconda Rs +103, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -44, gold Rs -203, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.