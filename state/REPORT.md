# Paper trading report

Updated 2026-11-18 13:13 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,892 | +11.45% | 0 | - | 236 |
| benchmark | 219,668 | +9.83% | 0 | - | 237 |
| intramonth | 212,850 | +6.42% | 0 | - | 235 |
| snake_abs_exit | 212,750 | +6.38% | 2 | 50% | 345 |
| intraweek | 212,584 | +6.29% | 35 | 54% | 3,851 |
| oracle | 212,008 | +6.00% | 0 | - | 233 |
| snake_abs_exit_conv | 211,008 | +5.50% | 2 | 50% | 345 |
| snake_abs | 208,193 | +4.10% | 1 | 100% | 255 |
| snake_abs_conv | 208,056 | +4.03% | 1 | 100% | 255 |
| random_hold | 206,997 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 206,828 | +3.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,296 | +1.65% | 15 | 47% | 2,625 |
| snake_anaconda | 203,175 | +1.59% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,148 | -0.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,877 | -11.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,162 (-4.42%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,453 | +0.66% |
| intramonth | +1,308 | +0.62% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_conv | -363 | -0.17% |
| snake_abs | -366 | -0.17% |
| snake_abs_exit | -392 | -0.18% |
| oracle | -478 | -0.23% |
| snake_abs_exit_conv | -565 | -0.27% |
| intraweek | -739 | -0.35% |
| snake_anaconda | -880 | -0.43% |
| benchmark_smallcap | -1,424 | -0.71% |
| random_hold | -1,435 | -0.69% |
| benchmark | -1,935 | -0.87% |
| snake_viper_tick | -2,540 | -1.23% |
| snake_viper_wild | -2,587 | -1.24% |
| gold | -3,847 | -2.13% |

Average per day so far: unified Rs +636, benchmark Rs +546, snake_abs_exit Rs +386, intramonth Rs +357, intraweek Rs +350, snake_abs_exit_conv Rs +334, oracle Rs +334, snake_abs_conv Rs +244, snake_viper_wild Rs +244, snake_abs Rs +241, random_hold Rs +194, snake_viper_tick Rs +132, snake_anaconda Rs +102, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -27, snake_nonews Rs -326, snake Rs -347, gold Rs -642

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.