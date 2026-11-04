# Paper trading report

Updated 2026-11-04 11:23 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,262 | +6.13% | 0 | - | 236 |
| snake_abs_exit_conv | 208,790 | +4.39% | 1 | 100% | 255 |
| snake_abs_exit | 208,624 | +4.31% | 1 | 100% | 260 |
| intraweek | 208,322 | +4.16% | 25 | 48% | 2,757 |
| benchmark | 207,833 | +3.92% | 0 | - | 237 |
| snake_viper_wild | 206,917 | +3.46% | 3 | 33% | 702 |
| snake_abs | 205,702 | +2.85% | 1 | 100% | 255 |
| snake_abs_conv | 205,547 | +2.77% | 1 | 100% | 255 |
| intramonth | 205,314 | +2.66% | 0 | - | 235 |
| snake_viper_tick | 203,312 | +1.66% | 2 | 0% | 532 |
| random_hold | 202,066 | +1.03% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,663 | +0.33% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,477 | -1.26% | 3 | 33% | 361 |
| benchmark_smallcap | 194,697 | -2.65% | 0 | - | 237 |
| gold | 189,569 | -5.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,607 (-5.70%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,609 | +2.26% |
| snake_abs_exit_conv | +4,452 | +2.18% |
| snake_abs_conv | +4,406 | +2.19% |
| snake_abs | +4,393 | +2.18% |
| gold | +4,291 | +2.32% |
| snake_anaconda | +3,653 | +1.89% |
| intraweek | +3,236 | +1.58% |
| benchmark_smallcap | +1,760 | +0.91% |
| random_hold | +1,598 | +0.80% |
| intramonth | +1,343 | +0.66% |
| benchmark | +1,132 | +0.55% |
| oracle | +674 | +0.34% |
| unified | +261 | +0.12% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,854 | -1.86% |
| snake_viper_wild | -3,976 | -1.89% |

Average per day so far: unified Rs +454, snake_abs_exit_conv Rs +366, snake_viper_wild Rs +364, snake_abs_exit Rs +359, intraweek Rs +308, benchmark Rs +290, snake_abs_conv Rs +231, snake_abs Rs +228, snake_viper_tick Rs +207, intramonth Rs +197, random_hold Rs +77, nifty_calls Rs +68, oracle Rs +25, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -115, benchmark_smallcap Rs -231, gold Rs -386, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.