# Paper trading report

Updated 2026-11-13 10:58 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,420 | +10.21% | 0 | - | 236 |
| benchmark | 219,966 | +9.98% | 0 | - | 237 |
| snake_abs_exit | 217,174 | +8.59% | 2 | 50% | 345 |
| snake_abs_exit_conv | 217,164 | +8.58% | 2 | 50% | 345 |
| intraweek | 215,783 | +7.89% | 30 | 53% | 3,302 |
| oracle | 213,526 | +6.76% | 0 | - | 233 |
| snake_abs | 213,201 | +6.60% | 1 | 100% | 255 |
| snake_abs_conv | 213,033 | +6.52% | 1 | 100% | 255 |
| intramonth | 211,143 | +5.57% | 0 | - | 235 |
| random_hold | 207,174 | +3.59% | 10 | 70% | 733 |
| snake_viper_wild | 206,532 | +3.27% | 14 | 50% | 2,496 |
| snake_anaconda | 205,144 | +2.57% | 3 | 33% | 374 |
| benchmark_smallcap | 203,620 | +1.81% | 0 | - | 237 |
| snake_viper_tick | 203,000 | +1.50% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,522 | -7.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,989 (-4.01%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +1,239 | +0.60% |
| snake_viper_tick | +1,218 | +0.60% |
| intraweek | +1,125 | +0.52% |
| benchmark_smallcap | +415 | +0.20% |
| oracle | +411 | +0.19% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -269 | -0.12% |
| unified | -277 | -0.12% |
| intramonth | -450 | -0.21% |
| benchmark | -581 | -0.26% |
| snake_anaconda | -783 | -0.38% |
| gold | -789 | -0.43% |
| random_hold | -880 | -0.42% |
| snake_abs_exit_conv | -1,510 | -0.69% |
| snake_abs_conv | -2,502 | -1.16% |
| snake_abs | -2,510 | -1.16% |

Average per day so far: unified Rs +619, benchmark Rs +605, snake_abs_exit Rs +572, snake_abs_exit_conv Rs +572, intraweek Rs +478, snake_abs_conv Rs +434, snake_abs Rs +426, oracle Rs +410, intramonth Rs +338, snake_viper_wild Rs +261, random_hold Rs +217, snake_anaconda Rs +184, snake_viper_tick Rs +136, benchmark_smallcap Rs +125, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -469

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.