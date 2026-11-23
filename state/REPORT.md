# Paper trading report

Updated 2026-11-23 15:19 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,730 | +11.87% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| oracle | 212,086 | +6.04% | 0 | - | 233 |
| intramonth | 211,820 | +5.91% | 0 | - | 235 |
| intraweek | 211,519 | +5.76% | 40 | 55% | 4,400 |
| random_hold | 208,365 | +4.18% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,935 | +3.97% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,571 | +3.79% | 2 | 50% | 345 |
| snake_abs | 205,776 | +2.89% | 1 | 100% | 255 |
| snake_abs_conv | 205,624 | +2.81% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,225 | +0.61% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,107 | -0.45% | 3 | 33% | 374 |
| benchmark_smallcap | 199,091 | -0.45% | 0 | - | 237 |
| snake_viper_tick | 197,791 | -1.10% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,512 | -15.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,083 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,463 | +0.87% |
| snake_abs_exit_conv | +954 | +0.46% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -144 | -0.07% |
| snake_abs_conv | -159 | -0.08% |
| oracle | -393 | -0.18% |
| snake_abs_exit | -628 | -0.30% |
| snake_anaconda | -798 | -0.40% |
| snake_viper_tick | -1,580 | -0.79% |
| snake_viper_wild | -1,604 | -0.79% |
| benchmark_smallcap | -1,816 | -0.90% |
| random_hold | -2,395 | -1.14% |
| unified | -2,452 | -1.08% |
| intramonth | -3,184 | -1.48% |
| benchmark | -3,611 | -1.60% |
| intraweek | -4,193 | -1.94% |

Average per day so far: unified Rs +608, benchmark Rs +552, oracle Rs +310, intramonth Rs +303, intraweek Rs +295, snake_abs_exit Rs +220, random_hold Rs +214, snake_abs_exit_conv Rs +210, snake_abs_conv Rs +156, snake_abs Rs +156, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -26, snake_anaconda Rs -26, snake_viper_tick Rs -79, snake_nonews Rs -300, snake Rs -320, gold Rs -782

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.