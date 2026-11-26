# Paper trading report

Updated 2026-11-26 12:01 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,048 | +13.02% | 0 | - | 237 |
| unified | 223,331 | +11.66% | 0 | - | 236 |
| oracle | 213,088 | +6.54% | 0 | - | 233 |
| intramonth | 210,479 | +5.24% | 0 | - | 235 |
| random_hold | 209,863 | +4.93% | 13 | 69% | 1,037 |
| intraweek | 208,479 | +4.24% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,118 | +0.56% | 2 | 50% | 345 |
| benchmark_smallcap | 200,728 | +0.36% | 0 | - | 237 |
| snake_abs_exit_conv | 200,599 | +0.30% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,858 | -0.57% | 1 | 100% | 255 |
| snake_abs_conv | 198,669 | -0.67% | 1 | 100% | 255 |
| snake_anaconda | 192,671 | -3.66% | 3 | 33% | 374 |
| snake_viper_wild | 192,326 | -3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,059 | -5.47% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,240 | -16.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,850 (-5.58%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,917 | +0.96% |
| intraweek | +1,736 | +0.84% |
| gold | +1,644 | +1.00% |
| benchmark | +1,025 | +0.46% |
| random_hold | +370 | +0.18% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -707 | -0.33% |
| unified | -769 | -0.34% |
| snake_abs_exit | -1,138 | -0.56% |
| intramonth | -1,214 | -0.57% |
| snake_abs | -1,292 | -0.65% |
| snake_abs_conv | -1,303 | -0.65% |
| snake_abs_exit_conv | -1,377 | -0.68% |
| snake_anaconda | -1,882 | -0.97% |
| snake_viper_tick | -5,118 | -2.64% |
| snake_viper_wild | -5,218 | -2.64% |

Average per day so far: benchmark Rs +635, unified Rs +569, oracle Rs +319, intramonth Rs +256, random_hold Rs +241, intraweek Rs +207, nifty_calls Rs +45, snake_abs_exit Rs +29, benchmark_smallcap Rs +20, snake_abs_exit_conv Rs +16, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -29, snake_abs_conv Rs -35, snake_anaconda Rs -204, snake_viper_wild Rs -233, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -365, gold Rs -823

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.