# Paper trading report

Updated 2026-11-11 12:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,647 | +10.32% | 0 | - | 237 |
| unified | 220,616 | +10.31% | 0 | - | 236 |
| snake_abs_exit_conv | 215,840 | +7.92% | 2 | 50% | 345 |
| snake_abs_exit | 214,657 | +7.33% | 2 | 50% | 345 |
| intraweek | 214,138 | +7.07% | 30 | 53% | 3,302 |
| snake_abs | 212,195 | +6.10% | 1 | 100% | 255 |
| snake_abs_conv | 212,037 | +6.02% | 1 | 100% | 255 |
| oracle | 211,970 | +5.99% | 0 | - | 233 |
| intramonth | 211,599 | +5.80% | 0 | - | 235 |
| random_hold | 207,031 | +3.52% | 9 | 67% | 709 |
| snake_viper_wild | 202,650 | +1.32% | 10 | 50% | 1,825 |
| snake_anaconda | 202,527 | +1.26% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,636 | +0.82% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,202 | -0.40% | 9 | 44% | 1,639 |
| gold | 189,996 | -5.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,291 (-4.35%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +5,220 | +2.64% |
| snake_viper_tick | +5,125 | +2.64% |
| snake_abs_exit_conv | +3,931 | +1.85% |
| benchmark_smallcap | +3,464 | +1.75% |
| snake_anaconda | +3,060 | +1.53% |
| snake_abs_exit | +2,673 | +1.26% |
| snake_abs_conv | +2,560 | +1.22% |
| benchmark | +2,555 | +1.17% |
| snake_abs | +2,548 | +1.22% |
| random_hold | +2,070 | +1.01% |
| oracle | +2,051 | +0.98% |
| intramonth | +990 | +0.47% |
| unified | +869 | +0.40% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -404 | -0.19% |
| gold | -2,137 | -1.11% |

Average per day so far: benchmark Rs +666, unified Rs +665, snake_abs_exit_conv Rs +566, snake_abs_exit Rs +523, intraweek Rs +456, snake_abs_conv Rs +430, snake_abs Rs +421, oracle Rs +386, intramonth Rs +374, random_hold Rs +227, snake_viper_wild Rs +115, snake_anaconda Rs +97, benchmark_smallcap Rs +61, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -40, gold Rs -323, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.