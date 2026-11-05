# Paper trading report

Updated 2026-11-05 14:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,296 | +8.15% | 0 | - | 236 |
| snake_abs_exit_conv | 214,570 | +7.29% | 1 | 100% | 255 |
| snake_abs_exit | 214,293 | +7.15% | 1 | 100% | 260 |
| benchmark | 214,114 | +7.06% | 0 | - | 237 |
| snake_abs | 211,462 | +5.73% | 1 | 100% | 255 |
| snake_abs_conv | 211,314 | +5.66% | 1 | 100% | 255 |
| intraweek | 209,555 | +4.78% | 25 | 48% | 2,757 |
| intramonth | 208,250 | +4.12% | 0 | - | 235 |
| snake_viper_wild | 205,437 | +2.72% | 3 | 33% | 702 |
| random_hold | 204,666 | +2.33% | 8 | 62% | 649 |
| oracle | 204,464 | +2.23% | 0 | - | 233 |
| snake_anaconda | 202,218 | +1.11% | 3 | 33% | 374 |
| snake_viper_tick | 201,906 | +0.95% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,192 | -0.40% | 0 | - | 237 |
| gold | 194,205 | -2.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,536 (-5.23%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,355 | +2.56% |
| gold | +2,811 | +1.47% |
| oracle | +2,672 | +1.32% |
| benchmark_smallcap | +2,522 | +1.28% |
| unified | +1,856 | +0.87% |
| random_hold | +1,357 | +0.67% |
| intramonth | +1,234 | +0.60% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -143 | -0.07% |
| snake_abs | -441 | -0.21% |
| snake_abs_conv | -445 | -0.21% |
| snake_abs_exit_conv | -445 | -0.21% |
| snake_abs_exit | -607 | -0.28% |
| snake_anaconda | -1,602 | -0.79% |
| snake_viper_tick | -3,494 | -1.70% |
| snake_viper_wild | -3,593 | -1.72% |

Average per day so far: snake_abs_exit_conv Rs +583, unified Rs +582, snake_abs_exit Rs +572, benchmark Rs +504, snake_abs_conv Rs +453, snake_abs Rs +441, intraweek Rs +341, intramonth Rs +295, snake_viper_wild Rs +272, random_hold Rs +167, oracle Rs +159, snake_viper_tick Rs +112, snake_anaconda Rs +96, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -34, gold Rs -207, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.