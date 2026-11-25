# Paper trading report

Updated 2026-11-25 15:30 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,023 | +12.51% | 0 | - | 237 |
| unified | 224,100 | +12.05% | 0 | - | 236 |
| oracle | 213,795 | +6.90% | 0 | - | 233 |
| intramonth | 211,693 | +5.85% | 0 | - | 235 |
| random_hold | 209,493 | +4.75% | 12 | 75% | 1,009 |
| intraweek | 206,743 | +3.37% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,256 | +1.13% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,976 | +0.99% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,150 | +0.07% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,972 | -0.01% | 1 | 100% | 255 |
| benchmark_smallcap | 198,811 | -0.59% | 0 | - | 237 |
| snake_viper_wild | 197,543 | -1.23% | 16 | 50% | 2,827 |
| snake_anaconda | 194,553 | -2.72% | 3 | 33% | 374 |
| snake_viper_tick | 194,177 | -2.91% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,596 | -17.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,057 (-5.47%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,550 | +1.60% |
| oracle | +1,453 | +0.68% |
| random_hold | +1,066 | +0.51% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| benchmark_smallcap | -168 | -0.09% |
| unified | -185 | -0.08% |
| intramonth | -1,058 | -0.50% |
| snake_viper_tick | -3,516 | -1.78% |
| snake_viper_wild | -3,581 | -1.78% |
| snake_anaconda | -4,150 | -2.09% |
| gold | -4,833 | -2.85% |
| intraweek | -4,876 | -2.30% |
| snake_abs_exit_conv | -5,070 | -2.45% |
| snake_abs_exit | -5,239 | -2.52% |
| snake_abs | -5,311 | -2.58% |
| snake_abs_conv | -5,330 | -2.60% |

Average per day so far: benchmark Rs +626, unified Rs +602, oracle Rs +345, intramonth Rs +292, random_hold Rs +237, intraweek Rs +169, snake_abs_exit Rs +61, snake_abs_exit_conv Rs +53, nifty_calls Rs +46, snake_abs Rs +4, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs_conv Rs -1, benchmark_smallcap Rs -33, snake_viper_wild Rs -77, snake_anaconda Rs -156, snake_viper_tick Rs -201, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.