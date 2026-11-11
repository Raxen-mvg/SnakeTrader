# Paper trading report

Updated 2026-11-11 10:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,137 | +10.57% | 0 | - | 237 |
| unified | 220,708 | +10.35% | 0 | - | 236 |
| snake_abs_exit_conv | 215,970 | +7.99% | 2 | 50% | 345 |
| intraweek | 214,632 | +7.32% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,389 | +7.19% | 2 | 50% | 345 |
| snake_abs | 212,824 | +6.41% | 1 | 100% | 255 |
| snake_abs_conv | 212,666 | +6.33% | 1 | 100% | 255 |
| oracle | 211,941 | +5.97% | 0 | - | 233 |
| intramonth | 211,473 | +5.74% | 0 | - | 235 |
| random_hold | 206,778 | +3.39% | 9 | 67% | 709 |
| snake_anaconda | 202,488 | +1.24% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,569 | +0.78% | 0 | - | 237 |
| snake_viper_wild | 200,207 | +0.10% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,809 | -1.59% | 9 | 44% | 1,639 |
| gold | 189,651 | -5.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,397 (-4.30%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,061 | +1.92% |
| benchmark_smallcap | +3,397 | +1.71% |
| snake_abs_conv | +3,188 | +1.52% |
| snake_abs | +3,177 | +1.51% |
| benchmark | +3,045 | +1.40% |
| snake_anaconda | +3,021 | +1.51% |
| snake_viper_wild | +2,777 | +1.41% |
| snake_viper_tick | +2,732 | +1.41% |
| snake_abs_exit | +2,405 | +1.14% |
| oracle | +2,023 | +0.96% |
| random_hold | +1,817 | +0.89% |
| unified | +961 | +0.44% |
| intramonth | +864 | +0.41% |
| intraweek | +90 | +0.04% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,482 | -1.29% |

Average per day so far: benchmark Rs +682, unified Rs +668, snake_abs_exit_conv Rs +570, snake_abs_exit Rs +514, intraweek Rs +472, snake_abs_conv Rs +452, snake_abs Rs +442, oracle Rs +385, intramonth Rs +370, random_hold Rs +219, snake_anaconda Rs +96, nifty_calls Rs +59, benchmark_smallcap Rs +58, snake_viper_wild Rs +9, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -160, gold Rs -334, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.