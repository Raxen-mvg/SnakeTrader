# Paper trading report

Updated 2026-11-25 10:42 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,235 | +12.62% | 0 | - | 236 |
| benchmark | 225,229 | +12.62% | 0 | - | 237 |
| intramonth | 213,020 | +6.51% | 0 | - | 235 |
| oracle | 212,018 | +6.01% | 0 | - | 233 |
| random_hold | 209,425 | +4.71% | 12 | 75% | 1,009 |
| intraweek | 207,576 | +3.79% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,939 | +0.97% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,339 | +0.67% | 2 | 50% | 345 |
| snake_abs | 200,798 | +0.40% | 1 | 100% | 255 |
| snake_abs_conv | 200,608 | +0.30% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_viper_wild | 195,546 | -2.23% | 16 | 50% | 2,827 |
| snake_anaconda | 193,294 | -3.35% | 3 | 33% | 374 |
| snake_viper_tick | 192,222 | -3.89% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,566 | -17.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,189 (-5.41%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,756 | +1.70% |
| random_hold | +999 | +0.48% |
| unified | +950 | +0.42% |
| benchmark_smallcap | +348 | +0.17% |
| intramonth | +268 | +0.13% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -324 | -0.15% |
| gold | -3,863 | -2.28% |
| intraweek | -4,043 | -1.91% |
| snake_abs | -4,662 | -2.27% |
| snake_abs_conv | -4,695 | -2.29% |
| snake_anaconda | -5,409 | -2.72% |
| snake_viper_tick | -5,471 | -2.77% |
| snake_abs_exit | -5,556 | -2.68% |
| snake_viper_wild | -5,578 | -2.77% |
| snake_abs_exit_conv | -5,707 | -2.76% |

Average per day so far: unified Rs +631, benchmark Rs +631, intramonth Rs +325, oracle Rs +300, random_hold Rs +236, intraweek Rs +189, snake_abs_exit Rs +52, nifty_calls Rs +46, snake_abs_exit_conv Rs +36, snake_abs Rs +21, snake_abs_conv Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -19, snake_viper_wild Rs -139, snake_anaconda Rs -192, snake_viper_tick Rs -268, snake_nonews Rs -292, snake Rs -311, gold Rs -861

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.