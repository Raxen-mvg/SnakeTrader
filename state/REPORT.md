# Paper trading report

Updated 2026-11-06 14:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,623 | +8.31% | 0 | - | 237 |
| unified | 215,019 | +7.51% | 0 | - | 236 |
| snake_abs_exit_conv | 208,899 | +4.45% | 1 | 100% | 255 |
| snake_abs_exit | 208,820 | +4.41% | 1 | 100% | 260 |
| intraweek | 208,587 | +4.29% | 25 | 48% | 2,757 |
| intramonth | 207,338 | +3.67% | 0 | - | 235 |
| snake_abs | 205,875 | +2.94% | 1 | 100% | 255 |
| snake_abs_conv | 205,696 | +2.85% | 1 | 100% | 255 |
| oracle | 205,534 | +2.77% | 0 | - | 233 |
| random_hold | 203,449 | +1.73% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,255 | -1.87% | 3 | 33% | 374 |
| snake_viper_wild | 196,089 | -1.96% | 4 | 25% | 842 |
| benchmark_smallcap | 195,807 | -2.10% | 0 | - | 237 |
| snake_viper_tick | 192,761 | -3.62% | 3 | 0% | 672 |
| gold | 191,443 | -4.28% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,118 (-6.44%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,853 | +1.33% |
| oracle | +1,462 | +0.72% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -611 | -0.29% |
| intraweek | -832 | -0.40% |
| random_hold | -874 | -0.43% |
| unified | -965 | -0.45% |
| gold | -2,778 | -1.43% |
| benchmark_smallcap | -2,881 | -1.45% |
| snake_abs | -5,813 | -2.75% |
| snake_abs_exit | -5,839 | -2.72% |
| snake_abs_conv | -5,849 | -2.77% |
| snake_abs_exit_conv | -5,904 | -2.75% |
| snake_anaconda | -6,224 | -3.07% |
| snake_viper_tick | -8,377 | -4.17% |
| snake_viper_wild | -8,567 | -4.19% |

Average per day so far: benchmark Rs +573, unified Rs +518, snake_abs_exit_conv Rs +342, snake_abs_exit Rs +339, intraweek Rs +296, intramonth Rs +253, snake_abs_conv Rs +219, snake_abs Rs +218, oracle Rs +191, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -156, benchmark_smallcap Rs -168, snake_viper_wild Rs -186, gold Rs -295, snake_viper_tick Rs -402, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.