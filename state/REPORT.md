# Paper trading report

Updated 2026-11-06 14:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,776 | +8.39% | 0 | - | 237 |
| unified | 215,091 | +7.55% | 0 | - | 236 |
| snake_abs_exit_conv | 208,888 | +4.44% | 1 | 100% | 255 |
| snake_abs_exit | 208,797 | +4.40% | 1 | 100% | 260 |
| intraweek | 208,574 | +4.29% | 25 | 48% | 2,757 |
| intramonth | 207,354 | +3.68% | 0 | - | 235 |
| snake_abs | 205,864 | +2.93% | 1 | 100% | 255 |
| snake_abs_conv | 205,684 | +2.84% | 1 | 100% | 255 |
| oracle | 205,420 | +2.71% | 0 | - | 233 |
| random_hold | 203,457 | +1.73% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,244 | -1.88% | 3 | 33% | 374 |
| snake_viper_wild | 196,068 | -1.97% | 4 | 25% | 842 |
| benchmark_smallcap | 195,818 | -2.09% | 0 | - | 237 |
| snake_viper_tick | 192,740 | -3.63% | 3 | 0% | 672 |
| gold | 191,542 | -4.23% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,114 (-6.44%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,006 | +1.41% |
| oracle | +1,348 | +0.66% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -594 | -0.29% |
| intraweek | -844 | -0.40% |
| random_hold | -866 | -0.42% |
| unified | -892 | -0.41% |
| gold | -2,680 | -1.38% |
| benchmark_smallcap | -2,870 | -1.44% |
| snake_abs | -5,824 | -2.75% |
| snake_abs_conv | -5,860 | -2.77% |
| snake_abs_exit | -5,862 | -2.73% |
| snake_abs_exit_conv | -5,915 | -2.75% |
| snake_anaconda | -6,235 | -3.08% |
| snake_viper_tick | -8,398 | -4.17% |
| snake_viper_wild | -8,587 | -4.20% |

Average per day so far: benchmark Rs +578, unified Rs +520, snake_abs_exit_conv Rs +342, snake_abs_exit Rs +338, intraweek Rs +296, intramonth Rs +254, snake_abs_conv Rs +219, snake_abs Rs +217, oracle Rs +187, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -156, benchmark_smallcap Rs -167, snake_viper_wild Rs -187, gold Rs -292, snake_viper_tick Rs -403, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.