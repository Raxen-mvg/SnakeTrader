# Paper trading report

Updated 2026-11-27 12:19 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,510 | +12.26% | 0 | - | 237 |
| unified | 223,362 | +11.68% | 0 | - | 236 |
| oracle | 211,963 | +5.98% | 0 | - | 233 |
| intramonth | 210,965 | +5.48% | 0 | - | 235 |
| random_hold | 210,106 | +5.05% | 13 | 69% | 1,037 |
| intraweek | 207,946 | +3.97% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,072 | +2.54% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,903 | +1.95% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_abs | 200,747 | +0.37% | 1 | 100% | 255 |
| snake_abs_conv | 200,571 | +0.28% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,088 | -2.96% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,200 | -15.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,770 (-5.61%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,994 | +1.99% |
| snake_abs_exit_conv | +3,506 | +1.75% |
| gold | +3,206 | +1.93% |
| snake_abs_conv | +2,204 | +1.11% |
| snake_abs | +2,195 | +1.10% |
| snake_anaconda | +1,792 | +0.93% |
| random_hold | +1,512 | +0.72% |
| intraweek | +897 | +0.43% |
| benchmark_smallcap | +841 | +0.42% |
| intramonth | +431 | +0.20% |
| unified | +284 | +0.13% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -273 | -0.13% |
| benchmark | -1,476 | -0.65% |

Average per day so far: benchmark Rs +584, unified Rs +556, oracle Rs +285, intramonth Rs +261, random_hold Rs +241, intraweek Rs +189, snake_abs_exit Rs +130, snake_abs_exit_conv Rs +100, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +19, snake_abs_conv Rs +15, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -160, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -733

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.