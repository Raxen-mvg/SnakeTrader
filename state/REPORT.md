# Paper trading report

Updated 2026-11-11 13:45 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,431 | +10.22% | 0 | - | 236 |
| benchmark | 220,058 | +10.03% | 0 | - | 237 |
| snake_abs_exit_conv | 217,676 | +8.84% | 2 | 50% | 345 |
| snake_abs_exit | 216,645 | +8.32% | 2 | 50% | 345 |
| snake_abs | 214,213 | +7.11% | 1 | 100% | 255 |
| snake_abs_conv | 214,057 | +7.03% | 1 | 100% | 255 |
| intraweek | 213,379 | +6.69% | 30 | 53% | 3,302 |
| oracle | 211,767 | +5.88% | 0 | - | 233 |
| intramonth | 211,352 | +5.68% | 0 | - | 235 |
| random_hold | 207,019 | +3.51% | 9 | 67% | 709 |
| snake_viper_wild | 205,014 | +2.51% | 10 | 50% | 1,825 |
| snake_anaconda | 204,465 | +2.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,517 | +0.76% | 9 | 44% | 1,639 |
| benchmark_smallcap | 200,975 | +0.49% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,766 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,247 (-4.38%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,584 | +3.84% |
| snake_viper_tick | +7,440 | +3.83% |
| snake_abs_exit_conv | +5,767 | +2.72% |
| snake_anaconda | +4,999 | +2.51% |
| snake_abs_exit | +4,661 | +2.20% |
| snake_abs_conv | +4,579 | +2.19% |
| snake_abs | +4,566 | +2.18% |
| benchmark_smallcap | +2,802 | +1.41% |
| random_hold | +2,058 | +1.00% |
| benchmark | +1,966 | +0.90% |
| oracle | +1,849 | +0.88% |
| intramonth | +743 | +0.35% |
| unified | +684 | +0.31% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,163 | -0.54% |
| gold | -2,367 | -1.23% |

Average per day so far: unified Rs +659, benchmark Rs +647, snake_abs_exit_conv Rs +631, snake_abs_exit Rs +594, snake_abs_conv Rs +502, snake_abs Rs +490, intraweek Rs +432, oracle Rs +380, intramonth Rs +366, random_hold Rs +226, snake_viper_wild Rs +218, snake_anaconda Rs +172, snake_viper_tick Rs +76, nifty_calls Rs +59, benchmark_smallcap Rs +36, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -330, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.