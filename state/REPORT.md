# Paper trading report

Updated 2026-11-05 11:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,382 | +9.19% | 0 | - | 236 |
| snake_abs_exit_conv | 215,013 | +7.51% | 1 | 100% | 255 |
| snake_abs_exit | 214,717 | +7.36% | 1 | 100% | 260 |
| benchmark | 212,484 | +6.24% | 0 | - | 237 |
| snake_abs | 211,890 | +5.95% | 1 | 100% | 255 |
| snake_abs_conv | 211,755 | +5.88% | 1 | 100% | 255 |
| intraweek | 210,883 | +5.44% | 25 | 48% | 2,757 |
| intramonth | 210,260 | +5.13% | 0 | - | 235 |
| random_hold | 206,874 | +3.44% | 8 | 62% | 649 |
| snake_viper_wild | 206,874 | +3.44% | 3 | 33% | 702 |
| oracle | 204,203 | +2.10% | 0 | - | 233 |
| snake_viper_tick | 203,320 | +1.66% | 2 | 0% | 532 |
| snake_anaconda | 203,195 | +1.60% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,304 | -0.35% | 0 | - | 237 |
| gold | 193,810 | -3.10% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,510 (-4.74%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +3,942 | +1.84% |
| benchmark | +3,726 | +1.78% |
| random_hold | +3,565 | +1.75% |
| intramonth | +3,244 | +1.57% |
| benchmark_smallcap | +2,634 | +1.34% |
| gold | +2,417 | +1.26% |
| oracle | +2,411 | +1.20% |
| intraweek | +1,186 | +0.56% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -2 | -0.00% |
| snake_abs_conv | -3 | -0.00% |
| snake_abs | -14 | -0.01% |
| snake_abs_exit | -184 | -0.09% |
| snake_anaconda | -625 | -0.31% |
| snake_viper_tick | -2,080 | -1.01% |
| snake_viper_wild | -2,156 | -1.03% |

Average per day so far: unified Rs +656, snake_abs_exit_conv Rs +601, snake_abs_exit Rs +589, snake_abs_conv Rs +470, snake_abs Rs +457, benchmark Rs +446, intraweek Rs +389, intramonth Rs +366, snake_viper_wild Rs +344, random_hold Rs +245, snake_viper_tick Rs +195, oracle Rs +150, snake_anaconda Rs +139, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -29, gold Rs -221, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.