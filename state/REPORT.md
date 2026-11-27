# Paper trading report

Updated 2026-11-27 13:04 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,204 | +12.10% | 0 | - | 237 |
| unified | 223,455 | +11.73% | 0 | - | 236 |
| oracle | 212,007 | +6.00% | 0 | - | 233 |
| intramonth | 211,000 | +5.50% | 0 | - | 235 |
| random_hold | 210,777 | +5.39% | 13 | 69% | 1,037 |
| intraweek | 208,515 | +4.26% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,672 | +2.34% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,428 | +2.21% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,546 | +0.77% | 0 | - | 237 |
| snake_abs | 200,383 | +0.19% | 1 | 100% | 255 |
| snake_abs_conv | 200,200 | +0.10% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,756 | -3.12% | 3 | 33% | 374 |
| snake_viper_wild | 192,140 | -3.93% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,877 | -5.56% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,775 | -15.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,962 (-5.52%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,031 | +2.01% |
| gold | +3,781 | +2.28% |
| snake_abs_exit | +3,595 | +1.79% |
| random_hold | +2,182 | +1.05% |
| snake_abs_conv | +1,833 | +0.92% |
| snake_abs | +1,831 | +0.92% |
| intraweek | +1,466 | +0.71% |
| snake_anaconda | +1,459 | +0.76% |
| benchmark_smallcap | +706 | +0.35% |
| intramonth | +467 | +0.22% |
| unified | +376 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -64 | -0.03% |
| snake_viper_wild | -66 | -0.03% |
| oracle | -229 | -0.11% |
| benchmark | -1,782 | -0.79% |

Average per day so far: benchmark Rs +576, unified Rs +558, oracle Rs +286, intramonth Rs +262, random_hold Rs +257, intraweek Rs +203, snake_abs_exit Rs +120, snake_abs_exit_conv Rs +114, nifty_calls Rs +44, benchmark_smallcap Rs +41, snake_abs Rs +10, snake_abs_conv Rs +5, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -169, snake_viper_wild Rs -231, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -359, gold Rs -720

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.