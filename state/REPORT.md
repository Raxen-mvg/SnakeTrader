# Paper trading report

Updated 2026-11-11 13:41 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,259 | +10.13% | 0 | - | 236 |
| benchmark | 219,890 | +9.95% | 0 | - | 237 |
| snake_abs_exit_conv | 217,748 | +8.87% | 2 | 50% | 345 |
| snake_abs_exit | 216,680 | +8.34% | 2 | 50% | 345 |
| snake_abs | 214,359 | +7.18% | 1 | 100% | 255 |
| snake_abs_conv | 214,203 | +7.10% | 1 | 100% | 255 |
| intraweek | 213,411 | +6.71% | 30 | 53% | 3,302 |
| oracle | 211,721 | +5.86% | 0 | - | 233 |
| intramonth | 211,237 | +5.62% | 0 | - | 235 |
| random_hold | 206,934 | +3.47% | 9 | 67% | 709 |
| snake_viper_wild | 204,918 | +2.46% | 10 | 50% | 1,825 |
| snake_anaconda | 204,614 | +2.31% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,423 | +0.71% | 9 | 44% | 1,639 |
| benchmark_smallcap | 200,997 | +0.50% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,717 | -5.14% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,204 (-4.40%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,488 | +3.79% |
| snake_viper_tick | +7,346 | +3.79% |
| snake_abs_exit_conv | +5,839 | +2.75% |
| snake_anaconda | +5,147 | +2.58% |
| snake_abs_conv | +4,726 | +2.26% |
| snake_abs | +4,712 | +2.25% |
| snake_abs_exit | +4,696 | +2.21% |
| benchmark_smallcap | +2,825 | +1.43% |
| random_hold | +1,974 | +0.96% |
| oracle | +1,802 | +0.86% |
| benchmark | +1,798 | +0.82% |
| intramonth | +627 | +0.30% |
| unified | +513 | +0.23% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,131 | -0.53% |
| gold | -2,417 | -1.26% |

Average per day so far: unified Rs +654, benchmark Rs +642, snake_abs_exit_conv Rs +634, snake_abs_exit Rs +596, snake_abs_conv Rs +507, snake_abs Rs +495, intraweek Rs +433, oracle Rs +378, intramonth Rs +362, random_hold Rs +224, snake_viper_wild Rs +214, snake_anaconda Rs +177, snake_viper_tick Rs +71, nifty_calls Rs +59, benchmark_smallcap Rs +37, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -332, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.