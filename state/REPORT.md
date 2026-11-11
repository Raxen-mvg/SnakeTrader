# Paper trading report

Updated 2026-11-11 10:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,259 | +10.63% | 0 | - | 237 |
| unified | 220,739 | +10.37% | 0 | - | 236 |
| snake_abs_exit_conv | 215,962 | +7.98% | 2 | 50% | 345 |
| intraweek | 214,663 | +7.33% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,504 | +7.25% | 2 | 50% | 345 |
| snake_abs | 212,492 | +6.25% | 1 | 100% | 255 |
| snake_abs_conv | 212,339 | +6.17% | 1 | 100% | 255 |
| oracle | 212,163 | +6.08% | 0 | - | 233 |
| intramonth | 211,587 | +5.79% | 0 | - | 235 |
| random_hold | 206,847 | +3.42% | 9 | 67% | 709 |
| snake_anaconda | 202,472 | +1.24% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,748 | +0.87% | 0 | - | 237 |
| snake_viper_wild | 200,898 | +0.45% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,485 | -1.26% | 9 | 44% | 1,639 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,444 (-4.28%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,053 | +1.91% |
| benchmark_smallcap | +3,576 | +1.80% |
| snake_viper_wild | +3,468 | +1.76% |
| snake_viper_tick | +3,409 | +1.76% |
| benchmark | +3,167 | +1.45% |
| snake_anaconda | +3,006 | +1.51% |
| snake_abs_conv | +2,861 | +1.37% |
| snake_abs | +2,845 | +1.36% |
| snake_abs_exit | +2,520 | +1.19% |
| oracle | +2,244 | +1.07% |
| random_hold | +1,887 | +0.92% |
| unified | +992 | +0.45% |
| intramonth | +978 | +0.46% |
| intraweek | +121 | +0.06% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,318 | -1.21% |

Average per day so far: benchmark Rs +686, unified Rs +669, snake_abs_exit_conv Rs +570, snake_abs_exit Rs +518, intraweek Rs +473, snake_abs_conv Rs +441, snake_abs Rs +431, oracle Rs +392, intramonth Rs +374, random_hold Rs +221, snake_anaconda Rs +95, benchmark_smallcap Rs +65, nifty_calls Rs +59, snake_viper_wild Rs +39, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -126, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.