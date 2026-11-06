# Paper trading report

Updated 2026-11-06 09:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,001 | +7.50% | 0 | - | 237 |
| unified | 214,734 | +7.37% | 0 | - | 236 |
| intraweek | 210,760 | +5.38% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 210,606 | +5.30% | 1 | 100% | 255 |
| snake_abs_exit | 210,356 | +5.18% | 1 | 100% | 260 |
| snake_abs | 207,543 | +3.77% | 1 | 100% | 255 |
| snake_abs_conv | 207,376 | +3.69% | 1 | 100% | 255 |
| intramonth | 206,607 | +3.30% | 0 | - | 235 |
| oracle | 204,724 | +2.36% | 0 | - | 233 |
| random_hold | 204,139 | +2.07% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,518 | -0.74% | 3 | 33% | 702 |
| snake_anaconda | 197,565 | -1.22% | 3 | 33% | 374 |
| benchmark_smallcap | 195,515 | -2.24% | 0 | - | 237 |
| snake_viper_tick | 195,151 | -2.42% | 2 | 0% | 532 |
| gold | 190,391 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,761 (-6.12%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,341 | +0.64% |
| benchmark | +1,232 | +0.58% |
| oracle | +652 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -184 | -0.09% |
| unified | -1,249 | -0.58% |
| intramonth | -1,341 | -0.65% |
| benchmark_smallcap | -3,172 | -1.60% |
| gold | -3,831 | -1.97% |
| snake_abs | -4,146 | -1.96% |
| snake_abs_conv | -4,169 | -1.97% |
| snake_abs_exit_conv | -4,197 | -1.95% |
| snake_abs_exit | -4,302 | -2.00% |
| snake_anaconda | -4,914 | -2.43% |
| snake_viper_tick | -5,987 | -2.98% |
| snake_viper_wild | -6,138 | -3.00% |

Average per day so far: benchmark Rs +517, unified Rs +508, snake_abs_exit_conv Rs +408, snake_abs_exit Rs +398, intraweek Rs +371, snake_abs_conv Rs +284, snake_abs Rs +279, intramonth Rs +228, oracle Rs +163, random_hold Rs +143, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -71, snake_anaconda Rs -101, benchmark_smallcap Rs -179, snake_viper_tick Rs -269, gold Rs -331, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.