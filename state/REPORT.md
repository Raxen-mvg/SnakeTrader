# Paper trading report

Updated 2026-11-27 11:49 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,166 | +12.08% | 0 | - | 237 |
| unified | 221,836 | +10.92% | 0 | - | 236 |
| oracle | 211,857 | +5.93% | 0 | - | 233 |
| random_hold | 210,251 | +5.12% | 13 | 69% | 1,037 |
| intramonth | 210,098 | +5.05% | 0 | - | 235 |
| intraweek | 207,777 | +3.89% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,585 | +2.79% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,119 | +2.06% | 2 | 50% | 345 |
| benchmark_smallcap | 201,838 | +0.92% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,859 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,684 | +0.34% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,415 | -2.79% | 3 | 33% | 374 |
| snake_viper_wild | 192,898 | -3.55% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,620 | -5.19% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,167 | -15.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,364 (-5.82%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,507 | +2.24% |
| snake_abs_exit_conv | +3,723 | +1.86% |
| gold | +3,173 | +1.91% |
| snake_abs_conv | +2,318 | +1.17% |
| snake_abs | +2,307 | +1.16% |
| snake_anaconda | +2,118 | +1.10% |
| random_hold | +1,657 | +0.79% |
| benchmark_smallcap | +998 | +0.50% |
| intraweek | +729 | +0.35% |
| snake_viper_wild | +693 | +0.36% |
| snake_viper_tick | +679 | +0.36% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -379 | -0.18% |
| intramonth | -435 | -0.21% |
| unified | -1,242 | -0.56% |
| benchmark | -1,821 | -0.81% |

Average per day so far: benchmark Rs +575, unified Rs +520, oracle Rs +282, random_hold Rs +244, intramonth Rs +240, intraweek Rs +185, snake_abs_exit Rs +143, snake_abs_exit_conv Rs +106, benchmark_smallcap Rs +48, nifty_calls Rs +44, snake_abs Rs +21, snake_abs_conv Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -151, snake_viper_wild Rs -209, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -335, gold Rs -734

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.