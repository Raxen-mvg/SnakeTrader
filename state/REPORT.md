# Paper trading report

Updated 2026-11-27 10:53 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,740 | +12.37% | 0 | - | 237 |
| unified | 223,112 | +11.56% | 0 | - | 236 |
| oracle | 212,491 | +6.25% | 0 | - | 233 |
| intramonth | 210,755 | +5.38% | 0 | - | 235 |
| random_hold | 210,319 | +5.16% | 13 | 69% | 1,037 |
| intraweek | 208,152 | +4.08% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,472 | +2.74% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,300 | +2.15% | 2 | 50% | 345 |
| benchmark_smallcap | 202,208 | +1.10% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,200 | +0.60% | 1 | 100% | 255 |
| snake_abs_conv | 201,023 | +0.51% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,799 | -2.60% | 3 | 33% | 374 |
| snake_viper_wild | 193,623 | -3.19% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,330 | -4.83% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,970 | -15.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,906 (-5.55%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,395 | +2.19% |
| snake_abs_exit_conv | +3,903 | +1.95% |
| gold | +2,976 | +1.79% |
| snake_abs_conv | +2,656 | +1.34% |
| snake_abs | +2,647 | +1.33% |
| snake_anaconda | +2,503 | +1.30% |
| random_hold | +1,725 | +0.83% |
| snake_viper_wild | +1,418 | +0.74% |
| snake_viper_tick | +1,389 | +0.73% |
| benchmark_smallcap | +1,368 | +0.68% |
| intraweek | +1,104 | +0.53% |
| oracle | +256 | +0.12% |
| intramonth | +221 | +0.10% |
| unified | +34 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -1,247 | -0.55% |

Average per day so far: benchmark Rs +589, unified Rs +550, oracle Rs +297, intramonth Rs +256, random_hold Rs +246, intraweek Rs +194, snake_abs_exit Rs +140, snake_abs_exit_conv Rs +110, benchmark_smallcap Rs +58, nifty_calls Rs +44, snake_abs Rs +30, snake_abs_conv Rs +26, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -141, snake_viper_wild Rs -188, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -312, gold Rs -739

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.