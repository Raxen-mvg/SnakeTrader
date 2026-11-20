# Paper trading report

Updated 2026-11-20 12:31 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,069 | +13.04% | 0 | - | 236 |
| benchmark | 224,097 | +12.05% | 0 | - | 237 |
| intramonth | 215,001 | +7.50% | 0 | - | 235 |
| intraweek | 214,565 | +7.28% | 35 | 54% | 3,851 |
| oracle | 212,707 | +6.35% | 0 | - | 233 |
| random_hold | 209,101 | +4.55% | 11 | 73% | 979 |
| snake_abs_exit | 209,071 | +4.54% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,111 | +3.56% | 2 | 50% | 345 |
| snake_abs | 206,262 | +3.13% | 1 | 100% | 255 |
| snake_abs_conv | 206,127 | +3.06% | 1 | 100% | 255 |
| snake_viper_wild | 205,382 | +2.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 201,879 | +0.94% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,896 | +0.45% | 0 | - | 237 |
| snake_anaconda | 200,218 | +0.11% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,619 | -16.69% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,872 (-4.06%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,721 | +0.77% |
| intraweek | +1,676 | +0.79% |
| unified | +1,454 | +0.65% |
| intramonth | +993 | +0.46% |
| random_hold | +648 | +0.31% |
| oracle | +618 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -572 | -0.28% |
| snake_viper_tick | -2,098 | -1.03% |
| snake_viper_wild | -2,141 | -1.03% |
| snake_abs | -2,718 | -1.30% |
| snake_abs_conv | -2,733 | -1.31% |
| snake_anaconda | -3,246 | -1.59% |
| snake_abs_exit_conv | -3,954 | -1.87% |
| snake_abs_exit | -4,280 | -2.01% |
| gold | -8,154 | -4.67% |

Average per day so far: unified Rs +686, benchmark Rs +634, intramonth Rs +395, intraweek Rs +383, oracle Rs +334, snake_abs_exit Rs +259, random_hold Rs +240, snake_abs_exit_conv Rs +203, snake_viper_wild Rs +179, snake_abs_conv Rs +175, snake_abs Rs +174, snake_viper_tick Rs +70, nifty_calls Rs +48, benchmark_smallcap Rs +26, snake_anaconda Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -878

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.