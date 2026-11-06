# Paper trading report

Updated 2026-11-06 12:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,108 | +7.55% | 0 | - | 237 |
| unified | 214,524 | +7.26% | 0 | - | 236 |
| intraweek | 209,205 | +4.60% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,847 | +4.42% | 1 | 100% | 255 |
| snake_abs_exit | 208,679 | +4.34% | 1 | 100% | 260 |
| intramonth | 206,748 | +3.37% | 0 | - | 235 |
| snake_abs | 205,825 | +2.91% | 1 | 100% | 255 |
| snake_abs_conv | 205,646 | +2.82% | 1 | 100% | 255 |
| oracle | 204,925 | +2.46% | 0 | - | 233 |
| random_hold | 203,257 | +1.63% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,362 | -1.82% | 3 | 33% | 702 |
| snake_anaconda | 196,285 | -1.86% | 3 | 33% | 374 |
| benchmark_smallcap | 194,720 | -2.64% | 0 | - | 237 |
| snake_viper_tick | 193,037 | -3.48% | 2 | 0% | 532 |
| gold | 190,078 | -4.96% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,965 (-6.52%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,339 | +0.63% |
| oracle | +853 | +0.42% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -214 | -0.10% |
| random_hold | -1,066 | -0.52% |
| intramonth | -1,201 | -0.58% |
| unified | -1,460 | -0.68% |
| benchmark_smallcap | -3,968 | -2.00% |
| gold | -4,143 | -2.13% |
| snake_abs | -5,863 | -2.77% |
| snake_abs_conv | -5,898 | -2.79% |
| snake_abs_exit_conv | -5,957 | -2.77% |
| snake_abs_exit | -5,980 | -2.79% |
| snake_anaconda | -6,194 | -3.06% |
| snake_viper_tick | -8,101 | -4.03% |
| snake_viper_wild | -8,294 | -4.05% |

Average per day so far: benchmark Rs +521, unified Rs +501, snake_abs_exit_conv Rs +340, snake_abs_exit Rs +334, intraweek Rs +317, intramonth Rs +233, snake_abs_conv Rs +217, snake_abs Rs +216, oracle Rs +170, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -155, snake_viper_wild Rs -173, benchmark_smallcap Rs -211, gold Rs -342, snake_viper_tick Rs -387, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.