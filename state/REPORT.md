# Paper trading report

Updated 2026-11-25 10:31 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,339 | +12.67% | 0 | - | 236 |
| benchmark | 225,030 | +12.52% | 0 | - | 237 |
| intramonth | 212,912 | +6.46% | 0 | - | 235 |
| oracle | 212,446 | +6.22% | 0 | - | 233 |
| random_hold | 209,224 | +4.61% | 12 | 75% | 1,009 |
| intraweek | 207,546 | +3.77% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,773 | +0.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,219 | +0.61% | 2 | 50% | 345 |
| snake_abs | 200,957 | +0.48% | 1 | 100% | 255 |
| snake_abs_conv | 200,767 | +0.38% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,125 | -0.44% | 0 | - | 237 |
| snake_viper_wild | 195,522 | -2.24% | 16 | 50% | 2,827 |
| snake_anaconda | 193,305 | -3.35% | 3 | 33% | 374 |
| snake_viper_tick | 192,198 | -3.90% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,501 | -17.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,211 (-5.39%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,557 | +1.61% |
| unified | +1,054 | +0.47% |
| random_hold | +798 | +0.38% |
| intramonth | +160 | +0.07% |
| benchmark_smallcap | +146 | +0.07% |
| oracle | +104 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,929 | -2.32% |
| intraweek | -4,073 | -1.93% |
| snake_abs | -4,503 | -2.19% |
| snake_abs_conv | -4,536 | -2.21% |
| snake_anaconda | -5,399 | -2.72% |
| snake_viper_tick | -5,494 | -2.78% |
| snake_viper_wild | -5,602 | -2.79% |
| snake_abs_exit | -5,722 | -2.76% |
| snake_abs_exit_conv | -5,827 | -2.81% |

Average per day so far: unified Rs +633, benchmark Rs +626, intramonth Rs +323, oracle Rs +311, random_hold Rs +231, intraweek Rs +189, snake_abs_exit Rs +48, nifty_calls Rs +46, snake_abs_exit_conv Rs +33, snake_abs Rs +25, snake_abs_conv Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -24, snake_viper_wild Rs -140, snake_anaconda Rs -191, snake_viper_tick Rs -269, snake_nonews Rs -292, snake Rs -311, gold Rs -862

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.