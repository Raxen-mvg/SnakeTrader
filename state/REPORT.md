# Paper trading report

Updated 2026-11-17 15:28 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| unified | 221,209 | +10.61% | 0 | - | 236 |
| snake_abs_exit | 213,277 | +6.64% | 2 | 50% | 345 |
| intraweek | 213,264 | +6.63% | 35 | 54% | 3,851 |
| oracle | 212,575 | +6.29% | 0 | - | 233 |
| snake_abs_exit_conv | 211,704 | +5.85% | 2 | 50% | 345 |
| intramonth | 211,476 | +5.74% | 0 | - | 235 |
| snake_viper_wild | 208,889 | +4.45% | 14 | 50% | 2,496 |
| snake_abs | 208,541 | +4.27% | 1 | 100% | 255 |
| snake_abs_conv | 208,405 | +4.20% | 1 | 100% | 255 |
| random_hold | 208,254 | +4.13% | 10 | 70% | 733 |
| snake_viper_tick | 205,319 | +2.66% | 13 | 46% | 2,299 |
| snake_anaconda | 204,250 | +2.12% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,235 | +0.12% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,823 | -9.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,092 (-4.45%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +2,745 | +1.33% |
| snake_viper_tick | +2,699 | +1.33% |
| intraweek | +1,998 | +0.95% |
| benchmark | +1,446 | +0.66% |
| oracle | +552 | +0.26% |
| random_hold | +460 | +0.22% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold | -132 | -0.07% |
| intramonth | -143 | -0.07% |
| unified | -228 | -0.10% |
| benchmark_smallcap | -594 | -0.30% |
| snake_anaconda | -853 | -0.42% |
| snake_abs_exit | -1,132 | -0.53% |
| snake_abs_exit_conv | -1,513 | -0.71% |
| snake_abs_conv | -1,585 | -0.76% |
| snake_abs | -1,592 | -0.76% |

Average per day so far: benchmark Rs +615, unified Rs +606, snake_abs_exit Rs +415, intraweek Rs +379, snake_abs_exit_conv Rs +366, oracle Rs +359, snake_viper_wild Rs +329, intramonth Rs +328, snake_abs_conv Rs +263, snake_abs Rs +259, random_hold Rs +236, snake_viper_tick Rs +222, snake_anaconda Rs +142, nifty_calls Rs +52, benchmark_smallcap Rs +8, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -548

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.