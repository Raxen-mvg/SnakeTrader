# Paper trading report

Updated 2026-11-20 10:59 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,946 | +12.47% | 0 | - | 236 |
| benchmark | 223,019 | +11.51% | 0 | - | 237 |
| intramonth | 213,980 | +6.99% | 0 | - | 235 |
| intraweek | 213,687 | +6.84% | 35 | 54% | 3,851 |
| oracle | 212,779 | +6.39% | 0 | - | 233 |
| snake_abs_exit | 210,628 | +5.31% | 2 | 50% | 345 |
| random_hold | 209,053 | +4.53% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,271 | +4.13% | 2 | 50% | 345 |
| snake_abs | 207,448 | +3.72% | 1 | 100% | 255 |
| snake_abs_conv | 207,308 | +3.65% | 1 | 100% | 255 |
| snake_viper_wild | 206,738 | +3.37% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,209 | +1.60% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,506 | +0.75% | 3 | 33% | 374 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,139 | -17.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,710 (-4.15%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +798 | +0.38% |
| oracle | +690 | +0.33% |
| benchmark | +643 | +0.29% |
| random_hold | +600 | +0.29% |
| unified | +331 | +0.15% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intramonth | -28 | -0.01% |
| snake_viper_tick | -768 | -0.38% |
| snake_viper_wild | -785 | -0.38% |
| benchmark_smallcap | -1,244 | -0.62% |
| snake_abs | -1,532 | -0.73% |
| snake_abs_conv | -1,552 | -0.74% |
| snake_anaconda | -1,957 | -0.96% |
| snake_abs_exit | -2,723 | -1.28% |
| snake_abs_exit_conv | -2,794 | -1.32% |
| gold | -9,634 | -5.51% |

Average per day so far: unified Rs +656, benchmark Rs +606, intramonth Rs +368, intraweek Rs +360, oracle Rs +336, snake_abs_exit Rs +304, random_hold Rs +238, snake_abs_exit_conv Rs +236, snake_viper_wild Rs +225, snake_abs_conv Rs +209, snake_abs Rs +207, snake_viper_tick Rs +119, nifty_calls Rs +48, snake_anaconda Rs +46, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -917

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.