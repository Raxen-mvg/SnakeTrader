# Paper trading report

Updated 2026-11-09 10:57 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,488 | +10.24% | 0 | - | 236 |
| benchmark | 217,097 | +8.55% | 0 | - | 237 |
| intraweek | 216,117 | +8.06% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,093 | +6.05% | 2 | 50% | 330 |
| snake_abs_exit | 212,075 | +6.04% | 2 | 50% | 308 |
| intramonth | 210,751 | +5.38% | 0 | - | 235 |
| oracle | 209,975 | +4.99% | 0 | - | 233 |
| snake_abs | 209,874 | +4.94% | 1 | 100% | 255 |
| snake_abs_conv | 209,704 | +4.85% | 1 | 100% | 255 |
| random_hold | 204,315 | +2.16% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,595 | -0.20% | 3 | 33% | 374 |
| benchmark_smallcap | 198,598 | -0.70% | 0 | - | 237 |
| snake_viper_wild | 197,430 | -1.28% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,075 | -2.96% | 6 | 50% | 1,154 |
| gold | 193,021 | -3.49% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,801 (-4.60%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,754 | +2.73% |
| unified | +4,879 | +2.26% |
| snake_abs_conv | +4,477 | +2.18% |
| snake_abs | +4,455 | +2.17% |
| oracle | +4,148 | +2.02% |
| snake_anaconda | +3,768 | +1.92% |
| snake_abs_exit | +3,763 | +1.81% |
| snake_abs_exit_conv | +3,672 | +1.76% |
| intramonth | +3,148 | +1.52% |
| gold | +1,973 | +1.03% |
| benchmark_smallcap | +1,805 | +0.92% |
| snake_viper_wild | +1,392 | +0.71% |
| snake_viper_tick | +1,365 | +0.71% |
| random_hold | +408 | +0.20% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -390 | -0.18% |

Average per day so far: unified Rs +683, benchmark Rs +570, intraweek Rs +537, snake_abs_exit_conv Rs +448, snake_abs_exit Rs +447, snake_abs_conv Rs +359, intramonth Rs +358, snake_abs Rs +353, oracle Rs +333, random_hold Rs +144, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -16, benchmark_smallcap Rs -54, snake_viper_wild Rs -117, gold Rs -233, snake_viper_tick Rs -312, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.