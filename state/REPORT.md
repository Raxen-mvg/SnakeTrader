# Paper trading report

Updated 2026-11-27 13:55 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,112 | +12.06% | 0 | - | 237 |
| unified | 223,269 | +11.63% | 0 | - | 236 |
| oracle | 211,859 | +5.93% | 0 | - | 233 |
| intramonth | 210,779 | +5.39% | 0 | - | 235 |
| random_hold | 210,771 | +5.38% | 13 | 69% | 1,037 |
| intraweek | 208,232 | +4.12% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,424 | +2.71% | 2 | 50% | 345 |
| snake_abs_exit | 204,736 | +2.37% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| snake_abs | 200,560 | +0.28% | 1 | 100% | 255 |
| snake_abs_conv | 200,378 | +0.19% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,869 | -3.07% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,416 | -14.79% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,847 (-5.58%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,027 | +2.51% |
| gold | +4,422 | +2.66% |
| snake_abs_exit | +3,658 | +1.82% |
| random_hold | +2,177 | +1.04% |
| snake_abs_conv | +2,011 | +1.01% |
| snake_abs | +2,007 | +1.01% |
| snake_anaconda | +1,572 | +0.82% |
| intraweek | +1,184 | +0.57% |
| benchmark_smallcap | +785 | +0.39% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| intramonth | +246 | +0.12% |
| unified | +190 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -377 | -0.18% |
| benchmark | -1,874 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +554, oracle Rs +282, intramonth Rs +257, random_hold Rs +256, intraweek Rs +196, snake_abs_exit_conv Rs +139, snake_abs_exit Rs +121, nifty_calls Rs +44, benchmark_smallcap Rs +43, snake_abs Rs +14, snake_abs_conv Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -166, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -704

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.