# Paper trading report

Updated 2026-11-09 14:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,034 | +10.02% | 0 | - | 236 |
| benchmark | 218,031 | +9.02% | 0 | - | 237 |
| intraweek | 214,284 | +7.14% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,513 | +6.26% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,419 | +6.21% | 2 | 50% | 330 |
| intramonth | 209,969 | +4.99% | 0 | - | 235 |
| snake_abs | 209,876 | +4.94% | 1 | 100% | 255 |
| snake_abs_conv | 209,710 | +4.86% | 1 | 100% | 255 |
| oracle | 209,259 | +4.63% | 0 | - | 233 |
| random_hold | 204,395 | +2.20% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,927 | -0.04% | 3 | 33% | 374 |
| benchmark_smallcap | 198,307 | -0.85% | 0 | - | 237 |
| snake_viper_wild | 197,986 | -1.01% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,625 | -2.69% | 6 | 50% | 1,154 |
| gold | 192,051 | -3.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,196 (-4.90%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,483 | +2.19% |
| snake_abs | +4,457 | +2.17% |
| unified | +4,425 | +2.05% |
| snake_abs_exit | +4,201 | +2.02% |
| snake_anaconda | +4,100 | +2.09% |
| snake_abs_exit_conv | +3,997 | +1.92% |
| intraweek | +3,921 | +1.86% |
| oracle | +3,432 | +1.67% |
| intramonth | +2,366 | +1.14% |
| snake_viper_wild | +1,949 | +0.99% |
| snake_viper_tick | +1,915 | +0.99% |
| benchmark_smallcap | +1,513 | +0.77% |
| gold | +1,003 | +0.53% |
| benchmark | +543 | +0.25% |
| random_hold | +488 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +668, benchmark Rs +601, intraweek Rs +476, snake_abs_exit Rs +463, snake_abs_exit_conv Rs +460, snake_abs_conv Rs +360, snake_abs Rs +353, intramonth Rs +332, oracle Rs +309, random_hold Rs +146, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -3, benchmark_smallcap Rs -65, snake_viper_wild Rs -92, gold Rs -265, snake_viper_tick Rs -283, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.