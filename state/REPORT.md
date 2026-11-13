# Paper trading report

Updated 2026-11-13 12:07 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,060 | +10.03% | 0 | - | 236 |
| benchmark | 219,278 | +9.64% | 0 | - | 237 |
| snake_abs_exit | 216,461 | +8.23% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,404 | +8.20% | 2 | 50% | 345 |
| intraweek | 215,557 | +7.78% | 30 | 53% | 3,302 |
| oracle | 213,036 | +6.52% | 0 | - | 233 |
| snake_abs | 212,368 | +6.18% | 1 | 100% | 255 |
| snake_abs_conv | 212,199 | +6.10% | 1 | 100% | 255 |
| intramonth | 210,701 | +5.35% | 0 | - | 235 |
| random_hold | 207,104 | +3.55% | 10 | 70% | 733 |
| snake_viper_wild | 205,613 | +2.81% | 14 | 50% | 2,496 |
| snake_anaconda | 204,779 | +2.39% | 3 | 33% | 374 |
| benchmark_smallcap | 202,701 | +1.35% | 0 | - | 237 |
| snake_viper_tick | 202,096 | +1.05% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,618 | -8.19% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,638 (-4.18%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +899 | +0.42% |
| snake_viper_wild | +321 | +0.16% |
| snake_viper_tick | +315 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -80 | -0.04% |
| benchmark_smallcap | -504 | -0.25% |
| unified | -637 | -0.29% |
| intramonth | -893 | -0.42% |
| random_hold | -950 | -0.46% |
| snake_abs_exit | -982 | -0.45% |
| snake_anaconda | -1,148 | -0.56% |
| benchmark | -1,270 | -0.58% |
| gold | -1,693 | -0.91% |
| snake_abs_exit_conv | -2,270 | -1.04% |
| snake_abs_conv | -3,336 | -1.55% |
| snake_abs | -3,344 | -1.55% |

Average per day so far: unified Rs +608, benchmark Rs +584, snake_abs_exit Rs +549, snake_abs_exit_conv Rs +547, intraweek Rs +471, snake_abs_conv Rs +407, snake_abs Rs +399, oracle Rs +395, intramonth Rs +324, snake_viper_wild Rs +225, random_hold Rs +215, snake_anaconda Rs +171, snake_viper_tick Rs +95, benchmark_smallcap Rs +93, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -496

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.