# Paper trading report

Updated 2026-11-27 13:46 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,197 | +12.10% | 0 | - | 237 |
| unified | 223,073 | +11.54% | 0 | - | 236 |
| oracle | 211,665 | +5.83% | 0 | - | 233 |
| random_hold | 210,965 | +5.48% | 13 | 69% | 1,037 |
| intramonth | 210,444 | +5.22% | 0 | - | 235 |
| intraweek | 208,489 | +4.25% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,324 | +2.66% | 2 | 50% | 345 |
| snake_abs_exit | 204,724 | +2.36% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| snake_abs | 200,485 | +0.24% | 1 | 100% | 255 |
| snake_abs_conv | 200,303 | +0.15% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,790 | -3.10% | 3 | 33% | 374 |
| snake_viper_wild | 192,298 | -3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,033 | -5.48% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,367 | -14.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,771 (-5.61%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,927 | +2.46% |
| gold | +4,373 | +2.63% |
| snake_abs_exit | +3,647 | +1.81% |
| random_hold | +2,371 | +1.14% |
| snake_abs_conv | +1,937 | +0.98% |
| snake_abs | +1,933 | +0.97% |
| snake_anaconda | +1,494 | +0.78% |
| intraweek | +1,440 | +0.70% |
| benchmark_smallcap | +617 | +0.31% |
| snake_viper_wild | +93 | +0.05% |
| snake_viper_tick | +91 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -5 | -0.00% |
| intramonth | -90 | -0.04% |
| oracle | -571 | -0.27% |
| benchmark | -1,790 | -0.79% |

Average per day so far: benchmark Rs +576, unified Rs +549, oracle Rs +278, random_hold Rs +261, intramonth Rs +249, intraweek Rs +202, snake_abs_exit_conv Rs +137, snake_abs_exit Rs +121, nifty_calls Rs +44, benchmark_smallcap Rs +38, snake_abs Rs +12, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -168, snake_viper_wild Rs -227, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -354, gold Rs -706

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.