# Paper trading report

Updated 2026-11-20 12:34 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,113 | +13.06% | 0 | - | 236 |
| benchmark | 224,120 | +12.06% | 0 | - | 237 |
| intramonth | 215,055 | +7.53% | 0 | - | 235 |
| intraweek | 214,899 | +7.45% | 35 | 54% | 3,851 |
| oracle | 212,742 | +6.37% | 0 | - | 233 |
| snake_abs_exit | 209,142 | +4.57% | 2 | 50% | 345 |
| random_hold | 209,115 | +4.56% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,197 | +3.60% | 2 | 50% | 345 |
| snake_abs | 206,357 | +3.18% | 1 | 100% | 255 |
| snake_abs_conv | 206,222 | +3.11% | 1 | 100% | 255 |
| snake_viper_wild | 205,574 | +2.79% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,067 | +1.03% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,941 | +0.47% | 0 | - | 237 |
| snake_anaconda | 200,317 | +0.16% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,586 | -16.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,952 (-4.02%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,010 | +0.94% |
| benchmark | +1,744 | +0.78% |
| unified | +1,498 | +0.67% |
| intramonth | +1,047 | +0.49% |
| random_hold | +662 | +0.32% |
| oracle | +653 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -527 | -0.26% |
| snake_viper_tick | -1,910 | -0.94% |
| snake_viper_wild | -1,949 | -0.94% |
| snake_abs | -2,623 | -1.25% |
| snake_abs_conv | -2,638 | -1.26% |
| snake_anaconda | -3,147 | -1.55% |
| snake_abs_exit_conv | -3,868 | -1.83% |
| snake_abs_exit | -4,209 | -1.97% |
| gold | -8,187 | -4.68% |

Average per day so far: unified Rs +687, benchmark Rs +635, intramonth Rs +396, intraweek Rs +392, oracle Rs +335, snake_abs_exit Rs +261, random_hold Rs +240, snake_abs_exit_conv Rs +206, snake_viper_wild Rs +186, snake_abs_conv Rs +178, snake_abs Rs +177, snake_viper_tick Rs +77, nifty_calls Rs +48, benchmark_smallcap Rs +28, snake_anaconda Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -879

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.