# Paper trading report

Updated 2026-11-06 09:17 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,852 | +7.43% | 0 | - | 236 |
| benchmark | 213,502 | +6.75% | 0 | - | 237 |
| snake_abs_exit_conv | 211,537 | +5.77% | 1 | 100% | 255 |
| snake_abs_exit | 211,298 | +5.65% | 1 | 100% | 260 |
| intraweek | 209,284 | +4.64% | 25 | 48% | 2,757 |
| snake_abs | 208,458 | +4.23% | 1 | 100% | 255 |
| snake_abs_conv | 208,306 | +4.15% | 1 | 100% | 255 |
| intramonth | 206,698 | +3.35% | 0 | - | 235 |
| oracle | 203,600 | +1.80% | 0 | - | 233 |
| random_hold | 203,406 | +1.70% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,801 | -0.10% | 3 | 33% | 702 |
| snake_anaconda | 198,792 | -0.60% | 3 | 33% | 374 |
| snake_viper_tick | 196,411 | -1.79% | 2 | 0% | 532 |
| benchmark_smallcap | 195,291 | -2.35% | 0 | - | 237 |
| gold | 190,605 | -4.70% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,757 (-6.12%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -134 | -0.06% |
| benchmark | -268 | -0.12% |
| oracle | -472 | -0.23% |
| random_hold | -917 | -0.45% |
| unified | -1,132 | -0.52% |
| intramonth | -1,251 | -0.60% |
| snake_abs | -3,230 | -1.53% |
| snake_abs_conv | -3,239 | -1.53% |
| snake_abs_exit_conv | -3,266 | -1.52% |
| snake_abs_exit | -3,361 | -1.57% |
| benchmark_smallcap | -3,397 | -1.71% |
| gold | -3,617 | -1.86% |
| snake_anaconda | -3,687 | -1.82% |
| snake_viper_tick | -4,727 | -2.35% |
| snake_viper_wild | -4,855 | -2.37% |

Average per day so far: unified Rs +512, benchmark Rs +466, snake_abs_exit_conv Rs +444, snake_abs_exit Rs +435, intraweek Rs +320, snake_abs_conv Rs +319, snake_abs Rs +313, intramonth Rs +231, oracle Rs +124, random_hold Rs +117, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -9, snake_anaconda Rs -50, benchmark_smallcap Rs -188, snake_viper_tick Rs -199, gold Rs -324, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.