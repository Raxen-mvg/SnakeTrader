# Paper trading report

Updated 2026-11-11 11:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,381 | +10.69% | 0 | - | 237 |
| unified | 220,854 | +10.43% | 0 | - | 236 |
| snake_abs_exit_conv | 216,390 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit | 215,203 | +7.60% | 2 | 50% | 345 |
| intraweek | 214,073 | +7.04% | 30 | 53% | 3,302 |
| snake_abs | 212,863 | +6.43% | 1 | 100% | 255 |
| snake_abs_conv | 212,711 | +6.36% | 1 | 100% | 255 |
| oracle | 212,187 | +6.09% | 0 | - | 233 |
| intramonth | 211,890 | +5.95% | 0 | - | 235 |
| random_hold | 206,996 | +3.50% | 9 | 67% | 709 |
| snake_anaconda | 203,097 | +1.55% | 3 | 33% | 374 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,807 | +0.90% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,376 | -0.81% | 9 | 44% | 1,639 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,455 (-4.27%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,482 | +2.12% |
| snake_viper_wild | +4,377 | +2.22% |
| snake_viper_tick | +4,299 | +2.21% |
| benchmark_smallcap | +3,733 | +1.88% |
| snake_anaconda | +3,630 | +1.82% |
| benchmark | +3,289 | +1.51% |
| snake_abs_conv | +3,234 | +1.54% |
| snake_abs_exit | +3,219 | +1.52% |
| snake_abs | +3,216 | +1.53% |
| oracle | +2,269 | +1.08% |
| random_hold | +2,035 | +0.99% |
| intramonth | +1,281 | +0.61% |
| unified | +1,107 | +0.50% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -468 | -0.22% |
| gold | -2,203 | -1.15% |

Average per day so far: benchmark Rs +690, unified Rs +673, snake_abs_exit_conv Rs +585, snake_abs_exit Rs +543, intraweek Rs +454, snake_abs_conv Rs +454, snake_abs Rs +444, oracle Rs +393, intramonth Rs +384, random_hold Rs +226, snake_anaconda Rs +119, snake_viper_wild Rs +79, benchmark_smallcap Rs +71, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -81, gold Rs -325, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.