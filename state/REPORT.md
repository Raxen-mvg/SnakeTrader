# Paper trading report

Updated 2026-11-26 11:05 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,186 | +13.09% | 0 | - | 237 |
| unified | 223,510 | +11.76% | 0 | - | 236 |
| oracle | 212,915 | +6.46% | 0 | - | 233 |
| intramonth | 210,822 | +5.41% | 0 | - | 235 |
| random_hold | 210,050 | +5.03% | 13 | 69% | 1,037 |
| intraweek | 207,774 | +3.89% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,897 | +0.95% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,334 | +0.67% | 2 | 50% | 345 |
| benchmark_smallcap | 200,650 | +0.33% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,560 | -0.22% | 1 | 100% | 255 |
| snake_abs_conv | 199,370 | -0.32% | 1 | 100% | 255 |
| snake_anaconda | 193,218 | -3.39% | 3 | 33% | 374 |
| snake_viper_wild | 193,185 | -3.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,900 | -5.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,131 | -15.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,907 (-5.55%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,535 | +2.15% |
| benchmark_smallcap | +1,838 | +0.93% |
| benchmark | +1,163 | +0.52% |
| intraweek | +1,031 | +0.50% |
| random_hold | +557 | +0.27% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -358 | -0.18% |
| snake_abs | -590 | -0.29% |
| unified | -590 | -0.26% |
| snake_abs_conv | -602 | -0.30% |
| snake_abs_exit_conv | -641 | -0.32% |
| intramonth | -871 | -0.41% |
| oracle | -880 | -0.41% |
| snake_anaconda | -1,335 | -0.69% |
| snake_viper_tick | -4,277 | -2.20% |
| snake_viper_wild | -4,359 | -2.21% |

Average per day so far: benchmark Rs +639, unified Rs +573, oracle Rs +315, intramonth Rs +264, random_hold Rs +245, intraweek Rs +190, snake_abs_exit Rs +50, nifty_calls Rs +45, snake_abs_exit_conv Rs +35, benchmark_smallcap Rs +18, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -11, snake_abs_conv Rs -17, snake_anaconda Rs -188, snake_viper_wild Rs -207, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -337, gold Rs -777

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.