# Paper trading report

Updated 2026-11-12 11:22 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,662 | +11.33% | 0 | - | 236 |
| benchmark | 220,655 | +10.33% | 0 | - | 237 |
| snake_abs_exit_conv | 219,845 | +9.92% | 2 | 50% | 345 |
| snake_abs_exit | 218,896 | +9.45% | 2 | 50% | 345 |
| snake_abs | 216,785 | +8.39% | 1 | 100% | 255 |
| snake_abs_conv | 216,625 | +8.31% | 1 | 100% | 255 |
| intraweek | 214,941 | +7.47% | 30 | 53% | 3,302 |
| oracle | 213,996 | +7.00% | 0 | - | 233 |
| intramonth | 212,944 | +6.47% | 0 | - | 235 |
| snake_viper_wild | 208,414 | +4.21% | 10 | 50% | 1,825 |
| random_hold | 207,945 | +3.97% | 10 | 70% | 733 |
| snake_anaconda | 207,402 | +3.70% | 3 | 33% | 374 |
| snake_viper_tick | 204,845 | +2.42% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,295 | +1.65% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,396 | -6.80% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,891 (-3.55%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +3,279 | +1.61% |
| snake_abs_conv | +3,167 | +1.48% |
| snake_abs | +3,160 | +1.48% |
| unified | +2,848 | +1.30% |
| snake_abs_exit | +2,734 | +1.26% |
| snake_abs_exit_conv | +2,694 | +1.24% |
| benchmark_smallcap | +2,489 | +1.24% |
| oracle | +1,993 | +0.94% |
| intramonth | +1,948 | +0.92% |
| intraweek | +1,808 | +0.85% |
| snake_viper_wild | +1,672 | +0.81% |
| snake_viper_tick | +1,636 | +0.81% |
| benchmark | +1,392 | +0.64% |
| random_hold | +835 | +0.40% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,189 | -1.68% |

Average per day so far: unified Rs +708, snake_abs_exit_conv Rs +684, snake_abs_exit Rs +652, benchmark Rs +645, snake_abs_conv Rs +573, snake_abs Rs +559, intraweek Rs +467, oracle Rs +437, intramonth Rs +405, snake_viper_wild Rs +351, snake_anaconda Rs +274, random_hold Rs +248, snake_viper_tick Rs +231, benchmark_smallcap Rs +118, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -425

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.