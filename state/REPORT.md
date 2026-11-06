# Paper trading report

Updated 2026-11-06 13:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,241 | +8.12% | 0 | - | 237 |
| unified | 214,701 | +7.35% | 0 | - | 236 |
| snake_abs_exit_conv | 208,585 | +4.29% | 1 | 100% | 255 |
| snake_abs_exit | 208,489 | +4.25% | 1 | 100% | 260 |
| intraweek | 208,459 | +4.23% | 25 | 48% | 2,757 |
| intramonth | 206,951 | +3.48% | 0 | - | 235 |
| snake_abs | 205,576 | +2.79% | 1 | 100% | 255 |
| snake_abs_conv | 205,387 | +2.69% | 1 | 100% | 255 |
| oracle | 205,220 | +2.61% | 0 | - | 233 |
| random_hold | 203,329 | +1.66% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,115 | -1.94% | 3 | 33% | 702 |
| snake_anaconda | 195,918 | -2.04% | 3 | 33% | 374 |
| benchmark_smallcap | 195,224 | -2.39% | 0 | - | 237 |
| snake_viper_tick | 192,790 | -3.60% | 2 | 0% | 532 |
| gold | 190,933 | -4.53% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,885 (-6.56%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,471 | +1.16% |
| oracle | +1,148 | +0.56% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -960 | -0.46% |
| random_hold | -994 | -0.49% |
| intramonth | -997 | -0.48% |
| unified | -1,283 | -0.59% |
| gold | -3,288 | -1.69% |
| benchmark_smallcap | -3,464 | -1.74% |
| snake_abs | -6,112 | -2.89% |
| snake_abs_conv | -6,158 | -2.91% |
| snake_abs_exit | -6,169 | -2.87% |
| snake_abs_exit_conv | -6,219 | -2.90% |
| snake_anaconda | -6,561 | -3.24% |
| snake_viper_tick | -8,348 | -4.15% |
| snake_viper_wild | -8,541 | -4.17% |

Average per day so far: benchmark Rs +560, unified Rs +507, snake_abs_exit_conv Rs +330, snake_abs_exit Rs +327, intraweek Rs +292, intramonth Rs +240, snake_abs_conv Rs +207, snake_abs Rs +207, oracle Rs +180, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -170, snake_viper_wild Rs -185, benchmark_smallcap Rs -191, gold Rs -313, snake_viper_tick Rs -401, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.