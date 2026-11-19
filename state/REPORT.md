# Paper trading report

Updated 2026-11-19 14:13 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,532 | +11.77% | 0 | - | 236 |
| benchmark | 222,177 | +11.09% | 0 | - | 237 |
| intramonth | 213,158 | +6.58% | 0 | - | 235 |
| snake_abs_exit | 213,123 | +6.56% | 2 | 50% | 345 |
| intraweek | 211,932 | +5.97% | 35 | 54% | 3,851 |
| oracle | 211,342 | +5.67% | 0 | - | 233 |
| snake_abs_exit_conv | 210,823 | +5.41% | 2 | 50% | 345 |
| snake_abs | 208,726 | +4.36% | 1 | 100% | 255 |
| snake_abs_conv | 208,599 | +4.30% | 1 | 100% | 255 |
| random_hold | 207,848 | +3.92% | 10 | 70% | 733 |
| snake_viper_wild | 207,580 | +3.79% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,033 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,215 | +1.61% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,795 | +0.40% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,937 | -12.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,229 (-4.39%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,882 | +0.85% |
| benchmark_smallcap | +1,469 | +0.74% |
| unified | +920 | +0.41% |
| random_hold | +915 | +0.44% |
| intramonth | +885 | +0.42% |
| oracle | +546 | +0.26% |
| snake_viper_wild | +541 | +0.26% |
| snake_viper_tick | +530 | +0.26% |
| intraweek | +92 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -710 | -0.34% |
| snake_abs_conv | -726 | -0.35% |
| snake_abs_exit | -909 | -0.42% |
| snake_anaconda | -1,186 | -0.58% |
| snake_abs_exit_conv | -1,561 | -0.73% |
| gold | -2,384 | -1.34% |

Average per day so far: unified Rs +636, benchmark Rs +599, snake_abs_exit Rs +386, intramonth Rs +356, intraweek Rs +322, snake_abs_exit_conv Rs +318, oracle Rs +307, snake_viper_wild Rs +261, snake_abs_conv Rs +253, snake_abs Rs +249, random_hold Rs +212, snake_viper_tick Rs +155, snake_anaconda Rs +100, nifty_calls Rs +50, benchmark_smallcap Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -677

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.