# Paper trading report

Updated 2026-11-05 12:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,537 | +8.77% | 0 | - | 236 |
| snake_abs_exit_conv | 213,579 | +6.79% | 1 | 100% | 255 |
| snake_abs_exit | 213,275 | +6.64% | 1 | 100% | 260 |
| benchmark | 212,836 | +6.42% | 0 | - | 237 |
| intraweek | 210,554 | +5.28% | 25 | 48% | 2,757 |
| snake_abs | 210,469 | +5.23% | 1 | 100% | 255 |
| snake_abs_conv | 210,329 | +5.16% | 1 | 100% | 255 |
| intramonth | 209,319 | +4.66% | 0 | - | 235 |
| snake_viper_wild | 206,366 | +3.18% | 3 | 33% | 702 |
| random_hold | 206,136 | +3.07% | 8 | 62% | 649 |
| oracle | 203,925 | +1.96% | 0 | - | 233 |
| snake_viper_tick | 202,819 | +1.41% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,644 | +0.82% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,901 | -0.55% | 0 | - | 237 |
| gold | 194,106 | -2.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,768 (-5.12%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,077 | +1.95% |
| unified | +3,098 | +1.45% |
| random_hold | +2,827 | +1.39% |
| gold | +2,713 | +1.42% |
| intramonth | +2,303 | +1.11% |
| benchmark_smallcap | +2,231 | +1.13% |
| oracle | +2,133 | +1.06% |
| intraweek | +856 | +0.41% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,429 | -0.68% |
| snake_abs | -1,435 | -0.68% |
| snake_abs_exit_conv | -1,436 | -0.67% |
| snake_abs_exit | -1,625 | -0.76% |
| snake_anaconda | -2,177 | -1.07% |
| snake_viper_tick | -2,581 | -1.26% |
| snake_viper_wild | -2,664 | -1.27% |

Average per day so far: unified Rs +626, snake_abs_exit_conv Rs +543, snake_abs_exit Rs +531, benchmark Rs +458, snake_abs_conv Rs +413, snake_abs Rs +403, intraweek Rs +377, intramonth Rs +333, snake_viper_wild Rs +318, random_hold Rs +219, snake_viper_tick Rs +166, oracle Rs +140, snake_anaconda Rs +71, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -46, gold Rs -210, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.