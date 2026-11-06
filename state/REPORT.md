# Paper trading report

Updated 2026-11-06 11:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,752 | +7.38% | 0 | - | 236 |
| benchmark | 214,420 | +7.21% | 0 | - | 237 |
| intraweek | 211,098 | +5.55% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,512 | +4.76% | 1 | 100% | 255 |
| snake_abs_exit | 209,299 | +4.65% | 1 | 100% | 260 |
| intramonth | 206,791 | +3.40% | 0 | - | 235 |
| snake_abs | 206,466 | +3.23% | 1 | 100% | 255 |
| snake_abs_conv | 206,299 | +3.15% | 1 | 100% | 255 |
| oracle | 204,628 | +2.31% | 0 | - | 233 |
| random_hold | 203,242 | +1.62% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,833 | -1.58% | 3 | 33% | 374 |
| snake_viper_wild | 195,721 | -2.14% | 3 | 33% | 702 |
| benchmark_smallcap | 194,574 | -2.71% | 0 | - | 237 |
| snake_viper_tick | 192,405 | -3.80% | 2 | 0% | 532 |
| gold | 189,996 | -5.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,349 (-6.33%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,679 | +0.80% |
| benchmark | +650 | +0.30% |
| oracle | +556 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,081 | -0.53% |
| intramonth | -1,157 | -0.56% |
| unified | -1,232 | -0.57% |
| benchmark_smallcap | -4,114 | -2.07% |
| gold | -4,225 | -2.17% |
| snake_abs | -5,222 | -2.47% |
| snake_abs_conv | -5,246 | -2.48% |
| snake_abs_exit_conv | -5,291 | -2.46% |
| snake_abs_exit | -5,360 | -2.50% |
| snake_anaconda | -5,647 | -2.79% |
| snake_viper_tick | -8,733 | -4.34% |
| snake_viper_wild | -8,935 | -4.37% |

Average per day so far: unified Rs +509, benchmark Rs +497, intraweek Rs +383, snake_abs_exit_conv Rs +366, snake_abs_exit Rs +358, snake_abs_conv Rs +242, snake_abs Rs +239, intramonth Rs +234, oracle Rs +160, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -132, snake_viper_wild Rs -204, benchmark_smallcap Rs -217, gold Rs -345, snake_nonews Rs -411, snake_viper_tick Rs -422, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.