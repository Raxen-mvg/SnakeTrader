# Paper trading report

Updated 2026-11-27 14:31 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,051 | +12.03% | 0 | - | 237 |
| unified | 223,818 | +11.91% | 0 | - | 236 |
| oracle | 212,044 | +6.02% | 0 | - | 233 |
| intramonth | 211,166 | +5.58% | 0 | - | 235 |
| random_hold | 211,153 | +5.58% | 13 | 69% | 1,037 |
| intraweek | 207,877 | +3.94% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,555 | +3.28% | 2 | 50% | 345 |
| snake_abs_exit | 204,274 | +2.14% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,603 | +0.80% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,772 | -0.11% | 1 | 100% | 255 |
| snake_abs_conv | 199,589 | -0.21% | 1 | 100% | 255 |
| snake_anaconda | 193,071 | -3.46% | 3 | 33% | 374 |
| snake_viper_wild | 192,313 | -3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,047 | -5.48% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,811 | -14.60% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,071 (-5.46%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,158 | +3.07% |
| gold | +4,817 | +2.90% |
| snake_abs_exit | +3,196 | +1.59% |
| random_hold | +2,559 | +1.23% |
| snake_abs_conv | +1,222 | +0.62% |
| snake_abs | +1,220 | +0.61% |
| intraweek | +828 | +0.40% |
| snake_anaconda | +775 | +0.40% |
| benchmark_smallcap | +762 | +0.38% |
| unified | +740 | +0.33% |
| intramonth | +632 | +0.30% |
| snake_viper_wild | +107 | +0.06% |
| snake_viper_tick | +106 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -191 | -0.09% |
| benchmark | -1,935 | -0.86% |

Average per day so far: benchmark Rs +573, unified Rs +567, oracle Rs +287, intramonth Rs +266, random_hold Rs +266, intraweek Rs +188, snake_abs_exit_conv Rs +168, snake_abs_exit Rs +110, nifty_calls Rs +44, benchmark_smallcap Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, snake_anaconda Rs -187, snake_viper_wild Rs -226, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -353, gold Rs -695

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.