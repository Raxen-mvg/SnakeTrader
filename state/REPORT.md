# Paper trading report

Updated 2026-11-04 10:29 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,611 | +6.81% | 0 | - | 236 |
| snake_abs_exit_conv | 208,641 | +4.32% | 1 | 100% | 255 |
| snake_abs_exit | 208,468 | +4.23% | 1 | 100% | 260 |
| benchmark | 207,749 | +3.88% | 0 | - | 237 |
| intraweek | 207,003 | +3.50% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,803 | +3.40% | 3 | 33% | 702 |
| intramonth | 205,749 | +2.88% | 0 | - | 235 |
| snake_abs | 205,553 | +2.78% | 1 | 100% | 255 |
| snake_abs_conv | 205,397 | +2.70% | 1 | 100% | 255 |
| snake_viper_tick | 203,194 | +1.60% | 2 | 0% | 532 |
| random_hold | 202,291 | +1.15% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,343 | +0.17% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,314 | -1.34% | 3 | 33% | 361 |
| benchmark_smallcap | 194,417 | -2.79% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,612 | -6.19% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,746 (-5.63%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,453 | +2.18% |
| snake_abs_exit_conv | +4,302 | +2.10% |
| snake_abs_conv | +4,256 | +2.12% |
| snake_abs | +4,244 | +2.11% |
| snake_anaconda | +3,490 | +1.80% |
| gold | +2,334 | +1.26% |
| intraweek | +1,917 | +0.94% |
| random_hold | +1,823 | +0.91% |
| intramonth | +1,778 | +0.87% |
| unified | +1,610 | +0.76% |
| benchmark_smallcap | +1,480 | +0.77% |
| benchmark | +1,048 | +0.51% |
| oracle | +354 | +0.18% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,972 | -1.92% |
| snake_viper_wild | -4,089 | -1.94% |

Average per day so far: unified Rs +504, snake_abs_exit_conv Rs +360, snake_viper_wild Rs +358, snake_abs_exit Rs +353, benchmark Rs +287, intraweek Rs +259, snake_abs_conv Rs +225, snake_abs Rs +222, intramonth Rs +213, snake_viper_tick Rs +200, random_hold Rs +85, nifty_calls Rs +68, oracle Rs +13, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -122, benchmark_smallcap Rs -243, snake_nonews Rs -444, gold Rs -459, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.