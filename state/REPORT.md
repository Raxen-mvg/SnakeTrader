# Paper trading report

Updated 2026-11-26 10:30 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,010 | +13.01% | 0 | - | 237 |
| unified | 223,717 | +11.86% | 0 | - | 236 |
| oracle | 213,160 | +6.58% | 0 | - | 233 |
| intramonth | 211,027 | +5.51% | 0 | - | 235 |
| random_hold | 210,022 | +5.01% | 13 | 69% | 1,037 |
| intraweek | 207,976 | +3.99% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,790 | +1.40% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,208 | +1.10% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,751 | +0.38% | 0 | - | 237 |
| snake_abs | 200,247 | +0.12% | 1 | 100% | 255 |
| snake_abs_conv | 200,070 | +0.04% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,059 | -2.97% | 3 | 33% | 374 |
| snake_viper_wild | 193,233 | -3.38% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,947 | -5.03% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,786 | -16.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,102 (-5.45%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,189 | +1.94% |
| benchmark_smallcap | +1,939 | +0.97% |
| intraweek | +1,233 | +0.60% |
| benchmark | +987 | +0.44% |
| snake_abs_exit | +535 | +0.26% |
| random_hold | +529 | +0.25% |
| snake_abs_exit_conv | +232 | +0.12% |
| snake_abs_conv | +98 | +0.05% |
| snake_abs | +97 | +0.05% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -382 | -0.17% |
| snake_anaconda | -494 | -0.25% |
| oracle | -636 | -0.30% |
| intramonth | -666 | -0.32% |
| snake_viper_tick | -4,230 | -2.18% |
| snake_viper_wild | -4,311 | -2.18% |

Average per day so far: benchmark Rs +634, unified Rs +578, oracle Rs +321, intramonth Rs +269, random_hold Rs +244, intraweek Rs +195, snake_abs_exit Rs +73, snake_abs_exit_conv Rs +58, nifty_calls Rs +45, benchmark_smallcap Rs +20, snake_abs Rs +6, snake_abs_conv Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -205, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -335, gold Rs -786

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.