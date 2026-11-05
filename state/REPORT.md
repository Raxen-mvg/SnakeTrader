# Paper trading report

Updated 2026-11-05 11:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,867 | +9.43% | 0 | - | 236 |
| snake_abs_exit_conv | 215,356 | +7.68% | 1 | 100% | 255 |
| snake_abs_exit | 215,061 | +7.53% | 1 | 100% | 260 |
| benchmark | 212,469 | +6.24% | 0 | - | 237 |
| snake_abs | 212,230 | +6.12% | 1 | 100% | 255 |
| snake_abs_conv | 212,093 | +6.05% | 1 | 100% | 255 |
| intraweek | 211,021 | +5.51% | 25 | 48% | 2,757 |
| intramonth | 210,583 | +5.29% | 0 | - | 235 |
| snake_viper_wild | 207,406 | +3.70% | 3 | 33% | 702 |
| random_hold | 207,071 | +3.54% | 8 | 62% | 649 |
| oracle | 204,492 | +2.25% | 0 | - | 233 |
| snake_viper_tick | 203,849 | +1.92% | 2 | 0% | 532 |
| snake_anaconda | 203,320 | +1.66% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,282 | -0.36% | 0 | - | 237 |
| gold | 193,613 | -3.19% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,803 (-4.60%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,427 | +2.06% |
| random_hold | +3,762 | +1.85% |
| benchmark | +3,710 | +1.78% |
| intramonth | +3,567 | +1.72% |
| oracle | +2,700 | +1.34% |
| benchmark_smallcap | +2,612 | +1.33% |
| gold | +2,219 | +1.16% |
| intraweek | +1,323 | +0.63% |
| snake_abs_exit_conv | +341 | +0.16% |
| snake_abs_conv | +335 | +0.16% |
| snake_abs | +327 | +0.15% |
| snake_abs_exit | +160 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -501 | -0.25% |
| snake_viper_tick | -1,552 | -0.76% |
| snake_viper_wild | -1,624 | -0.78% |

Average per day so far: unified Rs +674, snake_abs_exit_conv Rs +614, snake_abs_exit Rs +602, snake_abs_conv Rs +484, snake_abs Rs +470, benchmark Rs +445, intraweek Rs +394, intramonth Rs +378, snake_viper_wild Rs +370, random_hold Rs +253, snake_viper_tick Rs +226, oracle Rs +160, snake_anaconda Rs +144, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -30, gold Rs -228, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.