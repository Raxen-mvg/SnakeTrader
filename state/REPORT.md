# Paper trading report

Updated 2026-11-23 13:07 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,907 | +11.95% | 0 | - | 236 |
| benchmark | 222,590 | +11.29% | 0 | - | 237 |
| intraweek | 212,516 | +6.26% | 40 | 55% | 4,400 |
| intramonth | 212,002 | +6.00% | 0 | - | 235 |
| oracle | 211,602 | +5.80% | 0 | - | 233 |
| random_hold | 209,084 | +4.54% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,936 | +3.47% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,570 | +2.79% | 2 | 50% | 345 |
| snake_abs | 204,403 | +2.20% | 1 | 100% | 255 |
| snake_abs_conv | 204,241 | +2.12% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,894 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 197,965 | -1.02% | 3 | 33% | 374 |
| snake_viper_tick | 197,467 | -1.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,170 | -14.91% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,101 (-4.95%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,121 | +1.26% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -877 | -0.41% |
| snake_abs_exit_conv | -1,047 | -0.51% |
| snake_abs | -1,516 | -0.74% |
| snake_abs_conv | -1,542 | -0.75% |
| snake_abs_exit | -1,627 | -0.78% |
| benchmark_smallcap | -1,670 | -0.83% |
| random_hold | -1,675 | -0.80% |
| snake_viper_tick | -1,905 | -0.95% |
| snake_viper_wild | -1,935 | -0.95% |
| snake_anaconda | -1,940 | -0.97% |
| unified | -2,274 | -1.01% |
| benchmark | -2,547 | -1.13% |
| intramonth | -3,002 | -1.40% |
| intraweek | -3,197 | -1.48% |

Average per day so far: unified Rs +613, benchmark Rs +579, intraweek Rs +321, intramonth Rs +308, oracle Rs +297, random_hold Rs +233, snake_abs_exit Rs +193, snake_abs_exit_conv Rs +155, snake_abs Rs +119, snake_abs_conv Rs +118, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -60, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -765

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.