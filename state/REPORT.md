# Paper trading report

Updated 2026-11-06 11:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,700 | +7.35% | 0 | - | 236 |
| benchmark | 214,596 | +7.30% | 0 | - | 237 |
| intraweek | 211,182 | +5.59% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,386 | +4.69% | 1 | 100% | 255 |
| snake_abs_exit | 209,173 | +4.59% | 1 | 100% | 260 |
| intramonth | 206,752 | +3.38% | 0 | - | 235 |
| snake_abs | 206,339 | +3.17% | 1 | 100% | 255 |
| snake_abs_conv | 206,172 | +3.09% | 1 | 100% | 255 |
| oracle | 204,850 | +2.42% | 0 | - | 233 |
| random_hold | 203,235 | +1.62% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,710 | -1.65% | 3 | 33% | 374 |
| snake_viper_wild | 196,056 | -1.97% | 3 | 33% | 702 |
| benchmark_smallcap | 194,731 | -2.63% | 0 | - | 237 |
| snake_viper_tick | 192,735 | -3.63% | 2 | 0% | 532 |
| gold | 189,799 | -5.10% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,348 (-6.33%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,764 | +0.84% |
| benchmark | +826 | +0.39% |
| oracle | +778 | +0.38% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,088 | -0.53% |
| intramonth | -1,197 | -0.57% |
| unified | -1,283 | -0.59% |
| benchmark_smallcap | -3,957 | -1.99% |
| gold | -4,422 | -2.28% |
| snake_abs | -5,349 | -2.53% |
| snake_abs_conv | -5,373 | -2.54% |
| snake_abs_exit_conv | -5,417 | -2.52% |
| snake_abs_exit | -5,486 | -2.56% |
| snake_anaconda | -5,769 | -2.85% |
| snake_viper_tick | -8,403 | -4.18% |
| snake_viper_wild | -8,600 | -4.20% |

Average per day so far: unified Rs +507, benchmark Rs +503, intraweek Rs +386, snake_abs_exit_conv Rs +361, snake_abs_exit Rs +353, snake_abs_conv Rs +237, snake_abs Rs +235, intramonth Rs +233, oracle Rs +167, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -137, snake_viper_wild Rs -188, benchmark_smallcap Rs -211, gold Rs -352, snake_viper_tick Rs -404, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.