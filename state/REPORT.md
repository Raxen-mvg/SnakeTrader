# Paper trading report

Updated 2026-11-05 11:33 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,380 | +9.19% | 0 | - | 236 |
| snake_abs_exit_conv | 214,735 | +7.37% | 1 | 100% | 255 |
| snake_abs_exit | 214,435 | +7.22% | 1 | 100% | 260 |
| benchmark | 212,798 | +6.40% | 0 | - | 237 |
| snake_abs | 211,613 | +5.81% | 1 | 100% | 255 |
| snake_abs_conv | 211,479 | +5.74% | 1 | 100% | 255 |
| intraweek | 211,063 | +5.53% | 25 | 48% | 2,757 |
| intramonth | 210,111 | +5.05% | 0 | - | 235 |
| random_hold | 207,002 | +3.50% | 8 | 62% | 649 |
| snake_viper_wild | 206,771 | +3.39% | 3 | 33% | 702 |
| oracle | 204,278 | +2.14% | 0 | - | 233 |
| snake_viper_tick | 203,220 | +1.61% | 2 | 0% | 532 |
| snake_anaconda | 202,921 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,159 | -0.42% | 0 | - | 237 |
| gold | 193,893 | -3.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,428 (-4.79%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,039 | +1.94% |
| unified | +3,941 | +1.84% |
| random_hold | +3,693 | +1.82% |
| intramonth | +3,095 | +1.50% |
| gold | +2,499 | +1.31% |
| benchmark_smallcap | +2,489 | +1.26% |
| oracle | +2,486 | +1.23% |
| intraweek | +1,365 | +0.65% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -279 | -0.13% |
| snake_abs_exit_conv | -280 | -0.13% |
| snake_abs | -290 | -0.14% |
| snake_abs_exit | -465 | -0.22% |
| snake_anaconda | -900 | -0.44% |
| snake_viper_tick | -2,181 | -1.06% |
| snake_viper_wild | -2,258 | -1.08% |

Average per day so far: unified Rs +656, snake_abs_exit_conv Rs +589, snake_abs_exit Rs +577, snake_abs_conv Rs +459, benchmark Rs +457, snake_abs Rs +447, intraweek Rs +395, intramonth Rs +361, snake_viper_wild Rs +339, random_hold Rs +250, snake_viper_tick Rs +189, oracle Rs +153, snake_anaconda Rs +127, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -35, gold Rs -218, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.