# Paper trading report

Updated 2026-11-20 12:10 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,235 | +13.12% | 0 | - | 236 |
| benchmark | 223,631 | +11.81% | 0 | - | 237 |
| intramonth | 215,178 | +7.59% | 0 | - | 235 |
| intraweek | 214,606 | +7.30% | 35 | 54% | 3,851 |
| oracle | 212,692 | +6.35% | 0 | - | 233 |
| snake_abs_exit | 209,822 | +4.91% | 2 | 50% | 345 |
| random_hold | 208,821 | +4.41% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,880 | +3.94% | 2 | 50% | 345 |
| snake_abs | 206,990 | +3.50% | 1 | 100% | 255 |
| snake_abs_conv | 206,854 | +3.43% | 1 | 100% | 255 |
| snake_viper_wild | 206,098 | +3.05% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,580 | +1.29% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,053 | +0.53% | 3 | 33% | 374 |
| benchmark_smallcap | 200,762 | +0.38% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,421 | -16.79% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,051 (-3.97%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,717 | +0.81% |
| unified | +1,620 | +0.72% |
| benchmark | +1,255 | +0.56% |
| intramonth | +1,170 | +0.55% |
| oracle | +603 | +0.28% |
| random_hold | +368 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -706 | -0.35% |
| snake_viper_tick | -1,397 | -0.69% |
| snake_viper_wild | -1,425 | -0.69% |
| snake_abs | -1,990 | -0.95% |
| snake_abs_conv | -2,006 | -0.96% |
| snake_anaconda | -2,411 | -1.19% |
| snake_abs_exit_conv | -3,184 | -1.51% |
| snake_abs_exit | -3,529 | -1.65% |
| gold | -8,352 | -4.78% |

Average per day so far: unified Rs +690, benchmark Rs +622, intramonth Rs +399, intraweek Rs +384, oracle Rs +334, snake_abs_exit Rs +281, random_hold Rs +232, snake_abs_exit_conv Rs +225, snake_viper_wild Rs +203, snake_abs_conv Rs +196, snake_abs Rs +194, snake_viper_tick Rs +96, nifty_calls Rs +48, snake_anaconda Rs +32, benchmark_smallcap Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -884

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.