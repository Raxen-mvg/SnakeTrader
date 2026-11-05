# Paper trading report

Updated 2026-11-05 15:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,470 | +7.74% | 0 | - | 236 |
| snake_abs_exit_conv | 214,136 | +7.07% | 1 | 100% | 255 |
| snake_abs_exit | 213,986 | +6.99% | 1 | 100% | 260 |
| benchmark | 213,953 | +6.98% | 0 | - | 237 |
| snake_abs | 211,022 | +5.51% | 1 | 100% | 255 |
| snake_abs_conv | 210,878 | +5.44% | 1 | 100% | 255 |
| intraweek | 210,095 | +5.05% | 25 | 48% | 2,757 |
| intramonth | 207,486 | +3.74% | 0 | - | 235 |
| snake_viper_wild | 204,672 | +2.34% | 3 | 33% | 702 |
| random_hold | 204,233 | +2.12% | 8 | 62% | 649 |
| oracle | 203,817 | +1.91% | 0 | - | 233 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,677 | +0.84% | 3 | 33% | 374 |
| snake_viper_tick | 201,154 | +0.58% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,979 | -0.51% | 0 | - | 237 |
| gold | 194,238 | -2.88% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,228 (-5.39%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,194 | +2.49% |
| gold | +2,844 | +1.49% |
| benchmark_smallcap | +2,309 | +1.17% |
| oracle | +2,025 | +1.00% |
| unified | +1,030 | +0.48% |
| random_hold | +924 | +0.45% |
| intramonth | +470 | +0.23% |
| intraweek | +397 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -879 | -0.41% |
| snake_abs_conv | -880 | -0.41% |
| snake_abs | -881 | -0.42% |
| snake_abs_exit | -915 | -0.43% |
| snake_anaconda | -2,143 | -1.05% |
| snake_viper_tick | -4,247 | -2.07% |
| snake_viper_wild | -4,358 | -2.08% |

Average per day so far: snake_abs_exit_conv Rs +565, snake_abs_exit Rs +559, unified Rs +552, benchmark Rs +498, snake_abs_conv Rs +435, snake_abs Rs +424, intraweek Rs +361, intramonth Rs +267, snake_viper_wild Rs +234, random_hold Rs +151, oracle Rs +136, snake_anaconda Rs +73, snake_viper_tick Rs +68, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -43, gold Rs -206, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.