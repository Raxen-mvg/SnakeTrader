# Paper trading report

Updated 2026-11-20 09:28 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,065 | +12.53% | 0 | - | 236 |
| benchmark | 221,795 | +10.90% | 0 | - | 237 |
| intramonth | 214,278 | +7.14% | 0 | - | 235 |
| oracle | 212,987 | +6.49% | 0 | - | 233 |
| intraweek | 212,669 | +6.33% | 35 | 54% | 3,851 |
| snake_abs_exit | 210,750 | +5.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 208,802 | +4.40% | 2 | 50% | 345 |
| random_hold | 208,345 | +4.17% | 10 | 70% | 733 |
| snake_abs | 207,034 | +3.52% | 1 | 100% | 255 |
| snake_abs_conv | 206,896 | +3.45% | 1 | 100% | 255 |
| snake_viper_wild | 206,500 | +3.25% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,976 | +1.49% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,641 | +0.82% | 3 | 33% | 374 |
| benchmark_smallcap | 200,179 | +0.09% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,487 | -16.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,606 (-4.20%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +898 | +0.42% |
| unified | +450 | +0.20% |
| intramonth | +270 | +0.13% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -108 | -0.05% |
| intraweek | -220 | -0.10% |
| benchmark | -581 | -0.26% |
| snake_viper_tick | -1,001 | -0.49% |
| snake_viper_wild | -1,022 | -0.49% |
| benchmark_smallcap | -1,289 | -0.64% |
| snake_anaconda | -1,823 | -0.90% |
| snake_abs | -1,946 | -0.93% |
| snake_abs_conv | -1,964 | -0.94% |
| snake_abs_exit_conv | -2,262 | -1.07% |
| snake_abs_exit | -2,601 | -1.22% |
| gold | -8,286 | -4.74% |

Average per day so far: unified Rs +660, benchmark Rs +574, intramonth Rs +376, oracle Rs +342, intraweek Rs +333, snake_abs_exit Rs +307, snake_abs_exit_conv Rs +252, random_hold Rs +220, snake_viper_wild Rs +217, snake_abs_conv Rs +197, snake_abs Rs +195, snake_viper_tick Rs +110, snake_anaconda Rs +50, nifty_calls Rs +48, benchmark_smallcap Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -882

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.