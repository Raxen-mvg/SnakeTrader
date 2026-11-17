# Paper trading report

Updated 2026-11-17 11:24 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,091 | +11.04% | 0 | - | 236 |
| benchmark | 221,902 | +10.95% | 0 | - | 237 |
| snake_abs_exit | 215,610 | +7.80% | 2 | 50% | 345 |
| intraweek | 213,943 | +6.97% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,590 | +6.79% | 2 | 50% | 345 |
| oracle | 212,597 | +6.30% | 0 | - | 233 |
| intramonth | 212,057 | +6.03% | 0 | - | 235 |
| snake_abs | 209,966 | +4.98% | 1 | 100% | 255 |
| snake_abs_conv | 209,817 | +4.91% | 1 | 100% | 255 |
| random_hold | 207,993 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 207,765 | +3.88% | 14 | 50% | 2,496 |
| snake_anaconda | 205,521 | +2.76% | 3 | 33% | 374 |
| snake_viper_tick | 204,213 | +2.11% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,286 | +1.14% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,530 | -9.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,541 (-4.23%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,677 | +1.27% |
| benchmark | +1,821 | +0.83% |
| snake_viper_wild | +1,621 | +0.79% |
| snake_viper_tick | +1,593 | +0.79% |
| benchmark_smallcap | +1,457 | +0.73% |
| snake_abs_exit | +1,201 | +0.56% |
| unified | +653 | +0.29% |
| gold | +575 | +0.32% |
| oracle | +574 | +0.27% |
| intramonth | +438 | +0.21% |
| snake_anaconda | +419 | +0.20% |
| snake_abs_exit_conv | +372 | +0.17% |
| random_hold | +200 | +0.10% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -168 | -0.08% |
| snake_abs_conv | -172 | -0.08% |

Average per day so far: unified Rs +631, benchmark Rs +626, snake_abs_exit Rs +488, snake_abs_exit_conv Rs +425, intraweek Rs +398, oracle Rs +360, intramonth Rs +344, snake_abs_conv Rs +307, snake_abs Rs +302, snake_viper_wild Rs +288, random_hold Rs +228, snake_anaconda Rs +184, snake_viper_tick Rs +176, benchmark_smallcap Rs +74, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -528

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.