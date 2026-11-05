# Paper trading report

Updated 2026-11-05 13:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,814 | +8.41% | 0 | - | 236 |
| snake_abs_exit_conv | 214,175 | +7.09% | 1 | 100% | 255 |
| benchmark | 214,137 | +7.07% | 0 | - | 237 |
| snake_abs_exit | 213,943 | +6.97% | 1 | 100% | 260 |
| snake_abs | 211,060 | +5.53% | 1 | 100% | 255 |
| snake_abs_conv | 210,922 | +5.46% | 1 | 100% | 255 |
| intraweek | 209,820 | +4.91% | 25 | 48% | 2,757 |
| intramonth | 208,616 | +4.31% | 0 | - | 235 |
| snake_viper_wild | 206,938 | +3.47% | 3 | 33% | 702 |
| random_hold | 205,304 | +2.65% | 8 | 62% | 649 |
| oracle | 203,786 | +1.89% | 0 | - | 233 |
| snake_viper_tick | 203,382 | +1.69% | 2 | 0% | 532 |
| snake_anaconda | 202,331 | +1.17% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| gold | 194,156 | -2.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,793 (-5.10%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,378 | +2.58% |
| gold | +2,762 | +1.44% |
| benchmark_smallcap | +2,433 | +1.24% |
| unified | +2,375 | +1.11% |
| random_hold | +1,996 | +0.98% |
| oracle | +1,993 | +0.99% |
| intramonth | +1,600 | +0.77% |
| intraweek | +122 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -836 | -0.40% |
| snake_abs_exit_conv | -840 | -0.39% |
| snake_abs | -843 | -0.40% |
| snake_abs_exit | -957 | -0.45% |
| snake_anaconda | -1,489 | -0.73% |
| snake_viper_tick | -2,018 | -0.98% |
| snake_viper_wild | -2,092 | -1.00% |

Average per day so far: unified Rs +601, snake_abs_exit_conv Rs +567, snake_abs_exit Rs +558, benchmark Rs +505, snake_abs_conv Rs +437, snake_abs Rs +425, intraweek Rs +351, snake_viper_wild Rs +347, intramonth Rs +308, snake_viper_tick Rs +199, random_hold Rs +189, oracle Rs +135, snake_anaconda Rs +101, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -37, gold Rs -209, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.