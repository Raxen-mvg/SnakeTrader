# Paper trading report

Updated 2026-11-19 10:46 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,936 | +11.97% | 0 | - | 236 |
| benchmark | 220,731 | +10.37% | 0 | - | 237 |
| snake_abs_exit | 213,717 | +6.86% | 2 | 50% | 345 |
| intramonth | 213,503 | +6.75% | 0 | - | 235 |
| intraweek | 211,975 | +5.99% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,838 | +5.92% | 2 | 50% | 345 |
| oracle | 211,181 | +5.59% | 0 | - | 233 |
| snake_abs | 209,493 | +4.75% | 1 | 100% | 255 |
| snake_abs_conv | 209,369 | +4.68% | 1 | 100% | 255 |
| random_hold | 207,718 | +3.86% | 10 | 70% | 733 |
| snake_viper_wild | 207,542 | +3.77% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,996 | +2.00% | 15 | 47% | 2,625 |
| snake_anaconda | 203,621 | +1.81% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,425 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,773 | -12.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,350 (-4.32%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,324 | +0.59% |
| intramonth | +1,229 | +0.58% |
| benchmark_smallcap | +1,099 | +0.55% |
| random_hold | +785 | +0.38% |
| snake_viper_wild | +503 | +0.24% |
| snake_viper_tick | +493 | +0.24% |
| benchmark | +436 | +0.20% |
| oracle | +385 | +0.18% |
| intraweek | +135 | +0.06% |
| snake_abs | +57 | +0.03% |
| snake_abs_conv | +44 | +0.02% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -315 | -0.15% |
| snake_abs_exit_conv | -545 | -0.26% |
| snake_anaconda | -780 | -0.38% |
| gold | -2,548 | -1.44% |

Average per day so far: unified Rs +647, benchmark Rs +560, snake_abs_exit Rs +403, intramonth Rs +365, snake_abs_exit_conv Rs +348, intraweek Rs +324, oracle Rs +302, snake_abs_conv Rs +276, snake_abs Rs +271, snake_viper_wild Rs +260, random_hold Rs +209, snake_viper_tick Rs +154, snake_anaconda Rs +113, nifty_calls Rs +50, benchmark_smallcap Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -682

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.