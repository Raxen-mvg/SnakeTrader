# Paper trading report

Updated 2026-11-11 10:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,984 | +10.49% | 0 | - | 237 |
| unified | 220,158 | +10.08% | 0 | - | 236 |
| snake_abs_exit_conv | 216,353 | +8.18% | 2 | 50% | 345 |
| snake_abs_exit | 214,817 | +7.41% | 2 | 50% | 345 |
| intraweek | 214,437 | +7.22% | 30 | 53% | 3,302 |
| snake_abs | 212,979 | +6.49% | 1 | 100% | 255 |
| snake_abs_conv | 212,827 | +6.41% | 1 | 100% | 255 |
| oracle | 211,448 | +5.72% | 0 | - | 233 |
| intramonth | 211,184 | +5.59% | 0 | - | 235 |
| random_hold | 206,341 | +3.17% | 9 | 67% | 709 |
| snake_anaconda | 202,785 | +1.39% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| snake_viper_wild | 200,265 | +0.13% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,866 | -1.57% | 9 | 44% | 1,639 |
| gold | 189,437 | -5.28% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,150 (-4.42%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,445 | +2.10% |
| benchmark_smallcap | +3,453 | +1.74% |
| snake_abs_conv | +3,349 | +1.60% |
| snake_abs | +3,332 | +1.59% |
| snake_anaconda | +3,319 | +1.66% |
| benchmark | +2,892 | +1.33% |
| snake_viper_wild | +2,835 | +1.44% |
| snake_abs_exit | +2,833 | +1.34% |
| snake_viper_tick | +2,790 | +1.44% |
| oracle | +1,530 | +0.73% |
| random_hold | +1,380 | +0.67% |
| intramonth | +575 | +0.27% |
| unified | +411 | +0.19% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -104 | -0.05% |
| gold | -2,696 | -1.40% |

Average per day so far: benchmark Rs +677, unified Rs +650, snake_abs_exit_conv Rs +584, snake_abs_exit Rs +529, intraweek Rs +466, snake_abs_conv Rs +458, snake_abs Rs +448, oracle Rs +369, intramonth Rs +361, random_hold Rs +205, snake_anaconda Rs +107, benchmark_smallcap Rs +60, nifty_calls Rs +59, snake_viper_wild Rs +12, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -157, gold Rs -341, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.