# Paper trading report

Updated 2026-11-17 10:31 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,197 | +11.10% | 0 | - | 236 |
| benchmark | 221,496 | +10.75% | 0 | - | 237 |
| snake_abs_exit | 215,361 | +7.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,684 | +6.84% | 2 | 50% | 345 |
| intraweek | 213,639 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,600 | +6.30% | 0 | - | 233 |
| intramonth | 212,183 | +6.09% | 0 | - | 235 |
| snake_abs | 210,342 | +5.17% | 1 | 100% | 255 |
| snake_abs_conv | 210,191 | +5.10% | 1 | 100% | 255 |
| random_hold | 208,535 | +4.27% | 10 | 70% | 733 |
| snake_viper_wild | 206,994 | +3.50% | 14 | 50% | 2,496 |
| snake_anaconda | 205,788 | +2.89% | 3 | 33% | 374 |
| snake_viper_tick | 203,455 | +1.73% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,062 | +1.03% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,464 | -9.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,580 (-4.21%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,373 | +1.12% |
| benchmark | +1,415 | +0.64% |
| benchmark_smallcap | +1,233 | +0.61% |
| snake_abs_exit | +952 | +0.44% |
| snake_viper_wild | +850 | +0.41% |
| snake_viper_tick | +835 | +0.41% |
| unified | +759 | +0.34% |
| random_hold | +742 | +0.36% |
| snake_anaconda | +685 | +0.33% |
| oracle | +577 | +0.27% |
| intramonth | +564 | +0.27% |
| gold | +510 | +0.28% |
| snake_abs_exit_conv | +466 | +0.22% |
| snake_abs | +208 | +0.10% |
| snake_abs_conv | +202 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +634, benchmark Rs +614, snake_abs_exit Rs +480, snake_abs_exit_conv Rs +428, intraweek Rs +390, oracle Rs +360, intramonth Rs +348, snake_abs_conv Rs +318, snake_abs Rs +313, snake_viper_wild Rs +259, random_hold Rs +244, snake_anaconda Rs +193, snake_viper_tick Rs +144, benchmark_smallcap Rs +67, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -530

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.