# Paper trading report

Updated 2026-11-11 09:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,762 | +10.38% | 0 | - | 237 |
| unified | 219,569 | +9.79% | 0 | - | 236 |
| snake_abs_exit_conv | 217,100 | +8.55% | 2 | 50% | 330 |
| snake_abs_exit | 215,816 | +7.91% | 2 | 50% | 308 |
| snake_abs | 214,230 | +7.12% | 1 | 100% | 255 |
| snake_abs_conv | 214,075 | +7.04% | 1 | 100% | 255 |
| intraweek | 213,440 | +6.72% | 30 | 53% | 3,302 |
| oracle | 210,704 | +5.35% | 0 | - | 233 |
| intramonth | 210,467 | +5.23% | 0 | - | 235 |
| random_hold | 205,730 | +2.87% | 9 | 67% | 709 |
| snake_anaconda | 203,822 | +1.91% | 3 | 33% | 374 |
| snake_viper_wild | 201,883 | +0.94% | 7 | 57% | 1,332 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,941 | +0.47% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,453 | -0.77% | 6 | 50% | 1,154 |
| gold | 189,372 | -5.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,709 (-4.65%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,191 | +2.45% |
| snake_abs_conv | +4,597 | +2.19% |
| snake_abs | +4,583 | +2.19% |
| snake_viper_wild | +4,453 | +2.25% |
| snake_viper_tick | +4,376 | +2.25% |
| snake_anaconda | +4,355 | +2.18% |
| snake_abs_exit | +3,832 | +1.81% |
| benchmark_smallcap | +2,769 | +1.40% |
| benchmark | +2,670 | +1.22% |
| oracle | +786 | +0.37% |
| random_hold | +770 | +0.38% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intramonth | -143 | -0.07% |
| unified | -178 | -0.08% |
| intraweek | -1,102 | -0.51% |
| gold | -2,762 | -1.44% |

Average per day so far: benchmark Rs +670, unified Rs +631, snake_abs_exit_conv Rs +611, snake_abs_exit Rs +565, snake_abs_conv Rs +503, snake_abs Rs +491, intraweek Rs +434, oracle Rs +345, intramonth Rs +338, random_hold Rs +185, snake_anaconda Rs +147, snake_viper_wild Rs +82, nifty_calls Rs +59, benchmark_smallcap Rs +35, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -77, gold Rs -343, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.