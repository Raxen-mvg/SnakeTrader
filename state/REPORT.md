# Paper trading report

Updated 2026-11-09 13:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,809 | +9.90% | 0 | - | 236 |
| benchmark | 216,914 | +8.46% | 0 | - | 237 |
| intraweek | 214,560 | +7.28% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,973 | +6.49% | 2 | 50% | 330 |
| snake_abs_exit | 212,561 | +6.28% | 2 | 50% | 308 |
| intramonth | 209,937 | +4.97% | 0 | - | 235 |
| snake_abs | 209,762 | +4.88% | 1 | 100% | 255 |
| snake_abs_conv | 209,597 | +4.80% | 1 | 100% | 255 |
| oracle | 209,495 | +4.75% | 0 | - | 233 |
| random_hold | 204,358 | +2.18% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,065 | +0.03% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,686 | -0.16% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,363 | -0.82% | 0 | - | 237 |
| snake_viper_tick | 196,294 | -1.85% | 6 | 50% | 1,154 |
| gold | 191,969 | -4.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,247 (-4.88%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,551 | +2.18% |
| snake_abs_conv | +4,370 | +2.13% |
| snake_abs | +4,343 | +2.11% |
| snake_abs_exit | +4,249 | +2.04% |
| snake_anaconda | +4,238 | +2.16% |
| unified | +4,200 | +1.95% |
| intraweek | +4,198 | +2.00% |
| oracle | +3,669 | +1.78% |
| snake_viper_wild | +3,649 | +1.86% |
| snake_viper_tick | +3,584 | +1.86% |
| intramonth | +2,334 | +1.12% |
| benchmark_smallcap | +1,569 | +0.80% |
| gold | +921 | +0.48% |
| random_hold | +452 | +0.22% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -574 | -0.26% |

Average per day so far: unified Rs +660, benchmark Rs +564, intraweek Rs +485, snake_abs_exit_conv Rs +480, snake_abs_exit Rs +465, snake_abs_conv Rs +355, snake_abs Rs +349, intramonth Rs +331, oracle Rs +317, random_hold Rs +145, nifty_calls Rs +61, snake_anaconda Rs +3, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -14, benchmark_smallcap Rs -63, snake_viper_tick Rs -195, gold Rs -268, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.