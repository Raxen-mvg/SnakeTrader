# Paper trading report

Updated 2026-11-04 14:13 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,775 | +7.39% | 0 | - | 236 |
| snake_abs_exit_conv | 214,215 | +7.11% | 1 | 100% | 255 |
| snake_abs_exit | 214,079 | +7.04% | 1 | 100% | 260 |
| snake_abs | 211,099 | +5.55% | 1 | 100% | 255 |
| snake_abs_conv | 210,952 | +5.48% | 1 | 100% | 255 |
| intraweek | 209,847 | +4.92% | 25 | 48% | 2,757 |
| benchmark | 208,231 | +4.12% | 0 | - | 237 |
| snake_viper_wild | 207,727 | +3.86% | 3 | 33% | 702 |
| intramonth | 206,781 | +3.39% | 0 | - | 235 |
| snake_viper_tick | 204,104 | +2.05% | 2 | 0% | 532 |
| random_hold | 203,120 | +1.56% | 8 | 62% | 649 |
| snake_anaconda | 202,715 | +1.36% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,153 | +0.58% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,964 | -2.02% | 0 | - | 237 |
| gold | 191,377 | -4.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,809 (-5.10%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +10,065 | +4.93% |
| snake_abs_exit_conv | +9,876 | +4.83% |
| snake_abs_conv | +9,811 | +4.88% |
| snake_abs | +9,790 | +4.86% |
| snake_anaconda | +8,891 | +4.59% |
| gold | +6,099 | +3.29% |
| intraweek | +4,762 | +2.32% |
| benchmark_smallcap | +3,027 | +1.57% |
| intramonth | +2,810 | +1.38% |
| unified | +2,774 | +1.31% |
| random_hold | +2,652 | +1.32% |
| benchmark | +1,530 | +0.74% |
| oracle | +1,164 | +0.58% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,063 | -1.48% |
| snake_viper_wild | -3,165 | -1.50% |

Average per day so far: snake_abs_exit_conv Rs +592, snake_abs_exit Rs +587, unified Rs +547, snake_abs_conv Rs +456, snake_abs Rs +444, snake_viper_wild Rs +407, intraweek Rs +365, benchmark Rs +305, snake_viper_tick Rs +256, intramonth Rs +251, snake_anaconda Rs +123, random_hold Rs +116, nifty_calls Rs +68, oracle Rs +43, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -175, gold Rs -319, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.