# Paper trading report

Updated 2026-11-12 14:25 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,002 | +10.50% | 0 | - | 236 |
| benchmark | 220,448 | +10.22% | 0 | - | 237 |
| snake_abs_exit_conv | 218,219 | +9.11% | 2 | 50% | 345 |
| snake_abs_exit | 217,128 | +8.56% | 2 | 50% | 345 |
| snake_abs | 215,310 | +7.66% | 1 | 100% | 255 |
| snake_abs_conv | 215,134 | +7.57% | 1 | 100% | 255 |
| intraweek | 214,424 | +7.21% | 30 | 53% | 3,302 |
| oracle | 212,942 | +6.47% | 0 | - | 233 |
| intramonth | 211,764 | +5.88% | 0 | - | 235 |
| random_hold | 208,005 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 206,607 | +3.30% | 10 | 50% | 1,825 |
| snake_anaconda | 205,964 | +2.98% | 3 | 33% | 374 |
| snake_viper_tick | 203,074 | +1.54% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,959 | +1.48% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,114 | -7.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,928 (-4.04%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,152 | +1.07% |
| snake_anaconda | +1,841 | +0.90% |
| snake_abs | +1,685 | +0.79% |
| snake_abs_conv | +1,677 | +0.79% |
| intraweek | +1,291 | +0.61% |
| unified | +1,188 | +0.54% |
| benchmark | +1,186 | +0.54% |
| snake_abs_exit_conv | +1,067 | +0.49% |
| snake_abs_exit | +965 | +0.45% |
| oracle | +940 | +0.44% |
| random_hold | +895 | +0.43% |
| intramonth | +768 | +0.36% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_wild | -135 | -0.07% |
| snake_viper_tick | -135 | -0.07% |
| gold | -4,472 | -2.36% |

Average per day so far: unified Rs +656, benchmark Rs +639, snake_abs_exit_conv Rs +628, snake_abs_exit Rs +591, snake_abs_conv Rs +522, snake_abs Rs +510, intraweek Rs +451, oracle Rs +404, intramonth Rs +368, snake_viper_wild Rs +275, random_hold Rs +250, snake_anaconda Rs +221, snake_viper_tick Rs +146, benchmark_smallcap Rs +106, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -465

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.