# Paper trading report

Updated 2026-11-25 12:23 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,872 | +12.94% | 0 | - | 237 |
| unified | 225,553 | +12.78% | 0 | - | 236 |
| intramonth | 213,483 | +6.74% | 0 | - | 235 |
| oracle | 212,990 | +6.50% | 0 | - | 233 |
| random_hold | 210,208 | +5.10% | 12 | 75% | 1,009 |
| intraweek | 208,350 | +4.17% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,362 | +1.18% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,937 | +0.97% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,692 | +0.35% | 1 | 100% | 255 |
| snake_abs_conv | 200,511 | +0.26% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,607 | -0.20% | 0 | - | 237 |
| snake_viper_wild | 196,770 | -1.61% | 16 | 50% | 2,827 |
| snake_anaconda | 194,082 | -2.96% | 3 | 33% | 374 |
| snake_viper_tick | 193,420 | -3.29% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,531 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,706 (-5.15%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,399 | +1.99% |
| random_hold | +1,782 | +0.85% |
| unified | +1,268 | +0.56% |
| intramonth | +732 | +0.34% |
| oracle | +648 | +0.30% |
| benchmark_smallcap | +628 | +0.32% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,269 | -1.54% |
| snake_viper_tick | -4,272 | -2.16% |
| snake_viper_wild | -4,354 | -2.17% |
| snake_anaconda | -4,621 | -2.33% |
| snake_abs | -4,769 | -2.32% |
| snake_abs_conv | -4,792 | -2.33% |
| gold | -4,899 | -2.89% |
| snake_abs_exit_conv | -5,109 | -2.47% |
| snake_abs_exit | -5,133 | -2.47% |

Average per day so far: benchmark Rs +647, unified Rs +639, intramonth Rs +337, oracle Rs +325, random_hold Rs +255, intraweek Rs +209, snake_abs_exit Rs +64, snake_abs_exit_conv Rs +52, nifty_calls Rs +46, snake_abs Rs +18, snake_abs_conv Rs +14, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_viper_wild Rs -101, snake_anaconda Rs -169, snake_viper_tick Rs -227, snake_nonews Rs -292, snake Rs -311, gold Rs -887

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.