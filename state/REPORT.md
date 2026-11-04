# Paper trading report

Updated 2026-11-04 12:07 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,679 | +6.84% | 0 | - | 236 |
| snake_abs_exit_conv | 209,343 | +4.67% | 1 | 100% | 255 |
| snake_abs_exit | 209,212 | +4.61% | 1 | 100% | 260 |
| intraweek | 208,474 | +4.24% | 25 | 48% | 2,757 |
| benchmark | 207,313 | +3.66% | 0 | - | 237 |
| snake_viper_wild | 206,927 | +3.46% | 3 | 33% | 702 |
| snake_abs | 206,253 | +3.13% | 1 | 100% | 255 |
| snake_abs_conv | 206,101 | +3.05% | 1 | 100% | 255 |
| intramonth | 206,097 | +3.05% | 0 | - | 235 |
| snake_viper_tick | 203,322 | +1.66% | 2 | 0% | 532 |
| random_hold | 202,553 | +1.28% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,045 | +0.52% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,177 | -0.91% | 3 | 33% | 361 |
| benchmark_smallcap | 194,888 | -2.56% | 0 | - | 237 |
| gold | 190,654 | -4.67% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,048 (-5.48%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,376 | +2.90% |
| snake_abs_exit | +5,197 | +2.55% |
| snake_abs_exit_conv | +5,005 | +2.45% |
| snake_abs_conv | +4,960 | +2.47% |
| snake_abs | +4,944 | +2.46% |
| snake_anaconda | +4,352 | +2.25% |
| intraweek | +3,389 | +1.65% |
| intramonth | +2,126 | +1.04% |
| random_hold | +2,085 | +1.04% |
| benchmark_smallcap | +1,951 | +1.01% |
| unified | +1,678 | +0.79% |
| oracle | +1,055 | +0.53% |
| benchmark | +612 | +0.30% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,844 | -1.86% |
| snake_viper_wild | -3,965 | -1.88% |

Average per day so far: unified Rs +507, snake_abs_exit_conv Rs +389, snake_abs_exit Rs +384, snake_viper_wild Rs +365, intraweek Rs +314, benchmark Rs +271, snake_abs_conv Rs +254, snake_abs Rs +250, intramonth Rs +226, snake_viper_tick Rs +208, random_hold Rs +95, nifty_calls Rs +68, oracle Rs +39, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -83, benchmark_smallcap Rs -222, gold Rs -346, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.