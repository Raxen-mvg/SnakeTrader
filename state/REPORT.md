# Paper trading report

Updated 2026-11-27 12:25 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,212 | +12.11% | 0 | - | 237 |
| unified | 223,292 | +11.65% | 0 | - | 236 |
| oracle | 211,896 | +5.95% | 0 | - | 233 |
| intramonth | 210,849 | +5.42% | 0 | - | 235 |
| random_hold | 210,230 | +5.12% | 13 | 69% | 1,037 |
| intraweek | 207,965 | +3.98% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,020 | +2.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,740 | +1.87% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,558 | +0.78% | 0 | - | 237 |
| snake_abs | 200,642 | +0.32% | 1 | 100% | 255 |
| snake_abs_conv | 200,467 | +0.23% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,066 | -2.97% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,413 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,740 (-5.63%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,942 | +1.96% |
| gold | +3,420 | +2.06% |
| snake_abs_exit_conv | +3,343 | +1.67% |
| snake_abs_conv | +2,100 | +1.06% |
| snake_abs | +2,090 | +1.05% |
| snake_anaconda | +1,769 | +0.92% |
| random_hold | +1,636 | +0.78% |
| intraweek | +916 | +0.44% |
| benchmark_smallcap | +717 | +0.36% |
| intramonth | +316 | +0.15% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| unified | +214 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -339 | -0.16% |
| benchmark | -1,775 | -0.79% |

Average per day so far: benchmark Rs +576, unified Rs +555, oracle Rs +283, intramonth Rs +258, random_hold Rs +244, intraweek Rs +190, snake_abs_exit Rs +129, snake_abs_exit_conv Rs +96, nifty_calls Rs +44, benchmark_smallcap Rs +41, snake_abs Rs +16, snake_abs_conv Rs +12, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -160, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -728

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.