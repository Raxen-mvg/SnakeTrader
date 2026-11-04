# Paper trading report

Updated 2026-11-04 11:30 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,596 | +6.30% | 0 | - | 236 |
| snake_abs_exit_conv | 208,813 | +4.41% | 1 | 100% | 255 |
| snake_abs_exit | 208,666 | +4.33% | 1 | 100% | 260 |
| intraweek | 208,574 | +4.29% | 25 | 48% | 2,757 |
| benchmark | 207,665 | +3.83% | 0 | - | 237 |
| snake_viper_wild | 206,688 | +3.34% | 3 | 33% | 702 |
| snake_abs | 205,720 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,568 | +2.78% | 1 | 100% | 255 |
| intramonth | 205,444 | +2.72% | 0 | - | 235 |
| snake_viper_tick | 203,088 | +1.54% | 2 | 0% | 532 |
| random_hold | 202,241 | +1.12% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,566 | +0.28% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,542 | -1.23% | 3 | 33% | 361 |
| benchmark_smallcap | 194,787 | -2.61% | 0 | - | 237 |
| gold | 189,750 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,666 (-5.67%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,652 | +2.28% |
| snake_abs_exit_conv | +4,474 | +2.19% |
| gold | +4,472 | +2.41% |
| snake_abs_conv | +4,427 | +2.20% |
| snake_abs | +4,411 | +2.19% |
| snake_anaconda | +3,717 | +1.92% |
| intraweek | +3,489 | +1.70% |
| benchmark_smallcap | +1,850 | +0.96% |
| random_hold | +1,773 | +0.88% |
| intramonth | +1,473 | +0.72% |
| benchmark | +964 | +0.47% |
| unified | +595 | +0.28% |
| oracle | +577 | +0.29% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,079 | -1.97% |
| snake_viper_wild | -4,205 | -1.99% |

Average per day so far: unified Rs +467, snake_abs_exit_conv Rs +367, snake_abs_exit Rs +361, snake_viper_wild Rs +352, intraweek Rs +318, benchmark Rs +284, snake_abs_conv Rs +232, snake_abs Rs +229, intramonth Rs +202, snake_viper_tick Rs +193, random_hold Rs +83, nifty_calls Rs +68, oracle Rs +21, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -112, benchmark_smallcap Rs -227, gold Rs -380, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.