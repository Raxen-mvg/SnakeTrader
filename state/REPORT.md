# Paper trading report

Updated 2026-11-04 12:13 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,736 | +6.87% | 0 | - | 236 |
| snake_abs_exit_conv | 209,618 | +4.81% | 1 | 100% | 255 |
| snake_abs_exit | 209,494 | +4.75% | 1 | 100% | 260 |
| intraweek | 207,533 | +3.77% | 25 | 48% | 2,757 |
| benchmark | 207,260 | +3.63% | 0 | - | 237 |
| snake_viper_wild | 207,249 | +3.62% | 3 | 33% | 702 |
| snake_abs | 206,528 | +3.26% | 1 | 100% | 255 |
| snake_abs_conv | 206,370 | +3.19% | 1 | 100% | 255 |
| intramonth | 206,183 | +3.09% | 0 | - | 235 |
| snake_viper_tick | 203,642 | +1.82% | 2 | 0% | 532 |
| random_hold | 202,727 | +1.36% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,202 | +0.60% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,050 | -0.97% | 3 | 33% | 361 |
| benchmark_smallcap | 194,731 | -2.63% | 0 | - | 237 |
| gold | 190,753 | -4.62% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,038 (-5.48%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +5,480 | +2.69% |
| gold | +5,475 | +2.96% |
| snake_abs_exit_conv | +5,280 | +2.58% |
| snake_abs_conv | +5,229 | +2.60% |
| snake_abs | +5,219 | +2.59% |
| snake_anaconda | +4,225 | +2.18% |
| intraweek | +2,447 | +1.19% |
| random_hold | +2,258 | +1.13% |
| intramonth | +2,212 | +1.08% |
| benchmark_smallcap | +1,794 | +0.93% |
| unified | +1,736 | +0.82% |
| oracle | +1,213 | +0.61% |
| benchmark | +558 | +0.27% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,525 | -1.70% |
| snake_viper_wild | -3,644 | -1.73% |

Average per day so far: unified Rs +509, snake_abs_exit_conv Rs +401, snake_abs_exit Rs +396, snake_viper_wild Rs +382, intraweek Rs +279, benchmark Rs +269, snake_abs_conv Rs +265, snake_abs Rs +261, intramonth Rs +229, snake_viper_tick Rs +228, random_hold Rs +101, nifty_calls Rs +68, oracle Rs +45, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -89, benchmark_smallcap Rs -229, gold Rs -342, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.