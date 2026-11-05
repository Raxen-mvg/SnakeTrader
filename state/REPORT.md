# Paper trading report

Updated 2026-11-05 11:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,064 | +9.03% | 0 | - | 236 |
| snake_abs_exit_conv | 214,625 | +7.31% | 1 | 100% | 255 |
| snake_abs_exit | 214,341 | +7.17% | 1 | 100% | 260 |
| benchmark | 212,691 | +6.35% | 0 | - | 237 |
| snake_abs | 211,504 | +5.75% | 1 | 100% | 255 |
| snake_abs_conv | 211,371 | +5.68% | 1 | 100% | 255 |
| intraweek | 210,726 | +5.36% | 25 | 48% | 2,757 |
| intramonth | 209,931 | +4.97% | 0 | - | 235 |
| snake_viper_wild | 206,852 | +3.43% | 3 | 33% | 702 |
| random_hold | 206,780 | +3.39% | 8 | 62% | 649 |
| oracle | 204,207 | +2.10% | 0 | - | 233 |
| snake_viper_tick | 203,298 | +1.65% | 2 | 0% | 532 |
| snake_anaconda | 202,919 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| gold | 194,484 | -2.76% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,303 (-4.85%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,932 | +1.88% |
| unified | +3,625 | +1.69% |
| random_hold | +3,471 | +1.71% |
| gold | +3,091 | +1.61% |
| intramonth | +2,915 | +1.41% |
| benchmark_smallcap | +2,567 | +1.30% |
| oracle | +2,415 | +1.20% |
| intraweek | +1,028 | +0.49% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -387 | -0.18% |
| snake_abs_exit_conv | -390 | -0.18% |
| snake_abs | -399 | -0.19% |
| snake_abs_exit | -559 | -0.26% |
| snake_anaconda | -901 | -0.44% |
| snake_viper_tick | -2,103 | -1.02% |
| snake_viper_wild | -2,178 | -1.04% |

Average per day so far: unified Rs +645, snake_abs_exit_conv Rs +585, snake_abs_exit Rs +574, snake_abs_conv Rs +455, benchmark Rs +453, snake_abs Rs +442, intraweek Rs +383, intramonth Rs +355, snake_viper_wild Rs +343, random_hold Rs +242, snake_viper_tick Rs +194, oracle Rs +150, snake_anaconda Rs +127, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -32, gold Rs -197, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.