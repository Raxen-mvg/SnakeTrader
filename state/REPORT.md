# Paper trading report

Updated 2026-11-27 12:04 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,656 | +12.33% | 0 | - | 237 |
| unified | 222,596 | +11.30% | 0 | - | 236 |
| oracle | 211,773 | +5.89% | 0 | - | 233 |
| intramonth | 210,541 | +5.27% | 0 | - | 235 |
| random_hold | 210,111 | +5.06% | 13 | 69% | 1,037 |
| intraweek | 207,775 | +3.89% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,316 | +2.66% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,061 | +2.03% | 2 | 50% | 345 |
| benchmark_smallcap | 202,006 | +1.00% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,677 | +0.34% | 1 | 100% | 255 |
| snake_abs_conv | 200,502 | +0.25% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,107 | -2.95% | 3 | 33% | 374 |
| snake_viper_wild | 192,601 | -3.70% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,329 | -5.34% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,331 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,544 (-5.73%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,239 | +2.11% |
| snake_abs_exit_conv | +3,664 | +1.83% |
| gold | +3,337 | +2.01% |
| snake_abs_conv | +2,135 | +1.08% |
| snake_abs | +2,125 | +1.07% |
| snake_anaconda | +1,811 | +0.94% |
| random_hold | +1,517 | +0.73% |
| benchmark_smallcap | +1,166 | +0.58% |
| intraweek | +726 | +0.35% |
| snake_viper_wild | +395 | +0.21% |
| snake_viper_tick | +388 | +0.20% |
| intramonth | +8 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -462 | -0.22% |
| unified | -483 | -0.22% |
| benchmark | -1,331 | -0.59% |

Average per day so far: benchmark Rs +587, unified Rs +538, oracle Rs +280, intramonth Rs +251, random_hold Rs +241, intraweek Rs +185, snake_abs_exit Rs +136, snake_abs_exit_conv Rs +104, benchmark_smallcap Rs +53, nifty_calls Rs +44, snake_abs Rs +17, snake_abs_conv Rs +13, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -159, snake_viper_wild Rs -218, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -730

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.