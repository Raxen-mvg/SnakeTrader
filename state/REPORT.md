# Paper trading report

Updated 2026-11-25 13:02 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,563 | +12.28% | 0 | - | 236 |
| benchmark | 224,051 | +12.03% | 0 | - | 237 |
| oracle | 212,510 | +6.25% | 0 | - | 233 |
| intramonth | 212,499 | +6.25% | 0 | - | 235 |
| random_hold | 209,689 | +4.84% | 12 | 75% | 1,009 |
| intraweek | 208,360 | +4.18% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,541 | +0.77% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,245 | +0.62% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,886 | -0.06% | 1 | 100% | 255 |
| snake_abs_conv | 199,695 | -0.15% | 1 | 100% | 255 |
| benchmark_smallcap | 198,935 | -0.53% | 0 | - | 237 |
| snake_viper_wild | 196,756 | -1.62% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,406 | -3.30% | 15 | 47% | 2,625 |
| snake_anaconda | 193,296 | -3.35% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,646 | -17.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,125 (-5.44%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,578 | +1.16% |
| random_hold | +1,263 | +0.61% |
| unified | +278 | +0.12% |
| oracle | +168 | +0.08% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -45 | -0.02% |
| intramonth | -253 | -0.12% |
| intraweek | -3,259 | -1.54% |
| snake_viper_tick | -4,287 | -2.17% |
| snake_viper_wild | -4,368 | -2.17% |
| gold | -4,784 | -2.82% |
| snake_anaconda | -5,408 | -2.72% |
| snake_abs | -5,575 | -2.71% |
| snake_abs_conv | -5,608 | -2.73% |
| snake_abs_exit_conv | -5,801 | -2.80% |
| snake_abs_exit | -5,954 | -2.87% |

Average per day so far: unified Rs +614, benchmark Rs +601, oracle Rs +313, intramonth Rs +312, random_hold Rs +242, intraweek Rs +209, nifty_calls Rs +46, snake_abs_exit Rs +42, snake_abs_exit_conv Rs +34, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -3, snake_abs_conv Rs -8, benchmark_smallcap Rs -30, snake_viper_wild Rs -101, snake_anaconda Rs -192, snake_viper_tick Rs -227, snake_nonews Rs -292, snake Rs -311, gold Rs -884

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.