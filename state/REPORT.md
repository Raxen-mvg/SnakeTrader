# Paper trading report

Updated 2026-11-12 13:13 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,569 | +10.78% | 0 | - | 236 |
| benchmark | 220,180 | +10.09% | 0 | - | 237 |
| snake_abs_exit_conv | 218,690 | +9.35% | 2 | 50% | 345 |
| snake_abs_exit | 217,742 | +8.87% | 2 | 50% | 345 |
| snake_abs | 215,751 | +7.88% | 1 | 100% | 255 |
| snake_abs_conv | 215,580 | +7.79% | 1 | 100% | 255 |
| intraweek | 214,637 | +7.32% | 30 | 53% | 3,302 |
| oracle | 213,556 | +6.78% | 0 | - | 233 |
| intramonth | 212,174 | +6.09% | 0 | - | 235 |
| random_hold | 208,071 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,360 | +3.68% | 10 | 50% | 1,825 |
| snake_anaconda | 206,511 | +3.25% | 3 | 33% | 374 |
| snake_viper_tick | 203,813 | +1.91% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,161 | +1.58% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,886 | -7.06% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,305 (-3.85%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,388 | +1.17% |
| benchmark_smallcap | +2,354 | +1.17% |
| snake_abs | +2,126 | +0.99% |
| snake_abs_conv | +2,122 | +0.99% |
| unified | +1,755 | +0.80% |
| snake_abs_exit | +1,579 | +0.73% |
| oracle | +1,553 | +0.73% |
| snake_abs_exit_conv | +1,539 | +0.71% |
| intraweek | +1,504 | +0.70% |
| intramonth | +1,177 | +0.56% |
| random_hold | +960 | +0.46% |
| benchmark | +918 | +0.42% |
| snake_viper_wild | +619 | +0.30% |
| snake_viper_tick | +604 | +0.30% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,699 | -1.95% |

Average per day so far: unified Rs +674, snake_abs_exit_conv Rs +644, benchmark Rs +631, snake_abs_exit Rs +612, snake_abs_conv Rs +537, snake_abs Rs +525, intraweek Rs +457, oracle Rs +424, intramonth Rs +380, snake_viper_wild Rs +307, random_hold Rs +252, snake_anaconda Rs +241, snake_viper_tick Rs +182, benchmark_smallcap Rs +113, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -441

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.