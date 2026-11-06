# Paper trading report

Updated 2026-11-06 13:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,108 | +7.55% | 0 | - | 237 |
| unified | 214,527 | +7.26% | 0 | - | 236 |
| intraweek | 209,344 | +4.67% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,772 | +4.39% | 1 | 100% | 255 |
| snake_abs_exit | 208,620 | +4.31% | 1 | 100% | 260 |
| intramonth | 206,798 | +3.40% | 0 | - | 235 |
| snake_abs | 205,756 | +2.88% | 1 | 100% | 255 |
| snake_abs_conv | 205,574 | +2.79% | 1 | 100% | 255 |
| oracle | 204,970 | +2.48% | 0 | - | 233 |
| random_hold | 203,204 | +1.60% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,492 | -1.75% | 3 | 33% | 702 |
| snake_anaconda | 196,213 | -1.89% | 3 | 33% | 374 |
| benchmark_smallcap | 194,708 | -2.65% | 0 | - | 237 |
| snake_viper_tick | 193,165 | -3.42% | 2 | 0% | 532 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,975 (-6.51%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,339 | +0.63% |
| oracle | +898 | +0.44% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -74 | -0.04% |
| random_hold | -1,119 | -0.55% |
| intramonth | -1,151 | -0.55% |
| unified | -1,457 | -0.67% |
| benchmark_smallcap | -3,980 | -2.00% |
| gold | -4,291 | -2.21% |
| snake_abs | -5,932 | -2.80% |
| snake_abs_conv | -5,971 | -2.82% |
| snake_abs_exit_conv | -6,031 | -2.81% |
| snake_abs_exit | -6,039 | -2.81% |
| snake_anaconda | -6,267 | -3.10% |
| snake_viper_tick | -7,973 | -3.96% |
| snake_viper_wild | -8,164 | -3.99% |

Average per day so far: benchmark Rs +521, unified Rs +501, snake_abs_exit_conv Rs +337, snake_abs_exit Rs +332, intraweek Rs +322, intramonth Rs +234, snake_abs_conv Rs +214, snake_abs Rs +213, oracle Rs +171, random_hold Rs +110, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -158, snake_viper_wild Rs -167, benchmark_smallcap Rs -212, gold Rs -347, snake_viper_tick Rs -380, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.