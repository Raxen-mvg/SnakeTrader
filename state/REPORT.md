# Paper trading report

Updated 2026-11-27 09:28 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,291 | +12.64% | 0 | - | 237 |
| unified | 222,998 | +11.50% | 0 | - | 236 |
| oracle | 212,178 | +6.09% | 0 | - | 233 |
| intramonth | 210,564 | +5.28% | 0 | - | 235 |
| random_hold | 209,409 | +4.70% | 13 | 69% | 1,037 |
| intraweek | 207,377 | +3.69% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,431 | +1.22% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,722 | +0.86% | 2 | 50% | 345 |
| benchmark_smallcap | 201,210 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,139 | -0.43% | 1 | 100% | 255 |
| snake_abs_conv | 198,946 | -0.53% | 1 | 100% | 255 |
| snake_anaconda | 192,763 | -3.62% | 3 | 33% | 374 |
| snake_viper_wild | 192,033 | -3.98% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,772 | -5.61% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,049 | -15.98% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,466 (-5.77%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,055 | +1.24% |
| snake_abs_exit | +1,354 | +0.67% |
| snake_abs_exit_conv | +1,325 | +0.66% |
| random_hold | +815 | +0.39% |
| snake_abs | +587 | +0.30% |
| snake_abs_conv | +580 | +0.29% |
| snake_anaconda | +466 | +0.24% |
| benchmark_smallcap | +370 | +0.18% |
| intraweek | +328 | +0.16% |
| intramonth | +31 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -57 | -0.03% |
| unified | -81 | -0.04% |
| snake_viper_tick | -169 | -0.09% |
| snake_viper_wild | -173 | -0.09% |
| benchmark | -696 | -0.31% |

Average per day so far: benchmark Rs +602, unified Rs +548, oracle Rs +290, intramonth Rs +252, random_hold Rs +224, intraweek Rs +176, snake_abs_exit Rs +62, snake_abs_exit_conv Rs +44, nifty_calls Rs +44, benchmark_smallcap Rs +32, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -22, snake_abs_conv Rs -27, snake_anaconda Rs -196, snake_viper_wild Rs -234, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -362, gold Rs -761

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.