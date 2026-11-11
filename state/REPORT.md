# Paper trading report

Updated 2026-11-11 11:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,351 | +10.68% | 0 | - | 237 |
| unified | 220,706 | +10.35% | 0 | - | 236 |
| snake_abs_exit_conv | 216,681 | +8.34% | 2 | 50% | 345 |
| snake_abs_exit | 215,362 | +7.68% | 2 | 50% | 345 |
| intraweek | 214,431 | +7.21% | 30 | 53% | 3,302 |
| snake_abs | 213,030 | +6.51% | 1 | 100% | 255 |
| snake_abs_conv | 212,878 | +6.44% | 1 | 100% | 255 |
| oracle | 212,223 | +6.11% | 0 | - | 233 |
| intramonth | 211,811 | +5.91% | 0 | - | 235 |
| random_hold | 206,955 | +3.48% | 9 | 67% | 709 |
| snake_anaconda | 203,270 | +1.64% | 3 | 33% | 374 |
| snake_viper_wild | 202,032 | +1.02% | 10 | 50% | 1,825 |
| benchmark_smallcap | 201,883 | +0.94% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,597 | -0.70% | 9 | 44% | 1,639 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,511 (-4.24%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,772 | +2.25% |
| snake_viper_wild | +4,602 | +2.33% |
| snake_viper_tick | +4,520 | +2.33% |
| snake_anaconda | +3,804 | +1.91% |
| benchmark_smallcap | +3,711 | +1.87% |
| snake_abs_conv | +3,401 | +1.62% |
| snake_abs | +3,383 | +1.61% |
| snake_abs_exit | +3,378 | +1.59% |
| benchmark | +3,259 | +1.49% |
| oracle | +2,304 | +1.10% |
| random_hold | +1,994 | +0.97% |
| intramonth | +1,202 | +0.57% |
| unified | +959 | +0.44% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -111 | -0.05% |
| gold | -2,203 | -1.15% |

Average per day so far: benchmark Rs +689, unified Rs +668, snake_abs_exit_conv Rs +596, snake_abs_exit Rs +549, intraweek Rs +466, snake_abs_conv Rs +460, snake_abs Rs +449, oracle Rs +394, intramonth Rs +381, random_hold Rs +224, snake_anaconda Rs +126, snake_viper_wild Rs +88, benchmark_smallcap Rs +70, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -70, gold Rs -325, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.