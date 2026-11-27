# Paper trading report

Updated 2026-11-27 13:25 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,005 | +12.00% | 0 | - | 237 |
| unified | 223,258 | +11.63% | 0 | - | 236 |
| oracle | 211,826 | +5.91% | 0 | - | 233 |
| random_hold | 210,869 | +5.43% | 13 | 69% | 1,037 |
| intramonth | 210,858 | +5.43% | 0 | - | 235 |
| intraweek | 208,438 | +4.22% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,704 | +2.85% | 2 | 50% | 345 |
| snake_abs_exit | 204,668 | +2.33% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,333 | +0.67% | 0 | - | 237 |
| snake_abs | 200,345 | +0.17% | 1 | 100% | 255 |
| snake_abs_conv | 200,164 | +0.08% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,713 | -3.14% | 3 | 33% | 374 |
| snake_viper_wild | 191,953 | -4.02% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,694 | -5.65% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,890 | -15.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,858 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,307 | +2.65% |
| gold | +3,896 | +2.35% |
| snake_abs_exit | +3,591 | +1.79% |
| random_hold | +2,275 | +1.09% |
| snake_abs_conv | +1,797 | +0.91% |
| snake_abs | +1,793 | +0.90% |
| snake_anaconda | +1,417 | +0.74% |
| intraweek | +1,390 | +0.67% |
| benchmark_smallcap | +493 | +0.25% |
| intramonth | +324 | +0.15% |
| unified | +180 | +0.08% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -247 | -0.13% |
| snake_viper_wild | -253 | -0.13% |
| oracle | -410 | -0.19% |
| benchmark | -1,981 | -0.88% |

Average per day so far: benchmark Rs +572, unified Rs +554, oracle Rs +282, random_hold Rs +259, intramonth Rs +259, intraweek Rs +201, snake_abs_exit_conv Rs +146, snake_abs_exit Rs +120, nifty_calls Rs +44, benchmark_smallcap Rs +35, snake_abs Rs +9, snake_abs_conv Rs +4, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -170, snake_viper_wild Rs -237, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -365, gold Rs -717

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.