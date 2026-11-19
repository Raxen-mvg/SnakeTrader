# Paper trading report

Updated 2026-11-19 14:46 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,240 | +12.12% | 0 | - | 236 |
| benchmark | 222,215 | +11.11% | 0 | - | 237 |
| intramonth | 213,689 | +6.84% | 0 | - | 235 |
| snake_abs_exit | 213,690 | +6.84% | 2 | 50% | 345 |
| intraweek | 212,072 | +6.04% | 35 | 54% | 3,851 |
| oracle | 211,688 | +5.84% | 0 | - | 233 |
| snake_abs_exit_conv | 211,368 | +5.68% | 2 | 50% | 345 |
| snake_abs | 209,072 | +4.54% | 1 | 100% | 255 |
| snake_abs_conv | 208,955 | +4.48% | 1 | 100% | 255 |
| random_hold | 208,277 | +4.14% | 10 | 70% | 733 |
| snake_viper_wild | 207,691 | +3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,141 | +2.07% | 15 | 47% | 2,625 |
| snake_anaconda | 203,677 | +1.84% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,863 | +0.43% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,888 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,621 (-4.19%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,920 | +0.87% |
| unified | +1,629 | +0.73% |
| benchmark_smallcap | +1,536 | +0.77% |
| intramonth | +1,415 | +0.67% |
| random_hold | +1,344 | +0.65% |
| oracle | +892 | +0.42% |
| snake_viper_wild | +651 | +0.32% |
| snake_viper_tick | +638 | +0.31% |
| intraweek | +232 | +0.11% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -342 | -0.16% |
| snake_abs | -364 | -0.17% |
| snake_abs_conv | -370 | -0.18% |
| snake_anaconda | -724 | -0.35% |
| snake_abs_exit_conv | -1,016 | -0.48% |
| gold | -2,433 | -1.37% |

Average per day so far: unified Rs +655, benchmark Rs +600, snake_abs_exit Rs +403, intramonth Rs +370, snake_abs_exit_conv Rs +334, intraweek Rs +326, oracle Rs +316, snake_viper_wild Rs +265, snake_abs_conv Rs +263, snake_abs Rs +259, random_hold Rs +224, snake_viper_tick Rs +159, snake_anaconda Rs +115, nifty_calls Rs +50, benchmark_smallcap Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.