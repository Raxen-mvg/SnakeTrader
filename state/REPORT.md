# Paper trading report

Updated 2026-11-19 11:57 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,677 | +11.84% | 0 | - | 236 |
| benchmark | 221,374 | +10.69% | 0 | - | 237 |
| snake_abs_exit | 213,436 | +6.72% | 2 | 50% | 345 |
| intramonth | 213,232 | +6.62% | 0 | - | 235 |
| intraweek | 211,723 | +5.86% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,581 | +5.79% | 2 | 50% | 345 |
| oracle | 210,981 | +5.49% | 0 | - | 233 |
| snake_abs | 209,019 | +4.51% | 1 | 100% | 255 |
| snake_abs_conv | 208,892 | +4.45% | 1 | 100% | 255 |
| random_hold | 207,668 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 207,580 | +3.79% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,033 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,281 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,102 | -12.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,159 (-4.42%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,289 | +0.65% |
| benchmark | +1,079 | +0.49% |
| unified | +1,066 | +0.48% |
| intramonth | +959 | +0.45% |
| random_hold | +736 | +0.36% |
| snake_viper_wild | +541 | +0.26% |
| snake_viper_tick | +530 | +0.26% |
| oracle | +185 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -117 | -0.06% |
| snake_abs | -418 | -0.20% |
| snake_abs_conv | -432 | -0.21% |
| snake_abs_exit | -595 | -0.28% |
| snake_abs_exit_conv | -802 | -0.38% |
| snake_anaconda | -1,120 | -0.55% |
| gold | -2,219 | -1.25% |

Average per day so far: unified Rs +640, benchmark Rs +578, snake_abs_exit Rs +395, intramonth Rs +358, snake_abs_exit_conv Rs +341, intraweek Rs +317, oracle Rs +297, snake_abs_conv Rs +262, snake_viper_wild Rs +261, snake_abs Rs +258, random_hold Rs +207, snake_viper_tick Rs +155, snake_anaconda Rs +103, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -673

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.