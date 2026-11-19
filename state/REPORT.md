# Paper trading report

Updated 2026-11-19 10:17 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,999 | +12.00% | 0 | - | 236 |
| benchmark | 220,739 | +10.37% | 0 | - | 237 |
| snake_abs_exit | 213,976 | +6.99% | 2 | 50% | 345 |
| intramonth | 213,646 | +6.82% | 0 | - | 235 |
| intraweek | 212,679 | +6.34% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,186 | +6.09% | 2 | 50% | 345 |
| oracle | 211,208 | +5.60% | 0 | - | 233 |
| snake_abs | 209,449 | +4.72% | 1 | 100% | 255 |
| snake_abs_conv | 209,335 | +4.67% | 1 | 100% | 255 |
| random_hold | 207,978 | +3.99% | 10 | 70% | 733 |
| snake_viper_wild | 207,835 | +3.92% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,282 | +2.14% | 15 | 47% | 2,625 |
| snake_anaconda | 203,841 | +1.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,822 | -12.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,527 (-4.24%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,388 | +0.62% |
| intramonth | +1,372 | +0.65% |
| benchmark_smallcap | +1,065 | +0.53% |
| random_hold | +1,045 | +0.51% |
| intraweek | +840 | +0.40% |
| snake_viper_wild | +795 | +0.38% |
| snake_viper_tick | +779 | +0.38% |
| benchmark | +444 | +0.20% |
| oracle | +412 | +0.20% |
| snake_abs | +13 | +0.01% |
| snake_abs_conv | +11 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -56 | -0.03% |
| snake_abs_exit_conv | -198 | -0.09% |
| snake_anaconda | -560 | -0.27% |
| gold | -2,499 | -1.41% |

Average per day so far: unified Rs +649, benchmark Rs +561, snake_abs_exit Rs +411, intramonth Rs +369, snake_abs_exit_conv Rs +358, intraweek Rs +343, oracle Rs +303, snake_abs_conv Rs +275, snake_viper_wild Rs +270, snake_abs Rs +270, random_hold Rs +216, snake_viper_tick Rs +165, snake_anaconda Rs +120, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.