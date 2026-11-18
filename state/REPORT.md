# Paper trading report

Updated 2026-11-18 12:31 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,015 | +11.51% | 0 | - | 236 |
| benchmark | 220,043 | +10.02% | 0 | - | 237 |
| intraweek | 213,744 | +6.87% | 35 | 54% | 3,851 |
| intramonth | 213,002 | +6.50% | 0 | - | 235 |
| snake_abs_exit | 212,866 | +6.43% | 2 | 50% | 345 |
| oracle | 212,145 | +6.07% | 0 | - | 233 |
| snake_abs_exit_conv | 211,141 | +5.57% | 2 | 50% | 345 |
| snake_abs | 208,235 | +4.12% | 1 | 100% | 255 |
| snake_abs_conv | 208,100 | +4.05% | 1 | 100% | 255 |
| random_hold | 207,402 | +3.70% | 10 | 70% | 733 |
| snake_viper_wild | 207,294 | +3.65% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,752 | +1.88% | 15 | 47% | 2,625 |
| snake_anaconda | 203,093 | +1.55% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,157 | -11.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,460 (-4.27%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,576 | +0.71% |
| intramonth | +1,459 | +0.69% |
| intraweek | +421 | +0.20% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -276 | -0.13% |
| snake_abs_conv | -320 | -0.15% |
| snake_abs | -323 | -0.15% |
| oracle | -341 | -0.16% |
| snake_abs_exit_conv | -433 | -0.20% |
| snake_anaconda | -962 | -0.47% |
| random_hold | -1,031 | -0.49% |
| benchmark_smallcap | -1,244 | -0.62% |
| benchmark | -1,561 | -0.70% |
| snake_viper_tick | -2,084 | -1.01% |
| snake_viper_wild | -2,121 | -1.01% |
| gold | -3,567 | -1.97% |

Average per day so far: unified Rs +639, benchmark Rs +557, snake_abs_exit Rs +390, intraweek Rs +382, intramonth Rs +361, snake_abs_exit_conv Rs +338, oracle Rs +337, snake_viper_wild Rs +260, snake_abs_conv Rs +245, snake_abs Rs +242, random_hold Rs +206, snake_viper_tick Rs +150, snake_anaconda Rs +100, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -21, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.