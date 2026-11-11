# Paper trading report

Updated 2026-11-11 11:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,420 | +10.71% | 0 | - | 237 |
| unified | 220,657 | +10.33% | 0 | - | 236 |
| snake_abs_exit_conv | 216,197 | +8.10% | 2 | 50% | 345 |
| snake_abs_exit | 214,997 | +7.50% | 2 | 50% | 345 |
| intraweek | 214,161 | +7.08% | 30 | 53% | 3,302 |
| snake_abs | 212,704 | +6.35% | 1 | 100% | 255 |
| snake_abs_conv | 212,550 | +6.28% | 1 | 100% | 255 |
| oracle | 212,169 | +6.08% | 0 | - | 233 |
| intramonth | 211,762 | +5.88% | 0 | - | 235 |
| random_hold | 206,862 | +3.43% | 9 | 67% | 709 |
| snake_anaconda | 202,942 | +1.47% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,804 | +0.90% | 0 | - | 237 |
| snake_viper_wild | 201,669 | +0.83% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,241 | -0.88% | 9 | 44% | 1,639 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,389 (-4.31%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,288 | +2.02% |
| snake_viper_wild | +4,239 | +2.15% |
| snake_viper_tick | +4,165 | +2.15% |
| benchmark_smallcap | +3,632 | +1.83% |
| snake_anaconda | +3,475 | +1.74% |
| benchmark | +3,328 | +1.53% |
| snake_abs_conv | +3,073 | +1.47% |
| snake_abs | +3,057 | +1.46% |
| snake_abs_exit | +3,013 | +1.42% |
| oracle | +2,251 | +1.07% |
| random_hold | +1,902 | +0.93% |
| intramonth | +1,152 | +0.55% |
| unified | +910 | +0.41% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -381 | -0.18% |
| gold | -2,203 | -1.15% |

Average per day so far: benchmark Rs +691, unified Rs +666, snake_abs_exit_conv Rs +578, snake_abs_exit Rs +536, intraweek Rs +457, snake_abs_conv Rs +448, snake_abs Rs +438, oracle Rs +393, intramonth Rs +379, random_hold Rs +221, snake_anaconda Rs +113, snake_viper_wild Rs +73, benchmark_smallcap Rs +67, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -88, gold Rs -325, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.