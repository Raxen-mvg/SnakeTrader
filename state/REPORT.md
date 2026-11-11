# Paper trading report

Updated 2026-11-11 10:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,221 | +10.61% | 0 | - | 237 |
| unified | 220,969 | +10.48% | 0 | - | 236 |
| snake_abs_exit_conv | 215,985 | +7.99% | 2 | 50% | 345 |
| intraweek | 214,775 | +7.39% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,384 | +7.19% | 2 | 50% | 345 |
| snake_abs | 212,780 | +6.39% | 1 | 100% | 255 |
| snake_abs_conv | 212,624 | +6.31% | 1 | 100% | 255 |
| oracle | 212,155 | +6.08% | 0 | - | 233 |
| intramonth | 211,679 | +5.84% | 0 | - | 235 |
| random_hold | 207,060 | +3.53% | 9 | 67% | 709 |
| snake_anaconda | 202,538 | +1.27% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,726 | +0.86% | 0 | - | 237 |
| snake_viper_wild | 200,215 | +0.11% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,816 | -1.59% | 9 | 44% | 1,639 |
| gold | 189,667 | -5.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,548 (-4.23%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,076 | +1.92% |
| benchmark_smallcap | +3,554 | +1.79% |
| snake_abs_conv | +3,146 | +1.50% |
| snake_abs | +3,134 | +1.50% |
| benchmark | +3,129 | +1.44% |
| snake_anaconda | +3,071 | +1.54% |
| snake_viper_wild | +2,785 | +1.41% |
| snake_viper_tick | +2,740 | +1.41% |
| snake_abs_exit | +2,400 | +1.13% |
| oracle | +2,237 | +1.07% |
| random_hold | +2,100 | +1.02% |
| unified | +1,222 | +0.56% |
| intramonth | +1,070 | +0.51% |
| intraweek | +233 | +0.11% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,466 | -1.28% |

Average per day so far: benchmark Rs +685, unified Rs +676, snake_abs_exit_conv Rs +571, snake_abs_exit Rs +514, intraweek Rs +477, snake_abs_conv Rs +451, snake_abs Rs +441, oracle Rs +392, intramonth Rs +377, random_hold Rs +228, snake_anaconda Rs +98, benchmark_smallcap Rs +64, nifty_calls Rs +59, snake_viper_wild Rs +9, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -159, gold Rs -333, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.