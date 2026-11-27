# Paper trading report

Updated 2026-11-27 12:31 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,388 | +12.19% | 0 | - | 237 |
| unified | 223,544 | +11.77% | 0 | - | 236 |
| oracle | 212,116 | +6.06% | 0 | - | 233 |
| intramonth | 211,063 | +5.53% | 0 | - | 235 |
| random_hold | 210,422 | +5.21% | 13 | 69% | 1,037 |
| intraweek | 208,072 | +4.04% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,663 | +2.33% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,423 | +1.71% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,659 | +0.83% | 0 | - | 237 |
| snake_abs | 200,325 | +0.16% | 1 | 100% | 255 |
| snake_abs_conv | 200,145 | +0.07% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,743 | -3.13% | 3 | 33% | 374 |
| snake_viper_wild | 192,394 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,127 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,578 | -15.21% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,914 (-5.54%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,586 | +1.78% |
| gold | +3,584 | +2.16% |
| snake_abs_exit_conv | +3,026 | +1.51% |
| random_hold | +1,828 | +0.88% |
| snake_abs_conv | +1,778 | +0.90% |
| snake_abs | +1,773 | +0.89% |
| snake_anaconda | +1,447 | +0.75% |
| intraweek | +1,024 | +0.49% |
| benchmark_smallcap | +818 | +0.41% |
| intramonth | +530 | +0.25% |
| unified | +465 | +0.21% |
| snake_viper_wild | +189 | +0.10% |
| snake_viper_tick | +185 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -120 | -0.06% |
| benchmark | -1,599 | -0.71% |

Average per day so far: benchmark Rs +581, unified Rs +561, oracle Rs +288, intramonth Rs +263, random_hold Rs +248, intraweek Rs +192, snake_abs_exit Rs +120, snake_abs_exit_conv Rs +88, nifty_calls Rs +44, benchmark_smallcap Rs +44, snake_abs Rs +8, snake_abs_conv Rs +4, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -169, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -724

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.