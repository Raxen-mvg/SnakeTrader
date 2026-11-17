# Paper trading report

Updated 2026-11-17 09:39 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,111 | +11.56% | 0 | - | 236 |
| benchmark | 220,854 | +10.43% | 0 | - | 237 |
| snake_abs_exit | 214,708 | +7.35% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,755 | +6.88% | 2 | 50% | 345 |
| intramonth | 213,328 | +6.66% | 0 | - | 235 |
| intraweek | 212,842 | +6.42% | 35 | 54% | 3,851 |
| oracle | 212,805 | +6.40% | 0 | - | 233 |
| snake_abs | 210,525 | +5.26% | 1 | 100% | 255 |
| snake_abs_conv | 210,376 | +5.19% | 1 | 100% | 255 |
| random_hold | 207,986 | +3.99% | 10 | 70% | 733 |
| snake_viper_wild | 206,650 | +3.33% | 14 | 50% | 2,496 |
| snake_anaconda | 205,817 | +2.91% | 3 | 33% | 374 |
| snake_viper_tick | 203,117 | +1.56% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,129 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,250 | -9.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,876 (-4.06%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,709 | +0.81% |
| unified | +1,673 | +0.76% |
| intraweek | +1,576 | +0.75% |
| benchmark_smallcap | +1,300 | +0.65% |
| oracle | +782 | +0.37% |
| benchmark | +773 | +0.35% |
| snake_anaconda | +715 | +0.35% |
| snake_abs_exit_conv | +537 | +0.25% |
| snake_viper_wild | +506 | +0.24% |
| snake_viper_tick | +497 | +0.24% |
| snake_abs | +391 | +0.19% |
| snake_abs_conv | +387 | +0.18% |
| snake_abs_exit | +299 | +0.14% |
| gold | +296 | +0.16% |
| random_hold | +193 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +660, benchmark Rs +596, snake_abs_exit Rs +460, snake_abs_exit_conv Rs +430, intramonth Rs +381, intraweek Rs +367, oracle Rs +366, snake_abs_conv Rs +324, snake_abs Rs +319, snake_viper_wild Rs +246, random_hold Rs +228, snake_anaconda Rs +194, snake_viper_tick Rs +130, benchmark_smallcap Rs +69, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -536

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.