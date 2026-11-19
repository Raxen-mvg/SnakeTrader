# Paper trading report

Updated 2026-11-19 10:57 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,635 | +11.82% | 0 | - | 236 |
| benchmark | 220,854 | +10.43% | 0 | - | 237 |
| snake_abs_exit | 213,796 | +6.90% | 2 | 50% | 345 |
| intramonth | 213,190 | +6.59% | 0 | - | 235 |
| snake_abs_exit_conv | 211,871 | +5.93% | 2 | 50% | 345 |
| intraweek | 211,658 | +5.83% | 35 | 54% | 3,851 |
| oracle | 210,835 | +5.42% | 0 | - | 233 |
| snake_abs | 209,505 | +4.75% | 1 | 100% | 255 |
| snake_abs_conv | 209,378 | +4.69% | 1 | 100% | 255 |
| snake_viper_wild | 207,763 | +3.88% | 16 | 50% | 2,827 |
| random_hold | 207,512 | +3.76% | 10 | 70% | 733 |
| snake_viper_tick | 204,212 | +2.11% | 15 | 47% | 2,625 |
| snake_anaconda | 203,530 | +1.76% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,358 | +0.18% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,987 | -12.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,095 (-4.45%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,031 | +0.52% |
| unified | +1,024 | +0.46% |
| intramonth | +916 | +0.43% |
| snake_viper_wild | +723 | +0.35% |
| snake_viper_tick | +709 | +0.35% |
| random_hold | +580 | +0.28% |
| benchmark | +558 | +0.25% |
| snake_abs | +68 | +0.03% |
| snake_abs_conv | +53 | +0.03% |
| oracle | +39 | +0.02% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -182 | -0.09% |
| snake_abs_exit | -236 | -0.11% |
| snake_abs_exit_conv | -512 | -0.24% |
| snake_anaconda | -871 | -0.43% |
| gold | -2,334 | -1.32% |

Average per day so far: unified Rs +639, benchmark Rs +564, snake_abs_exit Rs +406, intramonth Rs +356, snake_abs_exit_conv Rs +349, intraweek Rs +315, oracle Rs +293, snake_abs_conv Rs +276, snake_abs Rs +272, snake_viper_wild Rs +268, random_hold Rs +203, snake_viper_tick Rs +162, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.