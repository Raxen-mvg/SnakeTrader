# Paper trading report

Updated 2026-11-04 11:19 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,344 | +6.17% | 0 | - | 236 |
| snake_abs_exit_conv | 208,835 | +4.42% | 1 | 100% | 255 |
| snake_abs_exit | 208,686 | +4.34% | 1 | 100% | 260 |
| intraweek | 207,948 | +3.97% | 25 | 48% | 2,757 |
| benchmark | 207,833 | +3.92% | 0 | - | 237 |
| snake_viper_wild | 206,821 | +3.41% | 3 | 33% | 702 |
| snake_abs | 205,745 | +2.87% | 1 | 100% | 255 |
| snake_abs_conv | 205,591 | +2.80% | 1 | 100% | 255 |
| intramonth | 205,522 | +2.76% | 0 | - | 235 |
| snake_viper_tick | 203,217 | +1.61% | 2 | 0% | 532 |
| random_hold | 202,006 | +1.00% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,465 | +0.23% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,524 | -1.24% | 3 | 33% | 361 |
| benchmark_smallcap | 194,607 | -2.70% | 0 | - | 237 |
| gold | 189,470 | -5.26% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,568 (-5.72%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,671 | +2.29% |
| snake_abs_exit_conv | +4,497 | +2.20% |
| snake_abs_conv | +4,450 | +2.21% |
| snake_abs | +4,436 | +2.20% |
| gold | +4,192 | +2.26% |
| snake_anaconda | +3,699 | +1.91% |
| intraweek | +2,863 | +1.40% |
| benchmark_smallcap | +1,670 | +0.87% |
| intramonth | +1,551 | +0.76% |
| random_hold | +1,537 | +0.77% |
| benchmark | +1,132 | +0.55% |
| oracle | +475 | +0.24% |
| unified | +343 | +0.16% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,950 | -1.91% |
| snake_viper_wild | -4,072 | -1.93% |

Average per day so far: unified Rs +457, snake_abs_exit_conv Rs +368, snake_abs_exit Rs +362, snake_viper_wild Rs +359, intraweek Rs +294, benchmark Rs +290, snake_abs_conv Rs +233, snake_abs Rs +230, intramonth Rs +205, snake_viper_tick Rs +201, random_hold Rs +74, nifty_calls Rs +68, oracle Rs +17, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -113, benchmark_smallcap Rs -234, gold Rs -390, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.