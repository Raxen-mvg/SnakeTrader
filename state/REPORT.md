# Paper trading report

Updated 2026-11-05 12:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,542 | +8.77% | 0 | - | 236 |
| snake_abs_exit_conv | 213,496 | +6.75% | 1 | 100% | 255 |
| snake_abs_exit | 213,192 | +6.60% | 1 | 100% | 260 |
| benchmark | 212,928 | +6.46% | 0 | - | 237 |
| intraweek | 210,958 | +5.48% | 25 | 48% | 2,757 |
| snake_abs | 210,388 | +5.19% | 1 | 100% | 255 |
| snake_abs_conv | 210,248 | +5.12% | 1 | 100% | 255 |
| intramonth | 209,427 | +4.71% | 0 | - | 235 |
| snake_viper_wild | 206,377 | +3.19% | 3 | 33% | 702 |
| random_hold | 206,104 | +3.05% | 8 | 62% | 649 |
| oracle | 204,111 | +2.06% | 0 | - | 233 |
| snake_viper_tick | 202,829 | +1.42% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,583 | +0.79% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,047 | -0.48% | 0 | - | 237 |
| gold | 194,106 | -2.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,820 (-5.09%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,169 | +2.00% |
| unified | +3,103 | +1.45% |
| random_hold | +2,795 | +1.38% |
| gold | +2,713 | +1.42% |
| intramonth | +2,411 | +1.17% |
| benchmark_smallcap | +2,377 | +1.21% |
| oracle | +2,318 | +1.15% |
| intraweek | +1,260 | +0.60% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,511 | -0.71% |
| snake_abs | -1,516 | -0.71% |
| snake_abs_exit_conv | -1,519 | -0.71% |
| snake_abs_exit | -1,708 | -0.80% |
| snake_anaconda | -2,237 | -1.10% |
| snake_viper_tick | -2,571 | -1.25% |
| snake_viper_wild | -2,653 | -1.27% |

Average per day so far: unified Rs +627, snake_abs_exit_conv Rs +540, snake_abs_exit Rs +528, benchmark Rs +462, snake_abs_conv Rs +410, snake_abs Rs +400, intraweek Rs +391, intramonth Rs +337, snake_viper_wild Rs +319, random_hold Rs +218, snake_viper_tick Rs +166, oracle Rs +147, snake_anaconda Rs +69, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -40, gold Rs -210, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.