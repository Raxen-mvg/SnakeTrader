# Paper trading report

Updated 2026-11-04 14:34 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,345 | +7.17% | 0 | - | 236 |
| snake_abs_exit_conv | 213,574 | +6.79% | 1 | 100% | 255 |
| snake_abs_exit | 213,439 | +6.72% | 1 | 100% | 260 |
| snake_abs | 210,462 | +5.23% | 1 | 100% | 255 |
| snake_abs_conv | 210,318 | +5.16% | 1 | 100% | 255 |
| intraweek | 209,640 | +4.82% | 25 | 48% | 2,757 |
| benchmark | 208,445 | +4.22% | 0 | - | 237 |
| snake_viper_wild | 208,054 | +4.03% | 3 | 33% | 702 |
| intramonth | 206,732 | +3.37% | 0 | - | 235 |
| snake_viper_tick | 204,434 | +2.22% | 2 | 0% | 532 |
| random_hold | 202,996 | +1.50% | 8 | 62% | 649 |
| snake_anaconda | 202,402 | +1.20% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,145 | +0.57% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,222 | -1.89% | 0 | - | 237 |
| gold | 191,180 | -4.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,774 (-5.11%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,425 | +4.62% |
| snake_abs_exit_conv | +9,236 | +4.52% |
| snake_abs_conv | +9,177 | +4.56% |
| snake_abs | +9,153 | +4.55% |
| snake_anaconda | +8,578 | +4.42% |
| gold | +5,902 | +3.19% |
| intraweek | +4,554 | +2.22% |
| benchmark_smallcap | +3,285 | +1.70% |
| intramonth | +2,761 | +1.35% |
| random_hold | +2,528 | +1.26% |
| unified | +2,344 | +1.11% |
| benchmark | +1,744 | +0.84% |
| oracle | +1,156 | +0.58% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,733 | -1.32% |
| snake_viper_wild | -2,839 | -1.35% |

Average per day so far: snake_abs_exit_conv Rs +566, snake_abs_exit Rs +560, unified Rs +531, snake_abs_conv Rs +430, snake_viper_wild Rs +424, snake_abs Rs +418, intraweek Rs +357, benchmark Rs +313, snake_viper_tick Rs +277, intramonth Rs +249, random_hold Rs +111, snake_anaconda Rs +109, nifty_calls Rs +68, oracle Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -164, gold Rs -327, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.