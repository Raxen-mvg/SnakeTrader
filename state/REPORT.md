# Paper trading report

Updated 2026-11-19 09:46 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,394 | +12.20% | 0 | - | 236 |
| benchmark | 220,188 | +10.09% | 0 | - | 237 |
| intramonth | 214,119 | +7.06% | 0 | - | 235 |
| snake_abs_exit | 213,871 | +6.93% | 2 | 50% | 345 |
| intraweek | 212,269 | +6.13% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,987 | +5.99% | 2 | 50% | 345 |
| oracle | 211,638 | +5.82% | 0 | - | 233 |
| snake_abs | 209,143 | +4.57% | 1 | 100% | 255 |
| snake_abs_conv | 209,022 | +4.51% | 1 | 100% | 255 |
| random_hold | 208,104 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 207,591 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,044 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,917 | +1.96% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,871 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,744 (-4.13%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,845 | +0.87% |
| unified | +1,782 | +0.80% |
| benchmark_smallcap | +1,289 | +0.65% |
| random_hold | +1,172 | +0.57% |
| oracle | +842 | +0.40% |
| snake_viper_wild | +552 | +0.27% |
| snake_viper_tick | +540 | +0.27% |
| intraweek | +429 | +0.20% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -107 | -0.05% |
| snake_abs_exit | -161 | -0.07% |
| snake_abs | -294 | -0.14% |
| snake_abs_conv | -303 | -0.14% |
| snake_abs_exit_conv | -397 | -0.19% |
| snake_anaconda | -484 | -0.24% |
| gold | -2,450 | -1.38% |

Average per day so far: unified Rs +659, benchmark Rs +546, snake_abs_exit Rs +408, intramonth Rs +382, snake_abs_exit_conv Rs +353, intraweek Rs +332, oracle Rs +315, snake_abs_conv Rs +265, snake_viper_wild Rs +262, snake_abs Rs +261, random_hold Rs +219, snake_viper_tick Rs +156, snake_anaconda Rs +122, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.