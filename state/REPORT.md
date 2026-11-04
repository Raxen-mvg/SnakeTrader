# Paper trading report

Updated 2026-11-04 12:16 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,768 | +6.88% | 0 | - | 236 |
| snake_abs_exit_conv | 210,467 | +5.23% | 1 | 100% | 255 |
| snake_abs_exit | 210,317 | +5.16% | 1 | 100% | 260 |
| intraweek | 208,260 | +4.13% | 25 | 48% | 2,757 |
| snake_abs | 207,377 | +3.69% | 1 | 100% | 255 |
| snake_viper_wild | 207,301 | +3.65% | 3 | 33% | 702 |
| snake_abs_conv | 207,218 | +3.61% | 1 | 100% | 255 |
| benchmark | 207,168 | +3.58% | 0 | - | 237 |
| intramonth | 206,177 | +3.09% | 0 | - | 235 |
| snake_viper_tick | 203,693 | +1.85% | 2 | 0% | 532 |
| random_hold | 202,636 | +1.32% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,211 | +0.60% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,924 | -0.54% | 3 | 33% | 361 |
| benchmark_smallcap | 194,563 | -2.72% | 0 | - | 237 |
| gold | 190,703 | -4.65% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,160 (-5.42%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +6,303 | +3.09% |
| snake_abs_exit_conv | +6,128 | +3.00% |
| snake_abs_conv | +6,077 | +3.02% |
| snake_abs | +6,068 | +3.01% |
| gold | +5,425 | +2.93% |
| snake_anaconda | +5,100 | +2.63% |
| intraweek | +3,174 | +1.55% |
| intramonth | +2,206 | +1.08% |
| random_hold | +2,168 | +1.08% |
| unified | +1,767 | +0.83% |
| benchmark_smallcap | +1,625 | +0.84% |
| oracle | +1,222 | +0.61% |
| benchmark | +467 | +0.23% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,474 | -1.68% |
| snake_viper_wild | -3,592 | -1.70% |

Average per day so far: unified Rs +510, snake_abs_exit_conv Rs +436, snake_abs_exit Rs +430, snake_viper_wild Rs +384, intraweek Rs +306, snake_abs_conv Rs +301, snake_abs Rs +295, benchmark Rs +265, snake_viper_tick Rs +231, intramonth Rs +229, random_hold Rs +98, nifty_calls Rs +68, oracle Rs +45, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -49, benchmark_smallcap Rs -236, gold Rs -344, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.