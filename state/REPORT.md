# Paper trading report

Updated 2026-11-11 12:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,762 | +10.38% | 0 | - | 237 |
| unified | 220,459 | +10.23% | 0 | - | 236 |
| snake_abs_exit_conv | 217,447 | +8.72% | 2 | 50% | 345 |
| snake_abs_exit | 216,369 | +8.19% | 2 | 50% | 345 |
| snake_abs | 213,764 | +6.88% | 1 | 100% | 255 |
| intraweek | 213,645 | +6.82% | 30 | 53% | 3,302 |
| snake_abs_conv | 213,609 | +6.80% | 1 | 100% | 255 |
| oracle | 211,903 | +5.95% | 0 | - | 233 |
| intramonth | 211,371 | +5.69% | 0 | - | 235 |
| random_hold | 206,949 | +3.48% | 9 | 67% | 709 |
| snake_viper_wild | 204,447 | +2.22% | 10 | 50% | 1,825 |
| snake_anaconda | 204,271 | +2.13% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,300 | +0.65% | 0 | - | 237 |
| snake_viper_tick | 200,962 | +0.48% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,029 | -4.99% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,283 (-4.36%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,017 | +3.55% |
| snake_viper_tick | +6,885 | +3.55% |
| snake_abs_exit_conv | +5,538 | +2.61% |
| snake_anaconda | +4,804 | +2.41% |
| snake_abs_exit | +4,385 | +2.07% |
| snake_abs_conv | +4,131 | +1.97% |
| snake_abs | +4,117 | +1.96% |
| benchmark_smallcap | +3,128 | +1.58% |
| benchmark | +2,670 | +1.22% |
| random_hold | +1,989 | +0.97% |
| oracle | +1,985 | +0.94% |
| intramonth | +762 | +0.36% |
| unified | +712 | +0.32% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -897 | -0.42% |
| gold | -2,104 | -1.09% |

Average per day so far: benchmark Rs +670, unified Rs +660, snake_abs_exit_conv Rs +623, snake_abs_exit Rs +585, snake_abs_conv Rs +486, snake_abs Rs +475, intraweek Rs +440, oracle Rs +384, intramonth Rs +367, random_hold Rs +224, snake_viper_wild Rs +193, snake_anaconda Rs +164, nifty_calls Rs +59, benchmark_smallcap Rs +48, snake_viper_tick Rs +48, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -322, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.