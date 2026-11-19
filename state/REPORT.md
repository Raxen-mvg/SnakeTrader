# Paper trading report

Updated 2026-11-19 15:28 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,574 | +12.29% | 0 | - | 236 |
| benchmark | 222,514 | +11.26% | 0 | - | 237 |
| intramonth | 213,973 | +6.99% | 0 | - | 235 |
| snake_abs_exit | 213,119 | +6.56% | 2 | 50% | 345 |
| intraweek | 213,115 | +6.56% | 35 | 54% | 3,851 |
| oracle | 212,195 | +6.10% | 0 | - | 233 |
| snake_abs_exit_conv | 210,811 | +5.41% | 2 | 50% | 345 |
| snake_abs | 209,318 | +4.66% | 1 | 100% | 255 |
| snake_abs_conv | 209,193 | +4.60% | 1 | 100% | 255 |
| random_hold | 208,522 | +4.26% | 10 | 70% | 733 |
| snake_viper_wild | 207,177 | +3.59% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,639 | +1.82% | 15 | 47% | 2,625 |
| snake_anaconda | 203,284 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,707 | -12.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,023 (-3.99%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,354 | +1.18% |
| benchmark | +2,218 | +1.01% |
| unified | +1,962 | +0.88% |
| intramonth | +1,699 | +0.80% |
| random_hold | +1,590 | +0.77% |
| oracle | +1,399 | +0.66% |
| intraweek | +1,276 | +0.60% |
| snake_viper_wild | +138 | +0.07% |
| snake_viper_tick | +135 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -118 | -0.06% |
| snake_abs_conv | -132 | -0.06% |
| snake_abs_exit | -913 | -0.43% |
| snake_anaconda | -1,117 | -0.55% |
| snake_abs_exit_conv | -1,573 | -0.74% |
| gold | -2,614 | -1.47% |

Average per day so far: unified Rs +664, benchmark Rs +608, snake_abs_exit Rs +386, intramonth Rs +378, intraweek Rs +354, oracle Rs +330, snake_abs_exit_conv Rs +318, snake_abs_conv Rs +270, snake_abs Rs +266, snake_viper_wild Rs +247, random_hold Rs +230, snake_viper_tick Rs +140, snake_anaconda Rs +103, benchmark_smallcap Rs +51, nifty_calls Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -684

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.