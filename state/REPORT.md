# Paper trading report

Updated 2026-11-27 14:37 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,120 | +12.06% | 0 | - | 237 |
| unified | 223,733 | +11.87% | 0 | - | 236 |
| oracle | 212,004 | +6.00% | 0 | - | 233 |
| random_hold | 211,164 | +5.58% | 13 | 69% | 1,037 |
| intramonth | 211,041 | +5.52% | 0 | - | 235 |
| intraweek | 207,830 | +3.92% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,659 | +3.33% | 2 | 50% | 345 |
| snake_abs_exit | 204,352 | +2.18% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,468 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,754 | -0.12% | 1 | 100% | 255 |
| snake_abs_conv | 199,572 | -0.21% | 1 | 100% | 255 |
| snake_anaconda | 193,202 | -3.40% | 3 | 33% | 374 |
| snake_viper_wild | 192,615 | -3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,343 | -5.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 171,074 | -14.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,015 (-5.49%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,262 | +3.12% |
| gold | +5,080 | +3.06% |
| snake_abs_exit | +3,275 | +1.63% |
| random_hold | +2,570 | +1.23% |
| snake_abs_conv | +1,205 | +0.61% |
| snake_abs | +1,202 | +0.60% |
| snake_anaconda | +905 | +0.47% |
| intraweek | +781 | +0.38% |
| unified | +655 | +0.29% |
| benchmark_smallcap | +628 | +0.31% |
| intramonth | +508 | +0.24% |
| snake_viper_wild | +410 | +0.21% |
| snake_viper_tick | +402 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -231 | -0.11% |
| benchmark | -1,867 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +565, oracle Rs +286, random_hold Rs +266, intramonth Rs +263, intraweek Rs +186, snake_abs_exit_conv Rs +171, snake_abs_exit Rs +112, nifty_calls Rs +44, benchmark_smallcap Rs +39, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, snake_anaconda Rs -184, snake_viper_wild Rs -217, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -689

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.