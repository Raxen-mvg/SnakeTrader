# Paper trading report

Updated 2026-11-06 13:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,713 | +7.86% | 0 | - | 237 |
| unified | 214,576 | +7.29% | 0 | - | 236 |
| snake_abs_exit_conv | 208,692 | +4.35% | 1 | 100% | 255 |
| snake_abs_exit | 208,586 | +4.29% | 1 | 100% | 260 |
| intraweek | 208,547 | +4.27% | 25 | 48% | 2,757 |
| intramonth | 206,917 | +3.46% | 0 | - | 235 |
| snake_abs | 205,676 | +2.84% | 1 | 100% | 255 |
| snake_abs_conv | 205,494 | +2.75% | 1 | 100% | 255 |
| oracle | 205,140 | +2.57% | 0 | - | 233 |
| random_hold | 203,270 | +1.64% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,424 | -1.79% | 3 | 33% | 702 |
| snake_anaconda | 196,104 | -1.95% | 3 | 33% | 374 |
| benchmark_smallcap | 194,933 | -2.53% | 0 | - | 237 |
| snake_viper_tick | 193,096 | -3.45% | 2 | 0% | 532 |
| gold | 190,407 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,900 (-6.55%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,943 | +0.91% |
| oracle | +1,068 | +0.52% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -872 | -0.42% |
| intramonth | -1,031 | -0.50% |
| random_hold | -1,053 | -0.52% |
| unified | -1,407 | -0.65% |
| benchmark_smallcap | -3,755 | -1.89% |
| gold | -3,814 | -1.96% |
| snake_abs | -6,013 | -2.84% |
| snake_abs_conv | -6,051 | -2.86% |
| snake_abs_exit | -6,073 | -2.83% |
| snake_abs_exit_conv | -6,111 | -2.85% |
| snake_anaconda | -6,375 | -3.15% |
| snake_viper_tick | -8,042 | -4.00% |
| snake_viper_wild | -8,232 | -4.02% |

Average per day so far: benchmark Rs +542, unified Rs +503, snake_abs_exit_conv Rs +334, snake_abs_exit Rs +330, intraweek Rs +295, intramonth Rs +239, snake_abs_conv Rs +211, snake_abs Rs +210, oracle Rs +177, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -162, snake_viper_wild Rs -170, benchmark_smallcap Rs -203, gold Rs -331, snake_viper_tick Rs -384, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.