# Paper trading report

Updated 2026-11-17 10:51 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,862 | +10.93% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| snake_abs_exit | 215,576 | +7.79% | 2 | 50% | 345 |
| intraweek | 214,001 | +7.00% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,720 | +6.86% | 2 | 50% | 345 |
| oracle | 212,548 | +6.27% | 0 | - | 233 |
| intramonth | 211,664 | +5.83% | 0 | - | 235 |
| snake_abs | 210,333 | +5.17% | 1 | 100% | 255 |
| snake_abs_conv | 210,184 | +5.09% | 1 | 100% | 255 |
| random_hold | 208,236 | +4.12% | 10 | 70% | 733 |
| snake_viper_wild | 207,297 | +3.65% | 14 | 50% | 2,496 |
| snake_anaconda | 205,744 | +2.87% | 3 | 33% | 374 |
| snake_viper_tick | 203,753 | +1.88% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,152 | +1.08% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,628 | -9.19% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,434 (-4.28%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,736 | +1.29% |
| benchmark | +1,522 | +0.69% |
| benchmark_smallcap | +1,323 | +0.66% |
| snake_abs_exit | +1,167 | +0.54% |
| snake_viper_wild | +1,153 | +0.56% |
| snake_viper_tick | +1,133 | +0.56% |
| gold | +674 | +0.37% |
| snake_anaconda | +641 | +0.31% |
| oracle | +525 | +0.25% |
| snake_abs_exit_conv | +503 | +0.24% |
| random_hold | +443 | +0.21% |
| unified | +424 | +0.19% |
| snake_abs | +200 | +0.10% |
| snake_abs_conv | +194 | +0.09% |
| intramonth | +45 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +625, benchmark Rs +617, snake_abs_exit Rs +487, snake_abs_exit_conv Rs +429, intraweek Rs +400, oracle Rs +359, intramonth Rs +333, snake_abs_conv Rs +318, snake_abs Rs +313, snake_viper_wild Rs +270, random_hold Rs +235, snake_anaconda Rs +191, snake_viper_tick Rs +156, benchmark_smallcap Rs +69, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -525

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.