# Paper trading report

Updated 2026-11-26 11:29 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,750 | +12.88% | 0 | - | 237 |
| unified | 223,363 | +11.68% | 0 | - | 236 |
| oracle | 213,118 | +6.56% | 0 | - | 233 |
| intramonth | 210,659 | +5.33% | 0 | - | 235 |
| random_hold | 209,851 | +4.93% | 13 | 69% | 1,037 |
| intraweek | 208,294 | +4.15% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,675 | +0.84% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,122 | +0.56% | 2 | 50% | 345 |
| benchmark_smallcap | 200,437 | +0.22% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,446 | -0.28% | 1 | 100% | 255 |
| snake_abs_conv | 199,257 | -0.37% | 1 | 100% | 255 |
| snake_anaconda | 193,330 | -3.33% | 3 | 33% | 374 |
| snake_viper_wild | 193,329 | -3.34% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,041 | -4.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,947 | -16.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,891 (-5.55%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,351 | +1.43% |
| benchmark_smallcap | +1,625 | +0.82% |
| intraweek | +1,550 | +0.75% |
| benchmark | +727 | +0.32% |
| random_hold | +358 | +0.17% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -580 | -0.29% |
| oracle | -677 | -0.32% |
| snake_abs | -704 | -0.35% |
| snake_abs_conv | -715 | -0.36% |
| unified | -737 | -0.33% |
| snake_abs_exit_conv | -853 | -0.42% |
| intramonth | -1,034 | -0.49% |
| snake_anaconda | -1,223 | -0.63% |
| snake_viper_tick | -4,136 | -2.13% |
| snake_viper_wild | -4,215 | -2.13% |

Average per day so far: benchmark Rs +628, unified Rs +570, oracle Rs +320, intramonth Rs +260, random_hold Rs +240, intraweek Rs +202, nifty_calls Rs +45, snake_abs_exit Rs +44, snake_abs_exit_conv Rs +30, benchmark_smallcap Rs +12, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -14, snake_abs_conv Rs -20, snake_anaconda Rs -185, snake_viper_wild Rs -202, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -332, gold Rs -806

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.