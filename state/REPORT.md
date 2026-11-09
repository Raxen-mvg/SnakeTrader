# Paper trading report

Updated 2026-11-09 14:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,285 | +10.14% | 0 | - | 236 |
| benchmark | 218,000 | +9.00% | 0 | - | 237 |
| intraweek | 214,418 | +7.21% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,852 | +6.43% | 2 | 50% | 330 |
| snake_abs_exit | 212,721 | +6.36% | 2 | 50% | 308 |
| intramonth | 210,322 | +5.16% | 0 | - | 235 |
| snake_abs | 210,104 | +5.05% | 1 | 100% | 255 |
| snake_abs_conv | 209,937 | +4.97% | 1 | 100% | 255 |
| oracle | 209,488 | +4.74% | 0 | - | 233 |
| random_hold | 204,526 | +2.26% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,127 | +0.06% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,483 | -0.76% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,195 | -0.90% | 0 | - | 237 |
| snake_viper_tick | 195,113 | -2.44% | 6 | 50% | 1,154 |
| gold | 191,986 | -4.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,389 (-4.81%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,710 | +2.29% |
| snake_abs | +4,685 | +2.28% |
| unified | +4,676 | +2.17% |
| snake_abs_exit_conv | +4,430 | +2.12% |
| snake_abs_exit | +4,409 | +2.12% |
| snake_anaconda | +4,300 | +2.20% |
| intraweek | +4,055 | +1.93% |
| oracle | +3,661 | +1.78% |
| intramonth | +2,719 | +1.31% |
| snake_viper_wild | +2,446 | +1.25% |
| snake_viper_tick | +2,403 | +1.25% |
| benchmark_smallcap | +1,401 | +0.71% |
| gold | +937 | +0.49% |
| random_hold | +619 | +0.30% |
| benchmark | +513 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +676, benchmark Rs +600, intraweek Rs +481, snake_abs_exit_conv Rs +476, snake_abs_exit Rs +471, snake_abs_conv Rs +368, snake_abs Rs +361, intramonth Rs +344, oracle Rs +316, random_hold Rs +151, nifty_calls Rs +61, snake_anaconda Rs +5, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -69, benchmark_smallcap Rs -69, snake_viper_tick Rs -257, gold Rs -267, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.