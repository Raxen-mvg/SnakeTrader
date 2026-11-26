# Paper trading report

Updated 2026-11-26 09:35 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,122 | +12.56% | 0 | - | 237 |
| unified | 224,165 | +12.08% | 0 | - | 236 |
| oracle | 214,012 | +7.01% | 0 | - | 233 |
| intramonth | 211,781 | +5.89% | 0 | - | 235 |
| random_hold | 210,589 | +5.29% | 13 | 69% | 1,037 |
| intraweek | 207,754 | +3.88% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,113 | +2.06% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,417 | +1.71% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,075 | +0.54% | 1 | 100% | 255 |
| snake_abs_conv | 200,903 | +0.45% | 1 | 100% | 255 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,770 | -1.61% | 16 | 50% | 2,827 |
| snake_anaconda | 195,565 | -2.22% | 3 | 33% | 374 |
| snake_viper_tick | 193,420 | -3.29% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,816 | -16.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,588 (-5.21%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,219 | +1.35% |
| benchmark_smallcap | +1,861 | +0.94% |
| snake_abs_exit | +1,858 | +0.92% |
| snake_abs_exit_conv | +1,441 | +0.71% |
| random_hold | +1,096 | +0.52% |
| snake_anaconda | +1,012 | +0.52% |
| intraweek | +1,011 | +0.49% |
| snake_abs_conv | +930 | +0.47% |
| snake_abs | +926 | +0.46% |
| oracle | +216 | +0.10% |
| benchmark | +99 | +0.04% |
| intramonth | +87 | +0.04% |
| unified | +65 | +0.03% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -757 | -0.39% |
| snake_viper_wild | -773 | -0.39% |

Average per day so far: benchmark Rs +613, unified Rs +589, oracle Rs +342, intramonth Rs +287, random_hold Rs +258, intraweek Rs +189, snake_abs_exit Rs +108, snake_abs_exit_conv Rs +90, nifty_calls Rs +45, snake_abs Rs +28, snake_abs_conv Rs +24, benchmark_smallcap Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -98, snake_anaconda Rs -123, snake_viper_tick Rs -219, snake_nonews Rs -284, snake Rs -304, gold Rs -809

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.