# Paper trading report

Updated 2026-11-11 15:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,922 | +9.96% | 0 | - | 236 |
| benchmark | 219,324 | +9.66% | 0 | - | 237 |
| snake_abs_exit_conv | 216,697 | +8.35% | 2 | 50% | 345 |
| snake_abs_exit | 215,792 | +7.90% | 2 | 50% | 345 |
| snake_abs | 213,590 | +6.79% | 1 | 100% | 255 |
| snake_abs_conv | 213,418 | +6.71% | 1 | 100% | 255 |
| intraweek | 213,148 | +6.57% | 30 | 53% | 3,302 |
| oracle | 211,687 | +5.84% | 0 | - | 233 |
| intramonth | 211,161 | +5.58% | 0 | - | 235 |
| random_hold | 207,053 | +3.53% | 9 | 67% | 709 |
| snake_viper_wild | 206,194 | +3.10% | 10 | 50% | 1,825 |
| snake_anaconda | 203,715 | +1.86% | 3 | 33% | 374 |
| snake_viper_tick | 202,672 | +1.34% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,165 | +0.58% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,585 | -5.21% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,996 (-4.50%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,764 | +4.44% |
| snake_viper_tick | +8,595 | +4.43% |
| snake_abs_exit_conv | +4,789 | +2.26% |
| snake_anaconda | +4,249 | +2.13% |
| snake_abs | +3,943 | +1.88% |
| snake_abs_conv | +3,941 | +1.88% |
| snake_abs_exit | +3,808 | +1.80% |
| benchmark_smallcap | +2,993 | +1.51% |
| random_hold | +2,092 | +1.02% |
| oracle | +1,768 | +0.84% |
| benchmark | +1,232 | +0.56% |
| intramonth | +552 | +0.26% |
| unified | +175 | +0.08% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,394 | -0.65% |
| gold | -2,548 | -1.33% |

Average per day so far: unified Rs +643, benchmark Rs +623, snake_abs_exit_conv Rs +596, snake_abs_exit Rs +564, snake_abs_conv Rs +479, snake_abs Rs +469, intraweek Rs +424, oracle Rs +377, intramonth Rs +360, snake_viper_wild Rs +269, random_hold Rs +228, snake_anaconda Rs +143, snake_viper_tick Rs +134, nifty_calls Rs +59, benchmark_smallcap Rs +43, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -336, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.