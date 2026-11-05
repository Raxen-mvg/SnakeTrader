# Paper trading report

Updated 2026-11-05 14:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,383 | +8.19% | 0 | - | 236 |
| snake_abs_exit_conv | 214,949 | +7.47% | 1 | 100% | 255 |
| snake_abs_exit | 214,654 | +7.33% | 1 | 100% | 260 |
| benchmark | 214,099 | +7.05% | 0 | - | 237 |
| snake_abs | 211,836 | +5.92% | 1 | 100% | 255 |
| snake_abs_conv | 211,690 | +5.84% | 1 | 100% | 255 |
| intraweek | 209,806 | +4.90% | 25 | 48% | 2,757 |
| intramonth | 208,235 | +4.12% | 0 | - | 235 |
| snake_viper_wild | 205,318 | +2.66% | 3 | 33% | 702 |
| random_hold | 204,735 | +2.37% | 8 | 62% | 649 |
| oracle | 204,418 | +2.21% | 0 | - | 233 |
| snake_anaconda | 202,585 | +1.29% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,792 | +0.90% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,136 | -0.43% | 0 | - | 237 |
| gold | 194,188 | -2.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,682 (-5.16%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,340 | +2.56% |
| gold | +2,795 | +1.46% |
| oracle | +2,626 | +1.30% |
| benchmark_smallcap | +2,466 | +1.25% |
| unified | +1,944 | +0.91% |
| random_hold | +1,426 | +0.70% |
| intramonth | +1,220 | +0.59% |
| intraweek | +108 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -66 | -0.03% |
| snake_abs | -67 | -0.03% |
| snake_abs_conv | -69 | -0.03% |
| snake_abs_exit | -246 | -0.11% |
| snake_anaconda | -1,235 | -0.61% |
| snake_viper_tick | -3,608 | -1.76% |
| snake_viper_wild | -3,712 | -1.78% |

Average per day so far: snake_abs_exit_conv Rs +598, snake_abs_exit Rs +586, unified Rs +585, benchmark Rs +504, snake_abs_conv Rs +468, snake_abs Rs +455, intraweek Rs +350, intramonth Rs +294, snake_viper_wild Rs +266, random_hold Rs +169, oracle Rs +158, snake_anaconda Rs +112, snake_viper_tick Rs +105, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -208, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.