# Paper trading report

Updated 2026-11-04 11:49 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,942 | +6.97% | 0 | - | 236 |
| intraweek | 209,386 | +4.69% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,701 | +4.35% | 1 | 100% | 255 |
| snake_abs_exit | 208,571 | +4.29% | 1 | 100% | 260 |
| benchmark | 207,481 | +3.74% | 0 | - | 237 |
| snake_viper_wild | 206,834 | +3.42% | 3 | 33% | 702 |
| intramonth | 205,948 | +2.97% | 0 | - | 235 |
| snake_abs | 205,607 | +2.80% | 1 | 100% | 255 |
| snake_abs_conv | 205,458 | +2.73% | 1 | 100% | 255 |
| snake_viper_tick | 203,231 | +1.61% | 2 | 0% | 532 |
| random_hold | 202,727 | +1.36% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,973 | +0.49% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,566 | -1.22% | 3 | 33% | 361 |
| benchmark_smallcap | 194,787 | -2.61% | 0 | - | 237 |
| gold | 190,670 | -4.67% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,191 (-5.40%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,392 | +2.91% |
| snake_abs_exit | +4,556 | +2.23% |
| snake_abs_exit_conv | +4,362 | +2.13% |
| snake_abs_conv | +4,317 | +2.15% |
| intraweek | +4,301 | +2.10% |
| snake_abs | +4,298 | +2.13% |
| snake_anaconda | +3,742 | +1.93% |
| random_hold | +2,259 | +1.13% |
| intramonth | +1,977 | +0.97% |
| unified | +1,941 | +0.92% |
| benchmark_smallcap | +1,850 | +0.96% |
| oracle | +983 | +0.49% |
| benchmark | +780 | +0.38% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,936 | -1.90% |
| snake_viper_wild | -4,059 | -1.93% |

Average per day so far: unified Rs +516, snake_abs_exit_conv Rs +363, snake_viper_wild Rs +360, snake_abs_exit Rs +357, intraweek Rs +348, benchmark Rs +277, snake_abs_conv Rs +227, snake_abs Rs +224, intramonth Rs +220, snake_viper_tick Rs +202, random_hold Rs +101, nifty_calls Rs +68, oracle Rs +36, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -111, benchmark_smallcap Rs -227, gold Rs -346, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.