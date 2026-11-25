# Paper trading report

Updated 2026-11-25 11:20 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,216 | +13.11% | 0 | - | 237 |
| unified | 224,917 | +12.46% | 0 | - | 236 |
| intramonth | 212,714 | +6.36% | 0 | - | 235 |
| oracle | 211,746 | +5.87% | 0 | - | 233 |
| random_hold | 210,243 | +5.12% | 12 | 75% | 1,009 |
| intraweek | 208,269 | +4.13% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,825 | +0.91% | 2 | 50% | 345 |
| snake_abs | 201,300 | +0.65% | 1 | 100% | 255 |
| snake_abs_exit_conv | 201,290 | +0.65% | 2 | 50% | 345 |
| snake_abs_conv | 201,106 | +0.55% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,517 | -0.24% | 0 | - | 237 |
| snake_viper_wild | 195,306 | -2.35% | 16 | 50% | 2,827 |
| snake_anaconda | 193,419 | -3.29% | 3 | 33% | 374 |
| snake_viper_tick | 191,987 | -4.01% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,531 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,292 (-5.35%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,743 | +2.14% |
| random_hold | +1,817 | +0.87% |
| unified | +632 | +0.28% |
| benchmark_smallcap | +538 | +0.27% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -38 | -0.02% |
| oracle | -597 | -0.28% |
| intraweek | -3,350 | -1.58% |
| snake_abs | -4,161 | -2.02% |
| snake_abs_conv | -4,197 | -2.04% |
| gold | -4,899 | -2.89% |
| snake_anaconda | -5,285 | -2.66% |
| snake_abs_exit | -5,670 | -2.73% |
| snake_viper_tick | -5,706 | -2.89% |
| snake_abs_exit_conv | -5,756 | -2.78% |
| snake_viper_wild | -5,818 | -2.89% |

Average per day so far: benchmark Rs +655, unified Rs +623, intramonth Rs +318, oracle Rs +294, random_hold Rs +256, intraweek Rs +207, snake_abs_exit Rs +49, nifty_calls Rs +46, snake_abs_exit_conv Rs +35, snake_abs Rs +34, snake_abs_conv Rs +30, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_viper_wild Rs -147, snake_anaconda Rs -188, snake_viper_tick Rs -276, snake_nonews Rs -292, snake Rs -311, gold Rs -887

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.