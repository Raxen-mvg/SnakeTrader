# Paper trading report

Updated 2026-11-17 12:20 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,276 | +11.14% | 0 | - | 237 |
| unified | 221,916 | +10.96% | 0 | - | 236 |
| snake_abs_exit | 214,603 | +7.30% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,841 | +6.42% | 2 | 50% | 345 |
| intraweek | 212,524 | +6.26% | 35 | 54% | 3,851 |
| oracle | 212,076 | +6.04% | 0 | - | 233 |
| intramonth | 211,890 | +5.95% | 0 | - | 235 |
| snake_abs | 209,567 | +4.78% | 1 | 100% | 255 |
| snake_abs_conv | 209,420 | +4.71% | 1 | 100% | 255 |
| snake_viper_wild | 207,812 | +3.91% | 14 | 50% | 2,496 |
| random_hold | 207,698 | +3.85% | 10 | 70% | 733 |
| snake_anaconda | 205,064 | +2.53% | 3 | 33% | 374 |
| snake_viper_tick | 204,259 | +2.13% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,085 | +1.04% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,152 | -9.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,107 (-4.45%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,196 | +1.00% |
| snake_viper_wild | +1,668 | +0.81% |
| snake_viper_tick | +1,639 | +0.81% |
| intraweek | +1,258 | +0.60% |
| benchmark_smallcap | +1,256 | +0.62% |
| unified | +478 | +0.22% |
| intramonth | +271 | +0.13% |
| gold | +197 | +0.11% |
| snake_abs_exit | +194 | +0.09% |
| oracle | +53 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -39 | -0.02% |
| random_hold | -95 | -0.05% |
| snake_abs_exit_conv | -376 | -0.18% |
| snake_abs | -567 | -0.27% |
| snake_abs_conv | -569 | -0.27% |

Average per day so far: benchmark Rs +636, unified Rs +626, snake_abs_exit Rs +456, snake_abs_exit_conv Rs +401, intraweek Rs +358, oracle Rs +345, intramonth Rs +340, snake_abs_conv Rs +294, snake_abs Rs +290, snake_viper_wild Rs +289, random_hold Rs +220, snake_viper_tick Rs +177, snake_anaconda Rs +169, benchmark_smallcap Rs +67, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -539

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.