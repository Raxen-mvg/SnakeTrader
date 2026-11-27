# Paper trading report

Updated 2026-11-27 12:58 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,120 | +12.06% | 0 | - | 237 |
| unified | 223,443 | +11.72% | 0 | - | 236 |
| oracle | 212,062 | +6.03% | 0 | - | 233 |
| intramonth | 210,941 | +5.47% | 0 | - | 235 |
| random_hold | 210,781 | +5.39% | 13 | 69% | 1,037 |
| intraweek | 208,471 | +4.24% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,767 | +2.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,058 | +2.03% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,546 | +0.77% | 0 | - | 237 |
| snake_abs | 200,497 | +0.25% | 1 | 100% | 255 |
| snake_abs_conv | 200,315 | +0.16% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,867 | -3.07% | 3 | 33% | 374 |
| snake_viper_wild | 192,145 | -3.93% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,882 | -5.56% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,545 | -15.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,960 (-5.52%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,690 | +1.83% |
| snake_abs_exit_conv | +3,661 | +1.83% |
| gold | +3,551 | +2.14% |
| random_hold | +2,187 | +1.05% |
| snake_abs_conv | +1,948 | +0.98% |
| snake_abs | +1,945 | +0.98% |
| snake_anaconda | +1,571 | +0.82% |
| intraweek | +1,423 | +0.69% |
| benchmark_smallcap | +706 | +0.35% |
| intramonth | +408 | +0.19% |
| unified | +364 | +0.16% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -59 | -0.03% |
| snake_viper_wild | -61 | -0.03% |
| oracle | -173 | -0.08% |
| benchmark | -1,867 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +558, oracle Rs +287, intramonth Rs +261, random_hold Rs +257, intraweek Rs +202, snake_abs_exit Rs +122, snake_abs_exit_conv Rs +104, nifty_calls Rs +44, benchmark_smallcap Rs +41, snake_abs Rs +12, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -166, snake_viper_wild Rs -231, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -359, gold Rs -725

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.