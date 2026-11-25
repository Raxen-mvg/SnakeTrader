# Paper trading report

Updated 2026-11-25 15:10 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,183 | +12.59% | 0 | - | 237 |
| unified | 223,929 | +11.96% | 0 | - | 236 |
| oracle | 213,178 | +6.59% | 0 | - | 233 |
| intramonth | 211,384 | +5.69% | 0 | - | 235 |
| random_hold | 209,248 | +4.62% | 12 | 75% | 1,009 |
| intraweek | 206,795 | +3.40% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,731 | +1.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,428 | +1.21% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,563 | +0.28% | 1 | 100% | 255 |
| snake_abs_conv | 200,387 | +0.19% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| snake_viper_wild | 197,774 | -1.11% | 16 | 50% | 2,827 |
| snake_anaconda | 194,731 | -2.63% | 3 | 33% | 374 |
| snake_viper_tick | 194,402 | -2.80% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,843 | -17.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,964 (-5.52%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,710 | +1.68% |
| oracle | +836 | +0.39% |
| random_hold | +822 | +0.39% |
| benchmark_smallcap | +123 | +0.06% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -356 | -0.16% |
| intramonth | -1,368 | -0.64% |
| snake_viper_tick | -3,290 | -1.66% |
| snake_viper_wild | -3,351 | -1.67% |
| snake_anaconda | -3,972 | -2.00% |
| gold | -4,587 | -2.71% |
| snake_abs_exit_conv | -4,618 | -2.23% |
| snake_abs_exit | -4,764 | -2.30% |
| intraweek | -4,824 | -2.28% |
| snake_abs | -4,898 | -2.38% |
| snake_abs_conv | -4,916 | -2.40% |

Average per day so far: benchmark Rs +630, unified Rs +598, oracle Rs +329, intramonth Rs +285, random_hold Rs +231, intraweek Rs +170, snake_abs_exit Rs +74, snake_abs_exit_conv Rs +66, nifty_calls Rs +46, snake_abs Rs +15, snake_abs_conv Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -25, snake_viper_wild Rs -70, snake_anaconda Rs -151, snake_viper_tick Rs -193, snake_nonews Rs -292, snake Rs -311, gold Rs -879

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.