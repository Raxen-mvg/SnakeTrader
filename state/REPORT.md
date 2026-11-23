# Paper trading report

Updated 2026-11-23 10:03 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,444 | +12.72% | 0 | - | 236 |
| benchmark | 223,745 | +11.87% | 0 | - | 237 |
| intraweek | 213,316 | +6.66% | 40 | 55% | 4,400 |
| intramonth | 213,294 | +6.65% | 0 | - | 235 |
| oracle | 211,722 | +5.86% | 0 | - | 233 |
| random_hold | 210,474 | +5.24% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,380 | +4.19% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,597 | +3.30% | 2 | 50% | 345 |
| snake_abs | 205,614 | +2.81% | 1 | 100% | 255 |
| snake_abs_conv | 205,467 | +2.73% | 1 | 100% | 255 |
| snake_viper_wild | 203,535 | +1.77% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,089 | +0.04% | 0 | - | 237 |
| snake_viper_tick | 200,063 | +0.03% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,463 | -0.27% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,986 | -15.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,095 (-4.45%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +937 | +0.56% |
| snake_viper_wild | +706 | +0.35% |
| snake_viper_tick | +691 | +0.35% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -19 | -0.01% |
| snake_abs_exit | -182 | -0.09% |
| random_hold | -285 | -0.14% |
| snake_abs | -306 | -0.15% |
| snake_abs_conv | -316 | -0.15% |
| snake_anaconda | -443 | -0.22% |
| unified | -738 | -0.33% |
| oracle | -757 | -0.36% |
| benchmark_smallcap | -818 | -0.41% |
| benchmark | -1,392 | -0.62% |
| intramonth | -1,710 | -0.80% |
| intraweek | -2,396 | -1.11% |

Average per day so far: unified Rs +652, benchmark Rs +609, intraweek Rs +341, intramonth Rs +341, oracle Rs +301, random_hold Rs +269, snake_abs_exit Rs +233, snake_abs_exit_conv Rs +183, snake_abs_conv Rs +152, snake_abs Rs +152, snake_viper_wild Rs +114, nifty_calls Rs +47, benchmark_smallcap Rs +3, snake_viper_tick Rs +2, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_anaconda Rs -16, snake_nonews Rs -300, snake Rs -320, gold Rs -795

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.