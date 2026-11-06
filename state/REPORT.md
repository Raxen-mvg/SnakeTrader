# Paper trading report

Updated 2026-11-06 14:30 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,348 | +8.17% | 0 | - | 237 |
| unified | 214,833 | +7.42% | 0 | - | 236 |
| snake_abs_exit_conv | 209,094 | +4.55% | 1 | 100% | 255 |
| snake_abs_exit | 209,001 | +4.50% | 1 | 100% | 260 |
| intraweek | 208,579 | +4.29% | 25 | 48% | 2,757 |
| intramonth | 207,297 | +3.65% | 0 | - | 235 |
| snake_abs | 206,073 | +3.04% | 1 | 100% | 255 |
| snake_abs_conv | 205,888 | +2.94% | 1 | 100% | 255 |
| oracle | 205,600 | +2.80% | 0 | - | 233 |
| random_hold | 203,571 | +1.78% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,220 | -1.89% | 3 | 33% | 374 |
| snake_viper_wild | 196,110 | -1.95% | 4 | 25% | 842 |
| benchmark_smallcap | 195,594 | -2.20% | 0 | - | 237 |
| snake_viper_tick | 192,781 | -3.61% | 3 | 0% | 672 |
| gold | 191,394 | -4.30% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,148 (-6.43%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,578 | +1.21% |
| oracle | +1,528 | +0.75% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -652 | -0.31% |
| random_hold | -752 | -0.37% |
| intraweek | -839 | -0.40% |
| unified | -1,150 | -0.53% |
| gold | -2,828 | -1.46% |
| benchmark_smallcap | -3,094 | -1.56% |
| snake_abs | -5,615 | -2.65% |
| snake_abs_conv | -5,657 | -2.67% |
| snake_abs_exit | -5,658 | -2.64% |
| snake_abs_exit_conv | -5,709 | -2.66% |
| snake_anaconda | -6,260 | -3.09% |
| snake_viper_tick | -8,357 | -4.16% |
| snake_viper_wild | -8,546 | -4.18% |

Average per day so far: benchmark Rs +564, unified Rs +511, snake_abs_exit_conv Rs +350, snake_abs_exit Rs +346, intraweek Rs +296, intramonth Rs +252, snake_abs_conv Rs +226, snake_abs Rs +225, oracle Rs +193, random_hold Rs +123, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -158, benchmark_smallcap Rs -176, snake_viper_wild Rs -185, gold Rs -297, snake_viper_tick Rs -401, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.