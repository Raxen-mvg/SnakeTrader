# Paper trading report

Updated 2026-11-25 10:28 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,287 | +12.64% | 0 | - | 236 |
| benchmark | 224,992 | +12.50% | 0 | - | 237 |
| intramonth | 212,909 | +6.46% | 0 | - | 235 |
| oracle | 212,699 | +6.35% | 0 | - | 233 |
| random_hold | 209,294 | +4.65% | 12 | 75% | 1,009 |
| intraweek | 207,782 | +3.89% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,810 | +0.91% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,240 | +0.62% | 2 | 50% | 345 |
| snake_abs | 200,983 | +0.49% | 1 | 100% | 255 |
| snake_abs_conv | 200,793 | +0.40% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,248 | -0.38% | 0 | - | 237 |
| snake_viper_wild | 195,542 | -2.23% | 16 | 50% | 2,827 |
| snake_anaconda | 193,384 | -3.31% | 3 | 33% | 374 |
| snake_viper_tick | 192,217 | -3.89% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,682 | -17.16% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,291 (-5.35%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,519 | +1.59% |
| unified | +1,002 | +0.45% |
| random_hold | +868 | +0.42% |
| oracle | +357 | +0.17% |
| benchmark_smallcap | +269 | +0.14% |
| intramonth | +158 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,748 | -2.21% |
| intraweek | -3,837 | -1.81% |
| snake_abs | -4,477 | -2.18% |
| snake_abs_conv | -4,510 | -2.20% |
| snake_anaconda | -5,319 | -2.68% |
| snake_viper_tick | -5,476 | -2.77% |
| snake_viper_wild | -5,583 | -2.78% |
| snake_abs_exit | -5,685 | -2.74% |
| snake_abs_exit_conv | -5,805 | -2.80% |

Average per day so far: unified Rs +632, benchmark Rs +625, intramonth Rs +323, oracle Rs +317, random_hold Rs +232, intraweek Rs +195, snake_abs_exit Rs +49, nifty_calls Rs +46, snake_abs_exit_conv Rs +34, snake_abs Rs +26, snake_abs_conv Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -21, snake_viper_wild Rs -139, snake_anaconda Rs -189, snake_viper_tick Rs -268, snake_nonews Rs -292, snake Rs -311, gold Rs -858

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.