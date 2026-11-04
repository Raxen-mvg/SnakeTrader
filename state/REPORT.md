# Paper trading report

Updated 2026-11-04 10:54 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,717 | +6.36% | 0 | - | 236 |
| snake_abs_exit_conv | 208,824 | +4.41% | 1 | 100% | 255 |
| snake_abs_exit | 208,680 | +4.34% | 1 | 100% | 260 |
| benchmark | 207,833 | +3.92% | 0 | - | 237 |
| intraweek | 207,347 | +3.67% | 25 | 48% | 2,757 |
| snake_viper_wild | 207,073 | +3.54% | 3 | 33% | 702 |
| snake_abs | 205,728 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,578 | +2.79% | 1 | 100% | 255 |
| intramonth | 205,463 | +2.73% | 0 | - | 235 |
| snake_viper_tick | 203,464 | +1.73% | 2 | 0% | 532 |
| random_hold | 202,330 | +1.17% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,456 | +0.23% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,589 | -1.21% | 3 | 33% | 361 |
| benchmark_smallcap | 194,607 | -2.70% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,744 | -6.13% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,641 (-5.68%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,666 | +2.29% |
| snake_abs_exit_conv | +4,486 | +2.19% |
| snake_abs_conv | +4,437 | +2.21% |
| snake_abs | +4,419 | +2.19% |
| snake_anaconda | +3,765 | +1.94% |
| gold | +2,466 | +1.33% |
| intraweek | +2,262 | +1.10% |
| random_hold | +1,861 | +0.93% |
| benchmark_smallcap | +1,670 | +0.87% |
| intramonth | +1,492 | +0.73% |
| benchmark | +1,132 | +0.55% |
| unified | +716 | +0.34% |
| oracle | +467 | +0.23% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,703 | -1.79% |
| snake_viper_wild | -3,820 | -1.81% |

Average per day so far: unified Rs +471, snake_viper_wild Rs +372, snake_abs_exit_conv Rs +368, snake_abs_exit Rs +362, benchmark Rs +290, intraweek Rs +272, snake_abs_conv Rs +232, snake_abs Rs +229, snake_viper_tick Rs +217, intramonth Rs +202, random_hold Rs +86, nifty_calls Rs +68, oracle Rs +17, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -110, benchmark_smallcap Rs -234, snake_nonews Rs -444, gold Rs -454, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.