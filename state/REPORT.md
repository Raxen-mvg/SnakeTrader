# Paper trading report

Updated 2026-11-23 10:52 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,438 | +12.22% | 0 | - | 236 |
| benchmark | 223,164 | +11.58% | 0 | - | 237 |
| intraweek | 212,635 | +6.32% | 40 | 55% | 4,400 |
| intramonth | 212,430 | +6.21% | 0 | - | 235 |
| oracle | 211,068 | +5.53% | 0 | - | 233 |
| random_hold | 210,031 | +5.02% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,919 | +3.46% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,850 | +2.92% | 2 | 50% | 345 |
| snake_abs | 204,312 | +2.16% | 1 | 100% | 255 |
| snake_abs_conv | 204,159 | +2.08% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,217 | +0.11% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,293 | -0.35% | 0 | - | 237 |
| snake_anaconda | 197,823 | -1.09% | 3 | 33% | 374 |
| snake_viper_tick | 196,804 | -1.60% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,561 | -15.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,302 (-4.85%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,512 | +0.90% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -728 | -0.34% |
| snake_abs_exit_conv | -766 | -0.37% |
| oracle | -1,410 | -0.66% |
| snake_abs | -1,608 | -0.78% |
| benchmark_smallcap | -1,614 | -0.80% |
| snake_abs_conv | -1,623 | -0.79% |
| snake_abs_exit | -1,643 | -0.79% |
| unified | -1,744 | -0.77% |
| benchmark | -1,974 | -0.88% |
| snake_anaconda | -2,083 | -1.04% |
| snake_viper_tick | -2,567 | -1.29% |
| intramonth | -2,574 | -1.20% |
| snake_viper_wild | -2,612 | -1.29% |
| intraweek | -3,077 | -1.43% |

Average per day so far: unified Rs +627, benchmark Rs +594, intraweek Rs +324, intramonth Rs +319, oracle Rs +284, random_hold Rs +257, snake_abs_exit Rs +192, snake_abs_exit_conv Rs +163, snake_abs Rs +117, snake_abs_conv Rs +116, nifty_calls Rs +47, snake_viper_wild Rs +7, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -20, snake_anaconda Rs -64, snake_viper_tick Rs -114, snake_nonews Rs -300, snake Rs -320, gold Rs -780

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.