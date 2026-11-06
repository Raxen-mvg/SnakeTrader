# Paper trading report

Updated 2026-11-06 13:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,629 | +7.81% | 0 | - | 237 |
| unified | 214,706 | +7.35% | 0 | - | 236 |
| intraweek | 209,219 | +4.61% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,541 | +4.27% | 1 | 100% | 255 |
| snake_abs_exit | 208,452 | +4.23% | 1 | 100% | 260 |
| intramonth | 207,092 | +3.55% | 0 | - | 235 |
| snake_abs | 205,530 | +2.77% | 1 | 100% | 255 |
| snake_abs_conv | 205,345 | +2.67% | 1 | 100% | 255 |
| oracle | 205,235 | +2.62% | 0 | - | 233 |
| random_hold | 203,367 | +1.68% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,800 | -1.60% | 3 | 33% | 702 |
| snake_anaconda | 195,978 | -2.01% | 3 | 33% | 374 |
| benchmark_smallcap | 194,977 | -2.51% | 0 | - | 237 |
| snake_viper_tick | 193,467 | -3.27% | 2 | 0% | 532 |
| gold | 190,062 | -4.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,013 (-6.49%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,859 | +0.87% |
| oracle | +1,163 | +0.57% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -199 | -0.10% |
| intramonth | -856 | -0.41% |
| random_hold | -956 | -0.47% |
| unified | -1,277 | -0.59% |
| benchmark_smallcap | -3,711 | -1.87% |
| gold | -4,159 | -2.14% |
| snake_abs | -6,159 | -2.91% |
| snake_abs_conv | -6,200 | -2.93% |
| snake_abs_exit | -6,207 | -2.89% |
| snake_abs_exit_conv | -6,262 | -2.92% |
| snake_anaconda | -6,501 | -3.21% |
| snake_viper_tick | -7,671 | -3.81% |
| snake_viper_wild | -7,856 | -3.84% |

Average per day so far: benchmark Rs +539, unified Rs +507, snake_abs_exit_conv Rs +329, snake_abs_exit Rs +325, intraweek Rs +318, intramonth Rs +245, snake_abs_conv Rs +206, snake_abs Rs +205, oracle Rs +181, random_hold Rs +116, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -152, snake_anaconda Rs -168, benchmark_smallcap Rs -201, gold Rs -343, snake_viper_tick Rs -363, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.