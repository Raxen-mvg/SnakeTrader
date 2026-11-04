# Paper trading report

Updated 2026-11-04 10:51 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,959 | +6.48% | 0 | - | 236 |
| snake_abs_exit_conv | 208,690 | +4.34% | 1 | 100% | 255 |
| snake_abs_exit | 208,557 | +4.28% | 1 | 100% | 260 |
| benchmark | 208,101 | +4.05% | 0 | - | 237 |
| intraweek | 207,983 | +3.99% | 25 | 48% | 2,757 |
| snake_viper_wild | 207,146 | +3.57% | 3 | 33% | 702 |
| intramonth | 205,715 | +2.86% | 0 | - | 235 |
| snake_abs | 205,598 | +2.80% | 1 | 100% | 255 |
| snake_abs_conv | 205,445 | +2.72% | 1 | 100% | 255 |
| snake_viper_tick | 203,535 | +1.77% | 2 | 0% | 532 |
| random_hold | 202,382 | +1.19% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,570 | +0.28% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,442 | -1.28% | 3 | 33% | 361 |
| benchmark_smallcap | 194,619 | -2.69% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| gold | 187,859 | -6.07% | 0 | - | 237 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,835 (-5.58%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,542 | +2.23% |
| snake_abs_exit_conv | +4,351 | +2.13% |
| snake_abs_conv | +4,304 | +2.14% |
| snake_abs | +4,289 | +2.13% |
| snake_anaconda | +3,617 | +1.87% |
| intraweek | +2,898 | +1.41% |
| gold | +2,581 | +1.39% |
| random_hold | +1,914 | +0.95% |
| intramonth | +1,744 | +0.85% |
| benchmark_smallcap | +1,682 | +0.87% |
| benchmark | +1,400 | +0.68% |
| unified | +958 | +0.45% |
| oracle | +581 | +0.29% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,631 | -1.75% |
| snake_viper_wild | -3,747 | -1.78% |

Average per day so far: unified Rs +480, snake_viper_wild Rs +376, snake_abs_exit_conv Rs +362, snake_abs_exit Rs +357, benchmark Rs +300, intraweek Rs +296, snake_abs_conv Rs +227, snake_abs Rs +224, snake_viper_tick Rs +221, intramonth Rs +212, random_hold Rs +88, nifty_calls Rs +68, oracle Rs +21, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -116, benchmark_smallcap Rs -234, snake_nonews Rs -444, gold Rs -450, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.