# Paper trading report

Updated 2026-11-12 14:02 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,931 | +10.47% | 0 | - | 236 |
| benchmark | 220,318 | +10.16% | 0 | - | 237 |
| snake_abs_exit_conv | 218,920 | +9.46% | 2 | 50% | 345 |
| snake_abs_exit | 217,852 | +8.93% | 2 | 50% | 345 |
| snake_abs | 216,060 | +8.03% | 1 | 100% | 255 |
| snake_abs_conv | 215,888 | +7.94% | 1 | 100% | 255 |
| intraweek | 214,354 | +7.18% | 30 | 53% | 3,302 |
| oracle | 212,832 | +6.42% | 0 | - | 233 |
| intramonth | 211,516 | +5.76% | 0 | - | 235 |
| random_hold | 207,955 | +3.98% | 10 | 70% | 733 |
| snake_viper_wild | 207,274 | +3.64% | 10 | 50% | 1,825 |
| snake_anaconda | 206,677 | +3.34% | 3 | 33% | 374 |
| snake_viper_tick | 203,727 | +1.86% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,802 | +1.40% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,771 | -7.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,984 (-4.01%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,554 | +1.25% |
| snake_abs | +2,436 | +1.14% |
| snake_abs_conv | +2,431 | +1.14% |
| benchmark_smallcap | +1,995 | +0.99% |
| snake_abs_exit_conv | +1,769 | +0.81% |
| snake_abs_exit | +1,690 | +0.78% |
| intraweek | +1,220 | +0.57% |
| unified | +1,117 | +0.51% |
| benchmark | +1,056 | +0.48% |
| random_hold | +845 | +0.41% |
| oracle | +830 | +0.39% |
| snake_viper_wild | +532 | +0.26% |
| intramonth | +520 | +0.25% |
| snake_viper_tick | +518 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,814 | -2.01% |

Average per day so far: unified Rs +654, snake_abs_exit_conv Rs +652, benchmark Rs +635, snake_abs_exit Rs +616, snake_abs_conv Rs +548, snake_abs Rs +535, intraweek Rs +449, oracle Rs +401, intramonth Rs +360, snake_viper_wild Rs +303, random_hold Rs +249, snake_anaconda Rs +247, snake_viper_tick Rs +177, benchmark_smallcap Rs +100, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -445

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.