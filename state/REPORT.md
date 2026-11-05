# Paper trading report

Updated 2026-11-05 10:11 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,998 | +9.50% | 0 | - | 236 |
| snake_abs_exit_conv | 215,564 | +7.78% | 1 | 100% | 255 |
| snake_abs_exit | 215,298 | +7.65% | 1 | 100% | 260 |
| snake_abs | 212,441 | +6.22% | 1 | 100% | 255 |
| benchmark | 212,423 | +6.21% | 0 | - | 237 |
| snake_abs_conv | 212,288 | +6.14% | 1 | 100% | 255 |
| intraweek | 211,076 | +5.54% | 25 | 48% | 2,757 |
| intramonth | 210,799 | +5.40% | 0 | - | 235 |
| random_hold | 206,916 | +3.46% | 8 | 62% | 649 |
| snake_viper_wild | 205,743 | +2.87% | 3 | 33% | 702 |
| oracle | 204,582 | +2.29% | 0 | - | 233 |
| snake_anaconda | 202,584 | +1.29% | 3 | 33% | 374 |
| snake_viper_tick | 202,220 | +1.11% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,540 | -0.23% | 0 | - | 237 |
| gold | 195,191 | -2.40% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,637 (-4.68%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,559 | +2.13% |
| gold | +3,798 | +1.98% |
| intramonth | +3,783 | +1.83% |
| benchmark | +3,664 | +1.75% |
| random_hold | +3,608 | +1.77% |
| benchmark_smallcap | +2,870 | +1.46% |
| oracle | +2,789 | +1.38% |
| intraweek | +1,379 | +0.66% |
| snake_abs_exit_conv | +549 | +0.26% |
| snake_abs | +538 | +0.25% |
| snake_abs_conv | +530 | +0.25% |
| snake_abs_exit | +398 | +0.18% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -1,236 | -0.61% |
| snake_viper_tick | -3,181 | -1.55% |
| snake_viper_wild | -3,287 | -1.57% |

Average per day so far: unified Rs +679, snake_abs_exit_conv Rs +623, snake_abs_exit Rs +612, snake_abs_conv Rs +492, snake_abs Rs +478, benchmark Rs +444, intraweek Rs +396, intramonth Rs +386, snake_viper_wild Rs +287, random_hold Rs +247, oracle Rs +164, snake_viper_tick Rs +131, snake_anaconda Rs +112, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -19, gold Rs -172, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.