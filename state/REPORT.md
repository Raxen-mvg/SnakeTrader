# Paper trading report

Updated 2026-11-06 15:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,893 | +8.95% | 0 | - | 237 |
| unified | 215,898 | +7.95% | 0 | - | 236 |
| intraweek | 210,695 | +5.35% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,677 | +4.34% | 1 | 100% | 255 |
| snake_abs_exit | 208,562 | +4.28% | 1 | 100% | 260 |
| intramonth | 207,746 | +3.87% | 0 | - | 235 |
| oracle | 205,817 | +2.91% | 0 | - | 233 |
| snake_abs | 205,669 | +2.83% | 1 | 100% | 255 |
| snake_abs_conv | 205,481 | +2.74% | 1 | 100% | 255 |
| random_hold | 204,092 | +2.05% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 197,197 | -1.40% | 0 | - | 237 |
| snake_viper_wild | 196,267 | -1.87% | 4 | 25% | 842 |
| snake_anaconda | 196,185 | -1.91% | 3 | 33% | 374 |
| snake_viper_tick | 192,938 | -3.53% | 3 | 0% | 672 |
| gold | 191,180 | -4.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,579 (-6.21%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,123 | +1.93% |
| oracle | +1,746 | +0.85% |
| intraweek | +1,277 | +0.61% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -85 | -0.04% |
| intramonth | -203 | -0.10% |
| random_hold | -231 | -0.11% |
| benchmark_smallcap | -1,491 | -0.75% |
| gold | -3,041 | -1.57% |
| snake_abs | -6,019 | -2.84% |
| snake_abs_conv | -6,064 | -2.87% |
| snake_abs_exit | -6,096 | -2.84% |
| snake_abs_exit_conv | -6,126 | -2.85% |
| snake_anaconda | -6,294 | -3.11% |
| snake_viper_tick | -8,200 | -4.08% |
| snake_viper_wild | -8,389 | -4.10% |

Average per day so far: benchmark Rs +617, unified Rs +548, intraweek Rs +369, snake_abs_exit_conv Rs +334, snake_abs_exit Rs +329, intramonth Rs +267, snake_abs_conv Rs +211, snake_abs Rs +210, oracle Rs +201, random_hold Rs +141, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -112, snake_anaconda Rs -159, snake_viper_wild Rs -178, gold Rs -304, snake_viper_tick Rs -392, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.