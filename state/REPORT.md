# Paper trading report

Updated 2026-11-06 12:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,024 | +7.51% | 0 | - | 237 |
| unified | 214,721 | +7.36% | 0 | - | 236 |
| intraweek | 209,085 | +4.54% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,768 | +4.38% | 1 | 100% | 255 |
| snake_abs_exit | 208,577 | +4.29% | 1 | 100% | 260 |
| intramonth | 207,019 | +3.51% | 0 | - | 235 |
| snake_abs | 205,734 | +2.87% | 1 | 100% | 255 |
| snake_abs_conv | 205,561 | +2.78% | 1 | 100% | 255 |
| oracle | 204,928 | +2.46% | 0 | - | 233 |
| random_hold | 203,030 | +1.51% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,009 | -2.00% | 3 | 33% | 374 |
| snake_viper_wild | 195,413 | -2.29% | 3 | 33% | 702 |
| benchmark_smallcap | 194,697 | -2.65% | 0 | - | 237 |
| snake_viper_tick | 192,103 | -3.95% | 2 | 0% | 532 |
| gold | 190,194 | -4.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,930 (-6.53%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,255 | +0.59% |
| oracle | +856 | +0.42% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -334 | -0.16% |
| intramonth | -929 | -0.45% |
| unified | -1,263 | -0.58% |
| random_hold | -1,293 | -0.63% |
| benchmark_smallcap | -3,991 | -2.01% |
| gold | -4,028 | -2.07% |
| snake_abs | -5,954 | -2.81% |
| snake_abs_conv | -5,984 | -2.83% |
| snake_abs_exit_conv | -6,035 | -2.81% |
| snake_abs_exit | -6,082 | -2.83% |
| snake_anaconda | -6,470 | -3.20% |
| snake_viper_tick | -9,035 | -4.49% |
| snake_viper_wild | -9,243 | -4.52% |

Average per day so far: benchmark Rs +518, unified Rs +508, snake_abs_exit_conv Rs +337, snake_abs_exit Rs +330, intraweek Rs +313, intramonth Rs +242, snake_abs_conv Rs +214, snake_abs Rs +212, oracle Rs +170, random_hold Rs +104, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -166, benchmark_smallcap Rs -212, snake_viper_wild Rs -218, gold Rs -338, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -439

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.