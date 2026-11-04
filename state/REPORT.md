# Paper trading report

Updated 2026-11-04 13:16 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,043 | +7.02% | 0 | - | 236 |
| snake_abs_exit_conv | 212,561 | +6.28% | 1 | 100% | 255 |
| snake_abs_exit | 212,416 | +6.21% | 1 | 100% | 260 |
| intraweek | 209,501 | +4.75% | 25 | 48% | 2,757 |
| snake_abs | 209,460 | +4.73% | 1 | 100% | 255 |
| snake_abs_conv | 209,304 | +4.65% | 1 | 100% | 255 |
| benchmark | 208,040 | +4.02% | 0 | - | 237 |
| snake_viper_wild | 207,146 | +3.57% | 3 | 33% | 702 |
| intramonth | 206,140 | +3.07% | 0 | - | 235 |
| snake_viper_tick | 203,538 | +1.77% | 2 | 0% | 532 |
| random_hold | 202,643 | +1.32% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,125 | +0.56% | 0 | - | 233 |
| snake_anaconda | 200,930 | +0.47% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,325 | -2.34% | 0 | - | 237 |
| gold | 190,966 | -4.52% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,344 (-5.33%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,402 | +4.12% |
| snake_abs_exit_conv | +8,222 | +4.02% |
| snake_abs_conv | +8,163 | +4.06% |
| snake_abs | +8,150 | +4.05% |
| snake_anaconda | +7,106 | +3.67% |
| gold | +5,688 | +3.07% |
| intraweek | +4,415 | +2.15% |
| benchmark_smallcap | +2,388 | +1.24% |
| random_hold | +2,175 | +1.08% |
| intramonth | +2,169 | +1.06% |
| unified | +2,042 | +0.96% |
| benchmark | +1,339 | +0.65% |
| oracle | +1,136 | +0.57% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,629 | -1.75% |
| snake_viper_wild | -3,747 | -1.78% |

Average per day so far: snake_abs_exit_conv Rs +523, unified Rs +520, snake_abs_exit Rs +517, snake_abs_conv Rs +388, snake_abs Rs +378, snake_viper_wild Rs +376, intraweek Rs +352, benchmark Rs +298, intramonth Rs +227, snake_viper_tick Rs +221, random_hold Rs +98, nifty_calls Rs +68, snake_anaconda Rs +42, oracle Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -203, gold Rs -335, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.