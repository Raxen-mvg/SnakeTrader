# Paper trading report

Updated 2026-11-03 13:23 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 211,923 | +5.96% | 0 | - | 236 |
| snake_viper_wild | 211,883 | +5.94% | 3 | 33% | 702 |
| snake_viper_tick | 208,141 | +4.07% | 2 | 0% | 532 |
| benchmark | 206,747 | +3.37% | 0 | - | 237 |
| intraweek | 204,932 | +2.47% | 25 | 48% | 2,757 |
| intramonth | 204,271 | +2.13% | 0 | - | 235 |
| snake_abs_exit_conv | 203,697 | +1.85% | 1 | 100% | 255 |
| snake_abs_exit | 203,420 | +1.71% | 1 | 100% | 260 |
| random_hold | 201,838 | +0.92% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,689 | +0.34% | 1 | 100% | 255 |
| snake_abs_conv | 200,511 | +0.26% | 1 | 100% | 255 |
| oracle | 200,234 | +0.12% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,563 | -3.22% | 3 | 33% | 342 |
| benchmark_smallcap | 193,296 | -3.35% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,821 | -7.09% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,572 (-5.21%).

Profit on 2026-11-03:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,274 | +1.61% |
| intraweek | +3,058 | +1.51% |
| snake_abs_exit_conv | +2,949 | +1.47% |
| snake_abs_exit | +2,936 | +1.46% |
| snake_abs_conv | +2,922 | +1.48% |
| snake_abs | +2,907 | +1.47% |
| intramonth | +2,579 | +1.28% |
| snake_anaconda | +2,464 | +1.29% |
| unified | +2,313 | +1.10% |
| benchmark_smallcap | +1,188 | +0.62% |
| random_hold | +1,052 | +0.52% |
| gold | +806 | +0.43% |
| oracle | +490 | +0.24% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,772 | -1.78% |
| snake_viper_wild | -3,865 | -1.79% |

Average per day so far: snake_viper_wild Rs +660, snake_viper_tick Rs +543, unified Rs +459, benchmark Rs +259, intraweek Rs +190, intramonth Rs +164, snake_abs_exit_conv Rs +161, snake_abs_exit Rs +149, random_hold Rs +71, nifty_calls Rs +71, snake_abs Rs +29, snake_abs_conv Rs +22, oracle Rs +9, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -305, snake_anaconda Rs -307, snake_nonews Rs -462, snake Rs -486, gold Rs -545

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.