# Paper trading report

Updated 2026-11-20 11:55 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,219 | +13.11% | 0 | - | 236 |
| benchmark | 223,133 | +11.57% | 0 | - | 237 |
| intramonth | 215,140 | +7.57% | 0 | - | 235 |
| intraweek | 213,956 | +6.98% | 35 | 54% | 3,851 |
| oracle | 213,054 | +6.53% | 0 | - | 233 |
| snake_abs_exit | 209,817 | +4.91% | 2 | 50% | 345 |
| random_hold | 208,773 | +4.39% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,845 | +3.92% | 2 | 50% | 345 |
| snake_abs | 206,890 | +3.44% | 1 | 100% | 255 |
| snake_abs_conv | 206,756 | +3.38% | 1 | 100% | 255 |
| snake_viper_wild | 205,954 | +2.98% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,439 | +1.22% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,366 | +0.68% | 3 | 33% | 374 |
| benchmark_smallcap | 200,694 | +0.35% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,767 | -16.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,017 (-3.99%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,604 | +0.71% |
| intramonth | +1,132 | +0.53% |
| intraweek | +1,067 | +0.50% |
| oracle | +965 | +0.46% |
| benchmark | +757 | +0.34% |
| random_hold | +320 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -773 | -0.38% |
| snake_viper_tick | -1,538 | -0.75% |
| snake_viper_wild | -1,569 | -0.76% |
| snake_abs | -2,090 | -1.00% |
| snake_anaconda | -2,098 | -1.03% |
| snake_abs_conv | -2,104 | -1.01% |
| snake_abs_exit_conv | -3,219 | -1.52% |
| snake_abs_exit | -3,534 | -1.66% |
| gold | -8,006 | -4.58% |

Average per day so far: unified Rs +690, benchmark Rs +609, intramonth Rs +398, intraweek Rs +367, oracle Rs +344, snake_abs_exit Rs +280, random_hold Rs +231, snake_abs_exit_conv Rs +224, snake_viper_wild Rs +198, snake_abs_conv Rs +193, snake_abs Rs +191, snake_viper_tick Rs +90, nifty_calls Rs +48, snake_anaconda Rs +41, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -875

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.