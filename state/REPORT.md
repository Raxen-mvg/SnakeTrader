# Paper trading report

Updated 2026-11-04 14:25 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,683 | +7.34% | 0 | - | 236 |
| snake_abs_exit_conv | 214,194 | +7.10% | 1 | 100% | 255 |
| snake_abs_exit | 214,066 | +7.03% | 1 | 100% | 260 |
| snake_abs | 211,078 | +5.54% | 1 | 100% | 255 |
| snake_abs_conv | 210,928 | +5.46% | 1 | 100% | 255 |
| intraweek | 209,524 | +4.76% | 25 | 48% | 2,757 |
| benchmark | 208,552 | +4.28% | 0 | - | 237 |
| snake_viper_wild | 207,660 | +3.83% | 3 | 33% | 702 |
| intramonth | 207,056 | +3.53% | 0 | - | 235 |
| snake_viper_tick | 204,037 | +2.02% | 2 | 0% | 532 |
| random_hold | 203,002 | +1.50% | 8 | 62% | 649 |
| snake_anaconda | 202,487 | +1.24% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,206 | +0.60% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,244 | -1.88% | 0 | - | 237 |
| gold | 191,311 | -4.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,754 (-5.12%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +10,052 | +4.93% |
| snake_abs_exit_conv | +9,856 | +4.82% |
| snake_abs_conv | +9,787 | +4.87% |
| snake_abs | +9,769 | +4.85% |
| snake_anaconda | +8,663 | +4.47% |
| gold | +6,033 | +3.26% |
| intraweek | +4,439 | +2.17% |
| benchmark_smallcap | +3,307 | +1.71% |
| intramonth | +3,085 | +1.51% |
| unified | +2,682 | +1.26% |
| random_hold | +2,534 | +1.26% |
| benchmark | +1,851 | +0.90% |
| oracle | +1,217 | +0.61% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,129 | -1.51% |
| snake_viper_wild | -3,233 | -1.53% |

Average per day so far: snake_abs_exit_conv Rs +591, snake_abs_exit Rs +586, unified Rs +544, snake_abs_conv Rs +455, snake_abs Rs +443, snake_viper_wild Rs +403, intraweek Rs +353, benchmark Rs +317, intramonth Rs +261, snake_viper_tick Rs +252, snake_anaconda Rs +113, random_hold Rs +111, nifty_calls Rs +68, oracle Rs +45, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -163, gold Rs -322, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.