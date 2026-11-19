# Paper trading report

Updated 2026-11-19 10:03 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,043 | +12.02% | 0 | - | 236 |
| benchmark | 220,502 | +10.25% | 0 | - | 237 |
| intramonth | 213,845 | +6.92% | 0 | - | 235 |
| snake_abs_exit | 213,689 | +6.84% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,903 | +5.95% | 2 | 50% | 345 |
| intraweek | 211,529 | +5.76% | 35 | 54% | 3,851 |
| oracle | 211,470 | +5.74% | 0 | - | 233 |
| snake_abs | 209,171 | +4.58% | 1 | 100% | 255 |
| snake_abs_conv | 209,050 | +4.53% | 1 | 100% | 255 |
| random_hold | 207,930 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 207,702 | +3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,152 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,904 | +1.95% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,627 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,904 | -12.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,465 (-4.27%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,572 | +0.74% |
| unified | +1,432 | +0.64% |
| benchmark_smallcap | +1,300 | +0.65% |
| random_hold | +998 | +0.48% |
| oracle | +674 | +0.32% |
| snake_viper_wild | +662 | +0.32% |
| snake_viper_tick | +649 | +0.32% |
| benchmark | +207 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -266 | -0.13% |
| snake_abs_conv | -275 | -0.13% |
| intraweek | -310 | -0.15% |
| snake_abs_exit | -342 | -0.16% |
| snake_abs_exit_conv | -480 | -0.23% |
| snake_anaconda | -497 | -0.24% |
| gold | -2,417 | -1.36% |

Average per day so far: unified Rs +650, benchmark Rs +554, snake_abs_exit Rs +403, intramonth Rs +374, snake_abs_exit_conv Rs +350, intraweek Rs +312, oracle Rs +310, snake_abs_conv Rs +266, snake_viper_wild Rs +266, snake_abs Rs +262, random_hold Rs +214, snake_viper_tick Rs +160, snake_anaconda Rs +122, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.