# Paper trading report

Updated 2026-11-09 10:21 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,364 | +10.18% | 0 | - | 236 |
| benchmark | 217,595 | +8.80% | 0 | - | 237 |
| intraweek | 216,651 | +8.32% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 211,208 | +5.60% | 2 | 50% | 330 |
| snake_abs_exit | 211,146 | +5.57% | 2 | 50% | 308 |
| intramonth | 210,376 | +5.19% | 0 | - | 235 |
| oracle | 209,636 | +4.82% | 0 | - | 233 |
| snake_abs | 209,125 | +4.56% | 1 | 100% | 255 |
| snake_abs_conv | 208,943 | +4.47% | 1 | 100% | 255 |
| random_hold | 204,233 | +2.12% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,708 | -0.65% | 3 | 33% | 374 |
| benchmark_smallcap | 198,542 | -0.73% | 0 | - | 237 |
| snake_viper_wild | 198,064 | -0.97% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,699 | -2.65% | 6 | 50% | 1,154 |
| gold | 193,071 | -3.46% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,671 (-4.66%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +6,288 | +2.99% |
| unified | +4,754 | +2.21% |
| oracle | +3,809 | +1.85% |
| snake_abs_conv | +3,716 | +1.81% |
| snake_abs | +3,706 | +1.80% |
| snake_anaconda | +2,881 | +1.47% |
| snake_abs_exit | +2,834 | +1.36% |
| snake_abs_exit_conv | +2,787 | +1.34% |
| intramonth | +2,773 | +1.34% |
| snake_viper_wild | +2,027 | +1.03% |
| gold | +2,022 | +1.06% |
| snake_viper_tick | +1,989 | +1.03% |
| benchmark_smallcap | +1,749 | +0.89% |
| random_hold | +326 | +0.16% |
| benchmark | +107 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +679, benchmark Rs +586, intraweek Rs +555, snake_abs_exit_conv Rs +415, snake_abs_exit Rs +413, intramonth Rs +346, snake_abs_conv Rs +331, snake_abs Rs +326, oracle Rs +321, random_hold Rs +141, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -52, benchmark_smallcap Rs -56, snake_viper_wild Rs -88, gold Rs -231, snake_viper_tick Rs -279, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.