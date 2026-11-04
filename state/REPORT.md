# Paper trading report

Updated 2026-11-04 13:40 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,985 | +6.99% | 0 | - | 236 |
| snake_abs_exit_conv | 212,702 | +6.35% | 1 | 100% | 255 |
| snake_abs_exit | 212,560 | +6.28% | 1 | 100% | 260 |
| snake_abs | 209,604 | +4.80% | 1 | 100% | 255 |
| snake_abs_conv | 209,449 | +4.72% | 1 | 100% | 255 |
| intraweek | 209,228 | +4.61% | 25 | 48% | 2,757 |
| benchmark | 208,598 | +4.30% | 0 | - | 237 |
| snake_viper_wild | 206,861 | +3.43% | 3 | 33% | 702 |
| intramonth | 206,236 | +3.12% | 0 | - | 235 |
| snake_viper_tick | 203,257 | +1.63% | 2 | 0% | 532 |
| random_hold | 202,578 | +1.29% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,249 | +0.62% | 3 | 33% | 361 |
| oracle | 201,204 | +0.60% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,841 | -2.08% | 0 | - | 237 |
| gold | 191,344 | -4.33% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,218 (-5.39%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,546 | +4.19% |
| snake_abs_exit_conv | +8,364 | +4.09% |
| snake_abs_conv | +8,308 | +4.13% |
| snake_abs | +8,295 | +4.12% |
| snake_anaconda | +7,424 | +3.83% |
| gold | +6,066 | +3.27% |
| intraweek | +4,143 | +2.02% |
| benchmark_smallcap | +2,903 | +1.50% |
| intramonth | +2,265 | +1.11% |
| random_hold | +2,110 | +1.05% |
| unified | +1,984 | +0.94% |
| benchmark | +1,897 | +0.92% |
| oracle | +1,215 | +0.61% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,910 | -1.89% |
| snake_viper_wild | -4,032 | -1.91% |

Average per day so far: snake_abs_exit_conv Rs +529, snake_abs_exit Rs +523, unified Rs +518, snake_abs_conv Rs +394, snake_abs Rs +384, snake_viper_wild Rs +361, intraweek Rs +342, benchmark Rs +318, intramonth Rs +231, snake_viper_tick Rs +204, random_hold Rs +95, nifty_calls Rs +68, snake_anaconda Rs +57, oracle Rs +45, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -181, gold Rs -321, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.