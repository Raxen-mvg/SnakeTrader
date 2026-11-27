# Paper trading report

Updated 2026-11-27 13:40 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,090 | +12.04% | 0 | - | 237 |
| unified | 223,020 | +11.51% | 0 | - | 236 |
| oracle | 211,595 | +5.80% | 0 | - | 233 |
| random_hold | 210,893 | +5.45% | 13 | 69% | 1,037 |
| intramonth | 210,335 | +5.17% | 0 | - | 235 |
| intraweek | 208,414 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,146 | +2.57% | 2 | 50% | 345 |
| snake_abs_exit | 204,474 | +2.24% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| snake_abs | 200,264 | +0.13% | 1 | 100% | 255 |
| snake_abs_conv | 200,082 | +0.04% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,565 | -3.22% | 3 | 33% | 374 |
| snake_viper_wild | 192,044 | -3.98% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,783 | -5.61% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,972 | -15.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,713 (-5.64%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,750 | +2.37% |
| gold | +3,978 | +2.40% |
| snake_abs_exit | +3,397 | +1.69% |
| random_hold | +2,299 | +1.10% |
| snake_abs_conv | +1,715 | +0.86% |
| snake_abs | +1,712 | +0.86% |
| intraweek | +1,366 | +0.66% |
| snake_anaconda | +1,268 | +0.66% |
| benchmark_smallcap | +617 | +0.31% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -59 | -0.03% |
| snake_viper_tick | -158 | -0.08% |
| snake_viper_wild | -162 | -0.08% |
| intramonth | -199 | -0.09% |
| oracle | -641 | -0.30% |
| benchmark | -1,897 | -0.84% |

Average per day so far: benchmark Rs +574, unified Rs +548, oracle Rs +276, random_hold Rs +259, intramonth Rs +246, intraweek Rs +200, snake_abs_exit_conv Rs +132, snake_abs_exit Rs +115, nifty_calls Rs +44, benchmark_smallcap Rs +38, snake_abs Rs +7, snake_abs_conv Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -174, snake_viper_wild Rs -234, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -362, gold Rs -715

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.