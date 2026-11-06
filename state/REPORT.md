# Paper trading report

Updated 2026-11-06 14:33 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,768 | +8.38% | 0 | - | 237 |
| unified | 215,213 | +7.61% | 0 | - | 236 |
| snake_abs_exit_conv | 209,020 | +4.51% | 1 | 100% | 255 |
| snake_abs_exit | 208,935 | +4.47% | 1 | 100% | 260 |
| intraweek | 208,755 | +4.38% | 25 | 48% | 2,757 |
| intramonth | 207,571 | +3.79% | 0 | - | 235 |
| snake_abs | 206,001 | +3.00% | 1 | 100% | 255 |
| snake_abs_conv | 205,815 | +2.91% | 1 | 100% | 255 |
| oracle | 205,696 | +2.85% | 0 | - | 233 |
| random_hold | 203,617 | +1.81% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,149 | -1.93% | 3 | 33% | 374 |
| snake_viper_wild | 196,110 | -1.95% | 4 | 25% | 842 |
| benchmark_smallcap | 195,897 | -2.05% | 0 | - | 237 |
| snake_viper_tick | 192,781 | -3.61% | 3 | 0% | 672 |
| gold | 191,492 | -4.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,251 (-6.37%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,999 | +1.40% |
| oracle | +1,624 | +0.80% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -378 | -0.18% |
| intraweek | -663 | -0.32% |
| random_hold | -706 | -0.34% |
| unified | -771 | -0.36% |
| gold | -2,729 | -1.41% |
| benchmark_smallcap | -2,791 | -1.41% |
| snake_abs | -5,687 | -2.69% |
| snake_abs_exit | -5,724 | -2.67% |
| snake_abs_conv | -5,730 | -2.71% |
| snake_abs_exit_conv | -5,783 | -2.69% |
| snake_anaconda | -6,330 | -3.13% |
| snake_viper_tick | -8,357 | -4.16% |
| snake_viper_wild | -8,546 | -4.18% |

Average per day so far: benchmark Rs +578, unified Rs +525, snake_abs_exit_conv Rs +347, snake_abs_exit Rs +344, intraweek Rs +302, intramonth Rs +261, snake_abs_conv Rs +224, snake_abs Rs +222, oracle Rs +196, random_hold Rs +125, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -160, benchmark_smallcap Rs -164, snake_viper_wild Rs -185, gold Rs -293, snake_viper_tick Rs -401, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.