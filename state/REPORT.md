# Paper trading report

Updated 2026-11-23 14:13 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,983 | +11.99% | 0 | - | 236 |
| benchmark | 222,047 | +11.02% | 0 | - | 237 |
| intraweek | 212,228 | +6.11% | 40 | 55% | 4,400 |
| intramonth | 212,076 | +6.04% | 0 | - | 235 |
| oracle | 211,657 | +5.83% | 0 | - | 233 |
| random_hold | 208,956 | +4.48% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,698 | +3.35% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,862 | +2.93% | 2 | 50% | 345 |
| snake_abs | 204,329 | +2.16% | 1 | 100% | 255 |
| snake_abs_conv | 204,154 | +2.08% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,827 | +0.41% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_anaconda | 197,746 | -1.13% | 3 | 33% | 374 |
| snake_viper_tick | 197,401 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,348 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,074 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,299 | +0.77% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -754 | -0.36% |
| oracle | -821 | -0.39% |
| benchmark_smallcap | -1,469 | -0.73% |
| snake_abs | -1,591 | -0.77% |
| snake_abs_conv | -1,629 | -0.79% |
| random_hold | -1,803 | -0.85% |
| snake_abs_exit | -1,865 | -0.89% |
| snake_viper_tick | -1,970 | -0.99% |
| snake_viper_wild | -2,003 | -0.99% |
| snake_anaconda | -2,159 | -1.08% |
| unified | -2,198 | -0.97% |
| intramonth | -2,928 | -1.36% |
| benchmark | -3,091 | -1.37% |
| intraweek | -3,484 | -1.61% |

Average per day so far: unified Rs +615, benchmark Rs +565, intraweek Rs +314, intramonth Rs +310, oracle Rs +299, random_hold Rs +230, snake_abs_exit Rs +186, snake_abs_exit_conv Rs +163, snake_abs Rs +117, snake_abs_conv Rs +115, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -66, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -786

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.