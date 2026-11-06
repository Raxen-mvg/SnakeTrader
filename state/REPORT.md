# Paper trading report

Updated 2026-11-06 13:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,225 | +8.11% | 0 | - | 237 |
| unified | 214,878 | +7.44% | 0 | - | 236 |
| intraweek | 208,395 | +4.20% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,336 | +4.17% | 1 | 100% | 255 |
| snake_abs_exit | 208,228 | +4.11% | 1 | 100% | 260 |
| intramonth | 207,172 | +3.59% | 0 | - | 235 |
| oracle | 205,371 | +2.69% | 0 | - | 233 |
| snake_abs | 205,333 | +2.67% | 1 | 100% | 255 |
| snake_abs_conv | 205,141 | +2.57% | 1 | 100% | 255 |
| random_hold | 203,424 | +1.71% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,200 | -1.90% | 3 | 33% | 702 |
| snake_anaconda | 195,590 | -2.21% | 3 | 33% | 374 |
| benchmark_smallcap | 195,179 | -2.41% | 0 | - | 237 |
| snake_viper_tick | 192,872 | -3.56% | 2 | 0% | 532 |
| gold | 190,605 | -4.70% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,883 (-6.56%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,456 | +1.15% |
| oracle | +1,299 | +0.64% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -776 | -0.37% |
| random_hold | -899 | -0.44% |
| intraweek | -1,023 | -0.49% |
| unified | -1,105 | -0.51% |
| benchmark_smallcap | -3,509 | -1.77% |
| gold | -3,617 | -1.86% |
| snake_abs | -6,355 | -3.00% |
| snake_abs_conv | -6,404 | -3.03% |
| snake_abs_exit | -6,431 | -3.00% |
| snake_abs_exit_conv | -6,467 | -3.01% |
| snake_anaconda | -6,890 | -3.40% |
| snake_viper_tick | -8,266 | -4.11% |
| snake_viper_wild | -8,456 | -4.13% |

Average per day so far: benchmark Rs +559, unified Rs +513, snake_abs_exit_conv Rs +321, snake_abs_exit Rs +316, intraweek Rs +289, intramonth Rs +247, snake_abs_conv Rs +198, snake_abs Rs +198, oracle Rs +185, random_hold Rs +118, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -181, snake_anaconda Rs -184, benchmark_smallcap Rs -193, gold Rs -324, snake_viper_tick Rs -396, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.