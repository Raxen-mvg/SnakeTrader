# Paper trading report

Updated 2026-11-25 13:49 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,635 | +12.32% | 0 | - | 236 |
| benchmark | 224,373 | +12.19% | 0 | - | 237 |
| oracle | 212,549 | +6.28% | 0 | - | 233 |
| intramonth | 212,214 | +6.11% | 0 | - | 235 |
| random_hold | 209,662 | +4.83% | 12 | 75% | 1,009 |
| intraweek | 207,537 | +3.77% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,549 | +0.77% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,169 | +0.58% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,742 | -0.13% | 1 | 100% | 255 |
| snake_abs_conv | 199,548 | -0.23% | 1 | 100% | 255 |
| benchmark_smallcap | 198,867 | -0.57% | 0 | - | 237 |
| snake_viper_wild | 197,058 | -1.47% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,702 | -3.15% | 15 | 47% | 2,625 |
| snake_anaconda | 193,270 | -3.37% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,646 | -17.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,999 (-5.50%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,899 | +1.31% |
| random_hold | +1,236 | +0.59% |
| unified | +350 | +0.16% |
| oracle | +207 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -112 | -0.06% |
| intramonth | -537 | -0.25% |
| snake_viper_tick | -3,990 | -2.02% |
| snake_viper_wild | -4,066 | -2.02% |
| intraweek | -4,082 | -1.93% |
| gold | -4,784 | -2.82% |
| snake_anaconda | -5,434 | -2.73% |
| snake_abs | -5,719 | -2.78% |
| snake_abs_conv | -5,755 | -2.80% |
| snake_abs_exit_conv | -5,877 | -2.84% |
| snake_abs_exit | -5,946 | -2.87% |

Average per day so far: unified Rs +616, benchmark Rs +609, oracle Rs +314, intramonth Rs +305, random_hold Rs +242, intraweek Rs +188, nifty_calls Rs +46, snake_abs_exit Rs +42, snake_abs_exit_conv Rs +32, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -7, snake_abs_conv Rs -12, benchmark_smallcap Rs -31, snake_viper_wild Rs -92, snake_anaconda Rs -192, snake_viper_tick Rs -217, snake_nonews Rs -292, snake Rs -311, gold Rs -884

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.