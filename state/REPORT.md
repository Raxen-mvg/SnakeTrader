# Paper trading report

Updated 2026-11-25 13:30 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,692 | +12.35% | 0 | - | 236 |
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| oracle | 212,466 | +6.23% | 0 | - | 233 |
| intramonth | 212,402 | +6.20% | 0 | - | 235 |
| random_hold | 209,798 | +4.90% | 12 | 75% | 1,009 |
| intraweek | 208,220 | +4.11% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,007 | +1.00% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,636 | +0.82% | 2 | 50% | 345 |
| snake_abs | 200,167 | +0.08% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,979 | -0.01% | 1 | 100% | 255 |
| benchmark_smallcap | 198,878 | -0.56% | 0 | - | 237 |
| snake_viper_wild | 197,025 | -1.49% | 16 | 50% | 2,827 |
| snake_anaconda | 193,697 | -3.15% | 3 | 33% | 374 |
| snake_viper_tick | 193,669 | -3.17% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,695 | -17.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,183 (-5.41%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,876 | +1.30% |
| random_hold | +1,371 | +0.66% |
| unified | +407 | +0.18% |
| oracle | +124 | +0.06% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -101 | -0.05% |
| intramonth | -349 | -0.16% |
| intraweek | -3,399 | -1.61% |
| snake_viper_tick | -4,023 | -2.04% |
| snake_viper_wild | -4,099 | -2.04% |
| gold | -4,735 | -2.79% |
| snake_anaconda | -5,006 | -2.52% |
| snake_abs | -5,294 | -2.58% |
| snake_abs_conv | -5,324 | -2.59% |
| snake_abs_exit_conv | -5,410 | -2.61% |
| snake_abs_exit | -5,488 | -2.65% |

Average per day so far: unified Rs +617, benchmark Rs +609, oracle Rs +312, intramonth Rs +310, random_hold Rs +245, intraweek Rs +206, snake_abs_exit Rs +54, nifty_calls Rs +46, snake_abs_exit_conv Rs +44, snake_abs Rs +4, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs_conv Rs -1, benchmark_smallcap Rs -31, snake_viper_wild Rs -93, snake_anaconda Rs -180, snake_viper_tick Rs -218, snake_nonews Rs -292, snake Rs -311, gold Rs -883

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.