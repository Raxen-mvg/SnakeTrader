# Paper trading report

Updated 2026-11-19 10:49 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,924 | +11.96% | 0 | - | 236 |
| benchmark | 220,800 | +10.40% | 0 | - | 237 |
| snake_abs_exit | 213,714 | +6.86% | 2 | 50% | 345 |
| intramonth | 213,455 | +6.73% | 0 | - | 235 |
| intraweek | 212,053 | +6.03% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,822 | +5.91% | 2 | 50% | 345 |
| oracle | 211,182 | +5.59% | 0 | - | 233 |
| snake_abs | 209,449 | +4.72% | 1 | 100% | 255 |
| snake_abs_conv | 209,325 | +4.66% | 1 | 100% | 255 |
| random_hold | 207,693 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 207,556 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,010 | +2.00% | 15 | 47% | 2,625 |
| snake_anaconda | 203,580 | +1.79% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,806 | -12.60% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,345 (-4.33%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,313 | +0.59% |
| intramonth | +1,181 | +0.56% |
| benchmark_smallcap | +1,065 | +0.53% |
| random_hold | +761 | +0.37% |
| snake_viper_wild | +517 | +0.25% |
| snake_viper_tick | +507 | +0.25% |
| benchmark | +505 | +0.23% |
| oracle | +386 | +0.18% |
| intraweek | +213 | +0.10% |
| snake_abs | +12 | +0.01% |
| snake_abs_conv | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -318 | -0.15% |
| snake_abs_exit_conv | -561 | -0.26% |
| snake_anaconda | -821 | -0.40% |
| gold | -2,515 | -1.42% |

Average per day so far: unified Rs +647, benchmark Rs +562, snake_abs_exit Rs +403, intramonth Rs +364, snake_abs_exit_conv Rs +348, intraweek Rs +326, oracle Rs +302, snake_abs_conv Rs +274, snake_abs Rs +270, snake_viper_wild Rs +261, random_hold Rs +208, snake_viper_tick Rs +154, snake_anaconda Rs +112, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -681

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.