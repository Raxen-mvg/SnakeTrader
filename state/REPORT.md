# Paper trading report

Updated 2026-11-27 10:32 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,916 | +12.46% | 0 | - | 237 |
| unified | 222,858 | +11.43% | 0 | - | 236 |
| oracle | 212,370 | +6.18% | 0 | - | 233 |
| intramonth | 210,631 | +5.32% | 0 | - | 235 |
| random_hold | 209,990 | +5.00% | 13 | 69% | 1,037 |
| intraweek | 208,178 | +4.09% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,983 | +2.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,750 | +1.88% | 2 | 50% | 345 |
| benchmark_smallcap | 201,995 | +1.00% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,823 | +0.41% | 1 | 100% | 255 |
| snake_abs_conv | 200,644 | +0.32% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,386 | -2.81% | 3 | 33% | 374 |
| snake_viper_wild | 193,518 | -3.24% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,226 | -4.89% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,575 | -15.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,741 (-5.63%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,906 | +1.94% |
| snake_abs_exit_conv | +3,353 | +1.67% |
| gold | +2,581 | +1.55% |
| snake_abs_conv | +2,277 | +1.15% |
| snake_abs | +2,270 | +1.14% |
| snake_anaconda | +2,089 | +1.09% |
| random_hold | +1,396 | +0.67% |
| snake_viper_wild | +1,312 | +0.68% |
| snake_viper_tick | +1,285 | +0.68% |
| benchmark_smallcap | +1,155 | +0.57% |
| intraweek | +1,129 | +0.55% |
| oracle | +135 | +0.06% |
| intramonth | +98 | +0.05% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -221 | -0.10% |
| benchmark | -1,071 | -0.47% |

Average per day so far: benchmark Rs +593, unified Rs +544, oracle Rs +295, intramonth Rs +253, random_hold Rs +238, intraweek Rs +195, snake_abs_exit Rs +128, snake_abs_exit_conv Rs +96, benchmark_smallcap Rs +52, nifty_calls Rs +44, snake_abs Rs +21, snake_abs_conv Rs +17, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -152, snake_viper_wild Rs -191, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -315, gold Rs -748

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.