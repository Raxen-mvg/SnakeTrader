# Paper trading report

Updated 2026-11-13 10:55 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,506 | +10.25% | 0 | - | 236 |
| benchmark | 220,035 | +10.02% | 0 | - | 237 |
| snake_abs_exit_conv | 217,200 | +8.60% | 2 | 50% | 345 |
| snake_abs_exit | 217,070 | +8.54% | 2 | 50% | 345 |
| intraweek | 215,988 | +7.99% | 30 | 53% | 3,302 |
| oracle | 213,691 | +6.84% | 0 | - | 233 |
| snake_abs | 213,182 | +6.59% | 1 | 100% | 255 |
| snake_abs_conv | 213,014 | +6.51% | 1 | 100% | 255 |
| intramonth | 211,238 | +5.62% | 0 | - | 235 |
| random_hold | 207,296 | +3.65% | 10 | 70% | 733 |
| snake_viper_wild | 206,636 | +3.32% | 14 | 50% | 2,496 |
| snake_anaconda | 205,121 | +2.56% | 3 | 33% | 374 |
| benchmark_smallcap | 203,688 | +1.84% | 0 | - | 237 |
| snake_viper_tick | 203,102 | +1.55% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,522 | -7.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,107 (-3.95%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +1,344 | +0.65% |
| intraweek | +1,330 | +0.62% |
| snake_viper_tick | +1,321 | +0.65% |
| oracle | +575 | +0.27% |
| benchmark_smallcap | +482 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -191 | -0.09% |
| intramonth | -355 | -0.17% |
| snake_abs_exit | -372 | -0.17% |
| benchmark | -513 | -0.23% |
| random_hold | -758 | -0.36% |
| gold | -789 | -0.43% |
| snake_anaconda | -806 | -0.39% |
| snake_abs_exit_conv | -1,474 | -0.67% |
| snake_abs_conv | -2,521 | -1.17% |
| snake_abs | -2,530 | -1.17% |

Average per day so far: unified Rs +621, benchmark Rs +607, snake_abs_exit_conv Rs +573, snake_abs_exit Rs +569, intraweek Rs +484, snake_abs_conv Rs +434, snake_abs Rs +425, oracle Rs +415, intramonth Rs +341, snake_viper_wild Rs +265, random_hold Rs +221, snake_anaconda Rs +183, snake_viper_tick Rs +141, benchmark_smallcap Rs +127, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -469

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.