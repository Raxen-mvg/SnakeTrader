# Paper trading report

Updated 2026-11-23 13:40 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,681 | +11.84% | 0 | - | 236 |
| benchmark | 222,254 | +11.13% | 0 | - | 237 |
| intraweek | 212,091 | +6.04% | 40 | 55% | 4,400 |
| intramonth | 211,880 | +5.94% | 0 | - | 235 |
| oracle | 211,513 | +5.76% | 0 | - | 233 |
| random_hold | 208,804 | +4.40% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,597 | +3.30% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,189 | +2.59% | 2 | 50% | 345 |
| snake_abs | 204,130 | +2.06% | 1 | 100% | 255 |
| snake_abs_conv | 203,961 | +1.98% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,510 | +0.26% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,248 | -0.38% | 0 | - | 237 |
| snake_anaconda | 197,690 | -1.16% | 3 | 33% | 374 |
| snake_viper_tick | 197,091 | -1.45% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,183 | -15.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,898 (-5.05%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,134 | +0.68% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -966 | -0.46% |
| snake_abs_exit_conv | -1,428 | -0.69% |
| benchmark_smallcap | -1,659 | -0.83% |
| snake_abs | -1,790 | -0.87% |
| snake_abs_conv | -1,822 | -0.89% |
| random_hold | -1,955 | -0.93% |
| snake_abs_exit | -1,965 | -0.94% |
| snake_anaconda | -2,215 | -1.11% |
| snake_viper_tick | -2,281 | -1.14% |
| snake_viper_wild | -2,319 | -1.14% |
| unified | -2,501 | -1.11% |
| benchmark | -2,884 | -1.28% |
| intramonth | -3,124 | -1.45% |
| intraweek | -3,621 | -1.68% |

Average per day so far: unified Rs +607, benchmark Rs +571, intraweek Rs +310, intramonth Rs +305, oracle Rs +295, random_hold Rs +226, snake_abs_exit Rs +183, snake_abs_exit_conv Rs +144, snake_abs Rs +112, snake_abs_conv Rs +110, nifty_calls Rs +47, snake_viper_wild Rs +16, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -21, snake_anaconda Rs -68, snake_viper_tick Rs -104, snake_nonews Rs -300, snake Rs -320, gold Rs -790

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.