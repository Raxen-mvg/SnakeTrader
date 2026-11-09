# Paper trading report

Updated 2026-11-09 14:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,211 | +10.11% | 0 | - | 236 |
| benchmark | 217,924 | +8.96% | 0 | - | 237 |
| intraweek | 214,186 | +7.09% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,777 | +6.39% | 2 | 50% | 330 |
| snake_abs_exit | 212,714 | +6.36% | 2 | 50% | 308 |
| intramonth | 210,263 | +5.13% | 0 | - | 235 |
| snake_abs | 209,951 | +4.97% | 1 | 100% | 255 |
| snake_abs_conv | 209,785 | +4.89% | 1 | 100% | 255 |
| oracle | 209,366 | +4.68% | 0 | - | 233 |
| random_hold | 204,452 | +2.23% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,115 | +0.06% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,376 | -0.81% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,262 | -0.87% | 0 | - | 237 |
| snake_viper_tick | 195,008 | -2.50% | 6 | 50% | 1,154 |
| gold | 191,986 | -4.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,289 (-4.86%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,602 | +2.13% |
| snake_abs_conv | +4,558 | +2.22% |
| snake_abs | +4,531 | +2.21% |
| snake_abs_exit | +4,402 | +2.11% |
| snake_abs_exit_conv | +4,356 | +2.09% |
| snake_anaconda | +4,288 | +2.19% |
| intraweek | +3,823 | +1.82% |
| oracle | +3,539 | +1.72% |
| intramonth | +2,660 | +1.28% |
| snake_viper_wild | +2,338 | +1.19% |
| snake_viper_tick | +2,298 | +1.19% |
| benchmark_smallcap | +1,469 | +0.75% |
| gold | +937 | +0.49% |
| random_hold | +545 | +0.27% |
| benchmark | +436 | +0.20% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +674, benchmark Rs +597, snake_abs_exit_conv Rs +473, intraweek Rs +473, snake_abs_exit Rs +471, snake_abs_conv Rs +362, snake_abs Rs +355, intramonth Rs +342, oracle Rs +312, random_hold Rs +148, nifty_calls Rs +61, snake_anaconda Rs +5, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -67, snake_viper_wild Rs -74, snake_viper_tick Rs -263, gold Rs -267, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.