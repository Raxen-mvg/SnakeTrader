# Paper trading report

Updated 2026-11-23 12:37 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,820 | +11.91% | 0 | - | 236 |
| benchmark | 222,873 | +11.44% | 0 | - | 237 |
| intraweek | 212,281 | +6.14% | 40 | 55% | 4,400 |
| oracle | 211,768 | +5.88% | 0 | - | 233 |
| intramonth | 211,680 | +5.84% | 0 | - | 235 |
| random_hold | 208,693 | +4.35% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,004 | +3.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,749 | +2.88% | 2 | 50% | 345 |
| snake_abs | 204,754 | +2.38% | 1 | 100% | 255 |
| snake_abs_conv | 204,590 | +2.29% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,927 | +0.46% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_anaconda | 198,207 | -0.90% | 3 | 33% | 374 |
| snake_viper_tick | 197,500 | -1.25% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,137 | -14.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,036 (-4.98%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,088 | +1.24% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -710 | -0.33% |
| snake_abs_exit_conv | -867 | -0.42% |
| snake_abs | -1,166 | -0.57% |
| snake_abs_conv | -1,192 | -0.58% |
| benchmark_smallcap | -1,356 | -0.68% |
| snake_abs_exit | -1,558 | -0.75% |
| snake_anaconda | -1,699 | -0.85% |
| snake_viper_tick | -1,872 | -0.94% |
| snake_viper_wild | -1,902 | -0.94% |
| random_hold | -2,066 | -0.98% |
| benchmark | -2,264 | -1.01% |
| unified | -2,362 | -1.04% |
| intramonth | -3,324 | -1.55% |
| intraweek | -3,431 | -1.59% |

Average per day so far: unified Rs +611, benchmark Rs +586, intraweek Rs +315, oracle Rs +302, intramonth Rs +299, random_hold Rs +223, snake_abs_exit Rs +195, snake_abs_exit_conv Rs +160, snake_abs Rs +128, snake_abs_conv Rs +128, nifty_calls Rs +47, snake_viper_wild Rs +30, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -53, snake_viper_tick Rs -89, snake_nonews Rs -300, snake Rs -320, gold Rs -766

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.