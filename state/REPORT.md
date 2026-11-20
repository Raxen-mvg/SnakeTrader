# Paper trading report

Updated 2026-11-20 12:25 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,162 | +13.08% | 0 | - | 236 |
| benchmark | 224,036 | +12.02% | 0 | - | 237 |
| intramonth | 215,139 | +7.57% | 0 | - | 235 |
| intraweek | 214,564 | +7.28% | 35 | 54% | 3,851 |
| oracle | 212,724 | +6.36% | 0 | - | 233 |
| snake_abs_exit | 209,498 | +4.75% | 2 | 50% | 345 |
| random_hold | 208,987 | +4.49% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,536 | +3.77% | 2 | 50% | 345 |
| snake_abs | 206,660 | +3.33% | 1 | 100% | 255 |
| snake_abs_conv | 206,524 | +3.26% | 1 | 100% | 255 |
| snake_viper_wild | 206,092 | +3.05% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,574 | +1.29% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,952 | +0.48% | 0 | - | 237 |
| snake_anaconda | 200,629 | +0.32% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,668 | -16.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,998 (-4.00%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,675 | +0.79% |
| benchmark | +1,660 | +0.75% |
| unified | +1,547 | +0.69% |
| intramonth | +1,131 | +0.53% |
| oracle | +636 | +0.30% |
| random_hold | +534 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -516 | -0.26% |
| snake_viper_tick | -1,403 | -0.69% |
| snake_viper_wild | -1,430 | -0.69% |
| snake_abs | -2,320 | -1.11% |
| snake_abs_conv | -2,336 | -1.12% |
| snake_anaconda | -2,834 | -1.39% |
| snake_abs_exit_conv | -3,528 | -1.67% |
| snake_abs_exit | -3,853 | -1.81% |
| gold | -8,105 | -4.64% |

Average per day so far: unified Rs +688, benchmark Rs +633, intramonth Rs +398, intraweek Rs +383, oracle Rs +335, snake_abs_exit Rs +271, random_hold Rs +237, snake_abs_exit_conv Rs +215, snake_viper_wild Rs +203, snake_abs_conv Rs +186, snake_abs Rs +185, snake_viper_tick Rs +95, nifty_calls Rs +48, benchmark_smallcap Rs +28, snake_anaconda Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -877

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.