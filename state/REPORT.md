# Paper trading report

Updated 2026-11-18 09:24 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,380 | +10.69% | 0 | - | 236 |
| benchmark | 221,198 | +10.60% | 0 | - | 237 |
| snake_abs_exit | 213,530 | +6.76% | 2 | 50% | 345 |
| intraweek | 212,952 | +6.48% | 35 | 54% | 3,851 |
| oracle | 212,488 | +6.24% | 0 | - | 233 |
| snake_abs_exit_conv | 211,740 | +5.87% | 2 | 50% | 345 |
| intramonth | 211,365 | +5.68% | 0 | - | 235 |
| snake_abs | 208,808 | +4.40% | 1 | 100% | 255 |
| snake_abs_conv | 208,667 | +4.33% | 1 | 100% | 255 |
| snake_viper_wild | 207,982 | +3.99% | 14 | 50% | 2,496 |
| random_hold | 207,466 | +3.73% | 10 | 70% | 733 |
| snake_viper_tick | 204,426 | +2.21% | 13 | 46% | 2,299 |
| snake_anaconda | 203,846 | +1.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,470 | +0.23% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,222 | -11.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,923 (-4.54%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +388 | +0.18% |
| snake_abs | +249 | +0.12% |
| snake_abs_conv | +248 | +0.12% |
| snake_abs_exit_conv | +167 | +0.08% |
| oracle | +2 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -59 | -0.03% |
| benchmark_smallcap | -101 | -0.05% |
| intramonth | -177 | -0.08% |
| snake_anaconda | -209 | -0.10% |
| intraweek | -371 | -0.17% |
| benchmark | -405 | -0.18% |
| random_hold | -966 | -0.46% |
| snake_viper_tick | -1,410 | -0.69% |
| snake_viper_wild | -1,434 | -0.69% |
| gold | -3,502 | -1.94% |

Average per day so far: unified Rs +594, benchmark Rs +589, snake_abs_exit Rs +410, intraweek Rs +360, snake_abs_exit_conv Rs +356, oracle Rs +347, intramonth Rs +316, snake_viper_wild Rs +285, snake_abs_conv Rs +263, snake_abs Rs +259, random_hold Rs +207, snake_viper_tick Rs +177, snake_anaconda Rs +124, nifty_calls Rs +51, benchmark_smallcap Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -633

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.