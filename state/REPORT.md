# Paper trading report

Updated 2026-11-27 12:01 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,587 | +12.29% | 0 | - | 237 |
| unified | 222,651 | +11.32% | 0 | - | 236 |
| oracle | 211,764 | +5.88% | 0 | - | 233 |
| intramonth | 210,543 | +5.27% | 0 | - | 235 |
| random_hold | 210,232 | +5.12% | 13 | 69% | 1,037 |
| intraweek | 207,799 | +3.90% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,330 | +2.67% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,310 | +2.15% | 2 | 50% | 345 |
| benchmark_smallcap | 202,006 | +1.00% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,679 | +0.34% | 1 | 100% | 255 |
| snake_abs_conv | 200,503 | +0.25% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,109 | -2.95% | 3 | 33% | 374 |
| snake_viper_wild | 192,606 | -3.70% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,333 | -5.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,331 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,577 (-5.71%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,252 | +2.12% |
| snake_abs_exit_conv | +3,913 | +1.95% |
| gold | +3,337 | +2.01% |
| snake_abs_conv | +2,137 | +1.08% |
| snake_abs | +2,127 | +1.07% |
| snake_anaconda | +1,812 | +0.94% |
| random_hold | +1,638 | +0.79% |
| benchmark_smallcap | +1,166 | +0.58% |
| intraweek | +750 | +0.36% |
| snake_viper_wild | +400 | +0.21% |
| snake_viper_tick | +392 | +0.21% |
| intramonth | +10 | +0.01% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -428 | -0.19% |
| oracle | -471 | -0.22% |
| benchmark | -1,400 | -0.62% |

Average per day so far: benchmark Rs +585, unified Rs +539, oracle Rs +280, intramonth Rs +251, random_hold Rs +244, intraweek Rs +186, snake_abs_exit Rs +137, snake_abs_exit_conv Rs +111, benchmark_smallcap Rs +53, nifty_calls Rs +44, snake_abs Rs +17, snake_abs_conv Rs +13, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -159, snake_viper_wild Rs -217, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -730

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.