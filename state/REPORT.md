# Paper trading report

Updated 2026-11-11 12:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,487 | +10.24% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| snake_abs_exit_conv | 217,845 | +8.92% | 2 | 50% | 345 |
| snake_abs_exit | 216,809 | +8.40% | 2 | 50% | 345 |
| snake_abs | 213,946 | +6.97% | 1 | 100% | 255 |
| snake_abs_conv | 213,796 | +6.90% | 1 | 100% | 255 |
| intraweek | 213,638 | +6.82% | 30 | 53% | 3,302 |
| oracle | 211,892 | +5.95% | 0 | - | 233 |
| intramonth | 211,426 | +5.71% | 0 | - | 235 |
| random_hold | 206,858 | +3.43% | 9 | 67% | 709 |
| snake_viper_wild | 205,541 | +2.77% | 10 | 50% | 1,825 |
| snake_anaconda | 204,763 | +2.38% | 3 | 33% | 374 |
| snake_viper_tick | 202,033 | +1.02% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,401 | +0.70% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,029 | -4.99% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,318 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,111 | +4.11% |
| snake_viper_tick | +7,956 | +4.10% |
| snake_abs_exit_conv | +5,937 | +2.80% |
| snake_anaconda | +5,297 | +2.65% |
| snake_abs_exit | +4,825 | +2.28% |
| snake_abs_conv | +4,318 | +2.06% |
| snake_abs | +4,299 | +2.05% |
| benchmark_smallcap | +3,228 | +1.63% |
| benchmark | +2,287 | +1.05% |
| oracle | +1,974 | +0.94% |
| random_hold | +1,897 | +0.93% |
| intramonth | +817 | +0.39% |
| unified | +740 | +0.34% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -904 | -0.42% |
| gold | -2,104 | -1.09% |

Average per day so far: unified Rs +661, benchmark Rs +657, snake_abs_exit_conv Rs +637, snake_abs_exit Rs +600, snake_abs_conv Rs +493, snake_abs Rs +481, intraweek Rs +440, oracle Rs +384, intramonth Rs +369, snake_viper_wild Rs +241, random_hold Rs +221, snake_anaconda Rs +183, snake_viper_tick Rs +102, nifty_calls Rs +59, benchmark_smallcap Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -322, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.