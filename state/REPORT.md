# Paper trading report

Updated 2026-11-06 10:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,185 | +7.59% | 0 | - | 237 |
| unified | 214,804 | +7.40% | 0 | - | 236 |
| intraweek | 210,731 | +5.37% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,635 | +4.82% | 1 | 100% | 255 |
| snake_abs_exit | 209,419 | +4.71% | 1 | 100% | 260 |
| intramonth | 206,772 | +3.39% | 0 | - | 235 |
| snake_abs | 206,586 | +3.29% | 1 | 100% | 255 |
| snake_abs_conv | 206,416 | +3.21% | 1 | 100% | 255 |
| oracle | 204,881 | +2.44% | 0 | - | 233 |
| random_hold | 203,362 | +1.68% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,925 | -1.04% | 3 | 33% | 702 |
| snake_anaconda | 196,743 | -1.63% | 3 | 33% | 374 |
| benchmark_smallcap | 195,235 | -2.38% | 0 | - | 237 |
| snake_viper_tick | 194,565 | -2.72% | 2 | 0% | 532 |
| gold | 190,062 | -4.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,464 (-6.27%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,415 | +0.66% |
| intraweek | +1,312 | +0.63% |
| oracle | +809 | +0.40% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -962 | -0.47% |
| intramonth | -1,177 | -0.57% |
| unified | -1,179 | -0.55% |
| benchmark_smallcap | -3,453 | -1.74% |
| gold | -4,159 | -2.14% |
| snake_abs | -5,103 | -2.41% |
| snake_abs_conv | -5,129 | -2.42% |
| snake_abs_exit_conv | -5,169 | -2.41% |
| snake_abs_exit | -5,240 | -2.44% |
| snake_anaconda | -5,736 | -2.83% |
| snake_viper_tick | -6,573 | -3.27% |
| snake_viper_wild | -6,731 | -3.29% |

Average per day so far: benchmark Rs +524, unified Rs +510, snake_abs_exit_conv Rs +371, intraweek Rs +370, snake_abs_exit Rs +362, snake_abs_conv Rs +247, snake_abs Rs +244, intramonth Rs +234, oracle Rs +168, random_hold Rs +116, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -99, snake_anaconda Rs -136, benchmark_smallcap Rs -191, snake_viper_tick Rs -302, gold Rs -343, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.