# Paper trading report

Updated 2026-11-06 11:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,851 | +7.42% | 0 | - | 236 |
| benchmark | 214,535 | +7.27% | 0 | - | 237 |
| intraweek | 211,212 | +5.61% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,818 | +4.91% | 1 | 100% | 255 |
| snake_abs_exit | 209,604 | +4.80% | 1 | 100% | 260 |
| intramonth | 206,902 | +3.45% | 0 | - | 235 |
| snake_abs | 206,767 | +3.38% | 1 | 100% | 255 |
| snake_abs_conv | 206,602 | +3.30% | 1 | 100% | 255 |
| oracle | 204,755 | +2.38% | 0 | - | 233 |
| random_hold | 203,461 | +1.73% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,138 | -1.43% | 3 | 33% | 374 |
| snake_viper_wild | 195,864 | -2.07% | 3 | 33% | 702 |
| benchmark_smallcap | 194,764 | -2.62% | 0 | - | 237 |
| snake_viper_tick | 192,546 | -3.73% | 2 | 0% | 532 |
| gold | 190,062 | -4.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,506 (-6.25%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,793 | +0.86% |
| benchmark | +765 | +0.36% |
| oracle | +683 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -862 | -0.42% |
| intramonth | -1,047 | -0.50% |
| unified | -1,133 | -0.52% |
| benchmark_smallcap | -3,924 | -1.98% |
| gold | -4,159 | -2.14% |
| snake_abs | -4,921 | -2.33% |
| snake_abs_conv | -4,943 | -2.34% |
| snake_abs_exit_conv | -4,985 | -2.32% |
| snake_abs_exit | -5,055 | -2.35% |
| snake_anaconda | -5,341 | -2.64% |
| snake_viper_tick | -8,592 | -4.27% |
| snake_viper_wild | -8,792 | -4.30% |

Average per day so far: unified Rs +512, benchmark Rs +501, intraweek Rs +387, snake_abs_exit_conv Rs +378, snake_abs_exit Rs +369, snake_abs_conv Rs +254, snake_abs Rs +251, intramonth Rs +238, oracle Rs +164, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -119, snake_viper_wild Rs -197, benchmark_smallcap Rs -209, gold Rs -343, snake_nonews Rs -411, snake_viper_tick Rs -414, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.