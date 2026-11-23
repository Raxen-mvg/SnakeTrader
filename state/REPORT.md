# Paper trading report

Updated 2026-11-23 12:34 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,865 | +11.93% | 0 | - | 236 |
| benchmark | 222,973 | +11.49% | 0 | - | 237 |
| intraweek | 212,278 | +6.14% | 40 | 55% | 4,400 |
| oracle | 211,850 | +5.92% | 0 | - | 233 |
| intramonth | 211,703 | +5.85% | 0 | - | 235 |
| random_hold | 208,873 | +4.44% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,094 | +3.55% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,814 | +2.91% | 2 | 50% | 345 |
| snake_abs | 204,887 | +2.44% | 1 | 100% | 255 |
| snake_abs_conv | 204,726 | +2.36% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,148 | +0.57% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,484 | -0.26% | 0 | - | 237 |
| snake_anaconda | 198,409 | -0.80% | 3 | 33% | 374 |
| snake_viper_tick | 197,716 | -1.14% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,087 | -14.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,099 (-4.95%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,039 | +1.21% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -629 | -0.30% |
| snake_abs_exit_conv | -803 | -0.39% |
| snake_abs | -1,033 | -0.50% |
| snake_abs_conv | -1,057 | -0.51% |
| benchmark_smallcap | -1,424 | -0.71% |
| snake_abs_exit | -1,468 | -0.70% |
| snake_anaconda | -1,497 | -0.75% |
| snake_viper_tick | -1,656 | -0.83% |
| snake_viper_wild | -1,681 | -0.83% |
| random_hold | -1,886 | -0.90% |
| benchmark | -2,165 | -0.96% |
| unified | -2,317 | -1.02% |
| intramonth | -3,301 | -1.54% |
| intraweek | -3,434 | -1.59% |

Average per day so far: unified Rs +612, benchmark Rs +589, intraweek Rs +315, oracle Rs +304, intramonth Rs +300, random_hold Rs +228, snake_abs_exit Rs +197, snake_abs_exit_conv Rs +161, snake_abs Rs +132, snake_abs_conv Rs +131, nifty_calls Rs +47, snake_viper_wild Rs +37, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_anaconda Rs -47, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -767

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.