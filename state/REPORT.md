# Paper trading report

Updated 2026-11-04 10:40 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,633 | +6.32% | 0 | - | 236 |
| snake_abs_exit_conv | 208,760 | +4.38% | 1 | 100% | 255 |
| snake_abs_exit | 208,592 | +4.30% | 1 | 100% | 260 |
| intraweek | 207,857 | +3.93% | 25 | 48% | 2,757 |
| benchmark | 207,826 | +3.91% | 0 | - | 237 |
| snake_viper_wild | 206,880 | +3.44% | 3 | 33% | 702 |
| snake_abs | 205,669 | +2.83% | 1 | 100% | 255 |
| snake_abs_conv | 205,516 | +2.76% | 1 | 100% | 255 |
| intramonth | 205,149 | +2.57% | 0 | - | 235 |
| snake_viper_tick | 203,270 | +1.64% | 2 | 0% | 532 |
| random_hold | 202,258 | +1.13% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,083 | +0.04% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,499 | -1.25% | 3 | 33% | 361 |
| benchmark_smallcap | 194,350 | -2.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,432 | -6.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,597 (-5.70%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,577 | +2.24% |
| snake_abs_exit_conv | +4,422 | +2.16% |
| snake_abs_conv | +4,375 | +2.17% |
| snake_abs | +4,359 | +2.17% |
| snake_anaconda | +3,674 | +1.90% |
| intraweek | +2,771 | +1.35% |
| gold | +2,154 | +1.16% |
| random_hold | +1,790 | +0.89% |
| benchmark_smallcap | +1,412 | +0.73% |
| intramonth | +1,178 | +0.58% |
| benchmark | +1,125 | +0.54% |
| unified | +632 | +0.30% |
| oracle | +94 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,897 | -1.88% |
| snake_viper_wild | -4,013 | -1.90% |

Average per day so far: unified Rs +468, snake_abs_exit_conv Rs +365, snake_viper_wild Rs +362, snake_abs_exit Rs +358, intraweek Rs +291, benchmark Rs +290, snake_abs_conv Rs +230, snake_abs Rs +227, snake_viper_tick Rs +204, intramonth Rs +191, random_hold Rs +84, nifty_calls Rs +68, oracle Rs +3, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -114, benchmark_smallcap Rs -246, snake_nonews Rs -444, gold Rs -465, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.