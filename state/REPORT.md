# Paper trading report

Updated 2026-11-18 09:35 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,857 | +10.93% | 0 | - | 236 |
| benchmark | 220,716 | +10.36% | 0 | - | 237 |
| snake_abs_exit | 213,185 | +6.59% | 2 | 50% | 345 |
| intraweek | 213,178 | +6.59% | 35 | 54% | 3,851 |
| oracle | 212,293 | +6.15% | 0 | - | 233 |
| snake_abs_exit_conv | 211,693 | +5.85% | 2 | 50% | 345 |
| intramonth | 211,678 | +5.84% | 0 | - | 235 |
| snake_abs | 209,129 | +4.57% | 1 | 100% | 255 |
| snake_abs_conv | 208,991 | +4.50% | 1 | 100% | 255 |
| snake_viper_wild | 207,338 | +3.67% | 16 | 50% | 2,827 |
| random_hold | 207,266 | +3.63% | 10 | 70% | 733 |
| snake_anaconda | 204,032 | +2.02% | 3 | 33% | 374 |
| snake_viper_tick | 203,796 | +1.90% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,067 | +0.03% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,042 | -11.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,016 (-4.49%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +572 | +0.27% |
| snake_abs | +571 | +0.27% |
| unified | +418 | +0.19% |
| intramonth | +136 | +0.06% |
| snake_abs_exit_conv | +119 | +0.06% |
| snake_abs_exit | +43 | +0.02% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -23 | -0.01% |
| intraweek | -144 | -0.07% |
| oracle | -193 | -0.09% |
| benchmark_smallcap | -504 | -0.25% |
| benchmark | -887 | -0.40% |
| random_hold | -1,166 | -0.56% |
| snake_viper_tick | -2,041 | -0.99% |
| snake_viper_wild | -2,077 | -0.99% |
| gold | -3,683 | -2.04% |

Average per day so far: unified Rs +607, benchmark Rs +575, snake_abs_exit Rs +400, intraweek Rs +366, snake_abs_exit_conv Rs +354, oracle Rs +341, intramonth Rs +324, snake_abs_conv Rs +272, snake_abs Rs +269, snake_viper_wild Rs +262, random_hold Rs +202, snake_viper_tick Rs +152, snake_anaconda Rs +130, nifty_calls Rs +51, benchmark_smallcap Rs +2, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -638

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.