# Paper trading report

Updated 2026-11-27 13:37 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,044 | +12.02% | 0 | - | 237 |
| unified | 222,832 | +11.42% | 0 | - | 236 |
| oracle | 211,409 | +5.71% | 0 | - | 233 |
| random_hold | 210,752 | +5.38% | 13 | 69% | 1,037 |
| intramonth | 210,019 | +5.01% | 0 | - | 235 |
| intraweek | 208,211 | +4.11% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,275 | +2.64% | 2 | 50% | 345 |
| snake_abs_exit | 204,548 | +2.27% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| snake_abs | 200,289 | +0.14% | 1 | 100% | 255 |
| snake_abs_conv | 200,107 | +0.05% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,589 | -3.21% | 3 | 33% | 374 |
| snake_viper_wild | 192,044 | -3.98% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,783 | -5.61% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,972 | -15.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,555 (-5.72%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,878 | +2.43% |
| gold | +3,978 | +2.40% |
| snake_abs_exit | +3,470 | +1.73% |
| random_hold | +2,158 | +1.03% |
| snake_abs_conv | +1,741 | +0.88% |
| snake_abs | +1,737 | +0.88% |
| snake_anaconda | +1,293 | +0.67% |
| intraweek | +1,162 | +0.56% |
| benchmark_smallcap | +617 | +0.31% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -158 | -0.08% |
| snake_viper_wild | -162 | -0.08% |
| unified | -247 | -0.11% |
| intramonth | -515 | -0.24% |
| oracle | -826 | -0.39% |
| benchmark | -1,943 | -0.86% |

Average per day so far: benchmark Rs +572, unified Rs +544, oracle Rs +272, random_hold Rs +256, intramonth Rs +239, intraweek Rs +195, snake_abs_exit_conv Rs +135, snake_abs_exit Rs +117, nifty_calls Rs +44, benchmark_smallcap Rs +38, snake_abs Rs +7, snake_abs_conv Rs +3, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -173, snake_viper_wild Rs -234, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -362, gold Rs -715

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.