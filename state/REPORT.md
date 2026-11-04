# Paper trading report

Updated 2026-11-04 11:34 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,542 | +6.27% | 0 | - | 236 |
| intraweek | 209,206 | +4.60% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,899 | +4.45% | 1 | 100% | 255 |
| snake_abs_exit | 208,759 | +4.38% | 1 | 100% | 260 |
| benchmark | 207,543 | +3.77% | 0 | - | 237 |
| snake_viper_wild | 206,698 | +3.35% | 3 | 33% | 702 |
| snake_abs | 205,804 | +2.90% | 1 | 100% | 255 |
| snake_abs_conv | 205,653 | +2.83% | 1 | 100% | 255 |
| intramonth | 205,368 | +2.68% | 0 | - | 235 |
| snake_viper_tick | 203,098 | +1.55% | 2 | 0% | 532 |
| random_hold | 202,391 | +1.20% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,560 | +0.28% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,624 | -1.19% | 3 | 33% | 361 |
| benchmark_smallcap | 194,809 | -2.60% | 0 | - | 237 |
| gold | 190,259 | -4.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,738 (-5.63%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +4,981 | +2.69% |
| snake_abs_exit | +4,745 | +2.33% |
| snake_abs_exit_conv | +4,560 | +2.23% |
| snake_abs_conv | +4,512 | +2.24% |
| snake_abs | +4,495 | +2.23% |
| intraweek | +4,121 | +2.01% |
| snake_anaconda | +3,800 | +1.96% |
| random_hold | +1,922 | +0.96% |
| benchmark_smallcap | +1,872 | +0.97% |
| intramonth | +1,397 | +0.69% |
| benchmark | +842 | +0.41% |
| oracle | +571 | +0.28% |
| unified | +541 | +0.26% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,068 | -1.96% |
| snake_viper_wild | -4,194 | -1.99% |

Average per day so far: unified Rs +465, snake_abs_exit_conv Rs +371, snake_abs_exit Rs +365, snake_viper_wild Rs +353, intraweek Rs +341, benchmark Rs +279, snake_abs_conv Rs +236, snake_abs Rs +232, intramonth Rs +199, snake_viper_tick Rs +194, random_hold Rs +89, nifty_calls Rs +68, oracle Rs +21, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -108, benchmark_smallcap Rs -226, gold Rs -361, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.