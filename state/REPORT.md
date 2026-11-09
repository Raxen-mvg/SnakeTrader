# Paper trading report

Updated 2026-11-09 10:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,192 | +10.10% | 0 | - | 236 |
| benchmark | 217,449 | +8.72% | 0 | - | 237 |
| intraweek | 216,791 | +8.39% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 211,218 | +5.61% | 2 | 50% | 330 |
| snake_abs_exit | 211,189 | +5.59% | 2 | 50% | 308 |
| intramonth | 210,208 | +5.10% | 0 | - | 235 |
| oracle | 209,587 | +4.79% | 0 | - | 233 |
| snake_abs | 209,329 | +4.66% | 1 | 100% | 255 |
| snake_abs_conv | 209,144 | +4.57% | 1 | 100% | 255 |
| random_hold | 204,056 | +2.03% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,755 | -0.62% | 3 | 33% | 374 |
| benchmark_smallcap | 198,531 | -0.73% | 0 | - | 237 |
| snake_viper_wild | 197,931 | -1.03% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,568 | -2.72% | 6 | 50% | 1,154 |
| gold | 193,071 | -3.46% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,643 (-4.68%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +6,428 | +3.06% |
| unified | +4,583 | +2.12% |
| snake_abs_conv | +3,917 | +1.91% |
| snake_abs | +3,909 | +1.90% |
| oracle | +3,760 | +1.83% |
| snake_anaconda | +2,928 | +1.50% |
| snake_abs_exit | +2,877 | +1.38% |
| snake_abs_exit_conv | +2,797 | +1.34% |
| intramonth | +2,605 | +1.25% |
| gold | +2,022 | +1.06% |
| snake_viper_wild | +1,893 | +0.97% |
| snake_viper_tick | +1,858 | +0.96% |
| benchmark_smallcap | +1,738 | +0.88% |
| random_hold | +150 | +0.07% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -38 | -0.02% |

Average per day so far: unified Rs +673, benchmark Rs +582, intraweek Rs +560, snake_abs_exit_conv Rs +415, snake_abs_exit Rs +414, intramonth Rs +340, snake_abs_conv Rs +339, snake_abs Rs +333, oracle Rs +320, random_hold Rs +135, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -50, benchmark_smallcap Rs -57, snake_viper_wild Rs -94, gold Rs -231, snake_viper_tick Rs -286, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.