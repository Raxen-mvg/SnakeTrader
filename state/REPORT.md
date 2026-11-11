# Paper trading report

Updated 2026-11-11 12:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,517 | +10.26% | 0 | - | 237 |
| unified | 220,458 | +10.23% | 0 | - | 236 |
| snake_abs_exit_conv | 217,468 | +8.73% | 2 | 50% | 345 |
| snake_abs_exit | 216,399 | +8.20% | 2 | 50% | 345 |
| snake_abs | 213,804 | +6.90% | 1 | 100% | 255 |
| intraweek | 213,703 | +6.85% | 30 | 53% | 3,302 |
| snake_abs_conv | 213,650 | +6.83% | 1 | 100% | 255 |
| oracle | 211,854 | +5.93% | 0 | - | 233 |
| intramonth | 211,399 | +5.70% | 0 | - | 235 |
| random_hold | 206,864 | +3.43% | 9 | 67% | 709 |
| snake_viper_wild | 204,446 | +2.22% | 10 | 50% | 1,825 |
| snake_anaconda | 204,295 | +2.15% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,244 | +0.62% | 0 | - | 237 |
| snake_viper_tick | 200,961 | +0.48% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,980 | -5.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,290 (-4.35%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,016 | +3.55% |
| snake_viper_tick | +6,885 | +3.55% |
| snake_abs_exit_conv | +5,559 | +2.62% |
| snake_anaconda | +4,828 | +2.42% |
| snake_abs_exit | +4,415 | +2.08% |
| snake_abs_conv | +4,172 | +1.99% |
| snake_abs | +4,157 | +1.98% |
| benchmark_smallcap | +3,072 | +1.55% |
| benchmark | +2,425 | +1.11% |
| oracle | +1,936 | +0.92% |
| random_hold | +1,903 | +0.93% |
| intramonth | +790 | +0.38% |
| unified | +711 | +0.32% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -839 | -0.39% |
| gold | -2,154 | -1.12% |

Average per day so far: benchmark Rs +662, unified Rs +660, snake_abs_exit_conv Rs +624, snake_abs_exit Rs +586, snake_abs_conv Rs +487, snake_abs Rs +476, intraweek Rs +442, oracle Rs +382, intramonth Rs +368, random_hold Rs +221, snake_viper_wild Rs +193, snake_anaconda Rs +165, nifty_calls Rs +59, snake_viper_tick Rs +48, benchmark_smallcap Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -323, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.