# Paper trading report

Updated 2026-11-13 14:04 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,144 | +10.07% | 0 | - | 236 |
| benchmark | 219,056 | +9.53% | 0 | - | 237 |
| snake_abs_exit | 216,537 | +8.27% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,225 | +8.11% | 2 | 50% | 345 |
| intraweek | 215,877 | +7.94% | 30 | 53% | 3,302 |
| oracle | 213,052 | +6.53% | 0 | - | 233 |
| snake_abs | 212,295 | +6.15% | 1 | 100% | 255 |
| snake_abs_conv | 212,129 | +6.07% | 1 | 100% | 255 |
| intramonth | 210,849 | +5.42% | 0 | - | 235 |
| random_hold | 207,207 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 205,821 | +2.91% | 14 | 50% | 2,496 |
| snake_anaconda | 204,520 | +2.26% | 3 | 33% | 374 |
| benchmark_smallcap | 202,567 | +1.28% | 0 | - | 237 |
| snake_viper_tick | 202,301 | +1.15% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,733 | -8.13% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,752 (-4.12%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,219 | +0.57% |
| snake_viper_wild | +528 | +0.26% |
| snake_viper_tick | +519 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -63 | -0.03% |
| unified | -553 | -0.25% |
| benchmark_smallcap | -639 | -0.31% |
| intramonth | -744 | -0.35% |
| random_hold | -847 | -0.41% |
| snake_abs_exit | -906 | -0.42% |
| snake_anaconda | -1,407 | -0.68% |
| benchmark | -1,492 | -0.68% |
| gold | -1,578 | -0.85% |
| snake_abs_exit_conv | -2,449 | -1.12% |
| snake_abs_conv | -3,406 | -1.58% |
| snake_abs | -3,416 | -1.58% |

Average per day so far: unified Rs +610, benchmark Rs +577, snake_abs_exit Rs +551, snake_abs_exit_conv Rs +541, intraweek Rs +481, snake_abs_conv Rs +404, snake_abs Rs +397, oracle Rs +396, intramonth Rs +329, snake_viper_wild Rs +233, random_hold Rs +218, snake_anaconda Rs +161, snake_viper_tick Rs +105, benchmark_smallcap Rs +89, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -493

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.