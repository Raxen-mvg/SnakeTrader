# Paper trading report

Updated 2026-11-11 09:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,489 | +10.74% | 0 | - | 237 |
| unified | 220,424 | +10.21% | 0 | - | 236 |
| snake_abs_exit_conv | 216,163 | +8.08% | 2 | 50% | 345 |
| snake_abs_exit | 214,744 | +7.37% | 2 | 50% | 345 |
| intraweek | 214,726 | +7.36% | 30 | 53% | 3,302 |
| snake_abs | 213,105 | +6.55% | 1 | 100% | 255 |
| snake_abs_conv | 212,945 | +6.47% | 1 | 100% | 255 |
| oracle | 211,238 | +5.62% | 0 | - | 233 |
| intramonth | 210,923 | +5.46% | 0 | - | 235 |
| random_hold | 205,951 | +2.98% | 9 | 67% | 709 |
| snake_anaconda | 202,808 | +1.40% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,053 | +0.53% | 0 | - | 237 |
| snake_viper_wild | 200,340 | +0.17% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,939 | -1.53% | 9 | 44% | 1,639 |
| gold | 189,388 | -5.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,158 (-4.42%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,254 | +2.01% |
| snake_abs_conv | +3,468 | +1.66% |
| snake_abs | +3,459 | +1.65% |
| benchmark | +3,397 | +1.56% |
| snake_anaconda | +3,342 | +1.68% |
| snake_viper_wild | +2,910 | +1.47% |
| benchmark_smallcap | +2,881 | +1.45% |
| snake_viper_tick | +2,862 | +1.48% |
| snake_abs_exit | +2,760 | +1.30% |
| oracle | +1,320 | +0.63% |
| random_hold | +991 | +0.48% |
| unified | +677 | +0.31% |
| intramonth | +314 | +0.15% |
| intraweek | +185 | +0.09% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,745 | -1.43% |

Average per day so far: benchmark Rs +693, unified Rs +659, snake_abs_exit_conv Rs +577, snake_abs_exit Rs +527, intraweek Rs +475, snake_abs_conv Rs +462, snake_abs Rs +452, oracle Rs +363, intramonth Rs +352, random_hold Rs +192, snake_anaconda Rs +108, nifty_calls Rs +59, benchmark_smallcap Rs +39, snake_viper_wild Rs +15, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -153, gold Rs -342, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.