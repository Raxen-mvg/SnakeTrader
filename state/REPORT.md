# Paper trading report

Updated 2026-11-27 11:19 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,388 | +12.19% | 0 | - | 237 |
| unified | 222,357 | +11.18% | 0 | - | 236 |
| oracle | 211,930 | +5.96% | 0 | - | 233 |
| intramonth | 210,144 | +5.07% | 0 | - | 235 |
| random_hold | 210,139 | +5.07% | 13 | 69% | 1,037 |
| intraweek | 207,637 | +3.82% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,301 | +2.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,161 | +2.08% | 2 | 50% | 345 |
| benchmark_smallcap | 201,838 | +0.92% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,020 | +0.51% | 1 | 100% | 255 |
| snake_abs_conv | 200,843 | +0.42% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,594 | -2.70% | 3 | 33% | 374 |
| snake_viper_wild | 193,556 | -3.22% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,264 | -4.87% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,134 | -15.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,452 (-5.77%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,223 | +2.10% |
| snake_abs_exit_conv | +3,764 | +1.88% |
| gold | +3,140 | +1.89% |
| snake_abs_conv | +2,476 | +1.25% |
| snake_abs | +2,467 | +1.24% |
| snake_anaconda | +2,298 | +1.20% |
| random_hold | +1,545 | +0.74% |
| snake_viper_wild | +1,350 | +0.70% |
| snake_viper_tick | +1,323 | +0.70% |
| benchmark_smallcap | +998 | +0.50% |
| intraweek | +588 | +0.28% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -306 | -0.14% |
| intramonth | -389 | -0.18% |
| unified | -721 | -0.32% |
| benchmark | -1,599 | -0.71% |

Average per day so far: benchmark Rs +581, unified Rs +532, oracle Rs +284, intramonth Rs +242, random_hold Rs +241, intraweek Rs +182, snake_abs_exit Rs +136, snake_abs_exit_conv Rs +107, benchmark_smallcap Rs +48, nifty_calls Rs +44, snake_abs Rs +25, snake_abs_conv Rs +22, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -146, snake_viper_wild Rs -190, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -314, gold Rs -735

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.