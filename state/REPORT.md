# Paper trading report

Updated 2026-11-11 14:57 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,371 | +10.19% | 0 | - | 236 |
| benchmark | 219,614 | +9.81% | 0 | - | 237 |
| snake_abs_exit_conv | 216,234 | +8.12% | 2 | 50% | 345 |
| snake_abs_exit | 215,399 | +7.70% | 2 | 50% | 345 |
| intraweek | 213,455 | +6.73% | 30 | 53% | 3,302 |
| snake_abs | 213,100 | +6.55% | 1 | 100% | 255 |
| snake_abs_conv | 212,927 | +6.46% | 1 | 100% | 255 |
| oracle | 211,848 | +5.92% | 0 | - | 233 |
| intramonth | 211,316 | +5.66% | 0 | - | 235 |
| random_hold | 207,188 | +3.59% | 9 | 67% | 709 |
| snake_viper_wild | 206,020 | +3.01% | 10 | 50% | 1,825 |
| snake_anaconda | 203,189 | +1.59% | 3 | 33% | 374 |
| snake_viper_tick | 202,502 | +1.25% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,233 | +0.62% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,470 | -5.26% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,141 (-4.43%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,590 | +4.35% |
| snake_viper_tick | +8,425 | +4.34% |
| snake_abs_exit_conv | +4,326 | +2.04% |
| snake_anaconda | +3,722 | +1.87% |
| snake_abs | +3,454 | +1.65% |
| snake_abs_conv | +3,450 | +1.65% |
| snake_abs_exit | +3,415 | +1.61% |
| benchmark_smallcap | +3,060 | +1.54% |
| random_hold | +2,228 | +1.09% |
| oracle | +1,929 | +0.92% |
| benchmark | +1,522 | +0.70% |
| intramonth | +707 | +0.34% |
| unified | +624 | +0.28% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,087 | -0.51% |
| gold | -2,663 | -1.39% |

Average per day so far: unified Rs +657, benchmark Rs +633, snake_abs_exit_conv Rs +580, snake_abs_exit Rs +550, snake_abs_conv Rs +462, snake_abs Rs +452, intraweek Rs +434, oracle Rs +382, intramonth Rs +365, snake_viper_wild Rs +262, random_hold Rs +232, snake_viper_tick Rs +125, snake_anaconda Rs +123, nifty_calls Rs +59, benchmark_smallcap Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -340, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.