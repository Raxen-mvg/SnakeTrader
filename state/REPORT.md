# Paper trading report

Updated 2026-11-25 14:46 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,510 | +12.26% | 0 | - | 237 |
| unified | 224,433 | +12.22% | 0 | - | 236 |
| oracle | 213,034 | +6.52% | 0 | - | 233 |
| intramonth | 211,934 | +5.97% | 0 | - | 235 |
| random_hold | 209,855 | +4.93% | 12 | 75% | 1,009 |
| intraweek | 207,063 | +3.53% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,556 | +0.78% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,235 | +0.62% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,626 | -0.19% | 1 | 100% | 255 |
| snake_abs_conv | 199,431 | -0.28% | 1 | 100% | 255 |
| benchmark_smallcap | 199,035 | -0.48% | 0 | - | 237 |
| snake_viper_wild | 197,433 | -1.28% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,069 | -2.97% | 15 | 47% | 2,625 |
| snake_anaconda | 193,504 | -3.25% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,188 | -17.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,000 (-5.50%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,037 | +1.37% |
| random_hold | +1,429 | +0.69% |
| oracle | +692 | +0.33% |
| unified | +148 | +0.07% |
| benchmark_smallcap | +56 | +0.03% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -817 | -0.38% |
| snake_viper_tick | -3,624 | -1.83% |
| snake_viper_wild | -3,691 | -1.83% |
| gold | -4,242 | -2.50% |
| intraweek | -4,556 | -2.15% |
| snake_anaconda | -5,199 | -2.62% |
| snake_abs_exit_conv | -5,811 | -2.81% |
| snake_abs | -5,835 | -2.84% |
| snake_abs_conv | -5,871 | -2.86% |
| snake_abs_exit | -5,939 | -2.86% |

Average per day so far: benchmark Rs +613, unified Rs +611, oracle Rs +326, intramonth Rs +298, random_hold Rs +246, intraweek Rs +177, nifty_calls Rs +46, snake_abs_exit Rs +42, snake_abs_exit_conv Rs +33, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -10, snake_abs_conv Rs -15, benchmark_smallcap Rs -27, snake_viper_wild Rs -80, snake_anaconda Rs -186, snake_viper_tick Rs -205, snake_nonews Rs -292, snake Rs -311, gold Rs -870

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.