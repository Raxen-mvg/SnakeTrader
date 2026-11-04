# Paper trading report

Updated 2026-11-04 14:46 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,252 | +7.13% | 0 | - | 236 |
| snake_abs_exit_conv | 213,785 | +6.89% | 1 | 100% | 255 |
| snake_abs_exit | 213,648 | +6.82% | 1 | 100% | 260 |
| snake_abs | 210,675 | +5.34% | 1 | 100% | 255 |
| snake_abs_conv | 210,530 | +5.26% | 1 | 100% | 255 |
| intraweek | 209,148 | +4.57% | 25 | 48% | 2,757 |
| benchmark | 208,560 | +4.28% | 0 | - | 237 |
| snake_viper_wild | 208,330 | +4.17% | 3 | 33% | 702 |
| intramonth | 206,742 | +3.37% | 0 | - | 235 |
| snake_viper_tick | 204,707 | +2.35% | 2 | 0% | 532 |
| random_hold | 202,660 | +1.33% | 8 | 62% | 649 |
| snake_anaconda | 202,626 | +1.31% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,294 | +0.65% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,345 | -1.83% | 0 | - | 237 |
| gold | 191,427 | -4.29% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,764 (-5.12%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,633 | +4.72% |
| snake_abs_exit_conv | +9,447 | +4.62% |
| snake_abs_conv | +9,389 | +4.67% |
| snake_abs | +9,366 | +4.65% |
| snake_anaconda | +8,802 | +4.54% |
| gold | +6,149 | +3.32% |
| intraweek | +4,063 | +1.98% |
| benchmark_smallcap | +3,408 | +1.77% |
| intramonth | +2,771 | +1.36% |
| unified | +2,251 | +1.06% |
| random_hold | +2,192 | +1.09% |
| benchmark | +1,859 | +0.90% |
| oracle | +1,304 | +0.65% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,460 | -1.19% |
| snake_viper_wild | -2,563 | -1.22% |

Average per day so far: snake_abs_exit_conv Rs +574, snake_abs_exit Rs +569, unified Rs +528, snake_abs_conv Rs +439, snake_viper_wild Rs +438, snake_abs Rs +427, intraweek Rs +339, benchmark Rs +317, snake_viper_tick Rs +294, intramonth Rs +250, snake_anaconda Rs +119, random_hold Rs +99, nifty_calls Rs +68, oracle Rs +48, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -159, gold Rs -318, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.