# Paper trading report

Updated 2026-11-25 13:46 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,609 | +12.30% | 0 | - | 236 |
| benchmark | 224,533 | +12.27% | 0 | - | 237 |
| oracle | 212,498 | +6.25% | 0 | - | 233 |
| intramonth | 212,215 | +6.11% | 0 | - | 235 |
| random_hold | 209,700 | +4.85% | 12 | 75% | 1,009 |
| intraweek | 207,504 | +3.75% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,508 | +0.75% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,164 | +0.58% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,758 | -0.12% | 1 | 100% | 255 |
| snake_abs_conv | 199,563 | -0.22% | 1 | 100% | 255 |
| benchmark_smallcap | 198,822 | -0.59% | 0 | - | 237 |
| snake_viper_wild | 197,058 | -1.47% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,702 | -3.15% | 15 | 47% | 2,625 |
| snake_anaconda | 193,285 | -3.36% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,662 | -17.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,986 (-5.51%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,060 | +1.38% |
| random_hold | +1,274 | +0.61% |
| unified | +323 | +0.14% |
| oracle | +156 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -157 | -0.08% |
| intramonth | -536 | -0.25% |
| snake_viper_tick | -3,990 | -2.02% |
| snake_viper_wild | -4,066 | -2.02% |
| intraweek | -4,115 | -1.95% |
| gold | -4,768 | -2.81% |
| snake_anaconda | -5,418 | -2.73% |
| snake_abs | -5,703 | -2.78% |
| snake_abs_conv | -5,739 | -2.80% |
| snake_abs_exit_conv | -5,882 | -2.84% |
| snake_abs_exit | -5,987 | -2.88% |

Average per day so far: unified Rs +615, benchmark Rs +613, oracle Rs +312, intramonth Rs +305, random_hold Rs +243, intraweek Rs +188, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -6, snake_abs_conv Rs -12, benchmark_smallcap Rs -33, snake_viper_wild Rs -92, snake_anaconda Rs -192, snake_viper_tick Rs -217, snake_nonews Rs -292, snake Rs -311, gold Rs -883

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.