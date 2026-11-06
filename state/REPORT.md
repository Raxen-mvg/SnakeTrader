# Paper trading report

Updated 2026-11-06 09:24 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,697 | +7.35% | 0 | - | 236 |
| benchmark | 213,456 | +6.73% | 0 | - | 237 |
| snake_abs_exit_conv | 211,043 | +5.52% | 1 | 100% | 255 |
| snake_abs_exit | 210,756 | +5.38% | 1 | 100% | 260 |
| intraweek | 208,911 | +4.46% | 25 | 48% | 2,757 |
| snake_abs | 207,950 | +3.98% | 1 | 100% | 255 |
| snake_abs_conv | 207,805 | +3.90% | 1 | 100% | 255 |
| intramonth | 206,409 | +3.20% | 0 | - | 235 |
| oracle | 203,671 | +1.83% | 0 | - | 233 |
| random_hold | 203,461 | +1.73% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,273 | -0.86% | 3 | 33% | 374 |
| snake_viper_wild | 198,084 | -0.96% | 3 | 33% | 702 |
| benchmark_smallcap | 194,921 | -2.54% | 0 | - | 237 |
| snake_viper_tick | 194,726 | -2.64% | 2 | 0% | 532 |
| gold | 190,457 | -4.77% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,456 (-6.27%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -314 | -0.15% |
| oracle | -401 | -0.20% |
| intraweek | -508 | -0.24% |
| random_hold | -862 | -0.42% |
| unified | -1,287 | -0.60% |
| intramonth | -1,540 | -0.74% |
| snake_abs | -3,739 | -1.77% |
| snake_abs_conv | -3,740 | -1.77% |
| snake_abs_exit_conv | -3,760 | -1.75% |
| gold | -3,765 | -1.94% |
| benchmark_smallcap | -3,767 | -1.90% |
| snake_abs_exit | -3,903 | -1.82% |
| snake_anaconda | -4,207 | -2.08% |
| snake_viper_tick | -6,412 | -3.19% |
| snake_viper_wild | -6,572 | -3.21% |

Average per day so far: unified Rs +507, benchmark Rs +464, snake_abs_exit_conv Rs +425, snake_abs_exit Rs +414, intraweek Rs +307, snake_abs_conv Rs +300, snake_abs Rs +294, intramonth Rs +221, oracle Rs +127, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -72, snake_viper_wild Rs -91, benchmark_smallcap Rs -203, snake_viper_tick Rs -293, gold Rs -329, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.