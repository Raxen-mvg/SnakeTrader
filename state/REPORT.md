# Paper trading report

Updated 2026-11-11 14:20 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,489 | +10.24% | 0 | - | 236 |
| benchmark | 219,943 | +9.97% | 0 | - | 237 |
| snake_abs_exit_conv | 216,816 | +8.41% | 2 | 50% | 345 |
| snake_abs_exit | 216,101 | +8.05% | 2 | 50% | 345 |
| snake_abs | 213,909 | +6.96% | 1 | 100% | 255 |
| snake_abs_conv | 213,745 | +6.87% | 1 | 100% | 255 |
| intraweek | 213,020 | +6.51% | 30 | 53% | 3,302 |
| oracle | 211,809 | +5.91% | 0 | - | 233 |
| intramonth | 211,454 | +5.73% | 0 | - | 235 |
| random_hold | 207,051 | +3.52% | 9 | 67% | 709 |
| snake_viper_wild | 205,182 | +2.59% | 10 | 50% | 1,825 |
| snake_anaconda | 203,886 | +1.94% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,681 | +0.84% | 9 | 44% | 1,639 |
| benchmark_smallcap | 200,930 | +0.47% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,684 | -5.16% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,159 (-4.42%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,752 | +3.93% |
| snake_viper_tick | +7,605 | +3.92% |
| snake_abs_exit_conv | +4,907 | +2.32% |
| snake_anaconda | +4,420 | +2.22% |
| snake_abs_conv | +4,267 | +2.04% |
| snake_abs | +4,263 | +2.03% |
| snake_abs_exit | +4,117 | +1.94% |
| benchmark_smallcap | +2,758 | +1.39% |
| random_hold | +2,090 | +1.02% |
| oracle | +1,890 | +0.90% |
| benchmark | +1,851 | +0.85% |
| intramonth | +845 | +0.40% |
| unified | +742 | +0.34% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,522 | -0.71% |
| gold | -2,450 | -1.27% |

Average per day so far: unified Rs +661, benchmark Rs +643, snake_abs_exit_conv Rs +601, snake_abs_exit Rs +575, snake_abs_conv Rs +491, snake_abs Rs +480, intraweek Rs +420, oracle Rs +381, intramonth Rs +369, random_hold Rs +227, snake_viper_wild Rs +225, snake_anaconda Rs +149, snake_viper_tick Rs +84, nifty_calls Rs +59, benchmark_smallcap Rs +34, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -333, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.