# Paper trading report

Updated 2026-11-06 14:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,899 | +8.45% | 0 | - | 237 |
| unified | 215,200 | +7.60% | 0 | - | 236 |
| intraweek | 209,467 | +4.73% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,901 | +4.45% | 1 | 100% | 255 |
| snake_abs_exit | 208,792 | +4.40% | 1 | 100% | 260 |
| intramonth | 207,504 | +3.75% | 0 | - | 235 |
| snake_abs | 205,888 | +2.94% | 1 | 100% | 255 |
| snake_abs_conv | 205,699 | +2.85% | 1 | 100% | 255 |
| oracle | 205,627 | +2.81% | 0 | - | 233 |
| random_hold | 203,538 | +1.77% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,569 | -1.72% | 0 | - | 237 |
| snake_anaconda | 196,143 | -1.93% | 3 | 33% | 374 |
| snake_viper_wild | 196,077 | -1.96% | 4 | 25% | 842 |
| snake_viper_tick | 192,748 | -3.63% | 3 | 0% | 672 |
| gold | 191,525 | -4.24% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,290 (-6.36%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,129 | +1.46% |
| oracle | +1,555 | +0.76% |
| intraweek | +48 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -445 | -0.21% |
| unified | -783 | -0.36% |
| random_hold | -786 | -0.38% |
| benchmark_smallcap | -2,119 | -1.07% |
| gold | -2,696 | -1.39% |
| snake_abs | -5,800 | -2.74% |
| snake_abs_conv | -5,846 | -2.76% |
| snake_abs_exit | -5,867 | -2.73% |
| snake_abs_exit_conv | -5,903 | -2.75% |
| snake_anaconda | -6,336 | -3.13% |
| snake_viper_tick | -8,390 | -4.17% |
| snake_viper_wild | -8,579 | -4.19% |

Average per day so far: benchmark Rs +583, unified Rs +524, snake_abs_exit_conv Rs +342, snake_abs_exit Rs +338, intraweek Rs +326, intramonth Rs +259, snake_abs_conv Rs +219, snake_abs Rs +218, oracle Rs +194, random_hold Rs +122, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -137, snake_anaconda Rs -161, snake_viper_wild Rs -187, gold Rs -292, snake_viper_tick Rs -403, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.