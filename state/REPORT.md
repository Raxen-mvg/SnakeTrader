# Paper trading report

Updated 2026-11-27 09:21 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,734 | +12.87% | 0 | - | 237 |
| unified | 223,104 | +11.55% | 0 | - | 236 |
| oracle | 212,712 | +6.36% | 0 | - | 233 |
| intramonth | 210,750 | +5.38% | 0 | - | 235 |
| random_hold | 209,971 | +4.99% | 13 | 69% | 1,037 |
| intraweek | 207,910 | +3.96% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,356 | +1.18% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,813 | +0.91% | 2 | 50% | 345 |
| benchmark_smallcap | 201,356 | +0.68% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,352 | -0.32% | 1 | 100% | 255 |
| snake_abs_conv | 199,172 | -0.41% | 1 | 100% | 255 |
| snake_anaconda | 193,213 | -3.39% | 3 | 33% | 374 |
| snake_viper_wild | 191,865 | -4.07% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,607 | -5.70% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,361 | -15.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,780 (-5.61%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,367 | +1.43% |
| snake_abs_exit_conv | +1,416 | +0.71% |
| random_hold | +1,377 | +0.66% |
| snake_abs_exit | +1,279 | +0.64% |
| snake_anaconda | +916 | +0.48% |
| intraweek | +861 | +0.42% |
| snake_abs_conv | +806 | +0.41% |
| snake_abs | +800 | +0.40% |
| benchmark_smallcap | +516 | +0.26% |
| oracle | +477 | +0.23% |
| intramonth | +217 | +0.10% |
| unified | +26 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -252 | -0.11% |
| snake_viper_tick | -334 | -0.18% |
| snake_viper_wild | -341 | -0.18% |

Average per day so far: benchmark Rs +613, unified Rs +550, oracle Rs +303, intramonth Rs +256, random_hold Rs +237, intraweek Rs +188, snake_abs_exit Rs +60, snake_abs_exit_conv Rs +46, nifty_calls Rs +44, benchmark_smallcap Rs +36, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -16, snake_abs_conv Rs -21, snake_anaconda Rs -183, snake_viper_wild Rs -239, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -368, gold Rs -753

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.