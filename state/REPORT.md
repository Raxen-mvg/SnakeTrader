# Paper trading report

Updated 2026-11-04 11:01 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,495 | +6.25% | 0 | - | 236 |
| snake_abs_exit_conv | 208,765 | +4.38% | 1 | 100% | 255 |
| snake_abs_exit | 208,634 | +4.32% | 1 | 100% | 260 |
| intraweek | 207,529 | +3.76% | 25 | 48% | 2,757 |
| benchmark | 207,390 | +3.69% | 0 | - | 237 |
| snake_viper_wild | 206,786 | +3.39% | 3 | 33% | 702 |
| snake_abs | 205,668 | +2.83% | 1 | 100% | 255 |
| snake_abs_conv | 205,518 | +2.76% | 1 | 100% | 255 |
| intramonth | 205,155 | +2.58% | 0 | - | 235 |
| snake_viper_tick | 203,184 | +1.59% | 2 | 0% | 532 |
| random_hold | 202,123 | +1.06% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,572 | +0.29% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,500 | -1.25% | 3 | 33% | 361 |
| benchmark_smallcap | 194,462 | -2.77% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| gold | 188,254 | -5.87% | 0 | - | 237 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,492 (-5.75%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,620 | +2.26% |
| snake_abs_exit_conv | +4,426 | +2.17% |
| snake_abs_conv | +4,377 | +2.18% |
| snake_abs | +4,359 | +2.17% |
| snake_anaconda | +3,676 | +1.90% |
| gold | +2,976 | +1.61% |
| intraweek | +2,444 | +1.19% |
| random_hold | +1,655 | +0.83% |
| benchmark_smallcap | +1,525 | +0.79% |
| intramonth | +1,184 | +0.58% |
| benchmark | +688 | +0.33% |
| oracle | +583 | +0.29% |
| unified | +494 | +0.23% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,983 | -1.92% |
| snake_viper_wild | -4,107 | -1.95% |

Average per day so far: unified Rs +463, snake_abs_exit_conv Rs +365, snake_abs_exit Rs +360, snake_viper_wild Rs +357, intraweek Rs +279, benchmark Rs +274, snake_abs_conv Rs +230, snake_abs Rs +227, snake_viper_tick Rs +199, intramonth Rs +191, random_hold Rs +79, nifty_calls Rs +68, oracle Rs +21, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -114, benchmark_smallcap Rs -241, gold Rs -435, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.