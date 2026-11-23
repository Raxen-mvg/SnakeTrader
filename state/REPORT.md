# Paper trading report

Updated 2026-11-23 09:45 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,431 | +12.71% | 0 | - | 236 |
| benchmark | 223,921 | +11.96% | 0 | - | 237 |
| intraweek | 213,739 | +6.87% | 40 | 55% | 4,400 |
| intramonth | 213,181 | +6.59% | 0 | - | 235 |
| oracle | 211,956 | +5.98% | 0 | - | 233 |
| random_hold | 210,870 | +5.43% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,355 | +4.18% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,862 | +3.43% | 2 | 50% | 345 |
| snake_abs | 205,536 | +2.77% | 1 | 100% | 255 |
| snake_abs_conv | 205,393 | +2.70% | 1 | 100% | 255 |
| snake_viper_wild | 203,832 | +1.92% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,354 | +0.18% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,798 | -0.10% | 0 | - | 237 |
| snake_anaconda | 199,683 | -0.16% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,183 | -15.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,210 (-4.39%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,134 | +0.68% |
| snake_viper_wild | +1,003 | +0.49% |
| snake_viper_tick | +982 | +0.49% |
| snake_abs_exit_conv | +245 | +0.12% |
| random_hold | +111 | +0.05% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -207 | -0.10% |
| snake_anaconda | -223 | -0.11% |
| snake_abs | -384 | -0.19% |
| snake_abs_conv | -390 | -0.19% |
| oracle | -522 | -0.25% |
| unified | -751 | -0.33% |
| benchmark_smallcap | -1,110 | -0.55% |
| benchmark | -1,216 | -0.54% |
| intramonth | -1,823 | -0.85% |
| intraweek | -1,973 | -0.92% |

Average per day so far: unified Rs +652, benchmark Rs +613, intraweek Rs +352, intramonth Rs +338, oracle Rs +307, random_hold Rs +279, snake_abs_exit Rs +232, snake_abs_exit_conv Rs +191, snake_abs_conv Rs +150, snake_abs Rs +150, snake_viper_wild Rs +124, nifty_calls Rs +47, snake_viper_tick Rs +13, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -6, snake_anaconda Rs -9, snake_nonews Rs -300, snake Rs -320, gold Rs -790

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.