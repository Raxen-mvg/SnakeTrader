# Paper trading report

Updated 2026-11-04 12:49 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,828 | +6.91% | 0 | - | 236 |
| snake_abs_exit_conv | 212,533 | +6.27% | 1 | 100% | 255 |
| snake_abs_exit | 212,394 | +6.20% | 1 | 100% | 260 |
| intraweek | 209,440 | +4.72% | 25 | 48% | 2,757 |
| snake_abs | 209,430 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,278 | +4.64% | 1 | 100% | 255 |
| benchmark | 207,925 | +3.96% | 0 | - | 237 |
| snake_viper_wild | 206,990 | +3.50% | 3 | 33% | 702 |
| intramonth | 206,198 | +3.10% | 0 | - | 235 |
| snake_viper_tick | 203,383 | +1.69% | 2 | 0% | 532 |
| random_hold | 202,907 | +1.45% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,121 | +0.56% | 0 | - | 233 |
| snake_anaconda | 200,940 | +0.47% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,033 | -2.48% | 0 | - | 237 |
| gold | 190,654 | -4.67% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,250 (-5.37%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,379 | +4.11% |
| snake_abs_exit_conv | +8,195 | +4.01% |
| snake_abs_conv | +8,137 | +4.04% |
| snake_abs | +8,121 | +4.03% |
| snake_anaconda | +7,115 | +3.67% |
| gold | +5,376 | +2.90% |
| intraweek | +4,355 | +2.12% |
| random_hold | +2,439 | +1.22% |
| intramonth | +2,227 | +1.09% |
| benchmark_smallcap | +2,096 | +1.09% |
| unified | +1,827 | +0.86% |
| benchmark | +1,224 | +0.59% |
| oracle | +1,132 | +0.57% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,784 | -1.83% |
| snake_viper_wild | -3,903 | -1.85% |

Average per day so far: snake_abs_exit_conv Rs +522, snake_abs_exit Rs +516, unified Rs +512, snake_abs_conv Rs +387, snake_abs Rs +377, snake_viper_wild Rs +368, intraweek Rs +350, benchmark Rs +294, intramonth Rs +230, snake_viper_tick Rs +211, random_hold Rs +108, nifty_calls Rs +68, snake_anaconda Rs +43, oracle Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -216, gold Rs -346, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.