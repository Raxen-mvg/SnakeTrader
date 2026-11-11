# Paper trading report

Updated 2026-11-11 11:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,290 | +10.64% | 0 | - | 237 |
| unified | 220,825 | +10.41% | 0 | - | 236 |
| snake_abs_exit_conv | 216,145 | +8.07% | 2 | 50% | 345 |
| snake_abs_exit | 214,728 | +7.36% | 2 | 50% | 345 |
| intraweek | 214,558 | +7.28% | 30 | 53% | 3,302 |
| snake_abs | 212,532 | +6.27% | 1 | 100% | 255 |
| snake_abs_conv | 212,380 | +6.19% | 1 | 100% | 255 |
| oracle | 211,960 | +5.98% | 0 | - | 233 |
| intramonth | 211,656 | +5.83% | 0 | - | 235 |
| random_hold | 206,924 | +3.46% | 9 | 67% | 709 |
| snake_anaconda | 202,527 | +1.26% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_viper_wild | 201,120 | +0.56% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,703 | -1.15% | 9 | 44% | 1,639 |
| gold | 190,046 | -4.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,439 (-4.28%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,236 | +2.00% |
| snake_viper_wild | +3,690 | +1.87% |
| snake_viper_tick | +3,627 | +1.87% |
| benchmark_smallcap | +3,509 | +1.77% |
| benchmark | +3,198 | +1.47% |
| snake_anaconda | +3,060 | +1.53% |
| snake_abs_conv | +2,903 | +1.39% |
| snake_abs | +2,885 | +1.38% |
| snake_abs_exit | +2,744 | +1.29% |
| oracle | +2,042 | +0.97% |
| random_hold | +1,963 | +0.96% |
| unified | +1,078 | +0.49% |
| intramonth | +1,047 | +0.50% |
| intraweek | +16 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,088 | -1.09% |

Average per day so far: benchmark Rs +687, unified Rs +672, snake_abs_exit_conv Rs +577, snake_abs_exit Rs +526, intraweek Rs +470, snake_abs_conv Rs +442, snake_abs Rs +432, oracle Rs +386, intramonth Rs +376, random_hold Rs +223, snake_anaconda Rs +97, benchmark_smallcap Rs +62, nifty_calls Rs +59, snake_viper_wild Rs +49, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -115, gold Rs -321, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.