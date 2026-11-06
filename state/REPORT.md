# Paper trading report

Updated 2026-11-06 10:41 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,718 | +7.36% | 0 | - | 237 |
| unified | 214,671 | +7.33% | 0 | - | 236 |
| intraweek | 210,449 | +5.22% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,630 | +4.82% | 1 | 100% | 255 |
| snake_abs_exit | 209,419 | +4.71% | 1 | 100% | 260 |
| intramonth | 206,644 | +3.32% | 0 | - | 235 |
| snake_abs | 206,582 | +3.29% | 1 | 100% | 255 |
| snake_abs_conv | 206,414 | +3.21% | 1 | 100% | 255 |
| oracle | 205,066 | +2.53% | 0 | - | 233 |
| random_hold | 203,249 | +1.62% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,573 | -0.71% | 3 | 33% | 702 |
| snake_anaconda | 197,038 | -1.48% | 3 | 33% | 374 |
| snake_viper_tick | 195,216 | -2.39% | 2 | 0% | 532 |
| benchmark_smallcap | 194,944 | -2.53% | 0 | - | 237 |
| gold | 190,325 | -4.84% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,432 (-6.28%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,031 | +0.49% |
| oracle | +994 | +0.49% |
| benchmark | +949 | +0.44% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,074 | -0.53% |
| intramonth | -1,305 | -0.63% |
| unified | -1,313 | -0.61% |
| benchmark_smallcap | -3,744 | -1.88% |
| gold | -3,896 | -2.01% |
| snake_abs | -5,106 | -2.41% |
| snake_abs_conv | -5,131 | -2.42% |
| snake_abs_exit_conv | -5,174 | -2.41% |
| snake_abs_exit | -5,240 | -2.44% |
| snake_anaconda | -5,441 | -2.69% |
| snake_viper_tick | -5,922 | -2.94% |
| snake_viper_wild | -6,083 | -2.97% |

Average per day so far: benchmark Rs +508, unified Rs +506, snake_abs_exit_conv Rs +370, snake_abs_exit Rs +362, intraweek Rs +360, snake_abs_conv Rs +247, snake_abs Rs +244, intramonth Rs +229, oracle Rs +175, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -68, snake_anaconda Rs -123, benchmark_smallcap Rs -202, snake_viper_tick Rs -266, gold Rs -334, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.