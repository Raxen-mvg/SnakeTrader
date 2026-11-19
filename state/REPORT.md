# Paper trading report

Updated 2026-11-19 12:15 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,707 | +11.85% | 0 | - | 236 |
| benchmark | 221,374 | +10.69% | 0 | - | 237 |
| intramonth | 213,337 | +6.67% | 0 | - | 235 |
| snake_abs_exit | 213,058 | +6.53% | 2 | 50% | 345 |
| intraweek | 211,555 | +5.78% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,147 | +5.57% | 2 | 50% | 345 |
| oracle | 211,022 | +5.51% | 0 | - | 233 |
| snake_abs | 208,696 | +4.35% | 1 | 100% | 255 |
| snake_abs_conv | 208,563 | +4.28% | 1 | 100% | 255 |
| random_hold | 207,644 | +3.82% | 10 | 70% | 733 |
| snake_viper_wild | 207,600 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,052 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 202,954 | +1.48% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,638 | +0.32% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,200 | -12.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,154 (-4.42%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,312 | +0.66% |
| unified | +1,095 | +0.49% |
| benchmark | +1,079 | +0.49% |
| intramonth | +1,063 | +0.50% |
| random_hold | +711 | +0.34% |
| snake_viper_wild | +560 | +0.27% |
| snake_viper_tick | +549 | +0.27% |
| oracle | +226 | +0.11% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -284 | -0.13% |
| snake_abs | -741 | -0.35% |
| snake_abs_conv | -762 | -0.36% |
| snake_abs_exit | -974 | -0.46% |
| snake_abs_exit_conv | -1,236 | -0.58% |
| snake_anaconda | -1,447 | -0.71% |
| gold | -2,121 | -1.20% |

Average per day so far: unified Rs +641, benchmark Rs +578, snake_abs_exit Rs +384, intramonth Rs +360, snake_abs_exit_conv Rs +328, intraweek Rs +312, oracle Rs +298, snake_viper_wild Rs +262, snake_abs_conv Rs +252, snake_abs Rs +248, random_hold Rs +207, snake_viper_tick Rs +156, snake_anaconda Rs +92, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -670

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.