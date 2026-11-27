# Paper trading report

Updated 2026-11-27 15:28 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,439 | +11.72% | 0 | - | 237 |
| unified | 223,084 | +11.54% | 0 | - | 236 |
| random_hold | 211,445 | +5.72% | 13 | 69% | 1,037 |
| oracle | 211,395 | +5.70% | 0 | - | 233 |
| intramonth | 210,987 | +5.49% | 0 | - | 235 |
| intraweek | 207,657 | +3.83% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,477 | +3.24% | 2 | 50% | 345 |
| snake_abs_exit | 204,198 | +2.10% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,562 | -0.22% | 1 | 100% | 255 |
| snake_abs_conv | 199,374 | -0.31% | 1 | 100% | 255 |
| snake_anaconda | 192,931 | -3.53% | 3 | 33% | 374 |
| snake_viper_wild | 192,620 | -3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,347 | -5.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,498 | -14.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,793 (-5.60%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,080 | +3.03% |
| gold | +4,505 | +2.71% |
| snake_abs_exit | +3,120 | +1.55% |
| random_hold | +2,851 | +1.37% |
| snake_abs | +1,010 | +0.51% |
| snake_abs_conv | +1,008 | +0.51% |
| snake_anaconda | +635 | +0.33% |
| benchmark_smallcap | +617 | +0.31% |
| intraweek | +609 | +0.29% |
| intramonth | +453 | +0.21% |
| snake_viper_wild | +414 | +0.22% |
| snake_viper_tick | +406 | +0.21% |
| unified | +6 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -841 | -0.40% |
| benchmark | -2,547 | -1.13% |

Average per day so far: benchmark Rs +558, unified Rs +550, random_hold Rs +272, oracle Rs +271, intramonth Rs +262, intraweek Rs +182, snake_abs_exit_conv Rs +166, snake_abs_exit Rs +108, nifty_calls Rs +44, benchmark_smallcap Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -11, snake_abs_conv Rs -16, snake_anaconda Rs -191, snake_viper_wild Rs -217, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -702

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.