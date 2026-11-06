# Paper trading report

Updated 2026-11-06 12:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,208 | +7.60% | 0 | - | 237 |
| unified | 214,537 | +7.27% | 0 | - | 236 |
| intraweek | 209,288 | +4.64% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,231 | +4.62% | 1 | 100% | 255 |
| snake_abs_exit | 209,054 | +4.53% | 1 | 100% | 260 |
| intramonth | 206,788 | +3.39% | 0 | - | 235 |
| snake_abs | 206,198 | +3.10% | 1 | 100% | 255 |
| snake_abs_conv | 206,026 | +3.01% | 1 | 100% | 255 |
| oracle | 205,024 | +2.51% | 0 | - | 233 |
| random_hold | 203,243 | +1.62% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,662 | -1.67% | 3 | 33% | 374 |
| snake_viper_wild | 195,966 | -2.02% | 3 | 33% | 702 |
| benchmark_smallcap | 194,776 | -2.61% | 0 | - | 237 |
| snake_viper_tick | 192,650 | -3.67% | 2 | 0% | 532 |
| gold | 190,194 | -4.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,077 (-6.46%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,438 | +0.67% |
| oracle | +952 | +0.47% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -131 | -0.06% |
| random_hold | -1,080 | -0.53% |
| intramonth | -1,160 | -0.56% |
| unified | -1,447 | -0.67% |
| benchmark_smallcap | -3,912 | -1.97% |
| gold | -4,028 | -2.07% |
| snake_abs | -5,490 | -2.59% |
| snake_abs_conv | -5,519 | -2.61% |
| snake_abs_exit_conv | -5,572 | -2.59% |
| snake_abs_exit | -5,605 | -2.61% |
| snake_anaconda | -5,818 | -2.87% |
| snake_viper_tick | -8,488 | -4.22% |
| snake_viper_wild | -8,690 | -4.25% |

Average per day so far: benchmark Rs +524, unified Rs +501, snake_abs_exit_conv Rs +355, snake_abs_exit Rs +348, intraweek Rs +320, intramonth Rs +234, snake_abs_conv Rs +232, snake_abs Rs +230, oracle Rs +173, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -139, snake_viper_wild Rs -192, benchmark_smallcap Rs -209, gold Rs -338, snake_viper_tick Rs -408, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.