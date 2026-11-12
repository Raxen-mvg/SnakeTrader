# Paper trading report

Updated 2026-11-12 13:34 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,233 | +10.62% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| snake_abs_exit_conv | 218,659 | +9.33% | 2 | 50% | 345 |
| snake_abs_exit | 217,628 | +8.81% | 2 | 50% | 345 |
| snake_abs | 215,684 | +7.84% | 1 | 100% | 255 |
| snake_abs_conv | 215,512 | +7.76% | 1 | 100% | 255 |
| intraweek | 214,557 | +7.28% | 30 | 53% | 3,302 |
| oracle | 213,158 | +6.58% | 0 | - | 233 |
| intramonth | 211,795 | +5.90% | 0 | - | 235 |
| random_hold | 208,037 | +4.02% | 10 | 70% | 733 |
| snake_viper_wild | 207,334 | +3.67% | 10 | 50% | 1,825 |
| snake_anaconda | 206,465 | +3.23% | 3 | 33% | 374 |
| snake_viper_tick | 203,786 | +1.89% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,314 | -6.84% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,110 (-3.94%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,342 | +1.15% |
| benchmark_smallcap | +2,107 | +1.05% |
| snake_abs | +2,059 | +0.96% |
| snake_abs_conv | +2,055 | +0.96% |
| snake_abs_exit_conv | +1,507 | +0.69% |
| snake_abs_exit | +1,466 | +0.68% |
| intraweek | +1,423 | +0.67% |
| unified | +1,419 | +0.65% |
| oracle | +1,155 | +0.55% |
| benchmark | +1,002 | +0.46% |
| random_hold | +927 | +0.45% |
| intramonth | +799 | +0.38% |
| snake_viper_wild | +592 | +0.29% |
| snake_viper_tick | +577 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,272 | -1.73% |

Average per day so far: unified Rs +664, snake_abs_exit_conv Rs +643, benchmark Rs +633, snake_abs_exit Rs +608, snake_abs_conv Rs +535, snake_abs Rs +523, intraweek Rs +455, oracle Rs +411, intramonth Rs +369, snake_viper_wild Rs +306, random_hold Rs +251, snake_anaconda Rs +239, snake_viper_tick Rs +180, benchmark_smallcap Rs +104, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -428

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.