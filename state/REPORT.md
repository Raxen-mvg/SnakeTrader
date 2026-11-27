# Paper trading report

Updated 2026-11-27 15:30 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,465 | +11.73% | 0 | - | 236 |
| benchmark | 223,439 | +11.72% | 0 | - | 237 |
| oracle | 211,600 | +5.80% | 0 | - | 233 |
| random_hold | 211,366 | +5.68% | 13 | 69% | 1,037 |
| intramonth | 211,162 | +5.58% | 0 | - | 235 |
| intraweek | 207,895 | +3.95% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,535 | +3.27% | 2 | 50% | 345 |
| snake_abs_exit | 204,294 | +2.15% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,446 | +0.72% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,704 | -0.15% | 1 | 100% | 255 |
| snake_abs_conv | 199,513 | -0.24% | 1 | 100% | 255 |
| snake_anaconda | 193,024 | -3.49% | 3 | 33% | 374 |
| snake_viper_wild | 192,855 | -3.57% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,578 | -5.21% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,630 | -14.69% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,938 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,138 | +3.06% |
| gold | +4,636 | +2.79% |
| snake_abs_exit | +3,216 | +1.60% |
| random_hold | +2,772 | +1.33% |
| snake_abs | +1,152 | +0.58% |
| snake_abs_conv | +1,147 | +0.58% |
| intraweek | +847 | +0.41% |
| snake_anaconda | +728 | +0.38% |
| snake_viper_wild | +650 | +0.34% |
| snake_viper_tick | +637 | +0.34% |
| intramonth | +628 | +0.30% |
| benchmark_smallcap | +605 | +0.30% |
| unified | +387 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -636 | -0.30% |
| benchmark | -2,547 | -1.13% |

Average per day so far: unified Rs +559, benchmark Rs +558, oracle Rs +276, random_hold Rs +271, intramonth Rs +266, intraweek Rs +188, snake_abs_exit_conv Rs +168, snake_abs_exit Rs +110, nifty_calls Rs +44, benchmark_smallcap Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -7, snake_abs_conv Rs -12, snake_anaconda Rs -189, snake_viper_wild Rs -210, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -336, gold Rs -699

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.