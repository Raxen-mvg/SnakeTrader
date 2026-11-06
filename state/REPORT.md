# Paper trading report

Updated 2026-11-06 10:48 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,871 | +7.44% | 0 | - | 237 |
| unified | 214,685 | +7.34% | 0 | - | 236 |
| intraweek | 210,495 | +5.25% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,433 | +4.72% | 1 | 100% | 255 |
| snake_abs_exit | 209,219 | +4.61% | 1 | 100% | 260 |
| intramonth | 206,650 | +3.33% | 0 | - | 235 |
| snake_abs | 206,386 | +3.19% | 1 | 100% | 255 |
| snake_abs_conv | 206,219 | +3.11% | 1 | 100% | 255 |
| oracle | 204,936 | +2.47% | 0 | - | 233 |
| random_hold | 203,320 | +1.66% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,281 | -0.86% | 3 | 33% | 702 |
| snake_anaconda | 196,853 | -1.57% | 3 | 33% | 374 |
| snake_viper_tick | 194,925 | -2.54% | 2 | 0% | 532 |
| benchmark_smallcap | 194,776 | -2.61% | 0 | - | 237 |
| gold | 190,210 | -4.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,367 (-6.32%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,102 | +0.52% |
| intraweek | +1,077 | +0.51% |
| oracle | +864 | +0.42% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,003 | -0.49% |
| unified | -1,299 | -0.60% |
| intramonth | -1,299 | -0.62% |
| benchmark_smallcap | -3,912 | -1.97% |
| gold | -4,011 | -2.06% |
| snake_abs | -5,303 | -2.50% |
| snake_abs_conv | -5,326 | -2.52% |
| snake_abs_exit_conv | -5,370 | -2.50% |
| snake_abs_exit | -5,440 | -2.53% |
| snake_anaconda | -5,626 | -2.78% |
| snake_viper_tick | -6,213 | -3.09% |
| snake_viper_wild | -6,375 | -3.12% |

Average per day so far: benchmark Rs +513, unified Rs +506, snake_abs_exit_conv Rs +363, intraweek Rs +362, snake_abs_exit Rs +355, snake_abs_conv Rs +239, snake_abs Rs +237, intramonth Rs +229, oracle Rs +170, random_hold Rs +114, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -82, snake_anaconda Rs -131, benchmark_smallcap Rs -209, snake_viper_tick Rs -282, gold Rs -338, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.