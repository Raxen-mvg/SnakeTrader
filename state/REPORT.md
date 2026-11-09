# Paper trading report

Updated 2026-11-09 14:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,038 | +10.02% | 0 | - | 236 |
| benchmark | 217,970 | +8.98% | 0 | - | 237 |
| intraweek | 214,520 | +7.26% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,698 | +6.35% | 2 | 50% | 330 |
| snake_abs_exit | 212,677 | +6.34% | 2 | 50% | 308 |
| intramonth | 210,085 | +5.04% | 0 | - | 235 |
| snake_abs | 210,036 | +5.02% | 1 | 100% | 255 |
| snake_abs_conv | 209,869 | +4.93% | 1 | 100% | 255 |
| oracle | 209,167 | +4.58% | 0 | - | 233 |
| random_hold | 204,446 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,067 | +0.03% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,334 | -0.83% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,150 | -0.93% | 0 | - | 237 |
| snake_viper_tick | 194,967 | -2.52% | 6 | 50% | 1,154 |
| gold | 192,002 | -4.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,277 (-4.86%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,642 | +2.26% |
| snake_abs | +4,616 | +2.25% |
| unified | +4,428 | +2.05% |
| snake_abs_exit | +4,365 | +2.10% |
| snake_abs_exit_conv | +4,277 | +2.05% |
| snake_anaconda | +4,240 | +2.17% |
| intraweek | +4,158 | +1.98% |
| oracle | +3,340 | +1.62% |
| intramonth | +2,482 | +1.20% |
| snake_viper_wild | +2,297 | +1.17% |
| snake_viper_tick | +2,258 | +1.17% |
| benchmark_smallcap | +1,356 | +0.69% |
| gold | +954 | +0.50% |
| random_hold | +539 | +0.27% |
| benchmark | +482 | +0.22% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +668, benchmark Rs +599, intraweek Rs +484, snake_abs_exit_conv Rs +470, snake_abs_exit Rs +470, snake_abs_conv Rs +366, snake_abs Rs +358, intramonth Rs +336, oracle Rs +306, random_hold Rs +148, nifty_calls Rs +61, snake_anaconda Rs +3, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -71, snake_viper_wild Rs -76, snake_viper_tick Rs -265, gold Rs -267, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.