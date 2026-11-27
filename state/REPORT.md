# Paper trading report

Updated 2026-11-27 09:38 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,795 | +12.90% | 0 | - | 237 |
| unified | 223,241 | +11.62% | 0 | - | 236 |
| oracle | 212,419 | +6.21% | 0 | - | 233 |
| intramonth | 210,901 | +5.45% | 0 | - | 235 |
| random_hold | 209,602 | +4.80% | 13 | 69% | 1,037 |
| intraweek | 207,801 | +3.90% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,620 | +2.31% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,713 | +1.86% | 2 | 50% | 345 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,733 | +0.37% | 1 | 100% | 255 |
| snake_abs_conv | 200,551 | +0.28% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,314 | -2.84% | 3 | 33% | 374 |
| snake_viper_wild | 192,983 | -3.51% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,703 | -5.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,000 | -16.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,746 (-5.63%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,542 | +1.76% |
| snake_abs_exit_conv | +3,316 | +1.66% |
| snake_abs_conv | +2,185 | +1.10% |
| snake_abs | +2,181 | +1.10% |
| snake_anaconda | +2,018 | +1.05% |
| gold | +2,006 | +1.21% |
| benchmark_smallcap | +1,065 | +0.53% |
| random_hold | +1,008 | +0.48% |
| snake_viper_wild | +778 | +0.41% |
| snake_viper_tick | +761 | +0.40% |
| intraweek | +753 | +0.36% |
| intramonth | +368 | +0.17% |
| oracle | +184 | +0.09% |
| unified | +163 | +0.07% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -191 | -0.09% |

Average per day so far: benchmark Rs +614, unified Rs +553, oracle Rs +296, intramonth Rs +260, random_hold Rs +229, intraweek Rs +186, snake_abs_exit Rs +118, snake_abs_exit_conv Rs +95, benchmark_smallcap Rs +50, nifty_calls Rs +44, snake_abs Rs +18, snake_abs_conv Rs +14, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -154, snake_viper_wild Rs -206, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -332, gold Rs -762

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.