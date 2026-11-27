# Paper trading report

Updated 2026-11-27 15:01 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,063 | +12.03% | 0 | - | 236 |
| benchmark | 223,738 | +11.87% | 0 | - | 237 |
| oracle | 212,099 | +6.05% | 0 | - | 233 |
| intramonth | 211,556 | +5.78% | 0 | - | 235 |
| random_hold | 211,283 | +5.64% | 13 | 69% | 1,037 |
| intraweek | 208,058 | +4.03% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,699 | +3.35% | 2 | 50% | 345 |
| snake_abs_exit | 204,418 | +2.21% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,715 | +0.86% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,912 | -0.04% | 1 | 100% | 255 |
| snake_abs_conv | 199,728 | -0.14% | 1 | 100% | 255 |
| snake_anaconda | 193,364 | -3.32% | 3 | 33% | 374 |
| snake_viper_wild | 192,610 | -3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,338 | -5.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 171,025 | -14.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,230 (-5.38%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,302 | +3.15% |
| gold | +5,031 | +3.03% |
| snake_abs_exit | +3,340 | +1.66% |
| random_hold | +2,689 | +1.29% |
| snake_abs_conv | +1,361 | +0.69% |
| snake_abs | +1,360 | +0.69% |
| snake_anaconda | +1,067 | +0.56% |
| intramonth | +1,023 | +0.49% |
| intraweek | +1,009 | +0.49% |
| unified | +984 | +0.44% |
| benchmark_smallcap | +874 | +0.43% |
| snake_viper_wild | +405 | +0.21% |
| snake_viper_tick | +397 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -137 | -0.07% |
| benchmark | -2,249 | -0.99% |

Average per day so far: unified Rs +573, benchmark Rs +565, oracle Rs +288, intramonth Rs +275, random_hold Rs +269, intraweek Rs +192, snake_abs_exit_conv Rs +172, snake_abs_exit Rs +113, benchmark_smallcap Rs +45, nifty_calls Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -2, snake_abs_conv Rs -7, snake_anaconda Rs -179, snake_viper_wild Rs -217, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -690

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.