# Paper trading report

Updated 2026-11-04 14:28 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,673 | +7.34% | 0 | - | 236 |
| snake_abs_exit_conv | 214,078 | +7.04% | 1 | 100% | 255 |
| snake_abs_exit | 213,946 | +6.97% | 1 | 100% | 260 |
| snake_abs | 210,965 | +5.48% | 1 | 100% | 255 |
| snake_abs_conv | 210,814 | +5.41% | 1 | 100% | 255 |
| intraweek | 209,559 | +4.78% | 25 | 48% | 2,757 |
| benchmark | 208,537 | +4.27% | 0 | - | 237 |
| snake_viper_wild | 207,722 | +3.86% | 3 | 33% | 702 |
| intramonth | 207,082 | +3.54% | 0 | - | 235 |
| snake_viper_tick | 204,099 | +2.05% | 2 | 0% | 532 |
| random_hold | 203,080 | +1.54% | 8 | 62% | 649 |
| snake_anaconda | 202,378 | +1.19% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,240 | +0.62% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,278 | -1.86% | 0 | - | 237 |
| gold | 191,262 | -4.37% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,779 (-5.11%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,932 | +4.87% |
| snake_abs_exit_conv | +9,740 | +4.77% |
| snake_abs_conv | +9,673 | +4.81% |
| snake_abs | +9,656 | +4.80% |
| snake_anaconda | +8,554 | +4.41% |
| gold | +5,984 | +3.23% |
| intraweek | +4,474 | +2.18% |
| benchmark_smallcap | +3,341 | +1.73% |
| intramonth | +3,111 | +1.52% |
| unified | +2,672 | +1.26% |
| random_hold | +2,611 | +1.30% |
| benchmark | +1,836 | +0.89% |
| oracle | +1,251 | +0.63% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,068 | -1.48% |
| snake_viper_wild | -3,171 | -1.50% |

Average per day so far: snake_abs_exit_conv Rs +587, snake_abs_exit Rs +581, unified Rs +543, snake_abs_conv Rs +451, snake_abs Rs +439, snake_viper_wild Rs +406, intraweek Rs +354, benchmark Rs +316, intramonth Rs +262, snake_viper_tick Rs +256, random_hold Rs +114, snake_anaconda Rs +108, nifty_calls Rs +68, oracle Rs +46, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -162, gold Rs -324, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.