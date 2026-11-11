# Paper trading report

Updated 2026-11-11 14:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,251 | +10.13% | 0 | - | 236 |
| benchmark | 219,767 | +9.88% | 0 | - | 237 |
| snake_abs_exit_conv | 216,630 | +8.31% | 2 | 50% | 345 |
| snake_abs_exit | 215,810 | +7.91% | 2 | 50% | 345 |
| intraweek | 213,392 | +6.70% | 30 | 53% | 3,302 |
| snake_abs | 213,336 | +6.67% | 1 | 100% | 255 |
| snake_abs_conv | 213,167 | +6.58% | 1 | 100% | 255 |
| oracle | 211,621 | +5.81% | 0 | - | 233 |
| intramonth | 211,167 | +5.58% | 0 | - | 235 |
| random_hold | 207,148 | +3.57% | 9 | 67% | 709 |
| snake_viper_wild | 206,298 | +3.15% | 10 | 50% | 1,825 |
| snake_anaconda | 203,524 | +1.76% | 3 | 33% | 374 |
| snake_viper_tick | 202,774 | +1.39% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,390 | +0.69% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,372 | -5.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,084 (-4.46%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,868 | +4.49% |
| snake_viper_tick | +8,697 | +4.48% |
| snake_abs_exit_conv | +4,721 | +2.23% |
| snake_anaconda | +4,058 | +2.03% |
| snake_abs_exit | +3,826 | +1.80% |
| snake_abs_conv | +3,689 | +1.76% |
| snake_abs | +3,689 | +1.76% |
| benchmark_smallcap | +3,217 | +1.62% |
| random_hold | +2,187 | +1.07% |
| oracle | +1,703 | +0.81% |
| benchmark | +1,675 | +0.77% |
| intramonth | +558 | +0.27% |
| unified | +504 | +0.23% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,150 | -0.54% |
| gold | -2,762 | -1.44% |

Average per day so far: unified Rs +653, benchmark Rs +638, snake_abs_exit_conv Rs +594, snake_abs_exit Rs +565, snake_abs_conv Rs +470, snake_abs Rs +460, intraweek Rs +432, oracle Rs +375, intramonth Rs +360, snake_viper_wild Rs +274, random_hold Rs +231, snake_viper_tick Rs +139, snake_anaconda Rs +136, nifty_calls Rs +59, benchmark_smallcap Rs +51, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -343, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.