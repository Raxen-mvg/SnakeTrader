# Paper trading report

Updated 2026-11-18 09:52 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,865 | +10.93% | 0 | - | 236 |
| benchmark | 220,364 | +10.18% | 0 | - | 237 |
| intraweek | 213,723 | +6.86% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,628 | +6.31% | 2 | 50% | 345 |
| oracle | 211,982 | +5.99% | 0 | - | 233 |
| intramonth | 211,803 | +5.90% | 0 | - | 235 |
| snake_abs_exit_conv | 211,170 | +5.58% | 2 | 50% | 345 |
| snake_abs | 208,497 | +4.25% | 1 | 100% | 255 |
| snake_abs_conv | 208,351 | +4.18% | 1 | 100% | 255 |
| random_hold | 207,194 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 206,868 | +3.43% | 16 | 50% | 2,827 |
| snake_anaconda | 203,339 | +1.67% | 3 | 33% | 374 |
| snake_viper_tick | 203,335 | +1.67% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,843 | -0.08% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,469 | -11.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,011 (-4.49%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +426 | +0.19% |
| intraweek | +400 | +0.19% |
| intramonth | +260 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -61 | -0.03% |
| snake_abs_conv | -68 | -0.03% |
| snake_abs_exit_conv | -403 | -0.19% |
| oracle | -505 | -0.24% |
| snake_abs_exit | -513 | -0.24% |
| snake_anaconda | -716 | -0.35% |
| benchmark_smallcap | -729 | -0.36% |
| random_hold | -1,238 | -0.59% |
| benchmark | -1,239 | -0.56% |
| snake_viper_tick | -2,501 | -1.22% |
| snake_viper_wild | -2,547 | -1.22% |
| gold | -3,255 | -1.80% |

Average per day so far: unified Rs +607, benchmark Rs +566, snake_abs_exit Rs +383, intraweek Rs +381, snake_abs_exit_conv Rs +338, oracle Rs +333, intramonth Rs +328, snake_abs_conv Rs +253, snake_abs Rs +250, snake_viper_wild Rs +245, random_hold Rs +200, snake_viper_tick Rs +133, snake_anaconda Rs +108, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -5, snake_nonews Rs -326, snake Rs -347, gold Rs -626

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.