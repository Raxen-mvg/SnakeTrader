# Paper trading report

Updated 2026-11-05 12:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,147 | +8.57% | 0 | - | 236 |
| snake_abs_exit_conv | 213,437 | +6.72% | 1 | 100% | 255 |
| snake_abs_exit | 213,136 | +6.57% | 1 | 100% | 260 |
| benchmark | 213,005 | +6.50% | 0 | - | 237 |
| intraweek | 211,268 | +5.63% | 25 | 48% | 2,757 |
| snake_abs | 210,329 | +5.17% | 1 | 100% | 255 |
| snake_abs_conv | 210,189 | +5.09% | 1 | 100% | 255 |
| intramonth | 209,233 | +4.62% | 0 | - | 235 |
| snake_viper_wild | 206,377 | +3.19% | 3 | 33% | 702 |
| random_hold | 205,645 | +2.82% | 8 | 62% | 649 |
| oracle | 203,849 | +1.93% | 0 | - | 233 |
| snake_viper_tick | 202,827 | +1.41% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,541 | +0.77% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,091 | -0.45% | 0 | - | 237 |
| gold | 194,041 | -2.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,793 (-5.10%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,246 | +2.03% |
| unified | +2,707 | +1.26% |
| gold | +2,647 | +1.38% |
| benchmark_smallcap | +2,421 | +1.23% |
| random_hold | +2,336 | +1.15% |
| intramonth | +2,218 | +1.07% |
| oracle | +2,057 | +1.02% |
| intraweek | +1,571 | +0.75% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,569 | -0.74% |
| snake_abs | -1,574 | -0.74% |
| snake_abs_exit_conv | -1,578 | -0.73% |
| snake_abs_exit | -1,764 | -0.82% |
| snake_anaconda | -2,280 | -1.12% |
| snake_viper_tick | -2,573 | -1.25% |
| snake_viper_wild | -2,653 | -1.27% |

Average per day so far: unified Rs +612, snake_abs_exit_conv Rs +537, snake_abs_exit Rs +525, benchmark Rs +464, snake_abs_conv Rs +408, intraweek Rs +402, snake_abs Rs +397, intramonth Rs +330, snake_viper_wild Rs +319, random_hold Rs +202, snake_viper_tick Rs +166, oracle Rs +137, snake_anaconda Rs +67, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -38, gold Rs -213, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.