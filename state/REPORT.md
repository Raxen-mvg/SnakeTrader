# Paper trading report

Updated 2026-11-06 12:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,307 | +7.65% | 0 | - | 237 |
| unified | 214,673 | +7.34% | 0 | - | 236 |
| intraweek | 209,697 | +4.85% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,898 | +4.45% | 1 | 100% | 255 |
| snake_abs_exit | 208,706 | +4.35% | 1 | 100% | 260 |
| intramonth | 206,950 | +3.48% | 0 | - | 235 |
| snake_abs | 205,865 | +2.93% | 1 | 100% | 255 |
| snake_abs_conv | 205,691 | +2.85% | 1 | 100% | 255 |
| oracle | 204,971 | +2.49% | 0 | - | 233 |
| random_hold | 203,194 | +1.60% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,195 | -1.90% | 3 | 33% | 374 |
| snake_viper_wild | 195,667 | -2.17% | 3 | 33% | 702 |
| benchmark_smallcap | 194,944 | -2.53% | 0 | - | 237 |
| snake_viper_tick | 192,357 | -3.82% | 2 | 0% | 532 |
| gold | 190,342 | -4.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,054 (-6.47%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,538 | +0.72% |
| oracle | +899 | +0.44% |
| intraweek | +279 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -999 | -0.48% |
| random_hold | -1,129 | -0.55% |
| unified | -1,310 | -0.61% |
| benchmark_smallcap | -3,744 | -1.88% |
| gold | -3,880 | -2.00% |
| snake_abs | -5,823 | -2.75% |
| snake_abs_conv | -5,854 | -2.77% |
| snake_abs_exit_conv | -5,906 | -2.75% |
| snake_abs_exit | -5,953 | -2.77% |
| snake_anaconda | -6,284 | -3.10% |
| snake_viper_tick | -8,781 | -4.37% |
| snake_viper_wild | -8,989 | -4.39% |

Average per day so far: benchmark Rs +528, unified Rs +506, snake_abs_exit_conv Rs +342, snake_abs_exit Rs +335, intraweek Rs +334, intramonth Rs +240, snake_abs_conv Rs +219, snake_abs Rs +217, oracle Rs +171, random_hold Rs +110, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -159, benchmark_smallcap Rs -202, snake_viper_wild Rs -206, gold Rs -333, snake_nonews Rs -411, snake_viper_tick Rs -425, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.