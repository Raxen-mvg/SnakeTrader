# Paper trading report

Updated 2026-11-12 12:10 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,515 | +10.76% | 0 | - | 236 |
| benchmark | 220,150 | +10.07% | 0 | - | 237 |
| snake_abs_exit_conv | 219,143 | +9.57% | 2 | 50% | 345 |
| snake_abs_exit | 218,170 | +9.09% | 2 | 50% | 345 |
| snake_abs | 216,004 | +8.00% | 1 | 100% | 255 |
| snake_abs_conv | 215,836 | +7.92% | 1 | 100% | 255 |
| intraweek | 214,973 | +7.49% | 30 | 53% | 3,302 |
| oracle | 213,339 | +6.67% | 0 | - | 233 |
| intramonth | 211,737 | +5.87% | 0 | - | 235 |
| random_hold | 207,993 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 207,659 | +3.83% | 10 | 50% | 1,825 |
| snake_anaconda | 206,722 | +3.36% | 3 | 33% | 374 |
| snake_viper_tick | 204,106 | +2.05% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,161 | +1.58% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,232 | -6.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,319 (-3.84%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,600 | +1.27% |
| snake_abs | +2,379 | +1.11% |
| snake_abs_conv | +2,378 | +1.11% |
| benchmark_smallcap | +2,354 | +1.17% |
| snake_abs_exit | +2,007 | +0.93% |
| snake_abs_exit_conv | +1,991 | +0.92% |
| intraweek | +1,840 | +0.86% |
| unified | +1,701 | +0.77% |
| oracle | +1,336 | +0.63% |
| snake_viper_wild | +917 | +0.44% |
| snake_viper_tick | +897 | +0.44% |
| benchmark | +887 | +0.41% |
| random_hold | +883 | +0.43% |
| intramonth | +741 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,354 | -1.77% |

Average per day so far: unified Rs +672, snake_abs_exit_conv Rs +660, benchmark Rs +630, snake_abs_exit Rs +627, snake_abs_conv Rs +546, snake_abs Rs +533, intraweek Rs +468, oracle Rs +417, intramonth Rs +367, snake_viper_wild Rs +319, random_hold Rs +250, snake_anaconda Rs +249, snake_viper_tick Rs +196, benchmark_smallcap Rs +113, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -430

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.