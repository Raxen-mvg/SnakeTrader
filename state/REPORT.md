# Paper trading report

Updated 2026-11-11 09:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,838 | +10.42% | 0 | - | 237 |
| unified | 219,471 | +9.73% | 0 | - | 236 |
| snake_abs_exit_conv | 216,359 | +8.18% | 2 | 50% | 330 |
| snake_abs_exit | 215,530 | +7.76% | 2 | 50% | 308 |
| snake_abs | 214,224 | +7.11% | 1 | 100% | 255 |
| snake_abs_conv | 214,059 | +7.03% | 1 | 100% | 255 |
| intraweek | 213,419 | +6.71% | 30 | 53% | 3,302 |
| oracle | 210,286 | +5.14% | 0 | - | 233 |
| intramonth | 210,268 | +5.13% | 0 | - | 235 |
| random_hold | 205,481 | +2.74% | 9 | 67% | 709 |
| snake_anaconda | 203,262 | +1.63% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,885 | +0.44% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,137 | -0.43% | 7 | 57% | 1,332 |
| snake_viper_tick | 195,756 | -2.12% | 6 | 50% | 1,154 |
| gold | 189,520 | -5.24% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,559 (-4.72%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,582 | +2.19% |
| snake_abs | +4,577 | +2.18% |
| snake_abs_exit_conv | +4,450 | +2.10% |
| snake_anaconda | +3,796 | +1.90% |
| snake_abs_exit | +3,546 | +1.67% |
| benchmark | +2,746 | +1.26% |
| benchmark_smallcap | +2,713 | +1.37% |
| snake_viper_wild | +1,707 | +0.86% |
| snake_viper_tick | +1,680 | +0.86% |
| random_hold | +521 | +0.25% |
| oracle | +367 | +0.17% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| unified | -276 | -0.13% |
| intramonth | -341 | -0.16% |
| intraweek | -1,123 | -0.52% |
| gold | -2,614 | -1.36% |

Average per day so far: benchmark Rs +672, unified Rs +628, snake_abs_exit_conv Rs +584, snake_abs_exit Rs +555, snake_abs_conv Rs +502, snake_abs Rs +490, intraweek Rs +433, oracle Rs +332, intramonth Rs +331, random_hold Rs +177, snake_anaconda Rs +125, nifty_calls Rs +59, benchmark_smallcap Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -38, snake_viper_tick Rs -212, gold Rs -338, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.