# Paper trading report

Updated 2026-11-17 12:03 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,299 | +11.15% | 0 | - | 237 |
| unified | 222,202 | +11.10% | 0 | - | 236 |
| snake_abs_exit | 215,156 | +7.58% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,380 | +6.69% | 2 | 50% | 345 |
| intraweek | 212,439 | +6.22% | 35 | 54% | 3,851 |
| oracle | 212,356 | +6.18% | 0 | - | 233 |
| intramonth | 212,058 | +6.03% | 0 | - | 235 |
| snake_abs | 210,007 | +5.00% | 1 | 100% | 255 |
| snake_abs_conv | 209,859 | +4.93% | 1 | 100% | 255 |
| random_hold | 207,881 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 207,289 | +3.64% | 14 | 50% | 2,496 |
| snake_anaconda | 205,612 | +2.81% | 3 | 33% | 374 |
| snake_viper_tick | 203,744 | +1.87% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,129 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,300 | -9.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,273 (-4.36%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,219 | +1.01% |
| benchmark_smallcap | +1,300 | +0.65% |
| intraweek | +1,174 | +0.56% |
| snake_viper_wild | +1,144 | +0.56% |
| snake_viper_tick | +1,125 | +0.56% |
| unified | +765 | +0.34% |
| snake_abs_exit | +747 | +0.35% |
| snake_anaconda | +510 | +0.25% |
| intramonth | +439 | +0.21% |
| gold | +345 | +0.19% |
| oracle | +333 | +0.16% |
| snake_abs_exit_conv | +163 | +0.08% |
| random_hold | +87 | +0.04% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -127 | -0.06% |
| snake_abs_conv | -130 | -0.06% |

Average per day so far: benchmark Rs +637, unified Rs +634, snake_abs_exit Rs +474, snake_abs_exit_conv Rs +418, intraweek Rs +355, oracle Rs +353, intramonth Rs +345, snake_abs_conv Rs +308, snake_abs Rs +303, snake_viper_wild Rs +270, random_hold Rs +225, snake_anaconda Rs +187, snake_viper_tick Rs +156, benchmark_smallcap Rs +69, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -534

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.