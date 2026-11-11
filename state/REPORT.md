# Paper trading report

Updated 2026-11-11 14:42 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,348 | +10.17% | 0 | - | 236 |
| benchmark | 220,012 | +10.01% | 0 | - | 237 |
| snake_abs_exit_conv | 217,560 | +8.78% | 2 | 50% | 345 |
| snake_abs_exit | 216,677 | +8.34% | 2 | 50% | 345 |
| snake_abs | 214,610 | +7.30% | 1 | 100% | 255 |
| snake_abs_conv | 214,444 | +7.22% | 1 | 100% | 255 |
| intraweek | 213,472 | +6.74% | 30 | 53% | 3,302 |
| oracle | 211,868 | +5.93% | 0 | - | 233 |
| intramonth | 211,211 | +5.61% | 0 | - | 235 |
| random_hold | 207,177 | +3.59% | 9 | 67% | 709 |
| snake_viper_wild | 206,532 | +3.27% | 10 | 50% | 1,825 |
| snake_anaconda | 204,427 | +2.21% | 3 | 33% | 374 |
| snake_viper_tick | 203,002 | +1.50% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,454 | -5.27% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,274 (-4.36%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,102 | +4.61% |
| snake_viper_tick | +8,926 | +4.60% |
| snake_abs_exit_conv | +5,651 | +2.67% |
| snake_abs_conv | +4,966 | +2.37% |
| snake_abs | +4,964 | +2.37% |
| snake_anaconda | +4,961 | +2.49% |
| snake_abs_exit | +4,693 | +2.21% |
| benchmark_smallcap | +3,285 | +1.66% |
| random_hold | +2,216 | +1.08% |
| oracle | +1,949 | +0.93% |
| benchmark | +1,920 | +0.88% |
| intramonth | +602 | +0.29% |
| unified | +601 | +0.27% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,070 | -0.50% |
| gold | -2,680 | -1.40% |

Average per day so far: unified Rs +656, benchmark Rs +646, snake_abs_exit_conv Rs +627, snake_abs_exit Rs +596, snake_abs_conv Rs +516, snake_abs Rs +504, intraweek Rs +435, oracle Rs +383, intramonth Rs +362, snake_viper_wild Rs +284, random_hold Rs +232, snake_anaconda Rs +170, snake_viper_tick Rs +150, nifty_calls Rs +59, benchmark_smallcap Rs +54, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -340, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.