# Paper trading report

Updated 2026-11-18 10:26 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,323 | +11.16% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| intraweek | 214,771 | +7.38% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,544 | +6.27% | 2 | 50% | 345 |
| intramonth | 212,309 | +6.15% | 0 | - | 235 |
| oracle | 212,197 | +6.10% | 0 | - | 233 |
| snake_abs_exit_conv | 210,859 | +5.43% | 2 | 50% | 345 |
| snake_abs | 207,999 | +4.00% | 1 | 100% | 255 |
| snake_abs_conv | 207,851 | +3.92% | 1 | 100% | 255 |
| random_hold | 207,373 | +3.69% | 10 | 70% | 733 |
| snake_viper_wild | 207,356 | +3.68% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,813 | +1.91% | 15 | 47% | 2,625 |
| snake_anaconda | 202,702 | +1.35% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,078 | +0.04% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,485 | -11.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,398 (-4.30%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,448 | +0.68% |
| unified | +884 | +0.40% |
| intramonth | +766 | +0.36% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -289 | -0.14% |
| benchmark_smallcap | -493 | -0.25% |
| snake_abs | -559 | -0.27% |
| snake_abs_conv | -569 | -0.27% |
| snake_abs_exit | -598 | -0.28% |
| snake_abs_exit_conv | -715 | -0.34% |
| random_hold | -1,060 | -0.51% |
| benchmark | -1,224 | -0.55% |
| snake_anaconda | -1,353 | -0.66% |
| snake_viper_tick | -2,023 | -0.98% |
| snake_viper_wild | -2,059 | -0.98% |
| gold | -3,239 | -1.79% |

Average per day so far: unified Rs +620, benchmark Rs +566, intraweek Rs +410, snake_abs_exit Rs +380, intramonth Rs +342, oracle Rs +339, snake_abs_exit_conv Rs +329, snake_viper_wild Rs +263, snake_abs_conv Rs +238, snake_abs Rs +235, random_hold Rs +205, snake_viper_tick Rs +153, snake_anaconda Rs +87, nifty_calls Rs +51, benchmark_smallcap Rs +2, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -625

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.