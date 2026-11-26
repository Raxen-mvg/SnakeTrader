# Paper trading report

Updated 2026-11-26 13:27 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,551 | +12.78% | 0 | - | 237 |
| unified | 223,470 | +11.73% | 0 | - | 236 |
| oracle | 213,312 | +6.66% | 0 | - | 233 |
| intramonth | 210,619 | +5.31% | 0 | - | 235 |
| random_hold | 209,376 | +4.69% | 13 | 69% | 1,037 |
| intraweek | 208,019 | +4.01% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,549 | +0.27% | 0 | - | 237 |
| snake_abs_exit | 200,117 | +0.06% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,547 | -0.23% | 2 | 50% | 345 |
| snake_abs | 197,887 | -1.06% | 1 | 100% | 255 |
| snake_abs_conv | 197,682 | -1.16% | 1 | 100% | 255 |
| snake_viper_wild | 192,110 | -3.94% | 16 | 50% | 2,827 |
| snake_anaconda | 191,634 | -4.18% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,847 | -5.58% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,125 | -16.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,714 (-5.64%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,738 | +0.87% |
| gold | +1,529 | +0.93% |
| intraweek | +1,276 | +0.62% |
| benchmark | +528 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -117 | -0.06% |
| oracle | -483 | -0.23% |
| unified | -630 | -0.28% |
| intramonth | -1,074 | -0.51% |
| snake_abs_exit | -2,138 | -1.06% |
| snake_abs | -2,263 | -1.13% |
| snake_abs_conv | -2,290 | -1.15% |
| snake_abs_exit_conv | -2,428 | -1.20% |
| snake_anaconda | -2,919 | -1.50% |
| snake_viper_tick | -5,330 | -2.75% |
| snake_viper_wild | -5,434 | -2.75% |

Average per day so far: benchmark Rs +623, unified Rs +572, oracle Rs +325, intramonth Rs +259, random_hold Rs +229, intraweek Rs +196, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -12, snake_abs Rs -54, snake_abs_conv Rs -61, snake_anaconda Rs -232, snake_viper_wild Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -372, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.