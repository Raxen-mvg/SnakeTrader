# Paper trading report

Updated 2026-11-04 12:40 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,857 | +6.93% | 0 | - | 236 |
| snake_abs_exit_conv | 212,316 | +6.16% | 1 | 100% | 255 |
| snake_abs_exit | 212,171 | +6.08% | 1 | 100% | 260 |
| intraweek | 209,344 | +4.67% | 25 | 48% | 2,757 |
| snake_abs | 209,217 | +4.61% | 1 | 100% | 255 |
| snake_abs_conv | 209,061 | +4.53% | 1 | 100% | 255 |
| benchmark | 207,810 | +3.90% | 0 | - | 237 |
| snake_viper_wild | 207,078 | +3.54% | 3 | 33% | 702 |
| intramonth | 206,185 | +3.09% | 0 | - | 235 |
| snake_viper_tick | 203,469 | +1.74% | 2 | 0% | 532 |
| random_hold | 202,820 | +1.41% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,104 | +0.55% | 0 | - | 233 |
| snake_anaconda | 200,717 | +0.36% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 194,921 | -2.54% | 0 | - | 237 |
| gold | 190,473 | -4.76% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,267 (-5.37%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,156 | +4.00% |
| snake_abs_exit_conv | +7,977 | +3.90% |
| snake_abs_conv | +7,920 | +3.94% |
| snake_abs | +7,907 | +3.93% |
| snake_anaconda | +6,892 | +3.56% |
| gold | +5,195 | +2.80% |
| intraweek | +4,259 | +2.08% |
| random_hold | +2,352 | +1.17% |
| intramonth | +2,214 | +1.09% |
| benchmark_smallcap | +1,984 | +1.03% |
| unified | +1,856 | +0.88% |
| oracle | +1,115 | +0.56% |
| benchmark | +1,109 | +0.54% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,697 | -1.78% |
| snake_viper_wild | -3,814 | -1.81% |

Average per day so far: unified Rs +513, snake_abs_exit_conv Rs +513, snake_abs_exit Rs +507, snake_abs_conv Rs +378, snake_viper_wild Rs +373, snake_abs Rs +369, intraweek Rs +346, benchmark Rs +289, intramonth Rs +229, snake_viper_tick Rs +217, random_hold Rs +104, nifty_calls Rs +68, oracle Rs +41, snake_anaconda Rs +33, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -221, gold Rs -353, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.