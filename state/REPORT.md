# Paper trading report

Updated 2026-11-04 09:46 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 211,203 | +5.60% | 0 | - | 236 |
| benchmark | 208,499 | +4.25% | 0 | - | 237 |
| snake_abs_exit_conv | 207,990 | +4.00% | 1 | 100% | 255 |
| snake_abs_exit | 207,756 | +3.88% | 1 | 100% | 260 |
| snake_viper_wild | 207,566 | +3.78% | 3 | 33% | 702 |
| intraweek | 207,361 | +3.68% | 25 | 48% | 2,757 |
| snake_abs | 204,918 | +2.46% | 1 | 100% | 255 |
| intramonth | 204,780 | +2.39% | 0 | - | 235 |
| snake_abs_conv | 204,755 | +2.38% | 1 | 100% | 255 |
| snake_viper_tick | 203,945 | +1.97% | 2 | 0% | 532 |
| random_hold | 203,070 | +1.53% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| oracle | 199,962 | -0.02% | 0 | - | 233 |
| snake_anaconda | 196,783 | -1.61% | 3 | 33% | 361 |
| benchmark_smallcap | 193,879 | -3.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,415 | -6.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,378 (-5.81%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,742 | +1.83% |
| snake_abs_exit_conv | +3,651 | +1.79% |
| snake_abs_conv | +3,614 | +1.80% |
| snake_abs | +3,608 | +1.79% |
| snake_anaconda | +2,958 | +1.53% |
| random_hold | +2,602 | +1.30% |
| intraweek | +2,275 | +1.11% |
| gold | +2,137 | +1.15% |
| benchmark | +1,798 | +0.87% |
| benchmark_smallcap | +942 | +0.49% |
| intramonth | +809 | +0.40% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -27 | -0.01% |
| unified | -798 | -0.38% |
| snake_viper_tick | -3,222 | -1.55% |
| snake_viper_wild | -3,327 | -1.58% |

Average per day so far: unified Rs +415, snake_viper_wild Rs +398, snake_abs_exit_conv Rs +333, snake_abs_exit Rs +323, benchmark Rs +315, intraweek Rs +273, snake_viper_tick Rs +247, snake_abs_conv Rs +198, snake_abs Rs +197, intramonth Rs +177, random_hold Rs +114, nifty_calls Rs +68, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, oracle Rs -1, snake_anaconda Rs -146, benchmark_smallcap Rs -266, snake_nonews Rs -444, gold Rs -466, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.