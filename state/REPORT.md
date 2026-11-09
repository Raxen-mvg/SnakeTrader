# Paper trading report

Updated 2026-11-09 13:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,826 | +9.91% | 0 | - | 236 |
| benchmark | 217,166 | +8.58% | 0 | - | 237 |
| intraweek | 214,616 | +7.31% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,958 | +6.48% | 2 | 50% | 330 |
| snake_abs_exit | 212,510 | +6.25% | 2 | 50% | 308 |
| intramonth | 209,923 | +4.96% | 0 | - | 235 |
| snake_abs | 209,718 | +4.86% | 1 | 100% | 255 |
| snake_abs_conv | 209,554 | +4.78% | 1 | 100% | 255 |
| oracle | 209,503 | +4.75% | 0 | - | 233 |
| random_hold | 204,304 | +2.15% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,019 | +0.01% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,661 | -0.17% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,307 | -0.85% | 0 | - | 237 |
| snake_viper_tick | 196,269 | -1.87% | 6 | 50% | 1,154 |
| gold | 192,183 | -3.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,250 (-4.87%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,537 | +2.18% |
| snake_abs_conv | +4,327 | +2.11% |
| snake_abs | +4,299 | +2.09% |
| intraweek | +4,253 | +2.02% |
| unified | +4,217 | +1.96% |
| snake_abs_exit | +4,198 | +2.02% |
| snake_anaconda | +4,192 | +2.14% |
| oracle | +3,676 | +1.79% |
| snake_viper_wild | +3,624 | +1.85% |
| snake_viper_tick | +3,559 | +1.85% |
| intramonth | +2,320 | +1.12% |
| benchmark_smallcap | +1,513 | +0.77% |
| gold | +1,134 | +0.59% |
| random_hold | +397 | +0.20% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -321 | -0.15% |

Average per day so far: unified Rs +661, benchmark Rs +572, intraweek Rs +487, snake_abs_exit_conv Rs +480, snake_abs_exit Rs +463, snake_abs_conv Rs +354, snake_abs Rs +347, intramonth Rs +331, oracle Rs +317, random_hold Rs +143, nifty_calls Rs +61, snake_anaconda Rs +1, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -15, benchmark_smallcap Rs -65, snake_viper_tick Rs -196, gold Rs -261, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.