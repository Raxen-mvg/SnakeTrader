# Paper trading report

Updated 2026-11-12 14:55 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,541 | +10.27% | 0 | - | 236 |
| benchmark | 220,303 | +10.15% | 0 | - | 237 |
| snake_abs_exit_conv | 219,105 | +9.55% | 2 | 50% | 345 |
| snake_abs_exit | 217,906 | +8.95% | 2 | 50% | 345 |
| snake_abs | 216,100 | +8.05% | 1 | 100% | 255 |
| snake_abs_conv | 215,931 | +7.97% | 1 | 100% | 255 |
| intraweek | 214,609 | +7.30% | 30 | 53% | 3,302 |
| oracle | 212,751 | +6.38% | 0 | - | 233 |
| intramonth | 211,329 | +5.66% | 0 | - | 235 |
| random_hold | 207,896 | +3.95% | 10 | 70% | 733 |
| snake_anaconda | 206,507 | +3.25% | 3 | 33% | 374 |
| snake_viper_wild | 205,681 | +2.84% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,004 | +1.50% | 0 | - | 237 |
| snake_viper_tick | 202,164 | +1.08% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,933 | -7.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,919 (-4.04%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs | +2,475 | +1.16% |
| snake_abs_conv | +2,473 | +1.16% |
| snake_anaconda | +2,384 | +1.17% |
| benchmark_smallcap | +2,197 | +1.09% |
| snake_abs_exit_conv | +1,954 | +0.90% |
| snake_abs_exit | +1,744 | +0.81% |
| intraweek | +1,475 | +0.69% |
| benchmark | +1,040 | +0.47% |
| random_hold | +785 | +0.38% |
| oracle | +748 | +0.35% |
| unified | +727 | +0.33% |
| intramonth | +333 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,045 | -0.51% |
| snake_viper_wild | -1,061 | -0.51% |
| gold | -4,653 | -2.45% |

Average per day so far: snake_abs_exit_conv Rs +659, unified Rs +642, benchmark Rs +634, snake_abs_exit Rs +617, snake_abs_conv Rs +549, snake_abs Rs +537, intraweek Rs +457, oracle Rs +398, intramonth Rs +354, random_hold Rs +247, snake_anaconda Rs +241, snake_viper_wild Rs +237, benchmark_smallcap Rs +107, snake_viper_tick Rs +103, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -471

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.