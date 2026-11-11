# Paper trading report

Updated 2026-11-11 12:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,259 | +10.63% | 0 | - | 237 |
| unified | 220,418 | +10.21% | 0 | - | 236 |
| snake_abs_exit_conv | 216,289 | +8.14% | 2 | 50% | 345 |
| snake_abs_exit | 214,906 | +7.45% | 2 | 50% | 345 |
| intraweek | 214,295 | +7.15% | 30 | 53% | 3,302 |
| snake_abs | 212,724 | +6.36% | 1 | 100% | 255 |
| snake_abs_conv | 212,568 | +6.28% | 1 | 100% | 255 |
| oracle | 211,868 | +5.93% | 0 | - | 233 |
| intramonth | 211,342 | +5.67% | 0 | - | 235 |
| random_hold | 206,849 | +3.42% | 9 | 67% | 709 |
| snake_anaconda | 202,935 | +1.47% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,816 | +0.91% | 0 | - | 237 |
| snake_viper_wild | 201,486 | +0.74% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,062 | -0.97% | 9 | 44% | 1,639 |
| gold | 189,766 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,269 (-4.37%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,380 | +2.07% |
| snake_viper_wild | +4,056 | +2.06% |
| snake_viper_tick | +3,986 | +2.05% |
| benchmark_smallcap | +3,643 | +1.84% |
| snake_anaconda | +3,469 | +1.74% |
| benchmark | +3,167 | +1.45% |
| snake_abs_conv | +3,091 | +1.48% |
| snake_abs | +3,078 | +1.47% |
| snake_abs_exit | +2,922 | +1.38% |
| oracle | +1,950 | +0.93% |
| random_hold | +1,889 | +0.92% |
| intramonth | +733 | +0.35% |
| unified | +671 | +0.30% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -247 | -0.12% |
| gold | -2,367 | -1.23% |

Average per day so far: benchmark Rs +686, unified Rs +659, snake_abs_exit_conv Rs +582, snake_abs_exit Rs +532, intraweek Rs +461, snake_abs_conv Rs +449, snake_abs Rs +439, oracle Rs +383, intramonth Rs +366, random_hold Rs +221, snake_anaconda Rs +113, benchmark_smallcap Rs +67, snake_viper_wild Rs +65, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -97, gold Rs -330, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.