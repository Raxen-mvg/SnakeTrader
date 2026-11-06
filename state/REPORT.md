# Paper trading report

Updated 2026-11-06 11:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,027 | +7.51% | 0 | - | 236 |
| benchmark | 214,711 | +7.36% | 0 | - | 237 |
| intraweek | 211,585 | +5.79% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,757 | +4.88% | 1 | 100% | 255 |
| snake_abs_exit | 209,546 | +4.77% | 1 | 100% | 260 |
| intramonth | 207,159 | +3.58% | 0 | - | 235 |
| snake_abs | 206,708 | +3.35% | 1 | 100% | 255 |
| snake_abs_conv | 206,542 | +3.27% | 1 | 100% | 255 |
| oracle | 205,110 | +2.56% | 0 | - | 233 |
| random_hold | 203,716 | +1.86% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,098 | -1.45% | 3 | 33% | 374 |
| snake_viper_wild | 196,241 | -1.88% | 3 | 33% | 702 |
| benchmark_smallcap | 195,011 | -2.49% | 0 | - | 237 |
| snake_viper_tick | 192,918 | -3.54% | 2 | 0% | 532 |
| gold | 189,783 | -5.11% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,659 (-6.17%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,167 | +1.03% |
| oracle | +1,038 | +0.51% |
| benchmark | +941 | +0.44% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -608 | -0.30% |
| intramonth | -790 | -0.38% |
| unified | -957 | -0.44% |
| benchmark_smallcap | -3,677 | -1.85% |
| gold | -4,439 | -2.29% |
| snake_abs | -4,981 | -2.35% |
| snake_abs_conv | -5,003 | -2.37% |
| snake_abs_exit_conv | -5,046 | -2.35% |
| snake_abs_exit | -5,113 | -2.38% |
| snake_anaconda | -5,381 | -2.66% |
| snake_viper_tick | -8,220 | -4.09% |
| snake_viper_wild | -8,415 | -4.11% |

Average per day so far: unified Rs +518, benchmark Rs +507, intraweek Rs +399, snake_abs_exit_conv Rs +375, snake_abs_exit Rs +367, snake_abs_conv Rs +252, snake_abs Rs +248, intramonth Rs +247, oracle Rs +176, random_hold Rs +128, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -121, snake_viper_wild Rs -179, benchmark_smallcap Rs -200, gold Rs -352, snake_viper_tick Rs -393, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.