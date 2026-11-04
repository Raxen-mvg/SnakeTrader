# Paper trading report

Updated 2026-11-04 12:58 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,607 | +6.80% | 0 | - | 236 |
| snake_abs_exit_conv | 212,410 | +6.21% | 1 | 100% | 255 |
| snake_abs_exit | 212,254 | +6.13% | 1 | 100% | 260 |
| snake_abs | 209,309 | +4.65% | 1 | 100% | 255 |
| snake_abs_conv | 209,155 | +4.58% | 1 | 100% | 255 |
| intraweek | 208,860 | +4.43% | 25 | 48% | 2,757 |
| benchmark | 207,925 | +3.96% | 0 | - | 237 |
| snake_viper_wild | 207,178 | +3.59% | 3 | 33% | 702 |
| intramonth | 206,016 | +3.01% | 0 | - | 235 |
| snake_viper_tick | 203,568 | +1.78% | 2 | 0% | 532 |
| random_hold | 202,771 | +1.39% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,024 | +0.51% | 0 | - | 233 |
| snake_anaconda | 200,847 | +0.42% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,000 | -2.50% | 0 | - | 237 |
| gold | 190,687 | -4.66% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,153 (-5.42%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,240 | +4.04% |
| snake_abs_exit_conv | +8,071 | +3.95% |
| snake_abs_conv | +8,014 | +3.98% |
| snake_abs | +8,000 | +3.97% |
| snake_anaconda | +7,022 | +3.62% |
| gold | +5,409 | +2.92% |
| intraweek | +3,775 | +1.84% |
| random_hold | +2,302 | +1.15% |
| benchmark_smallcap | +2,063 | +1.07% |
| intramonth | +2,045 | +1.00% |
| unified | +1,606 | +0.76% |
| benchmark | +1,224 | +0.59% |
| oracle | +1,034 | +0.52% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,599 | -1.74% |
| snake_viper_wild | -3,714 | -1.76% |

Average per day so far: snake_abs_exit_conv Rs +517, snake_abs_exit Rs +511, unified Rs +504, snake_abs_conv Rs +381, snake_viper_wild Rs +378, snake_abs Rs +372, intraweek Rs +328, benchmark Rs +294, snake_viper_tick Rs +223, intramonth Rs +223, random_hold Rs +103, nifty_calls Rs +68, snake_anaconda Rs +38, oracle Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -217, gold Rs -345, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.