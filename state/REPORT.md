# Paper trading report

Updated 2026-11-27 10:20 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,543 | +12.77% | 0 | - | 237 |
| unified | 222,808 | +11.40% | 0 | - | 236 |
| oracle | 212,400 | +6.20% | 0 | - | 233 |
| intramonth | 210,686 | +5.34% | 0 | - | 235 |
| random_hold | 210,196 | +5.10% | 13 | 69% | 1,037 |
| intraweek | 208,380 | +4.19% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,766 | +2.88% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,502 | +2.25% | 2 | 50% | 345 |
| benchmark_smallcap | 202,129 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,653 | +0.83% | 1 | 100% | 255 |
| snake_abs_conv | 201,478 | +0.74% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,946 | -2.53% | 3 | 33% | 374 |
| snake_viper_wild | 193,297 | -3.35% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,010 | -5.00% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,789 | -15.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,813 (-5.59%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,688 | +2.33% |
| snake_abs_exit_conv | +4,105 | +2.05% |
| snake_abs_conv | +3,111 | +1.57% |
| snake_abs | +3,101 | +1.56% |
| gold | +2,795 | +1.68% |
| snake_anaconda | +2,650 | +1.38% |
| random_hold | +1,602 | +0.77% |
| intraweek | +1,332 | +0.64% |
| benchmark_smallcap | +1,289 | +0.64% |
| snake_viper_wild | +1,091 | +0.57% |
| snake_viper_tick | +1,069 | +0.57% |
| oracle | +164 | +0.08% |
| intramonth | +153 | +0.07% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -271 | -0.12% |
| benchmark | -444 | -0.20% |

Average per day so far: benchmark Rs +608, unified Rs +543, oracle Rs +295, intramonth Rs +254, random_hold Rs +243, intraweek Rs +200, snake_abs_exit Rs +148, snake_abs_exit_conv Rs +115, benchmark_smallcap Rs +56, nifty_calls Rs +44, snake_abs Rs +41, snake_abs_conv Rs +38, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -137, snake_viper_wild Rs -197, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -322, gold Rs -743

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.