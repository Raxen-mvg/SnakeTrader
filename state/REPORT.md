# Paper trading report

Updated 2026-11-20 13:23 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,307 | +13.15% | 0 | - | 236 |
| benchmark | 224,204 | +12.10% | 0 | - | 237 |
| intraweek | 215,332 | +7.67% | 35 | 54% | 3,851 |
| intramonth | 215,296 | +7.65% | 0 | - | 235 |
| oracle | 212,539 | +6.27% | 0 | - | 233 |
| random_hold | 209,610 | +4.80% | 11 | 73% | 979 |
| snake_abs_exit | 208,754 | +4.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,721 | +3.36% | 2 | 50% | 345 |
| snake_abs | 205,870 | +2.94% | 1 | 100% | 255 |
| snake_abs_conv | 205,736 | +2.87% | 1 | 100% | 255 |
| snake_viper_wild | 203,248 | +1.62% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,008 | +0.50% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,993 | -0.00% | 3 | 33% | 374 |
| snake_viper_tick | 199,784 | -0.11% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,112 | -16.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,927 (-4.04%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,442 | +1.15% |
| benchmark | +1,828 | +0.82% |
| unified | +1,692 | +0.75% |
| intramonth | +1,288 | +0.60% |
| random_hold | +1,157 | +0.56% |
| oracle | +450 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -460 | -0.23% |
| snake_abs | -3,110 | -1.49% |
| snake_abs_conv | -3,124 | -1.50% |
| snake_anaconda | -3,471 | -1.71% |
| snake_viper_tick | -4,193 | -2.06% |
| snake_viper_wild | -4,274 | -2.06% |
| snake_abs_exit_conv | -4,344 | -2.06% |
| snake_abs_exit | -4,597 | -2.15% |
| gold | -7,661 | -4.38% |

Average per day so far: unified Rs +692, benchmark Rs +637, intraweek Rs +403, intramonth Rs +403, oracle Rs +330, random_hold Rs +253, snake_abs_exit Rs +250, snake_abs_exit_conv Rs +192, snake_abs_conv Rs +164, snake_abs Rs +163, snake_viper_wild Rs +108, nifty_calls Rs +48, benchmark_smallcap Rs +30, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -0, snake_viper_tick Rs -8, snake_nonews Rs -308, snake Rs -328, gold Rs -865

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.