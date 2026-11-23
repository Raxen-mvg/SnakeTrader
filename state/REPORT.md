# Paper trading report

Updated 2026-11-23 14:04 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,936 | +11.97% | 0 | - | 236 |
| benchmark | 222,215 | +11.11% | 0 | - | 237 |
| intraweek | 212,298 | +6.15% | 40 | 55% | 4,400 |
| intramonth | 211,982 | +5.99% | 0 | - | 235 |
| oracle | 211,451 | +5.73% | 0 | - | 233 |
| random_hold | 208,872 | +4.44% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,817 | +3.41% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,602 | +2.80% | 2 | 50% | 345 |
| snake_abs | 204,605 | +2.30% | 1 | 100% | 255 |
| snake_abs_conv | 204,425 | +2.21% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,158 | +0.58% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_anaconda | 197,742 | -1.13% | 3 | 33% | 374 |
| snake_viper_tick | 197,726 | -1.14% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,381 | -15.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,043 (-4.98%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,332 | +0.79% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -1,015 | -0.49% |
| oracle | -1,027 | -0.48% |
| snake_abs | -1,314 | -0.64% |
| snake_abs_conv | -1,358 | -0.66% |
| benchmark_smallcap | -1,469 | -0.73% |
| snake_viper_tick | -1,646 | -0.83% |
| snake_viper_wild | -1,671 | -0.82% |
| snake_abs_exit | -1,745 | -0.84% |
| random_hold | -1,888 | -0.90% |
| snake_anaconda | -2,163 | -1.08% |
| unified | -2,246 | -0.99% |
| benchmark | -2,922 | -1.30% |
| intramonth | -3,022 | -1.41% |
| intraweek | -3,414 | -1.58% |

Average per day so far: unified Rs +614, benchmark Rs +570, intraweek Rs +315, intramonth Rs +307, oracle Rs +294, random_hold Rs +227, snake_abs_exit Rs +189, snake_abs_exit_conv Rs +156, snake_abs Rs +124, snake_abs_conv Rs +123, nifty_calls Rs +47, snake_viper_wild Rs +37, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -66, snake_viper_tick Rs -81, snake_nonews Rs -300, snake Rs -320, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.