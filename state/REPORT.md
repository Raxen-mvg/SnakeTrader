# Paper trading report

Updated 2026-11-06 13:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,736 | +7.87% | 0 | - | 237 |
| unified | 214,637 | +7.32% | 0 | - | 236 |
| intraweek | 208,906 | +4.45% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,629 | +4.32% | 1 | 100% | 255 |
| snake_abs_exit | 208,540 | +4.27% | 1 | 100% | 260 |
| intramonth | 206,955 | +3.48% | 0 | - | 235 |
| snake_abs | 205,613 | +2.81% | 1 | 100% | 255 |
| snake_abs_conv | 205,431 | +2.72% | 1 | 100% | 255 |
| oracle | 205,241 | +2.62% | 0 | - | 233 |
| random_hold | 203,326 | +1.66% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,588 | -1.71% | 3 | 33% | 702 |
| snake_anaconda | 196,046 | -1.98% | 3 | 33% | 374 |
| benchmark_smallcap | 194,933 | -2.53% | 0 | - | 237 |
| snake_viper_tick | 193,257 | -3.37% | 2 | 0% | 532 |
| gold | 190,440 | -4.78% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,961 (-6.52%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,966 | +0.92% |
| oracle | +1,169 | +0.57% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -512 | -0.24% |
| intramonth | -994 | -0.48% |
| random_hold | -998 | -0.49% |
| unified | -1,347 | -0.62% |
| benchmark_smallcap | -3,755 | -1.89% |
| gold | -3,781 | -1.95% |
| snake_abs | -6,075 | -2.87% |
| snake_abs_conv | -6,114 | -2.89% |
| snake_abs_exit | -6,119 | -2.85% |
| snake_abs_exit_conv | -6,174 | -2.87% |
| snake_anaconda | -6,433 | -3.18% |
| snake_viper_tick | -7,881 | -3.92% |
| snake_viper_wild | -8,068 | -3.94% |

Average per day so far: benchmark Rs +543, unified Rs +505, snake_abs_exit_conv Rs +332, snake_abs_exit Rs +328, intraweek Rs +307, intramonth Rs +240, snake_abs_conv Rs +209, snake_abs Rs +208, oracle Rs +181, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -162, snake_anaconda Rs -165, benchmark_smallcap Rs -203, gold Rs -330, snake_viper_tick Rs -375, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.