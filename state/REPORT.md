# Paper trading report

Updated 2026-11-26 11:47 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,620 | +12.81% | 0 | - | 237 |
| unified | 223,132 | +11.57% | 0 | - | 236 |
| oracle | 213,040 | +6.52% | 0 | - | 233 |
| intramonth | 210,398 | +5.20% | 0 | - | 235 |
| random_hold | 209,799 | +4.90% | 13 | 69% | 1,037 |
| intraweek | 208,602 | +4.30% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 200,949 | +0.47% | 2 | 50% | 345 |
| benchmark_smallcap | 200,526 | +0.26% | 0 | - | 237 |
| snake_abs_exit_conv | 200,418 | +0.21% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,734 | -0.63% | 1 | 100% | 255 |
| snake_abs_conv | 198,545 | -0.73% | 1 | 100% | 255 |
| snake_anaconda | 192,618 | -3.69% | 3 | 33% | 374 |
| snake_viper_wild | 192,215 | -3.89% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,951 | -5.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,928 | -17.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,772 (-5.61%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,858 | +0.90% |
| benchmark_smallcap | +1,715 | +0.86% |
| gold | +1,332 | +0.81% |
| benchmark | +597 | +0.27% |
| random_hold | +307 | +0.15% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -756 | -0.35% |
| unified | -968 | -0.43% |
| intramonth | -1,295 | -0.61% |
| snake_abs_exit | -1,306 | -0.65% |
| snake_abs | -1,416 | -0.71% |
| snake_abs_conv | -1,427 | -0.71% |
| snake_abs_exit_conv | -1,558 | -0.77% |
| snake_anaconda | -1,935 | -0.99% |
| snake_viper_tick | -5,226 | -2.69% |
| snake_viper_wild | -5,328 | -2.70% |

Average per day so far: benchmark Rs +625, unified Rs +564, oracle Rs +318, intramonth Rs +254, random_hold Rs +239, intraweek Rs +210, nifty_calls Rs +45, snake_abs_exit Rs +25, benchmark_smallcap Rs +14, snake_abs_exit_conv Rs +11, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -32, snake_abs_conv Rs -38, snake_anaconda Rs -205, snake_viper_wild Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -831

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.