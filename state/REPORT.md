# Paper trading report

Updated 2026-11-20 14:48 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,168 | +13.08% | 0 | - | 236 |
| benchmark | 224,702 | +12.35% | 0 | - | 237 |
| intraweek | 215,306 | +7.65% | 35 | 54% | 3,851 |
| intramonth | 215,051 | +7.53% | 0 | - | 235 |
| oracle | 212,861 | +6.43% | 0 | - | 233 |
| random_hold | 209,738 | +4.87% | 11 | 73% | 979 |
| snake_abs_exit | 208,784 | +4.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,907 | +3.45% | 2 | 50% | 345 |
| snake_abs | 206,183 | +3.09% | 1 | 100% | 255 |
| snake_abs_conv | 206,050 | +3.02% | 1 | 100% | 255 |
| snake_viper_wild | 203,265 | +1.63% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,964 | +0.48% | 0 | - | 237 |
| snake_anaconda | 200,240 | +0.12% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,800 | -0.10% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,112 | -16.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,960 (-4.02%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,417 | +1.14% |
| benchmark | +2,326 | +1.05% |
| unified | +1,553 | +0.69% |
| random_hold | +1,285 | +0.62% |
| intramonth | +1,043 | +0.49% |
| oracle | +772 | +0.36% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -504 | -0.25% |
| snake_abs | -2,797 | -1.34% |
| snake_abs_conv | -2,811 | -1.35% |
| snake_anaconda | -3,223 | -1.58% |
| snake_abs_exit_conv | -4,157 | -1.97% |
| snake_viper_tick | -4,177 | -2.05% |
| snake_viper_wild | -4,257 | -2.05% |
| snake_abs_exit | -4,567 | -2.14% |
| gold | -7,661 | -4.38% |

Average per day so far: unified Rs +689, benchmark Rs +650, intraweek Rs +403, intramonth Rs +396, oracle Rs +338, random_hold Rs +256, snake_abs_exit Rs +251, snake_abs_exit_conv Rs +197, snake_abs_conv Rs +173, snake_abs Rs +172, snake_viper_wild Rs +109, nifty_calls Rs +48, benchmark_smallcap Rs +28, snake_anaconda Rs +7, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -7, snake_nonews Rs -308, snake Rs -328, gold Rs -865

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.