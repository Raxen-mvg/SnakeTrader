# Paper trading report

Updated 2026-11-09 15:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,292 | +9.65% | 0 | - | 236 |
| benchmark | 218,008 | +9.00% | 0 | - | 237 |
| intraweek | 214,619 | +7.31% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,320 | +6.16% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,223 | +6.11% | 2 | 50% | 330 |
| intramonth | 209,989 | +5.00% | 0 | - | 235 |
| snake_abs | 209,618 | +4.81% | 1 | 100% | 255 |
| oracle | 209,499 | +4.75% | 0 | - | 233 |
| snake_abs_conv | 209,452 | +4.73% | 1 | 100% | 255 |
| random_hold | 204,608 | +2.30% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,820 | -0.09% | 3 | 33% | 374 |
| benchmark_smallcap | 198,206 | -0.90% | 0 | - | 237 |
| snake_viper_wild | 197,949 | -1.03% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,587 | -2.71% | 6 | 50% | 1,154 |
| gold | 192,084 | -3.96% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,155 (-4.92%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,257 | +2.02% |
| snake_abs_conv | +4,225 | +2.06% |
| snake_abs | +4,199 | +2.04% |
| snake_abs_exit | +4,008 | +1.92% |
| snake_anaconda | +3,993 | +2.04% |
| snake_abs_exit_conv | +3,801 | +1.82% |
| unified | +3,683 | +1.71% |
| oracle | +3,672 | +1.78% |
| intramonth | +2,386 | +1.15% |
| snake_viper_wild | +1,912 | +0.97% |
| snake_viper_tick | +1,877 | +0.97% |
| benchmark_smallcap | +1,412 | +0.72% |
| gold | +1,036 | +0.54% |
| random_hold | +701 | +0.34% |
| benchmark | +520 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +643, benchmark Rs +600, intraweek Rs +487, snake_abs_exit Rs +456, snake_abs_exit_conv Rs +453, snake_abs_conv Rs +350, snake_abs Rs +344, intramonth Rs +333, oracle Rs +317, random_hold Rs +154, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -7, benchmark_smallcap Rs -69, snake_viper_wild Rs -93, gold Rs -264, snake_viper_tick Rs -285, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.