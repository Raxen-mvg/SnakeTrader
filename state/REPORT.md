# Paper trading report

Updated 2026-11-26 15:19 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,964 | +12.98% | 0 | - | 237 |
| unified | 223,097 | +11.55% | 0 | - | 236 |
| oracle | 212,103 | +6.05% | 0 | - | 233 |
| intramonth | 210,507 | +5.25% | 0 | - | 235 |
| random_hold | 208,533 | +4.27% | 13 | 69% | 1,037 |
| intraweek | 206,953 | +3.48% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,399 | +0.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,693 | +0.35% | 2 | 50% | 345 |
| benchmark_smallcap | 200,594 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,865 | -0.57% | 1 | 100% | 255 |
| snake_abs_conv | 198,682 | -0.66% | 1 | 100% | 255 |
| snake_viper_wild | 192,652 | -3.67% | 16 | 50% | 2,827 |
| snake_anaconda | 192,635 | -3.68% | 3 | 33% | 374 |
| snake_viper_tick | 189,378 | -5.31% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,276 (-5.86%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,782 | +0.90% |
| gold | +1,463 | +0.89% |
| benchmark | +941 | +0.42% |
| intraweek | +210 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -856 | -0.42% |
| random_hold | -960 | -0.46% |
| unified | -1,003 | -0.45% |
| intramonth | -1,186 | -0.56% |
| snake_abs_exit_conv | -1,283 | -0.64% |
| snake_abs | -1,285 | -0.64% |
| snake_abs_conv | -1,290 | -0.65% |
| oracle | -1,692 | -0.79% |
| snake_anaconda | -1,918 | -0.99% |
| snake_viper_tick | -4,799 | -2.47% |
| snake_viper_wild | -4,891 | -2.48% |

Average per day so far: benchmark Rs +633, unified Rs +563, oracle Rs +295, intramonth Rs +256, random_hold Rs +208, intraweek Rs +170, nifty_calls Rs +45, snake_abs_exit Rs +37, snake_abs_exit_conv Rs +18, benchmark_smallcap Rs +16, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -29, snake_abs_conv Rs -35, snake_anaconda Rs -205, snake_viper_wild Rs -223, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -354, gold Rs -828

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.