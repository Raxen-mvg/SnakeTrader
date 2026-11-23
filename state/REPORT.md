# Paper trading report

Updated 2026-11-23 14:31 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,990 | +11.99% | 0 | - | 236 |
| benchmark | 222,276 | +11.14% | 0 | - | 237 |
| intraweek | 212,125 | +6.06% | 40 | 55% | 4,400 |
| oracle | 212,107 | +6.05% | 0 | - | 233 |
| intramonth | 212,100 | +6.05% | 0 | - | 235 |
| random_hold | 208,685 | +4.34% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,140 | +3.57% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,416 | +3.21% | 2 | 50% | 345 |
| snake_abs | 205,058 | +2.53% | 1 | 100% | 255 |
| snake_abs_conv | 204,880 | +2.44% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,124 | +0.56% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,831 | -0.08% | 0 | - | 237 |
| snake_anaconda | 198,170 | -0.92% | 3 | 33% | 374 |
| snake_viper_tick | 197,693 | -1.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,496 | -15.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,198 (-4.90%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,447 | +0.86% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -201 | -0.10% |
| oracle | -371 | -0.17% |
| snake_abs | -862 | -0.42% |
| snake_abs_conv | -903 | -0.44% |
| benchmark_smallcap | -1,076 | -0.54% |
| snake_abs_exit | -1,422 | -0.68% |
| snake_viper_tick | -1,679 | -0.84% |
| snake_viper_wild | -1,705 | -0.84% |
| snake_anaconda | -1,736 | -0.87% |
| random_hold | -2,074 | -0.98% |
| unified | -2,192 | -0.97% |
| benchmark | -2,861 | -1.27% |
| intramonth | -2,904 | -1.35% |
| intraweek | -3,587 | -1.66% |

Average per day so far: unified Rs +615, benchmark Rs +571, intraweek Rs +311, oracle Rs +310, intramonth Rs +310, random_hold Rs +223, snake_abs_exit Rs +198, snake_abs_exit_conv Rs +178, snake_abs Rs +137, snake_abs_conv Rs +136, nifty_calls Rs +47, snake_viper_wild Rs +36, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -5, snake_anaconda Rs -54, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -782

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.