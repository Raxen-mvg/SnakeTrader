# Paper trading report

Updated 2026-11-27 10:39 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,969 | +12.48% | 0 | - | 237 |
| unified | 222,901 | +11.45% | 0 | - | 236 |
| oracle | 212,313 | +6.16% | 0 | - | 233 |
| intramonth | 210,715 | +5.36% | 0 | - | 235 |
| random_hold | 209,936 | +4.97% | 13 | 69% | 1,037 |
| intraweek | 208,044 | +4.02% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,267 | +2.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,006 | +2.00% | 2 | 50% | 345 |
| benchmark_smallcap | 202,107 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,177 | +0.59% | 1 | 100% | 255 |
| snake_abs_conv | 200,998 | +0.50% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,511 | -2.74% | 3 | 33% | 374 |
| snake_viper_wild | 193,287 | -3.36% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,001 | -5.00% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,657 | -15.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,737 (-5.63%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,190 | +2.08% |
| snake_abs_exit_conv | +3,609 | +1.80% |
| gold | +2,663 | +1.60% |
| snake_abs_conv | +2,632 | +1.33% |
| snake_abs | +2,625 | +1.32% |
| snake_anaconda | +2,215 | +1.15% |
| random_hold | +1,342 | +0.64% |
| benchmark_smallcap | +1,267 | +0.63% |
| snake_viper_wild | +1,082 | +0.56% |
| snake_viper_tick | +1,060 | +0.56% |
| intraweek | +996 | +0.48% |
| intramonth | +182 | +0.09% |
| oracle | +78 | +0.04% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -178 | -0.08% |
| benchmark | -1,017 | -0.45% |

Average per day so far: benchmark Rs +595, unified Rs +545, oracle Rs +293, intramonth Rs +255, random_hold Rs +237, intraweek Rs +192, snake_abs_exit Rs +135, snake_abs_exit_conv Rs +103, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +29, snake_abs_conv Rs +26, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -148, snake_viper_wild Rs -197, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -323, gold Rs -746

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.