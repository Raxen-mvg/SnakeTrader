# Paper trading report

Updated 2026-11-17 14:18 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,802 | +10.90% | 0 | - | 237 |
| unified | 221,712 | +10.86% | 0 | - | 236 |
| snake_abs_exit | 213,774 | +6.89% | 2 | 50% | 345 |
| intraweek | 213,646 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,575 | +6.29% | 0 | - | 233 |
| snake_abs_exit_conv | 212,245 | +6.12% | 2 | 50% | 345 |
| intramonth | 211,643 | +5.82% | 0 | - | 235 |
| snake_viper_wild | 209,792 | +4.90% | 14 | 50% | 2,496 |
| snake_abs | 208,955 | +4.48% | 1 | 100% | 255 |
| snake_abs_conv | 208,821 | +4.41% | 1 | 100% | 255 |
| random_hold | 207,751 | +3.88% | 10 | 70% | 733 |
| snake_viper_tick | 206,207 | +3.10% | 13 | 46% | 2,299 |
| snake_anaconda | 204,544 | +2.27% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,177 | +0.59% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,971 | -9.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,276 (-4.36%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,648 | +1.77% |
| snake_viper_tick | +3,587 | +1.77% |
| intraweek | +2,380 | +1.13% |
| benchmark | +1,721 | +0.78% |
| oracle | +552 | +0.26% |
| benchmark_smallcap | +348 | +0.17% |
| unified | +274 | +0.12% |
| intramonth | +24 | +0.01% |
| gold | +16 | +0.01% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| random_hold | -42 | -0.02% |
| snake_anaconda | -559 | -0.27% |
| snake_abs_exit | -635 | -0.30% |
| snake_abs_exit_conv | -973 | -0.46% |
| snake_abs_conv | -1,169 | -0.56% |
| snake_abs | -1,178 | -0.56% |

Average per day so far: benchmark Rs +623, unified Rs +620, snake_abs_exit Rs +430, intraweek Rs +390, snake_abs_exit_conv Rs +383, snake_viper_wild Rs +363, oracle Rs +359, intramonth Rs +333, snake_abs_conv Rs +276, snake_abs Rs +271, snake_viper_tick Rs +259, random_hold Rs +221, snake_anaconda Rs +151, nifty_calls Rs +52, benchmark_smallcap Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -544

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.