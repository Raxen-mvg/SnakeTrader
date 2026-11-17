# Paper trading report

Updated 2026-11-17 14:34 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,940 | +10.97% | 0 | - | 237 |
| unified | 221,384 | +10.69% | 0 | - | 236 |
| intraweek | 213,979 | +6.99% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,228 | +6.61% | 2 | 50% | 345 |
| oracle | 212,111 | +6.05% | 0 | - | 233 |
| snake_abs_exit_conv | 211,629 | +5.82% | 2 | 50% | 345 |
| intramonth | 211,188 | +5.59% | 0 | - | 235 |
| snake_viper_wild | 209,444 | +4.72% | 14 | 50% | 2,496 |
| snake_abs | 208,415 | +4.21% | 1 | 100% | 255 |
| snake_abs_conv | 208,275 | +4.14% | 1 | 100% | 255 |
| random_hold | 207,785 | +3.89% | 10 | 70% | 733 |
| snake_viper_tick | 205,865 | +2.93% | 13 | 46% | 2,299 |
| snake_anaconda | 203,844 | +1.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,177 | +0.59% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,889 | -9.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,057 (-4.47%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,300 | +1.60% |
| snake_viper_tick | +3,245 | +1.60% |
| intraweek | +2,713 | +1.28% |
| benchmark | +1,859 | +0.84% |
| benchmark_smallcap | +348 | +0.17% |
| oracle | +88 | +0.04% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -8 | -0.00% |
| unified | -54 | -0.02% |
| gold | -66 | -0.04% |
| intramonth | -431 | -0.20% |
| snake_abs_exit | -1,182 | -0.55% |
| snake_anaconda | -1,259 | -0.61% |
| snake_abs_exit_conv | -1,588 | -0.74% |
| snake_abs_conv | -1,715 | -0.82% |
| snake_abs | -1,719 | -0.82% |

Average per day so far: benchmark Rs +627, unified Rs +611, snake_abs_exit Rs +413, intraweek Rs +399, snake_abs_exit_conv Rs +363, snake_viper_wild Rs +350, oracle Rs +346, intramonth Rs +320, snake_abs_conv Rs +259, snake_abs Rs +255, snake_viper_tick Rs +244, random_hold Rs +222, snake_anaconda Rs +128, nifty_calls Rs +52, benchmark_smallcap Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -546

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.