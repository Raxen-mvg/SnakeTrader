# Paper trading report

Updated 2026-11-26 11:40 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,711 | +12.86% | 0 | - | 237 |
| unified | 223,256 | +11.63% | 0 | - | 236 |
| oracle | 213,051 | +6.53% | 0 | - | 233 |
| intramonth | 210,496 | +5.25% | 0 | - | 235 |
| random_hold | 209,765 | +4.88% | 13 | 69% | 1,037 |
| intraweek | 208,744 | +4.37% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 200,538 | +0.27% | 2 | 50% | 345 |
| benchmark_smallcap | 200,459 | +0.23% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,995 | -0.00% | 2 | 50% | 345 |
| snake_abs | 198,286 | -0.86% | 1 | 100% | 255 |
| snake_abs_conv | 198,096 | -0.95% | 1 | 100% | 255 |
| snake_anaconda | 192,160 | -3.92% | 3 | 33% | 374 |
| snake_viper_wild | 191,711 | -4.14% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,457 | -5.77% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,372 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,773 (-5.61%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,000 | +0.97% |
| gold | +1,776 | +1.08% |
| benchmark_smallcap | +1,648 | +0.83% |
| benchmark | +688 | +0.31% |
| random_hold | +272 | +0.13% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -745 | -0.35% |
| unified | -844 | -0.38% |
| intramonth | -1,197 | -0.56% |
| snake_abs_exit | -1,718 | -0.85% |
| snake_abs | -1,864 | -0.93% |
| snake_abs_conv | -1,877 | -0.94% |
| snake_abs_exit_conv | -1,981 | -0.98% |
| snake_anaconda | -2,393 | -1.23% |
| snake_viper_tick | -5,720 | -2.95% |
| snake_viper_wild | -5,832 | -2.95% |

Average per day so far: benchmark Rs +627, unified Rs +567, oracle Rs +318, intramonth Rs +256, random_hold Rs +238, intraweek Rs +213, nifty_calls Rs +45, snake_abs_exit Rs +14, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -0, snake_abs Rs -44, snake_abs_conv Rs -50, snake_anaconda Rs -218, snake_viper_wild Rs -251, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -385, gold Rs -820

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.