# Paper trading report

Updated 2026-11-11 11:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,144 | +10.57% | 0 | - | 237 |
| unified | 220,212 | +10.11% | 0 | - | 236 |
| snake_abs_exit_conv | 216,366 | +8.18% | 2 | 50% | 345 |
| snake_abs_exit | 215,093 | +7.55% | 2 | 50% | 345 |
| intraweek | 213,988 | +6.99% | 30 | 53% | 3,302 |
| snake_abs | 213,288 | +6.64% | 1 | 100% | 255 |
| snake_abs_conv | 213,130 | +6.57% | 1 | 100% | 255 |
| oracle | 211,830 | +5.92% | 0 | - | 233 |
| intramonth | 211,084 | +5.54% | 0 | - | 235 |
| random_hold | 206,868 | +3.43% | 9 | 67% | 709 |
| snake_anaconda | 203,083 | +1.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,771 | +0.89% | 0 | - | 237 |
| snake_viper_wild | 201,496 | +0.75% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,071 | -0.96% | 9 | 44% | 1,639 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,167 (-4.42%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,457 | +2.10% |
| snake_viper_wild | +4,065 | +2.06% |
| snake_viper_tick | +3,994 | +2.06% |
| snake_abs_conv | +3,652 | +1.74% |
| snake_abs | +3,641 | +1.74% |
| snake_anaconda | +3,616 | +1.81% |
| benchmark_smallcap | +3,598 | +1.82% |
| snake_abs_exit | +3,110 | +1.47% |
| benchmark | +3,052 | +1.40% |
| oracle | +1,912 | +0.91% |
| random_hold | +1,908 | +0.93% |
| intramonth | +475 | +0.23% |
| unified | +465 | +0.21% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -554 | -0.26% |
| gold | -2,236 | -1.16% |

Average per day so far: benchmark Rs +682, unified Rs +652, snake_abs_exit_conv Rs +585, snake_abs_exit Rs +539, snake_abs_conv Rs +469, snake_abs Rs +458, intraweek Rs +451, oracle Rs +382, intramonth Rs +358, random_hold Rs +222, snake_anaconda Rs +119, benchmark_smallcap Rs +66, snake_viper_wild Rs +65, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -96, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.