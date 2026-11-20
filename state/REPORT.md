# Paper trading report

Updated 2026-11-20 10:16 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,050 | +12.53% | 0 | - | 236 |
| benchmark | 222,651 | +11.33% | 0 | - | 237 |
| intramonth | 214,216 | +7.11% | 0 | - | 235 |
| intraweek | 213,663 | +6.83% | 35 | 54% | 3,851 |
| oracle | 212,931 | +6.46% | 0 | - | 233 |
| snake_abs_exit | 210,673 | +5.34% | 2 | 50% | 345 |
| random_hold | 208,824 | +4.41% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,420 | +4.21% | 2 | 50% | 345 |
| snake_abs | 206,991 | +3.50% | 1 | 100% | 255 |
| snake_abs_conv | 206,858 | +3.43% | 1 | 100% | 255 |
| snake_viper_wild | 205,682 | +2.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,175 | +1.09% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,079 | +0.54% | 3 | 33% | 374 |
| benchmark_smallcap | 200,448 | +0.22% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,402 | -17.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,681 (-4.16%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +842 | +0.40% |
| intraweek | +774 | +0.36% |
| unified | +435 | +0.19% |
| random_hold | +371 | +0.18% |
| benchmark | +275 | +0.12% |
| intramonth | +208 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,020 | -0.51% |
| snake_viper_tick | -1,802 | -0.88% |
| snake_viper_wild | -1,841 | -0.89% |
| snake_abs | -1,989 | -0.95% |
| snake_abs_conv | -2,002 | -0.96% |
| snake_anaconda | -2,385 | -1.17% |
| snake_abs_exit_conv | -2,644 | -1.25% |
| snake_abs_exit | -2,679 | -1.25% |
| gold | -9,371 | -5.36% |

Average per day so far: unified Rs +659, benchmark Rs +596, intramonth Rs +374, intraweek Rs +360, oracle Rs +340, snake_abs_exit Rs +305, snake_abs_exit_conv Rs +241, random_hold Rs +232, snake_abs_conv Rs +196, snake_abs Rs +194, snake_viper_wild Rs +189, snake_viper_tick Rs +81, nifty_calls Rs +48, snake_anaconda Rs +33, benchmark_smallcap Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -910

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.