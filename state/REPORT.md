# Paper trading report

Updated 2026-11-06 13:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,629 | +7.81% | 0 | - | 237 |
| unified | 214,588 | +7.29% | 0 | - | 236 |
| intraweek | 209,005 | +4.50% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,605 | +4.30% | 1 | 100% | 255 |
| snake_abs_exit | 208,516 | +4.26% | 1 | 100% | 260 |
| intramonth | 206,890 | +3.44% | 0 | - | 235 |
| snake_abs | 205,590 | +2.79% | 1 | 100% | 255 |
| snake_abs_conv | 205,407 | +2.70% | 1 | 100% | 255 |
| oracle | 205,134 | +2.57% | 0 | - | 233 |
| random_hold | 203,267 | +1.63% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,660 | -1.67% | 3 | 33% | 702 |
| snake_anaconda | 196,020 | -1.99% | 3 | 33% | 374 |
| benchmark_smallcap | 194,899 | -2.55% | 0 | - | 237 |
| snake_viper_tick | 193,327 | -3.34% | 2 | 0% | 532 |
| gold | 190,177 | -4.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,940 (-6.53%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,859 | +0.87% |
| oracle | +1,062 | +0.52% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -413 | -0.20% |
| random_hold | -1,056 | -0.52% |
| intramonth | -1,059 | -0.51% |
| unified | -1,396 | -0.65% |
| benchmark_smallcap | -3,789 | -1.91% |
| gold | -4,044 | -2.08% |
| snake_abs | -6,099 | -2.88% |
| snake_abs_conv | -6,138 | -2.90% |
| snake_abs_exit | -6,143 | -2.86% |
| snake_abs_exit_conv | -6,198 | -2.88% |
| snake_anaconda | -6,459 | -3.19% |
| snake_viper_tick | -7,811 | -3.88% |
| snake_viper_wild | -7,996 | -3.91% |

Average per day so far: benchmark Rs +539, unified Rs +503, snake_abs_exit_conv Rs +331, snake_abs_exit Rs +328, intraweek Rs +311, intramonth Rs +238, snake_abs_conv Rs +208, snake_abs Rs +207, oracle Rs +177, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -159, snake_anaconda Rs -166, benchmark_smallcap Rs -204, gold Rs -339, snake_viper_tick Rs -371, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.