# Paper trading report

Updated 2026-11-06 10:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,856 | +7.43% | 0 | - | 237 |
| unified | 214,686 | +7.34% | 0 | - | 236 |
| intraweek | 210,276 | +5.14% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,235 | +4.62% | 1 | 100% | 255 |
| snake_abs_exit | 209,019 | +4.51% | 1 | 100% | 260 |
| intramonth | 206,702 | +3.35% | 0 | - | 235 |
| snake_abs | 206,187 | +3.09% | 1 | 100% | 255 |
| snake_abs_conv | 206,016 | +3.01% | 1 | 100% | 255 |
| oracle | 204,169 | +2.08% | 0 | - | 233 |
| random_hold | 203,406 | +1.70% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,502 | -1.25% | 3 | 33% | 702 |
| snake_anaconda | 196,244 | -1.88% | 3 | 33% | 374 |
| benchmark_smallcap | 194,708 | -2.65% | 0 | - | 237 |
| snake_viper_tick | 194,145 | -2.93% | 2 | 0% | 532 |
| gold | 190,457 | -4.77% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,190 (-6.40%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,086 | +0.51% |
| intraweek | +857 | +0.41% |
| oracle | +97 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -917 | -0.45% |
| intramonth | -1,246 | -0.60% |
| unified | -1,298 | -0.60% |
| gold | -3,765 | -1.94% |
| benchmark_smallcap | -3,980 | -2.00% |
| snake_abs | -5,501 | -2.60% |
| snake_abs_conv | -5,528 | -2.61% |
| snake_abs_exit_conv | -5,569 | -2.59% |
| snake_abs_exit | -5,640 | -2.63% |
| snake_anaconda | -6,236 | -3.08% |
| snake_viper_tick | -6,993 | -3.48% |
| snake_viper_wild | -7,154 | -3.50% |

Average per day so far: benchmark Rs +512, unified Rs +506, snake_abs_exit_conv Rs +355, intraweek Rs +354, snake_abs_exit Rs +347, snake_abs_conv Rs +231, intramonth Rs +231, snake_abs Rs +229, oracle Rs +144, random_hold Rs +117, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -119, snake_anaconda Rs -157, benchmark_smallcap Rs -212, snake_viper_tick Rs -325, gold Rs -329, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.