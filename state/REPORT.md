# Paper trading report

Updated 2026-11-09 12:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,402 | +10.20% | 0 | - | 236 |
| benchmark | 217,319 | +8.66% | 0 | - | 237 |
| intraweek | 215,037 | +7.52% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,461 | +6.23% | 2 | 50% | 330 |
| snake_abs_exit | 212,137 | +6.07% | 2 | 50% | 308 |
| intramonth | 210,712 | +5.36% | 0 | - | 235 |
| snake_abs | 209,787 | +4.89% | 1 | 100% | 255 |
| snake_abs_conv | 209,611 | +4.81% | 1 | 100% | 255 |
| oracle | 209,473 | +4.74% | 0 | - | 233 |
| random_hold | 204,462 | +2.23% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,648 | -0.18% | 3 | 33% | 374 |
| snake_viper_wild | 199,329 | -0.34% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,688 | -0.66% | 0 | - | 237 |
| snake_viper_tick | 195,943 | -2.03% | 6 | 50% | 1,154 |
| gold | 192,561 | -3.72% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,525 (-4.74%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,792 | +2.22% |
| intraweek | +4,674 | +2.22% |
| snake_abs_conv | +4,384 | +2.14% |
| snake_abs | +4,367 | +2.13% |
| snake_abs_exit_conv | +4,040 | +1.94% |
| snake_abs_exit | +3,825 | +1.84% |
| snake_anaconda | +3,821 | +1.95% |
| oracle | +3,646 | +1.77% |
| snake_viper_wild | +3,292 | +1.68% |
| snake_viper_tick | +3,233 | +1.68% |
| intramonth | +3,109 | +1.50% |
| benchmark_smallcap | +1,894 | +0.96% |
| gold | +1,512 | +0.79% |
| random_hold | +556 | +0.27% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -168 | -0.08% |

Average per day so far: unified Rs +680, benchmark Rs +577, intraweek Rs +501, snake_abs_exit_conv Rs +462, snake_abs_exit Rs +450, intramonth Rs +357, snake_abs_conv Rs +356, snake_abs Rs +350, oracle Rs +316, random_hold Rs +149, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -14, snake_viper_wild Rs -31, benchmark_smallcap Rs -50, snake_viper_tick Rs -214, gold Rs -248, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.