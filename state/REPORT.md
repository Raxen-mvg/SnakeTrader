# Paper trading report

Updated 2026-11-18 11:52 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,038 | +11.52% | 0 | - | 236 |
| benchmark | 220,326 | +10.16% | 0 | - | 237 |
| intraweek | 214,277 | +7.14% | 35 | 54% | 3,851 |
| intramonth | 212,982 | +6.49% | 0 | - | 235 |
| snake_abs_exit | 212,535 | +6.27% | 2 | 50% | 345 |
| oracle | 212,526 | +6.26% | 0 | - | 233 |
| snake_abs_exit_conv | 210,879 | +5.44% | 2 | 50% | 345 |
| snake_abs | 207,694 | +3.85% | 1 | 100% | 255 |
| snake_abs_conv | 207,561 | +3.78% | 1 | 100% | 255 |
| random_hold | 207,442 | +3.72% | 10 | 70% | 733 |
| snake_viper_wild | 206,574 | +3.29% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,047 | +1.52% | 15 | 47% | 2,625 |
| snake_anaconda | 202,918 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,124 | -11.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,614 (-4.19%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,599 | +0.72% |
| intramonth | +1,440 | +0.68% |
| intraweek | +955 | +0.45% |
| oracle | +40 | +0.02% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -607 | -0.28% |
| snake_abs_exit_conv | -694 | -0.33% |
| snake_abs_conv | -859 | -0.41% |
| snake_abs | -865 | -0.41% |
| random_hold | -990 | -0.47% |
| benchmark_smallcap | -1,132 | -0.56% |
| snake_anaconda | -1,137 | -0.56% |
| benchmark | -1,278 | -0.58% |
| snake_viper_tick | -2,789 | -1.35% |
| snake_viper_wild | -2,841 | -1.36% |
| gold | -3,600 | -1.99% |

Average per day so far: unified Rs +640, benchmark Rs +565, intraweek Rs +397, snake_abs_exit Rs +380, intramonth Rs +361, oracle Rs +348, snake_abs_exit_conv Rs +330, snake_viper_wild Rs +235, snake_abs_conv Rs +229, snake_abs Rs +226, random_hold Rs +207, snake_viper_tick Rs +122, snake_anaconda Rs +94, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -18, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.