# Paper trading report

Updated 2026-11-25 13:16 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,335 | +12.17% | 0 | - | 236 |
| benchmark | 223,669 | +11.83% | 0 | - | 237 |
| oracle | 212,411 | +6.21% | 0 | - | 233 |
| intramonth | 212,198 | +6.10% | 0 | - | 235 |
| random_hold | 209,699 | +4.85% | 12 | 75% | 1,009 |
| intraweek | 208,217 | +4.11% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,601 | +0.80% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,232 | +0.62% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,789 | -0.10% | 1 | 100% | 255 |
| snake_abs_conv | 199,600 | -0.20% | 1 | 100% | 255 |
| benchmark_smallcap | 198,766 | -0.62% | 0 | - | 237 |
| snake_viper_wild | 196,934 | -1.53% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,580 | -3.21% | 15 | 47% | 2,625 |
| snake_anaconda | 193,323 | -3.34% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,596 | -17.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,012 (-5.49%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,196 | +0.99% |
| random_hold | +1,272 | +0.61% |
| oracle | +68 | +0.03% |
| unified | +50 | +0.02% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -213 | -0.11% |
| intramonth | -554 | -0.26% |
| intraweek | -3,402 | -1.61% |
| snake_viper_tick | -4,113 | -2.08% |
| snake_viper_wild | -4,191 | -2.08% |
| gold | -4,833 | -2.85% |
| snake_anaconda | -5,380 | -2.71% |
| snake_abs | -5,671 | -2.76% |
| snake_abs_conv | -5,703 | -2.78% |
| snake_abs_exit_conv | -5,813 | -2.81% |
| snake_abs_exit | -5,894 | -2.84% |

Average per day so far: unified Rs +608, benchmark Rs +592, oracle Rs +310, intramonth Rs +305, random_hold Rs +242, intraweek Rs +205, nifty_calls Rs +46, snake_abs_exit Rs +43, snake_abs_exit_conv Rs +33, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, benchmark_smallcap Rs -34, snake_viper_wild Rs -96, snake_anaconda Rs -191, snake_viper_tick Rs -221, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.