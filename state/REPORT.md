# Paper trading report

Updated 2026-11-27 14:58 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,093 | +12.05% | 0 | - | 236 |
| benchmark | 223,791 | +11.90% | 0 | - | 237 |
| oracle | 212,229 | +6.12% | 0 | - | 233 |
| intramonth | 211,541 | +5.77% | 0 | - | 235 |
| random_hold | 211,199 | +5.60% | 13 | 69% | 1,037 |
| intraweek | 208,030 | +4.01% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,608 | +3.30% | 2 | 50% | 345 |
| snake_abs_exit | 204,341 | +2.17% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,603 | +0.80% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,806 | -0.10% | 1 | 100% | 255 |
| snake_abs_conv | 199,622 | -0.19% | 1 | 100% | 255 |
| snake_anaconda | 193,249 | -3.38% | 3 | 33% | 374 |
| snake_viper_wild | 192,289 | -3.86% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,023 | -5.49% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 171,074 | -14.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,232 (-5.38%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,211 | +3.10% |
| gold | +5,080 | +3.06% |
| snake_abs_exit | +3,264 | +1.62% |
| random_hold | +2,605 | +1.25% |
| snake_abs_conv | +1,255 | +0.63% |
| snake_abs | +1,254 | +0.63% |
| unified | +1,014 | +0.46% |
| intramonth | +1,008 | +0.48% |
| intraweek | +981 | +0.47% |
| snake_anaconda | +953 | +0.49% |
| benchmark_smallcap | +762 | +0.38% |
| snake_viper_wild | +83 | +0.04% |
| snake_viper_tick | +82 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -6 | -0.00% |
| benchmark | -2,196 | -0.97% |

Average per day so far: unified Rs +574, benchmark Rs +566, oracle Rs +291, intramonth Rs +275, random_hold Rs +267, intraweek Rs +191, snake_abs_exit_conv Rs +169, snake_abs_exit Rs +111, nifty_calls Rs +44, benchmark_smallcap Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -5, snake_abs_conv Rs -10, snake_anaconda Rs -182, snake_viper_wild Rs -227, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -354, gold Rs -689

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.