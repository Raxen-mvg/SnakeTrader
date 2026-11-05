# Paper trading report

Updated 2026-11-05 12:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,162 | +8.58% | 0 | - | 236 |
| snake_abs_exit_conv | 213,620 | +6.81% | 1 | 100% | 255 |
| snake_abs_exit | 213,320 | +6.66% | 1 | 100% | 260 |
| benchmark | 212,974 | +6.49% | 0 | - | 237 |
| intraweek | 211,420 | +5.71% | 25 | 48% | 2,757 |
| snake_abs | 210,510 | +5.25% | 1 | 100% | 255 |
| snake_abs_conv | 210,371 | +5.18% | 1 | 100% | 255 |
| intramonth | 209,049 | +4.53% | 0 | - | 235 |
| snake_viper_wild | 206,322 | +3.16% | 3 | 33% | 702 |
| random_hold | 205,769 | +2.88% | 8 | 62% | 649 |
| oracle | 203,853 | +1.93% | 0 | - | 233 |
| snake_viper_tick | 202,774 | +1.39% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,690 | +0.84% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,047 | -0.48% | 0 | - | 237 |
| gold | 194,106 | -2.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,855 (-5.07%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,215 | +2.02% |
| unified | +2,722 | +1.27% |
| gold | +2,713 | +1.42% |
| random_hold | +2,460 | +1.21% |
| benchmark_smallcap | +2,377 | +1.21% |
| oracle | +2,061 | +1.02% |
| intramonth | +2,033 | +0.98% |
| intraweek | +1,722 | +0.82% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,387 | -0.66% |
| snake_abs | -1,393 | -0.66% |
| snake_abs_exit_conv | -1,395 | -0.65% |
| snake_abs_exit | -1,580 | -0.73% |
| snake_anaconda | -2,130 | -1.04% |
| snake_viper_tick | -2,626 | -1.28% |
| snake_viper_wild | -2,708 | -1.29% |

Average per day so far: unified Rs +613, snake_abs_exit_conv Rs +545, snake_abs_exit Rs +533, benchmark Rs +463, snake_abs_conv Rs +415, intraweek Rs +408, snake_abs Rs +404, intramonth Rs +323, snake_viper_wild Rs +316, random_hold Rs +206, snake_viper_tick Rs +163, oracle Rs +138, snake_anaconda Rs +73, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -40, gold Rs -210, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.