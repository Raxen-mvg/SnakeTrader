# Paper trading report

Updated 2026-11-18 09:38 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,693 | +10.85% | 0 | - | 236 |
| benchmark | 220,616 | +10.31% | 0 | - | 237 |
| intraweek | 213,339 | +6.67% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,515 | +6.26% | 2 | 50% | 345 |
| oracle | 212,031 | +6.01% | 0 | - | 233 |
| intramonth | 211,590 | +5.79% | 0 | - | 235 |
| snake_abs_exit_conv | 211,061 | +5.53% | 2 | 50% | 345 |
| snake_abs | 208,548 | +4.27% | 1 | 100% | 255 |
| snake_abs_conv | 208,408 | +4.20% | 1 | 100% | 255 |
| random_hold | 207,265 | +3.63% | 10 | 70% | 733 |
| snake_viper_wild | 206,791 | +3.40% | 16 | 50% | 2,827 |
| snake_anaconda | 203,399 | +1.70% | 3 | 33% | 374 |
| snake_viper_tick | 203,260 | +1.63% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,831 | -0.08% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,844 | -11.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,902 (-4.55%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +255 | +0.12% |
| intramonth | +48 | +0.02% |
| intraweek | +17 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -11 | -0.01% |
| snake_abs_conv | -12 | -0.01% |
| oracle | -456 | -0.21% |
| snake_abs_exit_conv | -513 | -0.24% |
| snake_abs_exit | -627 | -0.29% |
| snake_anaconda | -656 | -0.32% |
| benchmark_smallcap | -740 | -0.37% |
| benchmark | -987 | -0.45% |
| random_hold | -1,168 | -0.56% |
| snake_viper_tick | -2,577 | -1.25% |
| snake_viper_wild | -2,624 | -1.25% |
| gold | -3,880 | -2.15% |

Average per day so far: unified Rs +603, benchmark Rs +573, snake_abs_exit Rs +379, intraweek Rs +371, snake_abs_exit_conv Rs +335, oracle Rs +334, intramonth Rs +322, snake_abs_conv Rs +255, snake_abs Rs +251, snake_viper_wild Rs +243, random_hold Rs +202, snake_viper_tick Rs +130, snake_anaconda Rs +110, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -5, snake_nonews Rs -326, snake Rs -347, gold Rs -643

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.