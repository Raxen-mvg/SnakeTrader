# Paper trading report

Updated 2026-11-11 13:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,455 | +10.23% | 0 | - | 236 |
| benchmark | 220,402 | +10.20% | 0 | - | 237 |
| snake_abs_exit_conv | 217,892 | +8.95% | 2 | 50% | 345 |
| snake_abs_exit | 216,830 | +8.41% | 2 | 50% | 345 |
| snake_abs | 214,507 | +7.25% | 1 | 100% | 255 |
| snake_abs_conv | 214,347 | +7.17% | 1 | 100% | 255 |
| intraweek | 213,490 | +6.75% | 30 | 53% | 3,302 |
| oracle | 211,822 | +5.91% | 0 | - | 233 |
| intramonth | 211,453 | +5.73% | 0 | - | 235 |
| random_hold | 207,137 | +3.57% | 9 | 67% | 709 |
| snake_viper_wild | 205,299 | +2.65% | 10 | 50% | 1,825 |
| snake_anaconda | 204,797 | +2.40% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,796 | +0.90% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,233 | +0.62% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,783 | -5.11% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,330 (-4.33%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,869 | +3.99% |
| snake_viper_tick | +7,719 | +3.98% |
| snake_abs_exit_conv | +5,983 | +2.82% |
| snake_anaconda | +5,330 | +2.67% |
| snake_abs_conv | +4,870 | +2.33% |
| snake_abs | +4,860 | +2.32% |
| snake_abs_exit | +4,846 | +2.29% |
| benchmark_smallcap | +3,060 | +1.54% |
| benchmark | +2,310 | +1.06% |
| random_hold | +2,176 | +1.06% |
| oracle | +1,903 | +0.91% |
| intramonth | +844 | +0.40% |
| unified | +708 | +0.32% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,052 | -0.49% |
| gold | -2,351 | -1.22% |

Average per day so far: unified Rs +660, benchmark Rs +658, snake_abs_exit_conv Rs +639, snake_abs_exit Rs +601, snake_abs_conv Rs +512, snake_abs Rs +500, intraweek Rs +435, oracle Rs +381, intramonth Rs +369, snake_viper_wild Rs +230, random_hold Rs +230, snake_anaconda Rs +184, snake_viper_tick Rs +90, nifty_calls Rs +59, benchmark_smallcap Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -330, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.