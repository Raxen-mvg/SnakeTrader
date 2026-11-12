# Paper trading report

Updated 2026-11-12 14:52 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,584 | +10.29% | 0 | - | 236 |
| benchmark | 220,303 | +10.15% | 0 | - | 237 |
| snake_abs_exit_conv | 218,684 | +9.34% | 2 | 50% | 345 |
| snake_abs_exit | 217,564 | +8.78% | 2 | 50% | 345 |
| snake_abs | 215,683 | +7.84% | 1 | 100% | 255 |
| snake_abs_conv | 215,512 | +7.76% | 1 | 100% | 255 |
| intraweek | 214,557 | +7.28% | 30 | 53% | 3,302 |
| oracle | 212,752 | +6.38% | 0 | - | 233 |
| intramonth | 211,304 | +5.65% | 0 | - | 235 |
| random_hold | 207,901 | +3.95% | 10 | 70% | 733 |
| snake_anaconda | 206,166 | +3.08% | 3 | 33% | 374 |
| snake_viper_wild | 205,864 | +2.93% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,026 | +1.51% | 0 | - | 237 |
| snake_viper_tick | 202,344 | +1.17% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,851 | -7.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,847 (-4.08%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,220 | +1.10% |
| snake_abs | +2,059 | +0.96% |
| snake_abs_conv | +2,055 | +0.96% |
| snake_anaconda | +2,043 | +1.00% |
| snake_abs_exit_conv | +1,532 | +0.71% |
| intraweek | +1,424 | +0.67% |
| snake_abs_exit | +1,401 | +0.65% |
| benchmark | +1,040 | +0.47% |
| random_hold | +790 | +0.38% |
| unified | +770 | +0.35% |
| oracle | +749 | +0.35% |
| intramonth | +308 | +0.15% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -865 | -0.43% |
| snake_viper_wild | -878 | -0.42% |
| gold | -4,735 | -2.50% |

Average per day so far: snake_abs_exit_conv Rs +644, unified Rs +643, benchmark Rs +634, snake_abs_exit Rs +606, snake_abs_conv Rs +535, snake_abs Rs +523, intraweek Rs +455, oracle Rs +398, intramonth Rs +353, random_hold Rs +247, snake_viper_wild Rs +244, snake_anaconda Rs +228, snake_viper_tick Rs +112, benchmark_smallcap Rs +108, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -473

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.