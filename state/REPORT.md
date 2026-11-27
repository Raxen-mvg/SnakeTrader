# Paper trading report

Updated 2026-11-27 13:13 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,059 | +12.03% | 0 | - | 237 |
| unified | 223,480 | +11.74% | 0 | - | 236 |
| oracle | 212,013 | +6.01% | 0 | - | 233 |
| intramonth | 211,041 | +5.52% | 0 | - | 235 |
| random_hold | 210,826 | +5.41% | 13 | 69% | 1,037 |
| intraweek | 208,554 | +4.28% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,039 | +2.52% | 2 | 50% | 345 |
| snake_abs_exit | 204,763 | +2.38% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,513 | +0.76% | 0 | - | 237 |
| snake_abs | 200,490 | +0.24% | 1 | 100% | 255 |
| snake_abs_conv | 200,307 | +0.15% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,868 | -3.07% | 3 | 33% | 374 |
| snake_viper_wild | 192,418 | -3.79% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,150 | -5.42% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,578 | -15.21% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,983 (-5.51%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,642 | +2.32% |
| snake_abs_exit | +3,686 | +1.83% |
| gold | +3,584 | +2.16% |
| random_hold | +2,232 | +1.07% |
| snake_abs_conv | +1,940 | +0.98% |
| snake_abs | +1,938 | +0.98% |
| snake_anaconda | +1,572 | +0.82% |
| intraweek | +1,506 | +0.73% |
| benchmark_smallcap | +673 | +0.34% |
| intramonth | +508 | +0.24% |
| unified | +401 | +0.18% |
| snake_viper_wild | +213 | +0.11% |
| snake_viper_tick | +209 | +0.11% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -223 | -0.10% |
| benchmark | -1,928 | -0.85% |

Average per day so far: benchmark Rs +573, unified Rs +559, oracle Rs +286, intramonth Rs +263, random_hold Rs +258, intraweek Rs +204, snake_abs_exit_conv Rs +129, snake_abs_exit Rs +122, nifty_calls Rs +44, benchmark_smallcap Rs +40, snake_abs Rs +12, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -166, snake_viper_wild Rs -223, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -350, gold Rs -724

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.