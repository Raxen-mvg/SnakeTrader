# Paper trading report

Updated 2026-11-25 12:58 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,592 | +12.30% | 0 | - | 236 |
| benchmark | 224,243 | +12.12% | 0 | - | 237 |
| oracle | 212,489 | +6.25% | 0 | - | 233 |
| intramonth | 212,475 | +6.24% | 0 | - | 235 |
| random_hold | 209,997 | +5.00% | 12 | 75% | 1,009 |
| intraweek | 208,500 | +4.25% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,857 | +0.93% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,475 | +0.74% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,981 | -0.01% | 1 | 100% | 255 |
| snake_abs_conv | 199,799 | -0.10% | 1 | 100% | 255 |
| benchmark_smallcap | 199,047 | -0.48% | 0 | - | 237 |
| snake_viper_wild | 196,742 | -1.63% | 16 | 50% | 2,827 |
| snake_anaconda | 193,555 | -3.22% | 3 | 33% | 374 |
| snake_viper_tick | 193,392 | -3.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,662 | -17.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,220 (-5.39%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,769 | +1.25% |
| random_hold | +1,570 | +0.75% |
| unified | +307 | +0.14% |
| oracle | +147 | +0.07% |
| benchmark_smallcap | +67 | +0.03% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -276 | -0.13% |
| intraweek | -3,119 | -1.47% |
| snake_viper_tick | -4,301 | -2.17% |
| snake_viper_wild | -4,383 | -2.18% |
| gold | -4,768 | -2.81% |
| snake_anaconda | -5,148 | -2.59% |
| snake_abs | -5,480 | -2.67% |
| snake_abs_conv | -5,503 | -2.68% |
| snake_abs_exit_conv | -5,570 | -2.69% |
| snake_abs_exit | -5,638 | -2.72% |

Average per day so far: unified Rs +615, benchmark Rs +606, oracle Rs +312, intramonth Rs +312, random_hold Rs +250, intraweek Rs +213, snake_abs_exit Rs +50, nifty_calls Rs +46, snake_abs_exit_conv Rs +40, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -0, snake_abs_conv Rs -5, benchmark_smallcap Rs -26, snake_viper_wild Rs -102, snake_anaconda Rs -184, snake_viper_tick Rs -228, snake_nonews Rs -292, snake Rs -311, gold Rs -883

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.