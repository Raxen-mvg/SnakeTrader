# Paper trading report

Updated 2026-11-11 11:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,313 | +10.66% | 0 | - | 237 |
| unified | 220,494 | +10.25% | 0 | - | 236 |
| snake_abs_exit_conv | 216,282 | +8.14% | 2 | 50% | 345 |
| snake_abs_exit | 214,871 | +7.44% | 2 | 50% | 345 |
| intraweek | 214,080 | +7.04% | 30 | 53% | 3,302 |
| snake_abs | 213,053 | +6.53% | 1 | 100% | 255 |
| snake_abs_conv | 212,895 | +6.45% | 1 | 100% | 255 |
| oracle | 211,721 | +5.86% | 0 | - | 233 |
| intramonth | 211,380 | +5.69% | 0 | - | 235 |
| random_hold | 206,843 | +3.42% | 9 | 67% | 709 |
| snake_anaconda | 202,748 | +1.37% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,793 | +0.90% | 0 | - | 237 |
| snake_viper_wild | 200,858 | +0.43% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,447 | -1.28% | 9 | 44% | 1,639 |
| gold | 189,881 | -5.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,242 (-4.38%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,373 | +2.06% |
| benchmark_smallcap | +3,621 | +1.83% |
| snake_viper_wild | +3,428 | +1.74% |
| snake_abs_conv | +3,418 | +1.63% |
| snake_abs | +3,406 | +1.62% |
| snake_viper_tick | +3,371 | +1.74% |
| snake_anaconda | +3,282 | +1.65% |
| benchmark | +3,221 | +1.48% |
| snake_abs_exit | +2,887 | +1.36% |
| random_hold | +1,882 | +0.92% |
| oracle | +1,802 | +0.86% |
| intramonth | +770 | +0.37% |
| unified | +747 | +0.34% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -462 | -0.21% |
| gold | -2,252 | -1.17% |

Average per day so far: benchmark Rs +688, unified Rs +661, snake_abs_exit_conv Rs +581, snake_abs_exit Rs +531, snake_abs_conv Rs +461, intraweek Rs +454, snake_abs Rs +450, oracle Rs +378, intramonth Rs +367, random_hold Rs +221, snake_anaconda Rs +106, benchmark_smallcap Rs +66, nifty_calls Rs +59, snake_viper_wild Rs +37, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -128, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.