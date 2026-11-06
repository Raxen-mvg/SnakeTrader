# Paper trading report

Updated 2026-11-06 15:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,289 | +8.64% | 0 | - | 237 |
| unified | 216,065 | +8.03% | 0 | - | 236 |
| intraweek | 210,048 | +5.02% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,517 | +4.26% | 1 | 100% | 255 |
| snake_abs_exit | 208,395 | +4.20% | 1 | 100% | 260 |
| intramonth | 207,881 | +3.94% | 0 | - | 235 |
| oracle | 205,881 | +2.94% | 0 | - | 233 |
| snake_abs | 205,509 | +2.75% | 1 | 100% | 255 |
| snake_abs_conv | 205,323 | +2.66% | 1 | 100% | 255 |
| random_hold | 203,825 | +1.91% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 197,029 | -1.49% | 0 | - | 237 |
| snake_anaconda | 196,168 | -1.92% | 3 | 33% | 374 |
| snake_viper_wild | 196,041 | -1.98% | 4 | 25% | 842 |
| snake_viper_tick | 192,714 | -3.64% | 3 | 0% | 672 |
| gold | 191,081 | -4.46% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,475 (-6.26%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,519 | +1.65% |
| oracle | +1,809 | +0.89% |
| intraweek | +629 | +0.30% |
| unified | +82 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -68 | -0.03% |
| random_hold | -498 | -0.24% |
| benchmark_smallcap | -1,659 | -0.83% |
| gold | -3,140 | -1.62% |
| snake_abs | -6,179 | -2.92% |
| snake_abs_conv | -6,222 | -2.94% |
| snake_abs_exit | -6,264 | -2.92% |
| snake_abs_exit_conv | -6,286 | -2.93% |
| snake_anaconda | -6,311 | -3.12% |
| snake_viper_tick | -8,424 | -4.19% |
| snake_viper_wild | -8,615 | -4.21% |

Average per day so far: benchmark Rs +596, unified Rs +554, intraweek Rs +346, snake_abs_exit_conv Rs +328, snake_abs_exit Rs +323, intramonth Rs +272, snake_abs_conv Rs +205, snake_abs Rs +204, oracle Rs +203, random_hold Rs +132, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -119, snake_anaconda Rs -160, snake_viper_wild Rs -189, gold Rs -308, snake_viper_tick Rs -405, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.