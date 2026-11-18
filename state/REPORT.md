# Paper trading report

Updated 2026-11-18 13:16 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,008 | +11.50% | 0 | - | 236 |
| benchmark | 219,798 | +9.90% | 0 | - | 237 |
| intramonth | 212,890 | +6.45% | 0 | - | 235 |
| snake_abs_exit | 212,562 | +6.28% | 2 | 50% | 345 |
| intraweek | 212,539 | +6.27% | 35 | 54% | 3,851 |
| oracle | 212,005 | +6.00% | 0 | - | 233 |
| snake_abs_exit_conv | 210,838 | +5.42% | 2 | 50% | 345 |
| snake_abs | 207,813 | +3.91% | 1 | 100% | 255 |
| snake_abs_conv | 207,678 | +3.84% | 1 | 100% | 255 |
| random_hold | 207,037 | +3.52% | 10 | 70% | 733 |
| snake_viper_wild | 206,675 | +3.34% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,146 | +1.57% | 15 | 47% | 2,625 |
| snake_anaconda | 202,950 | +1.48% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,844 | -11.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,179 (-4.41%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,569 | +0.71% |
| intramonth | +1,348 | +0.64% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -481 | -0.23% |
| snake_abs_exit | -580 | -0.27% |
| snake_abs_exit_conv | -735 | -0.35% |
| snake_abs_conv | -742 | -0.36% |
| snake_abs | -746 | -0.36% |
| intraweek | -784 | -0.37% |
| snake_anaconda | -1,105 | -0.54% |
| benchmark_smallcap | -1,390 | -0.69% |
| random_hold | -1,396 | -0.67% |
| benchmark | -1,805 | -0.81% |
| snake_viper_tick | -2,691 | -1.31% |
| snake_viper_wild | -2,740 | -1.31% |
| gold | -3,880 | -2.15% |

Average per day so far: unified Rs +639, benchmark Rs +550, snake_abs_exit Rs +381, intramonth Rs +358, intraweek Rs +348, oracle Rs +333, snake_abs_exit_conv Rs +328, snake_viper_wild Rs +238, snake_abs_conv Rs +233, snake_abs Rs +230, random_hold Rs +195, snake_viper_tick Rs +126, snake_anaconda Rs +95, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -643

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.