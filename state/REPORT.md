# Paper trading report

Updated 2026-11-06 12:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,223 | +7.61% | 0 | - | 237 |
| unified | 214,719 | +7.36% | 0 | - | 236 |
| snake_abs_exit_conv | 208,835 | +4.42% | 1 | 100% | 255 |
| intraweek | 208,723 | +4.36% | 25 | 48% | 2,757 |
| snake_abs_exit | 208,651 | +4.33% | 1 | 100% | 260 |
| intramonth | 206,850 | +3.42% | 0 | - | 235 |
| snake_abs | 205,804 | +2.90% | 1 | 100% | 255 |
| snake_abs_conv | 205,628 | +2.81% | 1 | 100% | 255 |
| oracle | 204,925 | +2.46% | 0 | - | 233 |
| random_hold | 203,128 | +1.56% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,100 | -1.95% | 3 | 33% | 374 |
| snake_viper_wild | 195,609 | -2.19% | 3 | 33% | 702 |
| benchmark_smallcap | 194,843 | -2.58% | 0 | - | 237 |
| snake_viper_tick | 192,298 | -3.85% | 2 | 0% | 532 |
| gold | 190,095 | -4.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,901 (-6.55%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,454 | +0.68% |
| oracle | +853 | +0.42% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -696 | -0.33% |
| intramonth | -1,099 | -0.53% |
| random_hold | -1,196 | -0.58% |
| unified | -1,264 | -0.58% |
| benchmark_smallcap | -3,845 | -1.94% |
| gold | -4,126 | -2.12% |
| snake_abs | -5,885 | -2.78% |
| snake_abs_conv | -5,917 | -2.80% |
| snake_abs_exit_conv | -5,969 | -2.78% |
| snake_abs_exit | -6,008 | -2.80% |
| snake_anaconda | -6,379 | -3.15% |
| snake_viper_tick | -8,840 | -4.39% |
| snake_viper_wild | -9,047 | -4.42% |

Average per day so far: benchmark Rs +525, unified Rs +508, snake_abs_exit_conv Rs +340, snake_abs_exit Rs +333, intraweek Rs +301, intramonth Rs +236, snake_abs_conv Rs +216, snake_abs Rs +215, oracle Rs +170, random_hold Rs +108, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -162, benchmark_smallcap Rs -206, snake_viper_wild Rs -209, gold Rs -342, snake_nonews Rs -411, snake_viper_tick Rs -428, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.