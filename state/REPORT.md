# Paper trading report

Updated 2026-11-13 14:22 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,455 | +10.23% | 0 | - | 236 |
| benchmark | 218,880 | +9.44% | 0 | - | 237 |
| snake_abs_exit | 216,059 | +8.03% | 2 | 50% | 345 |
| snake_abs_exit_conv | 215,921 | +7.96% | 2 | 50% | 345 |
| intraweek | 215,752 | +7.88% | 30 | 53% | 3,302 |
| oracle | 212,883 | +6.44% | 0 | - | 233 |
| snake_abs | 212,061 | +6.03% | 1 | 100% | 255 |
| snake_abs_conv | 211,890 | +5.95% | 1 | 100% | 255 |
| intramonth | 210,884 | +5.44% | 0 | - | 235 |
| random_hold | 207,000 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 205,139 | +2.57% | 14 | 50% | 2,496 |
| snake_anaconda | 204,198 | +2.10% | 3 | 33% | 374 |
| benchmark_smallcap | 202,152 | +1.08% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,631 | +0.81% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,695 (-4.15%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,094 | +0.51% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -151 | -0.07% |
| snake_viper_wild | -153 | -0.07% |
| oracle | -233 | -0.11% |
| unified | -242 | -0.11% |
| intramonth | -709 | -0.34% |
| random_hold | -1,054 | -0.51% |
| benchmark_smallcap | -1,054 | -0.52% |
| snake_abs_exit | -1,384 | -0.64% |
| gold | -1,480 | -0.80% |
| benchmark | -1,668 | -0.76% |
| snake_anaconda | -1,730 | -0.84% |
| snake_abs_exit_conv | -2,753 | -1.26% |
| snake_abs_conv | -3,645 | -1.69% |
| snake_abs | -3,651 | -1.69% |

Average per day so far: unified Rs +620, benchmark Rs +572, snake_abs_exit Rs +535, snake_abs_exit_conv Rs +531, intraweek Rs +477, snake_abs_conv Rs +396, oracle Rs +390, snake_abs Rs +389, intramonth Rs +330, random_hold Rs +212, snake_viper_wild Rs +206, snake_anaconda Rs +150, benchmark_smallcap Rs +74, snake_viper_tick Rs +74, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.