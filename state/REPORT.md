# Paper trading report

Updated 2026-11-23 11:20 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,174 | +12.09% | 0 | - | 236 |
| benchmark | 223,294 | +11.65% | 0 | - | 237 |
| intraweek | 212,893 | +6.45% | 40 | 55% | 4,400 |
| intramonth | 212,493 | +6.25% | 0 | - | 235 |
| oracle | 211,576 | +5.79% | 0 | - | 233 |
| random_hold | 209,973 | +4.99% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,957 | +3.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,022 | +3.01% | 2 | 50% | 345 |
| snake_abs | 204,343 | +2.17% | 1 | 100% | 255 |
| snake_abs_conv | 204,179 | +2.09% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,124 | +0.56% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,562 | -0.22% | 0 | - | 237 |
| snake_anaconda | 198,138 | -0.93% | 3 | 33% | 374 |
| snake_viper_tick | 197,693 | -1.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,972 | -15.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,408 (-4.80%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,923 | +1.15% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -595 | -0.29% |
| random_hold | -787 | -0.37% |
| oracle | -903 | -0.42% |
| benchmark_smallcap | -1,345 | -0.67% |
| snake_abs | -1,577 | -0.77% |
| snake_abs_conv | -1,604 | -0.78% |
| snake_abs_exit | -1,605 | -0.77% |
| snake_viper_tick | -1,679 | -0.84% |
| snake_viper_wild | -1,705 | -0.84% |
| snake_anaconda | -1,768 | -0.88% |
| benchmark | -1,844 | -0.82% |
| unified | -2,008 | -0.89% |
| intramonth | -2,512 | -1.17% |
| intraweek | -2,819 | -1.31% |

Average per day so far: unified Rs +620, benchmark Rs +597, intraweek Rs +331, intramonth Rs +320, oracle Rs +297, random_hold Rs +256, snake_abs_exit Rs +193, snake_abs_exit_conv Rs +167, snake_abs Rs +117, snake_abs_conv Rs +116, nifty_calls Rs +47, snake_viper_wild Rs +36, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -55, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -770

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.