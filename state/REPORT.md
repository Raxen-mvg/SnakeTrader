# Paper trading report

Updated 2026-11-04 09:49 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 211,753 | +5.88% | 0 | - | 236 |
| benchmark | 208,606 | +4.30% | 0 | - | 237 |
| snake_abs_exit_conv | 208,265 | +4.13% | 1 | 100% | 255 |
| snake_abs_exit | 208,038 | +4.02% | 1 | 100% | 260 |
| intraweek | 207,844 | +3.92% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,854 | +3.43% | 3 | 33% | 702 |
| snake_abs | 205,183 | +2.59% | 1 | 100% | 255 |
| snake_abs_conv | 205,026 | +2.51% | 1 | 100% | 255 |
| intramonth | 204,988 | +2.49% | 0 | - | 235 |
| snake_viper_tick | 203,247 | +1.62% | 2 | 0% | 532 |
| random_hold | 203,081 | +1.54% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,019 | +0.01% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,068 | -1.47% | 3 | 33% | 361 |
| benchmark_smallcap | 194,058 | -2.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,382 | -6.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,382 (-5.81%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,024 | +1.97% |
| snake_abs_exit_conv | +3,927 | +1.92% |
| snake_abs_conv | +3,885 | +1.93% |
| snake_abs | +3,874 | +1.92% |
| snake_anaconda | +3,243 | +1.67% |
| intraweek | +2,759 | +1.34% |
| random_hold | +2,613 | +1.30% |
| gold | +2,104 | +1.14% |
| benchmark | +1,905 | +0.92% |
| benchmark_smallcap | +1,121 | +0.58% |
| intramonth | +1,017 | +0.50% |
| oracle | +29 | +0.01% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -248 | -0.12% |
| snake_viper_tick | -3,920 | -1.89% |
| snake_viper_wild | -4,039 | -1.92% |

Average per day so far: unified Rs +435, snake_viper_wild Rs +361, snake_abs_exit_conv Rs +344, snake_abs_exit Rs +335, benchmark Rs +319, intraweek Rs +291, snake_abs_conv Rs +209, snake_abs Rs +207, snake_viper_tick Rs +203, intramonth Rs +185, random_hold Rs +114, nifty_calls Rs +68, oracle Rs +1, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -133, benchmark_smallcap Rs -258, snake_nonews Rs -444, snake Rs -467, gold Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.