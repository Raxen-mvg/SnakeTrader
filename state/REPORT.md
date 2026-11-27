# Paper trading report

Updated 2026-11-27 09:24 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,459 | +12.73% | 0 | - | 237 |
| unified | 223,157 | +11.58% | 0 | - | 236 |
| oracle | 212,492 | +6.25% | 0 | - | 233 |
| intramonth | 210,796 | +5.40% | 0 | - | 235 |
| random_hold | 209,379 | +4.69% | 13 | 69% | 1,037 |
| intraweek | 207,777 | +3.89% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,348 | +1.17% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,513 | +0.76% | 2 | 50% | 345 |
| benchmark_smallcap | 201,289 | +0.64% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,179 | -0.41% | 1 | 100% | 255 |
| snake_abs_conv | 198,990 | -0.51% | 1 | 100% | 255 |
| snake_anaconda | 192,870 | -3.56% | 3 | 33% | 374 |
| snake_viper_wild | 191,942 | -4.03% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,683 | -5.66% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,263 | -15.87% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,630 (-5.69%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,269 | +1.37% |
| snake_abs_exit | +1,271 | +0.63% |
| snake_abs_exit_conv | +1,116 | +0.56% |
| random_hold | +785 | +0.38% |
| intraweek | +728 | +0.35% |
| snake_abs | +627 | +0.32% |
| snake_abs_conv | +623 | +0.31% |
| snake_anaconda | +573 | +0.30% |
| benchmark_smallcap | +448 | +0.22% |
| intramonth | +263 | +0.12% |
| oracle | +256 | +0.12% |
| unified | +78 | +0.04% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -258 | -0.14% |
| snake_viper_wild | -264 | -0.14% |
| benchmark | -528 | -0.23% |

Average per day so far: benchmark Rs +606, unified Rs +551, oracle Rs +297, intramonth Rs +257, random_hold Rs +223, intraweek Rs +185, snake_abs_exit Rs +60, nifty_calls Rs +44, snake_abs_exit_conv Rs +39, benchmark_smallcap Rs +34, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -21, snake_abs_conv Rs -26, snake_anaconda Rs -193, snake_viper_wild Rs -237, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -365, gold Rs -756

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.