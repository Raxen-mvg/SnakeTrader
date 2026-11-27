# Paper trading report

Updated 2026-11-27 09:17 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,780 | +12.89% | 0 | - | 237 |
| unified | 223,109 | +11.55% | 0 | - | 236 |
| oracle | 212,708 | +6.35% | 0 | - | 233 |
| intramonth | 210,769 | +5.38% | 0 | - | 235 |
| random_hold | 209,839 | +4.92% | 13 | 69% | 1,037 |
| intraweek | 207,899 | +3.95% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,287 | +1.14% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,794 | +0.90% | 2 | 50% | 345 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,110 | -0.45% | 1 | 100% | 255 |
| snake_abs_conv | 198,930 | -0.54% | 1 | 100% | 255 |
| snake_anaconda | 193,094 | -3.45% | 3 | 33% | 374 |
| snake_viper_wild | 192,177 | -3.91% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,913 | -5.54% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,411 | -15.79% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,768 (-5.62%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,417 | +1.46% |
| snake_abs_exit_conv | +1,397 | +0.70% |
| random_hold | +1,245 | +0.60% |
| snake_abs_exit | +1,209 | +0.60% |
| intraweek | +850 | +0.41% |
| snake_anaconda | +798 | +0.41% |
| benchmark_smallcap | +617 | +0.31% |
| snake_abs_conv | +563 | +0.28% |
| snake_abs | +557 | +0.28% |
| oracle | +472 | +0.22% |
| intramonth | +235 | +0.11% |
| unified | +31 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -28 | -0.01% |
| snake_viper_wild | -29 | -0.01% |
| benchmark | -207 | -0.09% |

Average per day so far: benchmark Rs +614, unified Rs +550, oracle Rs +303, intramonth Rs +256, random_hold Rs +234, intraweek Rs +188, snake_abs_exit Rs +59, snake_abs_exit_conv Rs +46, nifty_calls Rs +44, benchmark_smallcap Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -22, snake_abs_conv Rs -27, snake_anaconda Rs -187, snake_viper_wild Rs -230, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -358, gold Rs -752

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.