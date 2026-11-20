# Paper trading report

Updated 2026-11-20 14:41 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,512 | +13.26% | 0 | - | 236 |
| benchmark | 224,717 | +12.36% | 0 | - | 237 |
| intraweek | 215,702 | +7.85% | 35 | 54% | 3,851 |
| intramonth | 215,381 | +7.69% | 0 | - | 235 |
| oracle | 212,945 | +6.47% | 0 | - | 233 |
| random_hold | 209,975 | +4.99% | 11 | 73% | 979 |
| snake_abs_exit | 208,742 | +4.37% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,850 | +3.42% | 2 | 50% | 345 |
| snake_abs | 206,024 | +3.01% | 1 | 100% | 255 |
| snake_abs_conv | 205,892 | +2.95% | 1 | 100% | 255 |
| snake_viper_wild | 203,073 | +1.54% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,930 | +0.47% | 0 | - | 237 |
| snake_anaconda | 200,175 | +0.09% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,612 | -0.19% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,391 | -16.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,112 (-3.94%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,813 | +1.32% |
| benchmark | +2,341 | +1.05% |
| unified | +1,897 | +0.84% |
| random_hold | +1,522 | +0.73% |
| intramonth | +1,373 | +0.64% |
| oracle | +857 | +0.40% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -538 | -0.27% |
| snake_abs | -2,956 | -1.42% |
| snake_abs_conv | -2,968 | -1.42% |
| snake_anaconda | -3,289 | -1.62% |
| snake_abs_exit_conv | -4,214 | -2.00% |
| snake_viper_tick | -4,365 | -2.14% |
| snake_viper_wild | -4,449 | -2.14% |
| snake_abs_exit | -4,609 | -2.16% |
| gold | -7,382 | -4.22% |

Average per day so far: unified Rs +698, benchmark Rs +650, intraweek Rs +413, intramonth Rs +405, oracle Rs +341, random_hold Rs +263, snake_abs_exit Rs +250, snake_abs_exit_conv Rs +196, snake_abs_conv Rs +168, snake_abs Rs +167, snake_viper_wild Rs +102, nifty_calls Rs +48, benchmark_smallcap Rs +27, snake_anaconda Rs +5, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -14, snake_nonews Rs -308, snake Rs -328, gold Rs -858

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.