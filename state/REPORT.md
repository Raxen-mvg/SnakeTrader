# Paper trading report

Updated 2026-11-04 13:04 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,982 | +6.99% | 0 | - | 236 |
| snake_abs_exit_conv | 212,529 | +6.26% | 1 | 100% | 255 |
| snake_abs_exit | 212,373 | +6.19% | 1 | 100% | 260 |
| snake_abs | 209,432 | +4.72% | 1 | 100% | 255 |
| intraweek | 209,312 | +4.66% | 25 | 48% | 2,757 |
| snake_abs_conv | 209,276 | +4.64% | 1 | 100% | 255 |
| benchmark | 207,841 | +3.92% | 0 | - | 237 |
| snake_viper_wild | 207,105 | +3.55% | 3 | 33% | 702 |
| intramonth | 206,314 | +3.16% | 0 | - | 235 |
| snake_viper_tick | 203,497 | +1.75% | 2 | 0% | 532 |
| random_hold | 202,798 | +1.40% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,183 | +0.59% | 0 | - | 233 |
| snake_anaconda | 201,041 | +0.52% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,067 | -2.47% | 0 | - | 237 |
| gold | 190,753 | -4.62% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,314 (-5.34%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,359 | +4.10% |
| snake_abs_exit_conv | +8,191 | +4.01% |
| snake_abs_conv | +8,135 | +4.04% |
| snake_abs | +8,123 | +4.04% |
| snake_anaconda | +7,217 | +3.72% |
| gold | +5,475 | +2.96% |
| intraweek | +4,226 | +2.06% |
| intramonth | +2,343 | +1.15% |
| random_hold | +2,329 | +1.16% |
| benchmark_smallcap | +2,130 | +1.10% |
| unified | +1,981 | +0.93% |
| oracle | +1,194 | +0.60% |
| benchmark | +1,140 | +0.55% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,669 | -1.77% |
| snake_viper_wild | -3,787 | -1.80% |

Average per day so far: snake_abs_exit_conv Rs +522, unified Rs +518, snake_abs_exit Rs +516, snake_abs_conv Rs +387, snake_abs Rs +377, snake_viper_wild Rs +374, intraweek Rs +345, benchmark Rs +290, intramonth Rs +234, snake_viper_tick Rs +219, random_hold Rs +104, nifty_calls Rs +68, snake_anaconda Rs +47, oracle Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -214, gold Rs -342, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.