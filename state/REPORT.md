# Paper trading report

Updated 2026-11-05 13:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,349 | +8.67% | 0 | - | 236 |
| snake_abs_exit_conv | 213,830 | +6.92% | 1 | 100% | 255 |
| snake_abs_exit | 213,522 | +6.76% | 1 | 100% | 260 |
| benchmark | 213,188 | +6.59% | 0 | - | 237 |
| snake_abs | 210,713 | +5.36% | 1 | 100% | 255 |
| snake_abs_conv | 210,579 | +5.29% | 1 | 100% | 255 |
| intraweek | 210,519 | +5.26% | 25 | 48% | 2,757 |
| intramonth | 209,218 | +4.61% | 0 | - | 235 |
| snake_viper_wild | 206,417 | +3.21% | 3 | 33% | 702 |
| random_hold | 205,782 | +2.89% | 8 | 62% | 649 |
| oracle | 203,756 | +1.88% | 0 | - | 233 |
| snake_viper_tick | 202,870 | +1.44% | 2 | 0% | 532 |
| snake_anaconda | 202,055 | +1.03% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,935 | -0.53% | 0 | - | 237 |
| gold | 193,991 | -3.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,817 (-5.09%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,429 | +2.12% |
| unified | +2,909 | +1.36% |
| gold | +2,598 | +1.36% |
| random_hold | +2,473 | +1.22% |
| benchmark_smallcap | +2,264 | +1.15% |
| intramonth | +2,202 | +1.06% |
| oracle | +1,964 | +0.97% |
| intraweek | +822 | +0.39% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,179 | -0.56% |
| snake_abs_exit_conv | -1,184 | -0.55% |
| snake_abs | -1,190 | -0.56% |
| snake_abs_exit | -1,379 | -0.64% |
| snake_anaconda | -1,766 | -0.87% |
| snake_viper_tick | -2,531 | -1.23% |
| snake_viper_wild | -2,613 | -1.25% |

Average per day so far: unified Rs +620, snake_abs_exit_conv Rs +553, snake_abs_exit Rs +541, benchmark Rs +471, snake_abs_conv Rs +423, snake_abs Rs +412, intraweek Rs +376, intramonth Rs +329, snake_viper_wild Rs +321, random_hold Rs +206, snake_viper_tick Rs +169, oracle Rs +134, snake_anaconda Rs +89, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -44, gold Rs -215, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.