# Paper trading report

Updated 2026-11-09 14:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,911 | +9.96% | 0 | - | 236 |
| benchmark | 217,457 | +8.73% | 0 | - | 237 |
| intraweek | 214,907 | +7.45% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,250 | +6.62% | 2 | 50% | 330 |
| snake_abs_exit | 212,714 | +6.36% | 2 | 50% | 308 |
| snake_abs | 210,127 | +5.06% | 1 | 100% | 255 |
| intramonth | 210,015 | +5.01% | 0 | - | 235 |
| snake_abs_conv | 209,959 | +4.98% | 1 | 100% | 255 |
| oracle | 209,429 | +4.71% | 0 | - | 233 |
| random_hold | 204,396 | +2.20% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,115 | +0.06% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,801 | -0.10% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,161 | -0.92% | 0 | - | 237 |
| snake_viper_tick | 196,407 | -1.80% | 6 | 50% | 1,154 |
| gold | 192,117 | -3.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,376 (-4.81%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,829 | +2.32% |
| snake_abs_conv | +4,732 | +2.31% |
| snake_abs | +4,708 | +2.29% |
| intraweek | +4,545 | +2.16% |
| snake_abs_exit | +4,402 | +2.11% |
| unified | +4,301 | +2.00% |
| snake_anaconda | +4,287 | +2.19% |
| snake_viper_wild | +3,764 | +1.92% |
| snake_viper_tick | +3,697 | +1.92% |
| oracle | +3,603 | +1.75% |
| intramonth | +2,412 | +1.16% |
| benchmark_smallcap | +1,368 | +0.69% |
| gold | +1,069 | +0.56% |
| random_hold | +490 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -31 | -0.01% |

Average per day so far: unified Rs +664, benchmark Rs +582, intraweek Rs +497, snake_abs_exit_conv Rs +491, snake_abs_exit Rs +471, snake_abs_conv Rs +369, snake_abs Rs +362, intramonth Rs +334, oracle Rs +314, random_hold Rs +147, nifty_calls Rs +61, snake_anaconda Rs +5, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -9, benchmark_smallcap Rs -71, snake_viper_tick Rs -189, gold Rs -263, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.