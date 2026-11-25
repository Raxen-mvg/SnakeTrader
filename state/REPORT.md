# Paper trading report

Updated 2026-11-25 13:37 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,518 | +12.26% | 0 | - | 236 |
| benchmark | 224,044 | +12.02% | 0 | - | 237 |
| oracle | 212,408 | +6.20% | 0 | - | 233 |
| intramonth | 212,156 | +6.08% | 0 | - | 235 |
| random_hold | 209,594 | +4.80% | 12 | 75% | 1,009 |
| intraweek | 207,639 | +3.82% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,476 | +0.74% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,160 | +0.58% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,678 | -0.16% | 1 | 100% | 255 |
| snake_abs_conv | 199,481 | -0.26% | 1 | 100% | 255 |
| benchmark_smallcap | 198,834 | -0.58% | 0 | - | 237 |
| snake_viper_wild | 197,006 | -1.50% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,650 | -3.17% | 15 | 47% | 2,625 |
| snake_anaconda | 193,205 | -3.40% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,449 | -17.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,944 (-5.53%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,570 | +1.16% |
| random_hold | +1,167 | +0.56% |
| unified | +232 | +0.10% |
| oracle | +65 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -146 | -0.07% |
| intramonth | -596 | -0.28% |
| intraweek | -3,980 | -1.88% |
| snake_viper_tick | -4,042 | -2.04% |
| snake_viper_wild | -4,119 | -2.05% |
| gold | -4,981 | -2.94% |
| snake_anaconda | -5,498 | -2.77% |
| snake_abs | -5,782 | -2.81% |
| snake_abs_conv | -5,821 | -2.83% |
| snake_abs_exit_conv | -5,886 | -2.84% |
| snake_abs_exit | -6,019 | -2.90% |

Average per day so far: unified Rs +613, benchmark Rs +601, oracle Rs +310, intramonth Rs +304, random_hold Rs +240, intraweek Rs +191, nifty_calls Rs +46, snake_abs_exit Rs +40, snake_abs_exit_conv Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -8, snake_abs_conv Rs -14, benchmark_smallcap Rs -32, snake_viper_wild Rs -94, snake_anaconda Rs -194, snake_viper_tick Rs -219, snake_nonews Rs -292, snake Rs -311, gold Rs -889

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.