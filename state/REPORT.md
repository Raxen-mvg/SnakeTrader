# Paper trading report

Updated 2026-11-06 12:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,307 | +7.65% | 0 | - | 237 |
| unified | 214,613 | +7.31% | 0 | - | 236 |
| snake_abs_exit_conv | 208,979 | +4.49% | 1 | 100% | 255 |
| snake_abs_exit | 208,798 | +4.40% | 1 | 100% | 260 |
| intraweek | 208,772 | +4.39% | 25 | 48% | 2,757 |
| intramonth | 206,809 | +3.40% | 0 | - | 235 |
| snake_abs | 205,944 | +2.97% | 1 | 100% | 255 |
| snake_abs_conv | 205,771 | +2.88% | 1 | 100% | 255 |
| oracle | 204,955 | +2.48% | 0 | - | 233 |
| random_hold | 203,124 | +1.56% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,234 | -1.88% | 3 | 33% | 374 |
| snake_viper_wild | 195,354 | -2.32% | 3 | 33% | 702 |
| benchmark_smallcap | 194,731 | -2.63% | 0 | - | 237 |
| snake_viper_tick | 192,047 | -3.98% | 2 | 0% | 532 |
| gold | 190,144 | -4.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,917 (-6.54%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,538 | +0.72% |
| oracle | +883 | +0.43% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -647 | -0.31% |
| intramonth | -1,139 | -0.55% |
| random_hold | -1,199 | -0.59% |
| unified | -1,370 | -0.63% |
| benchmark_smallcap | -3,957 | -1.99% |
| gold | -4,077 | -2.10% |
| snake_abs | -5,744 | -2.71% |
| snake_abs_conv | -5,774 | -2.73% |
| snake_abs_exit_conv | -5,824 | -2.71% |
| snake_abs_exit | -5,861 | -2.73% |
| snake_anaconda | -6,246 | -3.08% |
| snake_viper_tick | -9,091 | -4.52% |
| snake_viper_wild | -9,302 | -4.54% |

Average per day so far: benchmark Rs +528, unified Rs +504, snake_abs_exit_conv Rs +345, snake_abs_exit Rs +338, intraweek Rs +302, intramonth Rs +235, snake_abs_conv Rs +222, snake_abs Rs +220, oracle Rs +171, random_hold Rs +108, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -157, benchmark_smallcap Rs -211, snake_viper_wild Rs -221, gold Rs -340, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -442

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.