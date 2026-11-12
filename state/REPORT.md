# Paper trading report

Updated 2026-11-12 12:14 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,584 | +10.79% | 0 | - | 236 |
| benchmark | 220,081 | +10.04% | 0 | - | 237 |
| snake_abs_exit_conv | 219,010 | +9.51% | 2 | 50% | 345 |
| snake_abs_exit | 218,069 | +9.03% | 2 | 50% | 345 |
| snake_abs | 216,004 | +8.00% | 1 | 100% | 255 |
| snake_abs_conv | 215,836 | +7.92% | 1 | 100% | 255 |
| intraweek | 214,795 | +7.40% | 30 | 53% | 3,302 |
| oracle | 213,374 | +6.69% | 0 | - | 233 |
| intramonth | 211,911 | +5.96% | 0 | - | 235 |
| random_hold | 208,031 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 207,441 | +3.72% | 10 | 50% | 1,825 |
| snake_anaconda | 206,715 | +3.36% | 3 | 33% | 374 |
| snake_viper_tick | 203,892 | +1.95% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,116 | +1.56% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,084 | -6.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,316 (-3.84%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,592 | +1.27% |
| snake_abs | +2,379 | +1.11% |
| snake_abs_conv | +2,378 | +1.11% |
| benchmark_smallcap | +2,309 | +1.15% |
| snake_abs_exit | +1,906 | +0.88% |
| snake_abs_exit_conv | +1,859 | +0.86% |
| unified | +1,770 | +0.81% |
| intraweek | +1,661 | +0.78% |
| oracle | +1,371 | +0.65% |
| random_hold | +920 | +0.44% |
| intramonth | +915 | +0.43% |
| benchmark | +819 | +0.37% |
| snake_viper_wild | +699 | +0.34% |
| snake_viper_tick | +683 | +0.34% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,502 | -1.85% |

Average per day so far: unified Rs +675, snake_abs_exit_conv Rs +656, benchmark Rs +628, snake_abs_exit Rs +623, snake_abs_conv Rs +546, snake_abs Rs +533, intraweek Rs +462, oracle Rs +418, intramonth Rs +372, snake_viper_wild Rs +310, random_hold Rs +251, snake_anaconda Rs +249, snake_viper_tick Rs +185, benchmark_smallcap Rs +111, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -435

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.