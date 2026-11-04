# Paper trading report

Updated 2026-11-04 13:10 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,650 | +6.83% | 0 | - | 236 |
| snake_abs_exit_conv | 212,496 | +6.25% | 1 | 100% | 255 |
| snake_abs_exit | 212,356 | +6.18% | 1 | 100% | 260 |
| intraweek | 209,881 | +4.94% | 25 | 48% | 2,757 |
| snake_abs | 209,395 | +4.70% | 1 | 100% | 255 |
| snake_abs_conv | 209,243 | +4.62% | 1 | 100% | 255 |
| benchmark | 208,025 | +4.01% | 0 | - | 237 |
| snake_viper_wild | 207,172 | +3.59% | 3 | 33% | 702 |
| intramonth | 205,928 | +2.96% | 0 | - | 235 |
| snake_viper_tick | 203,563 | +1.78% | 2 | 0% | 532 |
| random_hold | 202,677 | +1.34% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,058 | +0.53% | 3 | 33% | 361 |
| oracle | 201,046 | +0.52% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,090 | -2.46% | 0 | - | 237 |
| gold | 190,966 | -4.52% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,292 (-5.35%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,342 | +4.09% |
| snake_abs_exit_conv | +8,157 | +3.99% |
| snake_abs_conv | +8,102 | +4.03% |
| snake_abs | +8,086 | +4.02% |
| snake_anaconda | +7,233 | +3.73% |
| gold | +5,688 | +3.07% |
| intraweek | +4,796 | +2.34% |
| random_hold | +2,209 | +1.10% |
| benchmark_smallcap | +2,152 | +1.12% |
| intramonth | +1,957 | +0.96% |
| unified | +1,649 | +0.78% |
| benchmark | +1,323 | +0.64% |
| oracle | +1,057 | +0.53% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,603 | -1.74% |
| snake_viper_wild | -3,721 | -1.76% |

Average per day so far: snake_abs_exit_conv Rs +521, snake_abs_exit Rs +515, unified Rs +506, snake_abs_conv Rs +385, snake_viper_wild Rs +377, snake_abs Rs +376, intraweek Rs +366, benchmark Rs +297, snake_viper_tick Rs +223, intramonth Rs +220, random_hold Rs +99, nifty_calls Rs +68, snake_anaconda Rs +48, oracle Rs +39, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -214, gold Rs -335, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.