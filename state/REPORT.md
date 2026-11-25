# Paper trading report

Updated 2026-11-25 13:05 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,578 | +12.29% | 0 | - | 236 |
| benchmark | 224,090 | +12.04% | 0 | - | 237 |
| oracle | 212,600 | +6.30% | 0 | - | 233 |
| intramonth | 212,465 | +6.23% | 0 | - | 235 |
| random_hold | 209,923 | +4.96% | 12 | 75% | 1,009 |
| intraweek | 208,499 | +4.25% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,743 | +0.87% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,419 | +0.71% | 2 | 50% | 345 |
| snake_abs | 200,008 | +0.00% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,817 | -0.09% | 1 | 100% | 255 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| snake_viper_wild | 196,924 | -1.54% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,571 | -3.21% | 15 | 47% | 2,625 |
| snake_anaconda | 193,421 | -3.29% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,761 | -17.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,220 (-5.39%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,616 | +1.18% |
| random_hold | +1,496 | +0.72% |
| unified | +293 | +0.13% |
| oracle | +258 | +0.12% |
| benchmark_smallcap | +123 | +0.06% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -286 | -0.14% |
| intraweek | -3,120 | -1.48% |
| snake_viper_tick | -4,122 | -2.08% |
| snake_viper_wild | -4,200 | -2.09% |
| gold | -4,669 | -2.76% |
| snake_anaconda | -5,283 | -2.66% |
| snake_abs | -5,453 | -2.65% |
| snake_abs_conv | -5,486 | -2.67% |
| snake_abs_exit_conv | -5,627 | -2.72% |
| snake_abs_exit | -5,752 | -2.77% |

Average per day so far: unified Rs +614, benchmark Rs +602, oracle Rs +315, intramonth Rs +312, random_hold Rs +248, intraweek Rs +212, snake_abs_exit Rs +47, nifty_calls Rs +46, snake_abs_exit_conv Rs +38, snake_abs Rs +0, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs_conv Rs -5, benchmark_smallcap Rs -25, snake_viper_wild Rs -96, snake_anaconda Rs -188, snake_viper_tick Rs -222, snake_nonews Rs -292, snake Rs -311, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.