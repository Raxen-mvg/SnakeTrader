# Paper trading report

Updated 2026-11-18 13:01 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,687 | +11.34% | 0 | - | 236 |
| benchmark | 219,828 | +9.91% | 0 | - | 237 |
| intraweek | 212,792 | +6.40% | 35 | 54% | 3,851 |
| intramonth | 212,560 | +6.28% | 0 | - | 235 |
| snake_abs_exit | 212,294 | +6.15% | 2 | 50% | 345 |
| oracle | 211,572 | +5.79% | 0 | - | 233 |
| snake_abs_exit_conv | 210,523 | +5.26% | 2 | 50% | 345 |
| snake_abs | 207,676 | +3.84% | 1 | 100% | 255 |
| snake_abs_conv | 207,536 | +3.77% | 1 | 100% | 255 |
| random_hold | 206,911 | +3.46% | 10 | 70% | 733 |
| snake_viper_wild | 206,756 | +3.38% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,226 | +1.61% | 15 | 47% | 2,625 |
| snake_anaconda | 202,498 | +1.25% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,248 | -0.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,910 | -11.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,989 (-4.51%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,248 | +0.56% |
| intramonth | +1,018 | +0.48% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -531 | -0.25% |
| snake_abs_exit | -848 | -0.40% |
| snake_abs | -883 | -0.42% |
| snake_abs_conv | -884 | -0.42% |
| oracle | -915 | -0.43% |
| snake_abs_exit_conv | -1,050 | -0.50% |
| benchmark_smallcap | -1,323 | -0.66% |
| random_hold | -1,521 | -0.73% |
| snake_anaconda | -1,557 | -0.76% |
| benchmark | -1,775 | -0.80% |
| snake_viper_tick | -2,611 | -1.27% |
| snake_viper_wild | -2,659 | -1.27% |
| gold | -3,814 | -2.11% |

Average per day so far: unified Rs +630, benchmark Rs +551, snake_abs_exit Rs +373, intraweek Rs +355, intramonth Rs +349, oracle Rs +321, snake_abs_exit_conv Rs +319, snake_viper_wild Rs +241, snake_abs_conv Rs +228, snake_abs Rs +226, random_hold Rs +192, snake_viper_tick Rs +129, snake_anaconda Rs +81, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -23, snake_nonews Rs -326, snake Rs -347, gold Rs -641

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.