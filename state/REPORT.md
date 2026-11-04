# Paper trading report

Updated 2026-11-04 09:57 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,935 | +6.47% | 0 | - | 236 |
| snake_abs_exit_conv | 208,824 | +4.41% | 1 | 100% | 255 |
| snake_abs_exit | 208,606 | +4.30% | 1 | 100% | 260 |
| benchmark | 208,522 | +4.26% | 0 | - | 237 |
| intraweek | 208,061 | +4.03% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,907 | +3.45% | 3 | 33% | 702 |
| snake_abs | 205,721 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,577 | +2.79% | 1 | 100% | 255 |
| intramonth | 205,571 | +2.79% | 0 | - | 235 |
| snake_viper_tick | 203,300 | +1.65% | 2 | 0% | 532 |
| random_hold | 203,190 | +1.59% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,231 | +0.12% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,624 | -1.19% | 3 | 33% | 361 |
| benchmark_smallcap | 194,282 | -2.86% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,086 | -6.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,763 (-5.62%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,591 | +2.25% |
| snake_abs_exit_conv | +4,485 | +2.19% |
| snake_abs_conv | +4,436 | +2.21% |
| snake_abs | +4,412 | +2.19% |
| snake_anaconda | +3,800 | +1.96% |
| intraweek | +2,976 | +1.45% |
| random_hold | +2,722 | +1.36% |
| benchmark | +1,821 | +0.88% |
| gold | +1,808 | +0.98% |
| intramonth | +1,600 | +0.78% |
| benchmark_smallcap | +1,345 | +0.70% |
| unified | +934 | +0.44% |
| oracle | +242 | +0.12% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,867 | -1.87% |
| snake_viper_wild | -3,986 | -1.89% |

Average per day so far: unified Rs +479, snake_abs_exit_conv Rs +368, snake_viper_wild Rs +364, snake_abs_exit Rs +359, benchmark Rs +316, intraweek Rs +299, snake_abs_conv Rs +232, snake_abs Rs +229, intramonth Rs +206, snake_viper_tick Rs +206, random_hold Rs +118, nifty_calls Rs +68, oracle Rs +9, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -108, benchmark_smallcap Rs -249, snake_nonews Rs -444, snake Rs -467, gold Rs -478

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.