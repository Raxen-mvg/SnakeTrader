# Paper trading report

Updated 2026-11-12 12:28 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,660 | +10.83% | 0 | - | 236 |
| benchmark | 220,058 | +10.03% | 0 | - | 237 |
| snake_abs_exit_conv | 219,311 | +9.66% | 2 | 50% | 345 |
| snake_abs_exit | 218,399 | +9.20% | 2 | 50% | 345 |
| snake_abs | 216,278 | +8.14% | 1 | 100% | 255 |
| snake_abs_conv | 216,114 | +8.06% | 1 | 100% | 255 |
| intraweek | 214,995 | +7.50% | 30 | 53% | 3,302 |
| oracle | 213,469 | +6.74% | 0 | - | 233 |
| intramonth | 211,920 | +5.96% | 0 | - | 235 |
| random_hold | 207,998 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 207,461 | +3.73% | 10 | 50% | 1,825 |
| snake_anaconda | 207,011 | +3.50% | 3 | 33% | 374 |
| snake_viper_tick | 203,911 | +1.96% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,161 | +1.58% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,051 | -6.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,429 (-3.79%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,888 | +1.42% |
| snake_abs_conv | +2,656 | +1.24% |
| snake_abs | +2,653 | +1.24% |
| benchmark_smallcap | +2,354 | +1.17% |
| snake_abs_exit | +2,236 | +1.03% |
| snake_abs_exit_conv | +2,160 | +0.99% |
| intraweek | +1,862 | +0.87% |
| unified | +1,846 | +0.84% |
| oracle | +1,467 | +0.69% |
| intramonth | +924 | +0.44% |
| random_hold | +887 | +0.43% |
| benchmark | +796 | +0.36% |
| snake_viper_wild | +719 | +0.35% |
| snake_viper_tick | +702 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,535 | -1.86% |

Average per day so far: unified Rs +677, snake_abs_exit_conv Rs +666, snake_abs_exit Rs +634, benchmark Rs +627, snake_abs_conv Rs +556, snake_abs Rs +543, intraweek Rs +469, oracle Rs +421, intramonth Rs +372, snake_viper_wild Rs +311, snake_anaconda Rs +260, random_hold Rs +250, snake_viper_tick Rs +186, benchmark_smallcap Rs +113, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -436

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.