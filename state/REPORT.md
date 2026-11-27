# Paper trading report

Updated 2026-11-27 13:58 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,028 | +12.01% | 0 | - | 237 |
| unified | 223,226 | +11.61% | 0 | - | 236 |
| oracle | 211,753 | +5.88% | 0 | - | 233 |
| random_hold | 210,946 | +5.47% | 13 | 69% | 1,037 |
| intramonth | 210,708 | +5.35% | 0 | - | 235 |
| intraweek | 208,240 | +4.12% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,826 | +2.91% | 2 | 50% | 345 |
| snake_abs_exit | 204,628 | +2.31% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,513 | +0.76% | 0 | - | 237 |
| snake_abs | 200,504 | +0.25% | 1 | 100% | 255 |
| snake_abs_conv | 200,322 | +0.16% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,744 | -3.13% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,334 | -14.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,830 (-5.59%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,430 | +2.71% |
| gold | +4,340 | +2.62% |
| snake_abs_exit | +3,550 | +1.77% |
| random_hold | +2,352 | +1.13% |
| snake_abs_conv | +1,956 | +0.99% |
| snake_abs | +1,952 | +0.98% |
| snake_anaconda | +1,448 | +0.75% |
| intraweek | +1,191 | +0.57% |
| benchmark_smallcap | +673 | +0.34% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| intramonth | +174 | +0.08% |
| unified | +147 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -483 | -0.23% |
| benchmark | -1,958 | -0.87% |

Average per day so far: benchmark Rs +572, unified Rs +553, oracle Rs +280, random_hold Rs +261, intramonth Rs +255, intraweek Rs +196, snake_abs_exit_conv Rs +149, snake_abs_exit Rs +119, nifty_calls Rs +44, benchmark_smallcap Rs +40, snake_abs Rs +13, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -169, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -706

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.