# Paper trading report

Updated 2026-11-27 11:31 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,937 | +11.97% | 0 | - | 237 |
| unified | 222,345 | +11.17% | 0 | - | 236 |
| oracle | 211,736 | +5.87% | 0 | - | 233 |
| intramonth | 210,427 | +5.21% | 0 | - | 235 |
| random_hold | 210,151 | +5.08% | 13 | 69% | 1,037 |
| intraweek | 207,643 | +3.82% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,274 | +2.64% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,970 | +1.99% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,513 | +0.76% | 0 | - | 237 |
| snake_abs | 200,861 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,684 | +0.34% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,315 | -2.84% | 3 | 33% | 374 |
| snake_viper_wild | 193,436 | -3.28% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,146 | -4.93% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,101 | -15.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,420 (-5.79%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,197 | +2.09% |
| snake_abs_exit_conv | +3,573 | +1.78% |
| gold | +3,107 | +1.87% |
| snake_abs_conv | +2,317 | +1.17% |
| snake_abs | +2,309 | +1.16% |
| snake_anaconda | +2,019 | +1.05% |
| random_hold | +1,557 | +0.75% |
| snake_viper_wild | +1,230 | +0.64% |
| snake_viper_tick | +1,205 | +0.64% |
| benchmark_smallcap | +673 | +0.34% |
| intraweek | +595 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -106 | -0.05% |
| oracle | -499 | -0.23% |
| unified | -733 | -0.33% |
| benchmark | -2,050 | -0.91% |

Average per day so far: benchmark Rs +570, unified Rs +532, oracle Rs +279, intramonth Rs +248, random_hold Rs +242, intraweek Rs +182, snake_abs_exit Rs +135, snake_abs_exit_conv Rs +102, nifty_calls Rs +44, benchmark_smallcap Rs +40, snake_abs Rs +22, snake_abs_conv Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -154, snake_viper_wild Rs -193, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -318, gold Rs -736

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.