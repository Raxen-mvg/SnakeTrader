# Paper trading report

Updated 2026-11-06 11:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,558 | +7.28% | 0 | - | 236 |
| benchmark | 214,550 | +7.28% | 0 | - | 237 |
| intraweek | 211,695 | +5.85% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,208 | +4.60% | 1 | 100% | 255 |
| snake_abs_exit | 208,994 | +4.50% | 1 | 100% | 260 |
| intramonth | 206,639 | +3.32% | 0 | - | 235 |
| snake_abs | 206,165 | +3.08% | 1 | 100% | 255 |
| snake_abs_conv | 205,997 | +3.00% | 1 | 100% | 255 |
| oracle | 204,761 | +2.38% | 0 | - | 233 |
| random_hold | 203,336 | +1.67% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,585 | -1.71% | 3 | 33% | 374 |
| snake_viper_wild | 195,290 | -2.35% | 3 | 33% | 702 |
| benchmark_smallcap | 194,832 | -2.58% | 0 | - | 237 |
| snake_viper_tick | 191,982 | -4.01% | 2 | 0% | 532 |
| gold | 190,111 | -4.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,300 (-6.35%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,276 | +1.09% |
| benchmark | +780 | +0.36% |
| oracle | +689 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -987 | -0.48% |
| intramonth | -1,309 | -0.63% |
| unified | -1,426 | -0.66% |
| benchmark_smallcap | -3,856 | -1.94% |
| gold | -4,110 | -2.12% |
| snake_abs | -5,523 | -2.61% |
| snake_abs_conv | -5,548 | -2.62% |
| snake_abs_exit_conv | -5,596 | -2.60% |
| snake_abs_exit | -5,664 | -2.64% |
| snake_anaconda | -5,895 | -2.91% |
| snake_viper_tick | -9,156 | -4.55% |
| snake_viper_wild | -9,366 | -4.58% |

Average per day so far: unified Rs +502, benchmark Rs +502, intraweek Rs +403, snake_abs_exit_conv Rs +354, snake_abs_exit Rs +346, snake_abs_conv Rs +231, intramonth Rs +229, snake_abs Rs +228, oracle Rs +164, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -142, benchmark_smallcap Rs -207, snake_viper_wild Rs -224, gold Rs -341, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -445

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.