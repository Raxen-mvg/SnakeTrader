# Paper trading report

Updated 2026-11-11 13:38 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,290 | +10.14% | 0 | - | 236 |
| benchmark | 220,112 | +10.06% | 0 | - | 237 |
| snake_abs_exit_conv | 217,997 | +9.00% | 2 | 50% | 345 |
| snake_abs_exit | 216,971 | +8.49% | 2 | 50% | 345 |
| snake_abs | 214,602 | +7.30% | 1 | 100% | 255 |
| snake_abs_conv | 214,447 | +7.22% | 1 | 100% | 255 |
| intraweek | 213,195 | +6.60% | 30 | 53% | 3,302 |
| oracle | 211,724 | +5.86% | 0 | - | 233 |
| intramonth | 211,244 | +5.62% | 0 | - | 235 |
| random_hold | 206,975 | +3.49% | 9 | 67% | 709 |
| snake_viper_wild | 205,301 | +2.65% | 10 | 50% | 1,825 |
| snake_anaconda | 204,861 | +2.43% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,798 | +0.90% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,076 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,733 | -5.13% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,198 (-4.40%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,871 | +3.99% |
| snake_viper_tick | +7,722 | +3.98% |
| snake_abs_exit_conv | +6,089 | +2.87% |
| snake_anaconda | +5,394 | +2.70% |
| snake_abs_exit | +4,987 | +2.35% |
| snake_abs_conv | +4,970 | +2.37% |
| snake_abs | +4,955 | +2.36% |
| benchmark_smallcap | +2,903 | +1.47% |
| benchmark | +2,020 | +0.93% |
| random_hold | +2,015 | +0.98% |
| oracle | +1,805 | +0.86% |
| intramonth | +635 | +0.30% |
| unified | +543 | +0.25% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,347 | -0.63% |
| gold | -2,400 | -1.25% |

Average per day so far: unified Rs +655, benchmark Rs +649, snake_abs_exit_conv Rs +643, snake_abs_exit Rs +606, snake_abs_conv Rs +516, snake_abs Rs +504, intraweek Rs +426, oracle Rs +378, intramonth Rs +363, snake_viper_wild Rs +230, random_hold Rs +225, snake_anaconda Rs +187, snake_viper_tick Rs +90, nifty_calls Rs +59, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -331, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.