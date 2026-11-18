# Paper trading report

Updated 2026-11-18 09:45 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,736 | +10.87% | 0 | - | 236 |
| benchmark | 220,035 | +10.02% | 0 | - | 237 |
| intraweek | 212,842 | +6.42% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,690 | +6.34% | 2 | 50% | 345 |
| oracle | 211,487 | +5.74% | 0 | - | 233 |
| intramonth | 211,485 | +5.74% | 0 | - | 235 |
| snake_abs_exit_conv | 211,254 | +5.63% | 2 | 50% | 345 |
| snake_abs | 208,702 | +4.35% | 1 | 100% | 255 |
| snake_abs_conv | 208,563 | +4.28% | 1 | 100% | 255 |
| random_hold | 206,837 | +3.42% | 10 | 70% | 733 |
| snake_viper_wild | 206,719 | +3.36% | 16 | 50% | 2,827 |
| snake_anaconda | 203,508 | +1.75% | 3 | 33% | 374 |
| snake_viper_tick | 203,190 | +1.59% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,405 | -0.30% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,074 | -11.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,648 (-4.68%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +298 | +0.13% |
| snake_abs_conv | +143 | +0.07% |
| snake_abs | +143 | +0.07% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intramonth | -57 | -0.03% |
| snake_abs_exit_conv | -320 | -0.15% |
| snake_abs_exit | -452 | -0.21% |
| intraweek | -480 | -0.23% |
| snake_anaconda | -547 | -0.27% |
| oracle | -1,000 | -0.47% |
| benchmark_smallcap | -1,166 | -0.58% |
| benchmark | -1,568 | -0.71% |
| random_hold | -1,595 | -0.77% |
| snake_viper_tick | -2,647 | -1.29% |
| snake_viper_wild | -2,696 | -1.29% |
| gold | -3,650 | -2.02% |

Average per day so far: unified Rs +604, benchmark Rs +557, snake_abs_exit Rs +385, intraweek Rs +357, snake_abs_exit_conv Rs +341, oracle Rs +319, intramonth Rs +319, snake_abs_conv Rs +259, snake_abs Rs +256, snake_viper_wild Rs +240, random_hold Rs +190, snake_viper_tick Rs +128, snake_anaconda Rs +113, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -19, snake_nonews Rs -326, snake Rs -347, gold Rs -637

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.