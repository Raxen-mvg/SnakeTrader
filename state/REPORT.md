# Paper trading report

Updated 2026-11-17 11:44 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,399 | +11.20% | 0 | - | 236 |
| benchmark | 221,879 | +10.94% | 0 | - | 237 |
| snake_abs_exit | 215,155 | +7.58% | 2 | 50% | 345 |
| intraweek | 213,841 | +6.92% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,294 | +6.65% | 2 | 50% | 345 |
| oracle | 212,686 | +6.34% | 0 | - | 233 |
| intramonth | 212,313 | +6.16% | 0 | - | 235 |
| snake_abs | 209,964 | +4.98% | 1 | 100% | 255 |
| snake_abs_conv | 209,813 | +4.91% | 1 | 100% | 255 |
| random_hold | 208,100 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 207,564 | +3.78% | 14 | 50% | 2,496 |
| snake_anaconda | 205,520 | +2.76% | 3 | 33% | 374 |
| snake_viper_tick | 204,015 | +2.01% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,174 | +1.09% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,332 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,664 (-4.17%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,575 | +1.22% |
| benchmark | +1,798 | +0.82% |
| snake_viper_wild | +1,420 | +0.69% |
| snake_viper_tick | +1,395 | +0.69% |
| benchmark_smallcap | +1,345 | +0.67% |
| unified | +961 | +0.43% |
| snake_abs_exit | +745 | +0.35% |
| intramonth | +694 | +0.33% |
| oracle | +663 | +0.31% |
| snake_anaconda | +417 | +0.20% |
| gold | +378 | +0.21% |
| random_hold | +307 | +0.15% |
| snake_abs_exit_conv | +77 | +0.04% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -170 | -0.08% |
| snake_abs_conv | -176 | -0.08% |

Average per day so far: unified Rs +640, benchmark Rs +625, snake_abs_exit Rs +474, snake_abs_exit_conv Rs +415, intraweek Rs +395, oracle Rs +362, intramonth Rs +352, snake_abs_conv Rs +307, snake_abs Rs +302, snake_viper_wild Rs +280, random_hold Rs +231, snake_anaconda Rs +184, snake_viper_tick Rs +167, benchmark_smallcap Rs +70, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.