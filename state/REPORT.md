# Paper trading report

Updated 2026-11-11 10:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,098 | +10.55% | 0 | - | 237 |
| unified | 220,977 | +10.49% | 0 | - | 236 |
| snake_abs_exit_conv | 215,781 | +7.89% | 2 | 50% | 345 |
| snake_abs_exit | 214,402 | +7.20% | 2 | 50% | 345 |
| intraweek | 214,271 | +7.13% | 30 | 53% | 3,302 |
| snake_abs | 212,816 | +6.41% | 1 | 100% | 255 |
| snake_abs_conv | 212,660 | +6.33% | 1 | 100% | 255 |
| oracle | 211,859 | +5.93% | 0 | - | 233 |
| intramonth | 211,664 | +5.83% | 0 | - | 235 |
| random_hold | 206,797 | +3.40% | 9 | 67% | 709 |
| snake_anaconda | 202,506 | +1.25% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| snake_viper_wild | 200,058 | +0.03% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,662 | -1.67% | 9 | 44% | 1,639 |
| gold | 189,585 | -5.21% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,387 (-4.31%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +3,872 | +1.83% |
| benchmark_smallcap | +3,453 | +1.74% |
| snake_abs_conv | +3,182 | +1.52% |
| snake_abs | +3,169 | +1.51% |
| snake_anaconda | +3,040 | +1.52% |
| benchmark | +3,006 | +1.38% |
| snake_viper_wild | +2,627 | +1.33% |
| snake_viper_tick | +2,586 | +1.33% |
| snake_abs_exit | +2,418 | +1.14% |
| oracle | +1,940 | +0.92% |
| random_hold | +1,836 | +0.90% |
| unified | +1,230 | +0.56% |
| intramonth | +1,055 | +0.50% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -271 | -0.13% |
| gold | -2,548 | -1.33% |

Average per day so far: benchmark Rs +681, unified Rs +677, snake_abs_exit_conv Rs +564, snake_abs_exit Rs +514, intraweek Rs +460, snake_abs_conv Rs +452, snake_abs Rs +442, oracle Rs +383, intramonth Rs +376, random_hold Rs +219, snake_anaconda Rs +96, benchmark_smallcap Rs +60, nifty_calls Rs +59, snake_viper_wild Rs +2, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -167, gold Rs -336, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.