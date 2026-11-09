# Paper trading report

Updated 2026-11-09 12:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,059 | +10.03% | 0 | - | 236 |
| benchmark | 217,120 | +8.56% | 0 | - | 237 |
| intraweek | 214,706 | +7.35% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,673 | +6.34% | 2 | 50% | 330 |
| snake_abs_exit | 212,304 | +6.15% | 2 | 50% | 308 |
| intramonth | 210,223 | +5.11% | 0 | - | 235 |
| snake_abs | 210,115 | +5.06% | 1 | 100% | 255 |
| snake_abs_conv | 209,941 | +4.97% | 1 | 100% | 255 |
| oracle | 209,472 | +4.74% | 0 | - | 233 |
| random_hold | 204,468 | +2.23% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,756 | -0.12% | 3 | 33% | 374 |
| snake_viper_wild | 199,340 | -0.33% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,520 | -0.74% | 0 | - | 237 |
| snake_viper_tick | 195,954 | -2.02% | 6 | 50% | 1,154 |
| gold | 192,577 | -3.71% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,369 (-4.82%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,714 | +2.30% |
| snake_abs | +4,696 | +2.29% |
| unified | +4,449 | +2.06% |
| intraweek | +4,344 | +2.06% |
| snake_abs_exit_conv | +4,251 | +2.04% |
| snake_abs_exit | +3,992 | +1.92% |
| snake_anaconda | +3,929 | +2.01% |
| oracle | +3,645 | +1.77% |
| snake_viper_wild | +3,302 | +1.69% |
| snake_viper_tick | +3,244 | +1.68% |
| intramonth | +2,620 | +1.26% |
| benchmark_smallcap | +1,726 | +0.88% |
| gold | +1,529 | +0.80% |
| random_hold | +562 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -367 | -0.17% |

Average per day so far: unified Rs +669, benchmark Rs +571, intraweek Rs +490, snake_abs_exit_conv Rs +469, snake_abs_exit Rs +456, snake_abs_conv Rs +368, snake_abs Rs +361, intramonth Rs +341, oracle Rs +316, random_hold Rs +149, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -10, snake_viper_wild Rs -30, benchmark_smallcap Rs -57, snake_viper_tick Rs -213, gold Rs -247, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.