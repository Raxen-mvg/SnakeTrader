# Paper trading report

Updated 2026-11-23 12:58 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,929 | +11.96% | 0 | - | 236 |
| benchmark | 222,544 | +11.27% | 0 | - | 237 |
| intraweek | 212,363 | +6.18% | 40 | 55% | 4,400 |
| intramonth | 212,000 | +6.00% | 0 | - | 235 |
| oracle | 211,740 | +5.87% | 0 | - | 233 |
| random_hold | 208,442 | +4.22% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,979 | +3.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,684 | +2.84% | 2 | 50% | 345 |
| snake_abs | 204,532 | +2.27% | 1 | 100% | 255 |
| snake_abs_conv | 204,371 | +2.19% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,966 | +0.48% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,293 | -0.35% | 0 | - | 237 |
| snake_anaconda | 198,164 | -0.92% | 3 | 33% | 374 |
| snake_viper_tick | 197,538 | -1.23% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,498 | -14.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,039 (-4.98%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,450 | +1.46% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -739 | -0.35% |
| snake_abs_exit_conv | -932 | -0.45% |
| snake_abs | -1,388 | -0.67% |
| snake_abs_conv | -1,412 | -0.69% |
| snake_abs_exit | -1,584 | -0.76% |
| benchmark_smallcap | -1,614 | -0.80% |
| snake_anaconda | -1,742 | -0.87% |
| snake_viper_tick | -1,834 | -0.92% |
| snake_viper_wild | -1,863 | -0.92% |
| unified | -2,253 | -1.00% |
| random_hold | -2,317 | -1.10% |
| benchmark | -2,593 | -1.15% |
| intramonth | -3,005 | -1.40% |
| intraweek | -3,349 | -1.55% |

Average per day so far: unified Rs +614, benchmark Rs +578, intraweek Rs +317, intramonth Rs +308, oracle Rs +301, random_hold Rs +216, snake_abs_exit Rs +194, snake_abs_exit_conv Rs +158, snake_abs Rs +122, snake_abs_conv Rs +121, nifty_calls Rs +47, snake_viper_wild Rs +31, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -20, snake_anaconda Rs -54, snake_viper_tick Rs -88, snake_nonews Rs -300, snake Rs -320, gold Rs -756

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.