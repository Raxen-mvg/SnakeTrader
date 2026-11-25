# Paper trading report

Updated 2026-11-25 14:10 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,740 | +12.37% | 0 | - | 237 |
| unified | 224,613 | +12.31% | 0 | - | 236 |
| oracle | 212,544 | +6.27% | 0 | - | 233 |
| intramonth | 212,170 | +6.08% | 0 | - | 235 |
| random_hold | 209,520 | +4.76% | 12 | 75% | 1,009 |
| intraweek | 207,084 | +3.54% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,379 | +0.69% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,082 | +0.54% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,615 | -0.19% | 1 | 100% | 255 |
| snake_abs_conv | 199,416 | -0.29% | 1 | 100% | 255 |
| benchmark_smallcap | 198,587 | -0.71% | 0 | - | 237 |
| snake_viper_wild | 197,183 | -1.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,824 | -3.09% | 15 | 47% | 2,625 |
| snake_anaconda | 193,135 | -3.43% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,057 | -17.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,880 (-5.56%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,267 | +1.48% |
| random_hold | +1,093 | +0.53% |
| unified | +328 | +0.15% |
| oracle | +202 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -392 | -0.20% |
| intramonth | -582 | -0.27% |
| snake_viper_tick | -3,868 | -1.96% |
| snake_viper_wild | -3,941 | -1.96% |
| gold | -4,373 | -2.58% |
| intraweek | -4,535 | -2.14% |
| snake_anaconda | -5,569 | -2.80% |
| snake_abs | -5,845 | -2.85% |
| snake_abs_conv | -5,886 | -2.87% |
| snake_abs_exit_conv | -5,964 | -2.88% |
| snake_abs_exit | -6,116 | -2.95% |

Average per day so far: benchmark Rs +618, unified Rs +615, oracle Rs +314, intramonth Rs +304, random_hold Rs +238, intraweek Rs +177, nifty_calls Rs +46, snake_abs_exit Rs +37, snake_abs_exit_conv Rs +29, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -10, snake_abs_conv Rs -16, benchmark_smallcap Rs -39, snake_viper_wild Rs -88, snake_anaconda Rs -196, snake_viper_tick Rs -213, snake_nonews Rs -292, snake Rs -311, gold Rs -874

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.