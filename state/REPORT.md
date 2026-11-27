# Paper trading report

Updated 2026-11-27 09:45 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,704 | +12.85% | 0 | - | 237 |
| unified | 223,183 | +11.59% | 0 | - | 236 |
| oracle | 212,626 | +6.31% | 0 | - | 233 |
| intramonth | 210,801 | +5.40% | 0 | - | 235 |
| random_hold | 209,788 | +4.89% | 13 | 69% | 1,037 |
| intraweek | 207,991 | +4.00% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,559 | +2.28% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,705 | +1.85% | 2 | 50% | 345 |
| benchmark_smallcap | 202,017 | +1.01% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,523 | +0.26% | 1 | 100% | 255 |
| snake_abs_conv | 200,344 | +0.17% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,463 | -2.77% | 3 | 33% | 374 |
| snake_viper_wild | 192,892 | -3.55% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,613 | -5.19% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,263 | -15.87% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,824 (-5.59%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,482 | +1.73% |
| snake_abs_exit_conv | +3,309 | +1.65% |
| gold | +2,269 | +1.37% |
| snake_anaconda | +2,167 | +1.13% |
| snake_abs_conv | +1,977 | +1.00% |
| snake_abs | +1,971 | +0.99% |
| random_hold | +1,194 | +0.57% |
| benchmark_smallcap | +1,177 | +0.59% |
| intraweek | +942 | +0.46% |
| snake_viper_wild | +686 | +0.36% |
| snake_viper_tick | +672 | +0.36% |
| oracle | +390 | +0.18% |
| intramonth | +267 | +0.13% |
| unified | +105 | +0.05% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -283 | -0.12% |

Average per day so far: benchmark Rs +612, unified Rs +552, oracle Rs +301, intramonth Rs +257, random_hold Rs +233, intraweek Rs +190, snake_abs_exit Rs +117, snake_abs_exit_conv Rs +95, benchmark_smallcap Rs +53, nifty_calls Rs +44, snake_abs Rs +13, snake_abs_conv Rs +9, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -150, snake_viper_wild Rs -209, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -335, gold Rs -756

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.