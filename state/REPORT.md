# Paper trading report

Updated 2026-11-11 12:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,075 | +10.54% | 0 | - | 237 |
| unified | 220,805 | +10.40% | 0 | - | 236 |
| snake_abs_exit_conv | 216,101 | +8.05% | 2 | 50% | 345 |
| snake_abs_exit | 214,898 | +7.45% | 2 | 50% | 345 |
| intraweek | 214,159 | +7.08% | 30 | 53% | 3,302 |
| snake_abs | 212,644 | +6.32% | 1 | 100% | 255 |
| snake_abs_conv | 212,488 | +6.24% | 1 | 100% | 255 |
| oracle | 212,150 | +6.08% | 0 | - | 233 |
| intramonth | 211,780 | +5.89% | 0 | - | 235 |
| random_hold | 207,102 | +3.55% | 9 | 67% | 709 |
| snake_anaconda | 202,859 | +1.43% | 3 | 33% | 374 |
| snake_viper_wild | 202,123 | +1.06% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,827 | +0.91% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,685 | -0.66% | 9 | 44% | 1,639 |
| gold | 189,865 | -5.07% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,423 (-4.29%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +4,693 | +2.38% |
| snake_viper_tick | +4,608 | +2.37% |
| snake_abs_exit_conv | +4,192 | +1.98% |
| benchmark_smallcap | +3,654 | +1.84% |
| snake_anaconda | +3,393 | +1.70% |
| snake_abs_conv | +3,010 | +1.44% |
| snake_abs | +2,997 | +1.43% |
| benchmark | +2,983 | +1.37% |
| snake_abs_exit | +2,914 | +1.38% |
| oracle | +2,231 | +1.06% |
| random_hold | +2,142 | +1.04% |
| intramonth | +1,171 | +0.56% |
| unified | +1,058 | +0.48% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -383 | -0.18% |
| gold | -2,269 | -1.18% |

Average per day so far: benchmark Rs +680, unified Rs +671, snake_abs_exit_conv Rs +575, snake_abs_exit Rs +532, intraweek Rs +457, snake_abs_conv Rs +446, snake_abs Rs +436, oracle Rs +392, intramonth Rs +380, random_hold Rs +229, snake_anaconda Rs +110, snake_viper_wild Rs +92, benchmark_smallcap Rs +68, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -66, gold Rs -327, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.