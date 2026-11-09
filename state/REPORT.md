# Paper trading report

Updated 2026-11-09 12:18 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,195 | +10.10% | 0 | - | 236 |
| benchmark | 217,319 | +8.66% | 0 | - | 237 |
| intraweek | 214,270 | +7.13% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,342 | +6.17% | 2 | 50% | 330 |
| snake_abs_exit | 211,957 | +5.98% | 2 | 50% | 308 |
| intramonth | 210,438 | +5.22% | 0 | - | 235 |
| snake_abs | 209,729 | +4.86% | 1 | 100% | 255 |
| snake_abs_conv | 209,552 | +4.78% | 1 | 100% | 255 |
| oracle | 209,490 | +4.75% | 0 | - | 233 |
| random_hold | 204,530 | +2.27% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,423 | -0.29% | 3 | 33% | 374 |
| snake_viper_wild | 199,154 | -0.42% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,733 | -0.63% | 0 | - | 237 |
| snake_viper_tick | 195,770 | -2.12% | 6 | 50% | 1,154 |
| gold | 192,758 | -3.62% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,295 (-4.85%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,585 | +2.13% |
| snake_abs_conv | +4,325 | +2.11% |
| snake_abs | +4,309 | +2.10% |
| snake_abs_exit_conv | +3,921 | +1.88% |
| intraweek | +3,908 | +1.86% |
| oracle | +3,663 | +1.78% |
| snake_abs_exit | +3,645 | +1.75% |
| snake_anaconda | +3,595 | +1.84% |
| snake_viper_wild | +3,117 | +1.59% |
| snake_viper_tick | +3,061 | +1.59% |
| intramonth | +2,835 | +1.37% |
| benchmark_smallcap | +1,939 | +0.98% |
| gold | +1,710 | +0.90% |
| random_hold | +624 | +0.31% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -168 | -0.08% |

Average per day so far: unified Rs +673, benchmark Rs +577, intraweek Rs +476, snake_abs_exit_conv Rs +457, snake_abs_exit Rs +443, snake_abs_conv Rs +354, intramonth Rs +348, snake_abs Rs +347, oracle Rs +316, random_hold Rs +151, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -23, snake_viper_wild Rs -38, benchmark_smallcap Rs -49, snake_viper_tick Rs -223, gold Rs -241, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.