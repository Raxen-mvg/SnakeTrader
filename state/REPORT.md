# Paper trading report

Updated 2026-11-05 12:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,158 | +9.08% | 0 | - | 236 |
| snake_abs_exit_conv | 213,422 | +6.71% | 1 | 100% | 255 |
| snake_abs_exit | 213,129 | +6.57% | 1 | 100% | 260 |
| benchmark | 212,890 | +6.45% | 0 | - | 237 |
| intraweek | 211,347 | +5.67% | 25 | 48% | 2,757 |
| snake_abs | 210,309 | +5.16% | 1 | 100% | 255 |
| snake_abs_conv | 210,174 | +5.09% | 1 | 100% | 255 |
| intramonth | 209,844 | +4.92% | 0 | - | 235 |
| snake_viper_wild | 206,797 | +3.40% | 3 | 33% | 702 |
| random_hold | 206,620 | +3.31% | 8 | 62% | 649 |
| oracle | 204,054 | +2.03% | 0 | - | 233 |
| snake_viper_tick | 203,240 | +1.62% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,614 | +0.81% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,170 | -0.41% | 0 | - | 237 |
| gold | 194,106 | -2.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,031 (-4.98%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,131 | +1.98% |
| unified | +3,718 | +1.73% |
| random_hold | +3,311 | +1.63% |
| intramonth | +2,828 | +1.37% |
| gold | +2,713 | +1.42% |
| benchmark_smallcap | +2,500 | +1.27% |
| oracle | +2,262 | +1.12% |
| intraweek | +1,649 | +0.79% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,584 | -0.75% |
| snake_abs_exit_conv | -1,593 | -0.74% |
| snake_abs | -1,594 | -0.75% |
| snake_abs_exit | -1,771 | -0.82% |
| snake_viper_tick | -2,161 | -1.05% |
| snake_anaconda | -2,206 | -1.08% |
| snake_viper_wild | -2,233 | -1.07% |

Average per day so far: unified Rs +648, snake_abs_exit_conv Rs +537, snake_abs_exit Rs +525, benchmark Rs +460, snake_abs_conv Rs +407, intraweek Rs +405, snake_abs Rs +397, intramonth Rs +352, snake_viper_wild Rs +340, random_hold Rs +236, snake_viper_tick Rs +191, oracle Rs +145, snake_anaconda Rs +70, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -35, gold Rs -210, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.