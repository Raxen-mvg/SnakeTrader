# Paper trading report

Updated 2026-11-04 13:52 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,406 | +7.20% | 0 | - | 236 |
| snake_abs_exit_conv | 213,304 | +6.65% | 1 | 100% | 255 |
| snake_abs_exit | 213,147 | +6.57% | 1 | 100% | 260 |
| snake_abs | 210,203 | +5.10% | 1 | 100% | 255 |
| snake_abs_conv | 210,049 | +5.03% | 1 | 100% | 255 |
| intraweek | 209,339 | +4.67% | 25 | 48% | 2,757 |
| benchmark | 208,445 | +4.22% | 0 | - | 237 |
| snake_viper_wild | 207,037 | +3.52% | 3 | 33% | 702 |
| intramonth | 206,652 | +3.33% | 0 | - | 235 |
| snake_viper_tick | 203,427 | +1.71% | 2 | 0% | 532 |
| random_hold | 202,937 | +1.47% | 8 | 62% | 649 |
| snake_anaconda | 201,856 | +0.93% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,270 | +0.64% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,076 | -1.96% | 0 | - | 237 |
| gold | 191,147 | -4.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,433 (-5.28%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,133 | +4.48% |
| snake_abs_exit_conv | +8,966 | +4.39% |
| snake_abs_conv | +8,908 | +4.43% |
| snake_abs | +8,894 | +4.42% |
| snake_anaconda | +8,031 | +4.14% |
| gold | +5,869 | +3.17% |
| intraweek | +4,254 | +2.07% |
| benchmark_smallcap | +3,139 | +1.63% |
| intramonth | +2,681 | +1.31% |
| random_hold | +2,469 | +1.23% |
| unified | +2,405 | +1.13% |
| benchmark | +1,744 | +0.84% |
| oracle | +1,280 | +0.64% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,740 | -1.80% |
| snake_viper_wild | -3,856 | -1.83% |

Average per day so far: snake_abs_exit_conv Rs +554, snake_abs_exit Rs +548, unified Rs +534, snake_abs_conv Rs +419, snake_abs Rs +408, snake_viper_wild Rs +370, intraweek Rs +346, benchmark Rs +313, intramonth Rs +246, snake_viper_tick Rs +214, random_hold Rs +109, snake_anaconda Rs +84, nifty_calls Rs +68, oracle Rs +47, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -171, gold Rs -328, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.