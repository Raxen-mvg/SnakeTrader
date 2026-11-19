# Paper trading report

Updated 2026-11-19 13:19 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,720 | +11.86% | 0 | - | 236 |
| benchmark | 221,466 | +10.73% | 0 | - | 237 |
| intramonth | 213,345 | +6.67% | 0 | - | 235 |
| snake_abs_exit | 212,862 | +6.43% | 2 | 50% | 345 |
| intraweek | 211,858 | +5.93% | 35 | 54% | 3,851 |
| oracle | 211,369 | +5.68% | 0 | - | 233 |
| snake_abs_exit_conv | 210,967 | +5.48% | 2 | 50% | 345 |
| snake_abs | 208,515 | +4.26% | 1 | 100% | 255 |
| snake_abs_conv | 208,387 | +4.19% | 1 | 100% | 255 |
| snake_viper_wild | 207,705 | +3.85% | 16 | 50% | 2,827 |
| random_hold | 207,648 | +3.82% | 10 | 70% | 733 |
| snake_viper_tick | 204,156 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,054 | +1.53% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,627 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,019 | -12.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,269 (-4.37%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,300 | +0.65% |
| benchmark | +1,170 | +0.53% |
| unified | +1,109 | +0.50% |
| intramonth | +1,071 | +0.51% |
| random_hold | +716 | +0.35% |
| snake_viper_wild | +666 | +0.32% |
| snake_viper_tick | +652 | +0.32% |
| oracle | +573 | +0.27% |
| intraweek | +19 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -921 | -0.44% |
| snake_abs_conv | -938 | -0.45% |
| snake_abs_exit | -1,169 | -0.55% |
| snake_anaconda | -1,347 | -0.66% |
| snake_abs_exit_conv | -1,416 | -0.67% |
| gold | -2,302 | -1.30% |

Average per day so far: unified Rs +641, benchmark Rs +580, snake_abs_exit Rs +378, intramonth Rs +361, snake_abs_exit_conv Rs +323, intraweek Rs +320, oracle Rs +307, snake_viper_wild Rs +266, snake_abs_conv Rs +247, snake_abs Rs +243, random_hold Rs +207, snake_viper_tick Rs +160, snake_anaconda Rs +95, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -675

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.