# Paper trading report

Updated 2026-11-09 10:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,890 | +9.95% | 0 | - | 236 |
| benchmark | 216,914 | +8.46% | 0 | - | 237 |
| intraweek | 216,851 | +8.43% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,195 | +6.10% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,099 | +6.05% | 2 | 50% | 330 |
| snake_abs | 210,137 | +5.07% | 1 | 100% | 255 |
| intramonth | 209,993 | +5.00% | 0 | - | 235 |
| snake_abs_conv | 209,964 | +4.98% | 1 | 100% | 255 |
| oracle | 209,659 | +4.83% | 0 | - | 233 |
| random_hold | 203,944 | +1.97% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,728 | -0.14% | 3 | 33% | 374 |
| benchmark_smallcap | 198,251 | -0.88% | 0 | - | 237 |
| snake_viper_wild | 197,211 | -1.39% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,860 | -3.07% | 6 | 50% | 1,154 |
| gold | 192,939 | -3.53% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,692 (-4.65%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +6,488 | +3.08% |
| snake_abs_conv | +4,737 | +2.31% |
| snake_abs | +4,718 | +2.30% |
| unified | +4,280 | +1.99% |
| snake_anaconda | +3,901 | +1.99% |
| snake_abs_exit | +3,883 | +1.86% |
| oracle | +3,832 | +1.86% |
| snake_abs_exit_conv | +3,677 | +1.76% |
| intramonth | +2,390 | +1.15% |
| gold | +1,891 | +0.99% |
| benchmark_smallcap | +1,457 | +0.74% |
| snake_viper_wild | +1,174 | +0.60% |
| snake_viper_tick | +1,150 | +0.60% |
| random_hold | +37 | +0.02% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -574 | -0.26% |

Average per day so far: unified Rs +663, benchmark Rs +564, intraweek Rs +562, snake_abs_exit Rs +452, snake_abs_exit_conv Rs +448, snake_abs_conv Rs +369, snake_abs Rs +362, intramonth Rs +333, oracle Rs +322, random_hold Rs +131, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -11, benchmark_smallcap Rs -67, snake_viper_wild Rs -127, gold Rs -235, snake_viper_tick Rs -323, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.