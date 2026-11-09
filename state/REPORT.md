# Paper trading report

Updated 2026-11-09 10:17 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,436 | +10.22% | 0 | - | 236 |
| benchmark | 217,350 | +8.68% | 0 | - | 237 |
| intraweek | 216,166 | +8.08% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 211,224 | +5.61% | 2 | 50% | 330 |
| snake_abs_exit | 211,189 | +5.59% | 2 | 50% | 308 |
| intramonth | 210,470 | +5.24% | 0 | - | 235 |
| oracle | 209,535 | +4.77% | 0 | - | 233 |
| snake_abs | 209,068 | +4.53% | 1 | 100% | 255 |
| snake_abs_conv | 208,884 | +4.44% | 1 | 100% | 255 |
| random_hold | 204,171 | +2.08% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,755 | -0.62% | 3 | 33% | 374 |
| benchmark_smallcap | 198,430 | -0.79% | 0 | - | 237 |
| snake_viper_wild | 197,964 | -1.02% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,601 | -2.70% | 6 | 50% | 1,154 |
| gold | 193,120 | -3.44% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,583 (-4.71%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,804 | +2.76% |
| unified | +4,826 | +2.24% |
| oracle | +3,708 | +1.80% |
| snake_abs_conv | +3,657 | +1.78% |
| snake_abs | +3,648 | +1.78% |
| snake_anaconda | +2,928 | +1.50% |
| snake_abs_exit | +2,877 | +1.38% |
| intramonth | +2,867 | +1.38% |
| snake_abs_exit_conv | +2,803 | +1.34% |
| gold | +2,071 | +1.08% |
| snake_viper_wild | +1,927 | +0.98% |
| snake_viper_tick | +1,891 | +0.98% |
| benchmark_smallcap | +1,637 | +0.83% |
| random_hold | +264 | +0.13% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -138 | -0.06% |

Average per day so far: unified Rs +681, benchmark Rs +578, intraweek Rs +539, snake_abs_exit_conv Rs +416, snake_abs_exit Rs +414, intramonth Rs +349, snake_abs_conv Rs +329, snake_abs Rs +324, oracle Rs +318, random_hold Rs +139, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -50, benchmark_smallcap Rs -60, snake_viper_wild Rs -93, gold Rs -229, snake_viper_tick Rs -284, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.