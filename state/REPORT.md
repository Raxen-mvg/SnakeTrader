# Paper trading report

Updated 2026-11-20 09:24 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,848 | +12.42% | 0 | - | 236 |
| benchmark | 222,039 | +11.02% | 0 | - | 237 |
| intramonth | 214,166 | +7.08% | 0 | - | 235 |
| intraweek | 212,958 | +6.48% | 35 | 54% | 3,851 |
| oracle | 212,421 | +6.21% | 0 | - | 233 |
| snake_abs_exit | 211,353 | +5.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 209,311 | +4.66% | 2 | 50% | 345 |
| random_hold | 208,414 | +4.21% | 10 | 70% | 733 |
| snake_abs | 207,592 | +3.80% | 1 | 100% | 255 |
| snake_abs_conv | 207,458 | +3.73% | 1 | 100% | 255 |
| snake_viper_wild | 206,654 | +3.33% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,126 | +1.56% | 15 | 47% | 2,625 |
| snake_anaconda | 201,920 | +0.96% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,280 | +0.14% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,520 | -16.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,616 (-4.19%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +332 | +0.16% |
| unified | +233 | +0.10% |
| intramonth | +158 | +0.07% |
| intraweek | +69 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -39 | -0.02% |
| benchmark | -337 | -0.15% |
| snake_viper_tick | -851 | -0.42% |
| snake_viper_wild | -869 | -0.42% |
| benchmark_smallcap | -1,188 | -0.59% |
| snake_abs | -1,388 | -0.66% |
| snake_abs_conv | -1,402 | -0.67% |
| snake_anaconda | -1,543 | -0.76% |
| snake_abs_exit_conv | -1,754 | -0.83% |
| snake_abs_exit | -1,998 | -0.94% |
| gold | -8,253 | -4.72% |

Average per day so far: unified Rs +654, benchmark Rs +580, intramonth Rs +373, intraweek Rs +341, oracle Rs +327, snake_abs_exit Rs +324, snake_abs_exit_conv Rs +266, snake_viper_wild Rs +222, random_hold Rs +221, snake_abs_conv Rs +213, snake_abs Rs +211, snake_viper_tick Rs +116, snake_anaconda Rs +58, nifty_calls Rs +48, benchmark_smallcap Rs +8, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.