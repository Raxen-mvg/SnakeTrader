# Paper trading report

Updated 2026-11-20 12:37 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,299 | +13.15% | 0 | - | 236 |
| benchmark | 224,174 | +12.09% | 0 | - | 237 |
| intramonth | 215,209 | +7.61% | 0 | - | 235 |
| intraweek | 214,800 | +7.40% | 35 | 54% | 3,851 |
| oracle | 212,764 | +6.38% | 0 | - | 233 |
| snake_abs_exit | 209,562 | +4.78% | 2 | 50% | 345 |
| random_hold | 209,024 | +4.51% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,612 | +3.81% | 2 | 50% | 345 |
| snake_abs | 206,606 | +3.30% | 1 | 100% | 255 |
| snake_abs_conv | 206,474 | +3.24% | 1 | 100% | 255 |
| snake_viper_wild | 205,550 | +2.77% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,043 | +1.02% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,896 | +0.45% | 0 | - | 237 |
| snake_anaconda | 200,674 | +0.34% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,388 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,043 (-3.98%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,911 | +0.90% |
| benchmark | +1,798 | +0.81% |
| unified | +1,684 | +0.75% |
| intramonth | +1,201 | +0.56% |
| oracle | +675 | +0.32% |
| random_hold | +570 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -572 | -0.28% |
| snake_viper_tick | -1,934 | -0.95% |
| snake_viper_wild | -1,973 | -0.95% |
| snake_abs | -2,374 | -1.14% |
| snake_abs_conv | -2,386 | -1.14% |
| snake_anaconda | -2,790 | -1.37% |
| snake_abs_exit_conv | -3,452 | -1.64% |
| snake_abs_exit | -3,789 | -1.78% |
| gold | -8,384 | -4.80% |

Average per day so far: unified Rs +692, benchmark Rs +636, intramonth Rs +400, intraweek Rs +389, oracle Rs +336, snake_abs_exit Rs +273, random_hold Rs +237, snake_abs_exit_conv Rs +217, snake_viper_wild Rs +185, snake_abs_conv Rs +185, snake_abs Rs +184, snake_viper_tick Rs +76, nifty_calls Rs +48, benchmark_smallcap Rs +26, snake_anaconda Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.