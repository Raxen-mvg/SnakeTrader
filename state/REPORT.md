# Paper trading report

Updated 2026-11-19 12:08 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,756 | +11.88% | 0 | - | 236 |
| benchmark | 221,450 | +10.72% | 0 | - | 237 |
| intramonth | 213,403 | +6.70% | 0 | - | 235 |
| snake_abs_exit | 213,333 | +6.67% | 2 | 50% | 345 |
| intraweek | 211,569 | +5.79% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,491 | +5.75% | 2 | 50% | 345 |
| oracle | 211,030 | +5.51% | 0 | - | 233 |
| snake_abs | 208,981 | +4.49% | 1 | 100% | 255 |
| snake_abs_conv | 208,855 | +4.43% | 1 | 100% | 255 |
| random_hold | 207,620 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,576 | +3.79% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,029 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 203,244 | +1.62% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,414 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,904 | -12.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,183 (-4.41%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,155 | +0.52% |
| unified | +1,144 | +0.51% |
| intramonth | +1,129 | +0.53% |
| benchmark_smallcap | +1,087 | +0.55% |
| random_hold | +687 | +0.33% |
| snake_viper_wild | +536 | +0.26% |
| snake_viper_tick | +525 | +0.26% |
| oracle | +234 | +0.11% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -270 | -0.13% |
| snake_abs | -455 | -0.22% |
| snake_abs_conv | -470 | -0.22% |
| snake_abs_exit | -698 | -0.33% |
| snake_abs_exit_conv | -892 | -0.42% |
| snake_anaconda | -1,157 | -0.57% |
| gold | -2,417 | -1.36% |

Average per day so far: unified Rs +642, benchmark Rs +580, snake_abs_exit Rs +392, intramonth Rs +362, snake_abs_exit_conv Rs +338, intraweek Rs +313, oracle Rs +298, snake_viper_wild Rs +261, snake_abs_conv Rs +260, snake_abs Rs +257, random_hold Rs +206, snake_viper_tick Rs +155, snake_anaconda Rs +101, nifty_calls Rs +50, benchmark_smallcap Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.