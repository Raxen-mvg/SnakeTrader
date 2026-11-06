# Paper trading report

Updated 2026-11-06 10:45 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,742 | +7.37% | 0 | - | 236 |
| benchmark | 214,604 | +7.30% | 0 | - | 237 |
| intraweek | 210,195 | +5.10% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,544 | +4.77% | 1 | 100% | 255 |
| snake_abs_exit | 209,334 | +4.67% | 1 | 100% | 260 |
| intramonth | 206,663 | +3.33% | 0 | - | 235 |
| snake_abs | 206,496 | +3.25% | 1 | 100% | 255 |
| snake_abs_conv | 206,329 | +3.16% | 1 | 100% | 255 |
| oracle | 204,796 | +2.40% | 0 | - | 233 |
| random_hold | 203,164 | +1.58% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,417 | -0.79% | 3 | 33% | 702 |
| snake_anaconda | 196,951 | -1.52% | 3 | 33% | 374 |
| snake_viper_tick | 195,061 | -2.47% | 2 | 0% | 532 |
| benchmark_smallcap | 194,686 | -2.66% | 0 | - | 237 |
| gold | 190,144 | -4.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,351 (-6.32%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +834 | +0.39% |
| intraweek | +777 | +0.37% |
| oracle | +724 | +0.35% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,159 | -0.57% |
| unified | -1,241 | -0.57% |
| intramonth | -1,286 | -0.62% |
| benchmark_smallcap | -4,002 | -2.01% |
| gold | -4,077 | -2.10% |
| snake_abs | -5,193 | -2.45% |
| snake_abs_conv | -5,216 | -2.47% |
| snake_abs_exit_conv | -5,260 | -2.45% |
| snake_abs_exit | -5,325 | -2.48% |
| snake_anaconda | -5,528 | -2.73% |
| snake_viper_tick | -6,077 | -3.02% |
| snake_viper_wild | -6,239 | -3.05% |

Average per day so far: unified Rs +508, benchmark Rs +504, snake_abs_exit_conv Rs +367, snake_abs_exit Rs +359, intraweek Rs +352, snake_abs_conv Rs +243, snake_abs Rs +241, intramonth Rs +230, oracle Rs +165, random_hold Rs +109, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -75, snake_anaconda Rs -127, benchmark_smallcap Rs -213, snake_viper_tick Rs -274, gold Rs -340, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.