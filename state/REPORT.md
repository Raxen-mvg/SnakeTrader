# Paper trading report

Updated 2026-11-04 09:39 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 211,526 | +5.76% | 0 | - | 236 |
| benchmark | 208,392 | +4.20% | 0 | - | 237 |
| snake_abs_exit_conv | 207,794 | +3.90% | 1 | 100% | 255 |
| snake_abs_exit | 207,560 | +3.78% | 1 | 100% | 260 |
| snake_viper_wild | 207,474 | +3.74% | 3 | 33% | 702 |
| intraweek | 206,383 | +3.19% | 25 | 48% | 2,757 |
| snake_abs | 204,723 | +2.36% | 1 | 100% | 255 |
| intramonth | 204,695 | +2.35% | 0 | - | 235 |
| snake_abs_conv | 204,560 | +2.28% | 1 | 100% | 255 |
| snake_viper_tick | 203,855 | +1.93% | 2 | 0% | 532 |
| random_hold | 202,942 | +1.47% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| oracle | 199,513 | -0.24% | 0 | - | 233 |
| snake_anaconda | 196,613 | -1.69% | 3 | 33% | 361 |
| benchmark_smallcap | 193,565 | -3.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,415 | -6.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,276 (-5.86%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,546 | +1.74% |
| snake_abs_exit_conv | +3,455 | +1.69% |
| snake_abs_conv | +3,419 | +1.70% |
| snake_abs | +3,414 | +1.70% |
| snake_anaconda | +2,789 | +1.44% |
| random_hold | +2,474 | +1.23% |
| gold | +2,137 | +1.15% |
| benchmark | +1,691 | +0.82% |
| intraweek | +1,298 | +0.63% |
| intramonth | +724 | +0.35% |
| benchmark_smallcap | +628 | +0.33% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -475 | -0.22% |
| oracle | -477 | -0.24% |
| snake_viper_tick | -3,312 | -1.60% |
| snake_viper_wild | -3,419 | -1.62% |

Average per day so far: unified Rs +427, snake_viper_wild Rs +393, snake_abs_exit_conv Rs +325, snake_abs_exit Rs +315, benchmark Rs +311, snake_viper_tick Rs +241, intraweek Rs +236, snake_abs_conv Rs +190, snake_abs Rs +189, intramonth Rs +174, random_hold Rs +109, nifty_calls Rs +68, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, oracle Rs -18, snake_anaconda Rs -154, benchmark_smallcap Rs -280, snake_nonews Rs -444, gold Rs -466, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.