# Paper trading report

Updated 2026-11-05 12:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,322 | +8.66% | 0 | - | 236 |
| snake_abs_exit_conv | 213,619 | +6.81% | 1 | 100% | 255 |
| snake_abs_exit | 213,321 | +6.66% | 1 | 100% | 260 |
| benchmark | 212,943 | +6.47% | 0 | - | 237 |
| intraweek | 210,810 | +5.41% | 25 | 48% | 2,757 |
| snake_abs | 210,509 | +5.25% | 1 | 100% | 255 |
| snake_abs_conv | 210,370 | +5.18% | 1 | 100% | 255 |
| intramonth | 209,143 | +4.57% | 0 | - | 235 |
| snake_viper_wild | 206,411 | +3.21% | 3 | 33% | 702 |
| random_hold | 205,840 | +2.92% | 8 | 62% | 649 |
| oracle | 203,973 | +1.99% | 0 | - | 233 |
| snake_viper_tick | 202,862 | +1.43% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,747 | +0.87% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,991 | -0.51% | 0 | - | 237 |
| gold | 194,221 | -2.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,793 (-5.10%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,185 | +2.00% |
| unified | +2,883 | +1.34% |
| gold | +2,828 | +1.48% |
| random_hold | +2,531 | +1.25% |
| benchmark_smallcap | +2,320 | +1.18% |
| oracle | +2,181 | +1.08% |
| intramonth | +2,127 | +1.03% |
| intraweek | +1,112 | +0.53% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,388 | -0.66% |
| snake_abs | -1,394 | -0.66% |
| snake_abs_exit_conv | -1,396 | -0.65% |
| snake_abs_exit | -1,579 | -0.73% |
| snake_anaconda | -2,074 | -1.02% |
| snake_viper_tick | -2,539 | -1.24% |
| snake_viper_wild | -2,619 | -1.25% |

Average per day so far: unified Rs +619, snake_abs_exit_conv Rs +545, snake_abs_exit Rs +533, benchmark Rs +462, snake_abs_conv Rs +415, snake_abs Rs +404, intraweek Rs +386, intramonth Rs +327, snake_viper_wild Rs +321, random_hold Rs +209, snake_viper_tick Rs +168, oracle Rs +142, snake_anaconda Rs +76, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -42, gold Rs -206, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.