# Paper trading report

Updated 2026-11-11 15:14 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,783 | +9.89% | 0 | - | 236 |
| benchmark | 219,163 | +9.58% | 0 | - | 237 |
| snake_abs_exit_conv | 216,925 | +8.46% | 2 | 50% | 345 |
| snake_abs_exit | 216,001 | +8.00% | 2 | 50% | 345 |
| snake_abs | 213,688 | +6.84% | 1 | 100% | 255 |
| snake_abs_conv | 213,520 | +6.76% | 1 | 100% | 255 |
| intraweek | 213,093 | +6.55% | 30 | 53% | 3,302 |
| oracle | 211,990 | +6.00% | 0 | - | 233 |
| intramonth | 211,096 | +5.55% | 0 | - | 235 |
| random_hold | 206,989 | +3.50% | 9 | 67% | 709 |
| snake_viper_wild | 206,310 | +3.15% | 10 | 50% | 1,825 |
| snake_anaconda | 203,947 | +1.97% | 3 | 33% | 374 |
| snake_viper_tick | 202,786 | +1.39% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,493 | +0.25% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,651 | -5.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,003 (-4.50%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,880 | +4.50% |
| snake_viper_tick | +8,709 | +4.49% |
| snake_abs_exit_conv | +5,016 | +2.37% |
| snake_anaconda | +4,481 | +2.25% |
| snake_abs_conv | +4,042 | +1.93% |
| snake_abs | +4,042 | +1.93% |
| snake_abs_exit | +4,018 | +1.90% |
| benchmark_smallcap | +2,320 | +1.17% |
| oracle | +2,071 | +0.99% |
| random_hold | +2,028 | +0.99% |
| benchmark | +1,071 | +0.49% |
| intramonth | +487 | +0.23% |
| unified | +36 | +0.02% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,449 | -0.68% |
| gold | -2,482 | -1.29% |

Average per day so far: unified Rs +638, benchmark Rs +618, snake_abs_exit_conv Rs +604, snake_abs_exit Rs +571, snake_abs_conv Rs +483, snake_abs Rs +472, intraweek Rs +422, oracle Rs +387, intramonth Rs +358, snake_viper_wild Rs +274, random_hold Rs +225, snake_anaconda Rs +152, snake_viper_tick Rs +139, nifty_calls Rs +59, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -334, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.