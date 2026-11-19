# Paper trading report

Updated 2026-11-19 14:43 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,128 | +12.06% | 0 | - | 236 |
| benchmark | 222,292 | +11.15% | 0 | - | 237 |
| intramonth | 213,646 | +6.82% | 0 | - | 235 |
| snake_abs_exit | 213,626 | +6.81% | 2 | 50% | 345 |
| intraweek | 211,960 | +5.98% | 35 | 54% | 3,851 |
| oracle | 211,656 | +5.83% | 0 | - | 233 |
| snake_abs_exit_conv | 211,330 | +5.67% | 2 | 50% | 345 |
| snake_abs | 209,084 | +4.54% | 1 | 100% | 255 |
| snake_abs_conv | 208,967 | +4.48% | 1 | 100% | 255 |
| random_hold | 208,088 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,609 | +3.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,062 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,684 | +1.84% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,863 | +0.43% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,019 | -12.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,553 (-4.22%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,997 | +0.91% |
| benchmark_smallcap | +1,536 | +0.77% |
| unified | +1,517 | +0.68% |
| intramonth | +1,372 | +0.65% |
| random_hold | +1,156 | +0.56% |
| oracle | +860 | +0.41% |
| snake_viper_wild | +570 | +0.28% |
| snake_viper_tick | +558 | +0.27% |
| intraweek | +121 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -353 | -0.17% |
| snake_abs_conv | -357 | -0.17% |
| snake_abs_exit | -406 | -0.19% |
| snake_anaconda | -717 | -0.35% |
| snake_abs_exit_conv | -1,053 | -0.50% |
| gold | -2,302 | -1.30% |

Average per day so far: unified Rs +652, benchmark Rs +602, snake_abs_exit Rs +401, intramonth Rs +369, snake_abs_exit_conv Rs +333, intraweek Rs +323, oracle Rs +315, snake_abs_conv Rs +264, snake_viper_wild Rs +262, snake_abs Rs +260, random_hold Rs +219, snake_viper_tick Rs +156, snake_anaconda Rs +115, nifty_calls Rs +50, benchmark_smallcap Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -675

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.