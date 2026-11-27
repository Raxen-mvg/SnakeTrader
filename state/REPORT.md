# Paper trading report

Updated 2026-11-27 13:52 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,128 | +12.06% | 0 | - | 237 |
| unified | 223,242 | +11.62% | 0 | - | 236 |
| oracle | 211,835 | +5.92% | 0 | - | 233 |
| intramonth | 210,818 | +5.41% | 0 | - | 235 |
| random_hold | 210,816 | +5.41% | 13 | 69% | 1,037 |
| intraweek | 208,265 | +4.13% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,358 | +2.68% | 2 | 50% | 345 |
| snake_abs_exit | 204,756 | +2.38% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,591 | +0.80% | 0 | - | 237 |
| snake_abs | 200,562 | +0.28% | 1 | 100% | 255 |
| snake_abs_conv | 200,380 | +0.19% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,871 | -3.06% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,466 | -14.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,850 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,961 | +2.48% |
| gold | +4,472 | +2.69% |
| snake_abs_exit | +3,678 | +1.83% |
| random_hold | +2,222 | +1.06% |
| snake_abs_conv | +2,013 | +1.01% |
| snake_abs | +2,009 | +1.01% |
| snake_anaconda | +1,574 | +0.82% |
| intraweek | +1,216 | +0.59% |
| benchmark_smallcap | +751 | +0.37% |
| intramonth | +284 | +0.14% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| unified | +164 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -400 | -0.19% |
| benchmark | -1,859 | -0.82% |

Average per day so far: benchmark Rs +574, unified Rs +553, oracle Rs +282, intramonth Rs +258, random_hold Rs +258, intraweek Rs +197, snake_abs_exit_conv Rs +137, snake_abs_exit Rs +122, nifty_calls Rs +44, benchmark_smallcap Rs +42, snake_abs Rs +14, snake_abs_conv Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -166, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -703

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.