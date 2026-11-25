# Paper trading report

Updated 2026-11-25 14:40 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,594 | +12.30% | 0 | - | 237 |
| unified | 224,389 | +12.19% | 0 | - | 236 |
| oracle | 212,876 | +6.44% | 0 | - | 233 |
| intramonth | 211,859 | +5.93% | 0 | - | 235 |
| random_hold | 209,857 | +4.93% | 12 | 75% | 1,009 |
| intraweek | 207,135 | +3.57% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,445 | +0.72% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,141 | +0.57% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,556 | -0.22% | 1 | 100% | 255 |
| snake_abs_conv | 199,357 | -0.32% | 1 | 100% | 255 |
| benchmark_smallcap | 198,946 | -0.53% | 0 | - | 237 |
| snake_viper_wild | 197,452 | -1.27% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,088 | -2.96% | 15 | 47% | 2,625 |
| snake_anaconda | 193,284 | -3.36% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,221 | -17.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,943 (-5.53%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,121 | +1.41% |
| random_hold | +1,431 | +0.69% |
| oracle | +533 | +0.25% |
| unified | +104 | +0.05% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -34 | -0.02% |
| intramonth | -893 | -0.42% |
| snake_viper_tick | -3,605 | -1.82% |
| snake_viper_wild | -3,672 | -1.83% |
| gold | -4,209 | -2.48% |
| intraweek | -4,484 | -2.12% |
| snake_anaconda | -5,419 | -2.73% |
| snake_abs_exit_conv | -5,904 | -2.85% |
| snake_abs | -5,905 | -2.87% |
| snake_abs_conv | -5,945 | -2.90% |
| snake_abs_exit | -6,050 | -2.92% |

Average per day so far: benchmark Rs +615, unified Rs +610, oracle Rs +322, intramonth Rs +296, random_hold Rs +246, intraweek Rs +178, nifty_calls Rs +46, snake_abs_exit Rs +39, snake_abs_exit_conv Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -12, snake_abs_conv Rs -17, benchmark_smallcap Rs -29, snake_viper_wild Rs -80, snake_anaconda Rs -192, snake_viper_tick Rs -204, snake_nonews Rs -292, snake Rs -311, gold Rs -869

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.