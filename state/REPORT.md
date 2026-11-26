# Paper trading report

Updated 2026-11-26 10:41 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,002 | +13.00% | 0 | - | 237 |
| unified | 223,553 | +11.78% | 0 | - | 236 |
| oracle | 212,823 | +6.41% | 0 | - | 233 |
| intramonth | 210,924 | +5.46% | 0 | - | 235 |
| random_hold | 209,879 | +4.94% | 13 | 69% | 1,037 |
| intraweek | 208,034 | +4.02% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,033 | +1.02% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,498 | +0.75% | 2 | 50% | 345 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,665 | -0.17% | 1 | 100% | 255 |
| snake_abs_conv | 199,480 | -0.26% | 1 | 100% | 255 |
| snake_viper_wild | 193,468 | -3.27% | 16 | 50% | 2,827 |
| snake_anaconda | 193,457 | -3.27% | 3 | 33% | 374 |
| snake_viper_tick | 190,177 | -4.91% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,819 | -16.09% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,922 (-5.54%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,222 | +1.96% |
| benchmark_smallcap | +1,861 | +0.94% |
| intraweek | +1,290 | +0.62% |
| benchmark | +979 | +0.43% |
| random_hold | +386 | +0.18% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -222 | -0.11% |
| snake_abs_exit_conv | -478 | -0.24% |
| snake_abs | -485 | -0.24% |
| snake_abs_conv | -492 | -0.25% |
| unified | -546 | -0.24% |
| intramonth | -770 | -0.36% |
| oracle | -972 | -0.46% |
| snake_anaconda | -1,096 | -0.56% |
| snake_viper_tick | -4,000 | -2.06% |
| snake_viper_wild | -4,075 | -2.06% |

Average per day so far: benchmark Rs +634, unified Rs +574, oracle Rs +313, intramonth Rs +266, random_hold Rs +241, intraweek Rs +196, snake_abs_exit Rs +54, nifty_calls Rs +45, snake_abs_exit_conv Rs +39, benchmark_smallcap Rs +18, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -9, snake_abs_conv Rs -14, snake_anaconda Rs -182, snake_viper_wild Rs -198, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -327, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.