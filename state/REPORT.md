# Paper trading report

Updated 2026-11-06 09:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,897 | +7.45% | 0 | - | 236 |
| benchmark | 214,795 | +7.40% | 0 | - | 237 |
| snake_abs_exit_conv | 210,373 | +5.19% | 1 | 100% | 255 |
| intraweek | 210,277 | +5.14% | 25 | 48% | 2,757 |
| snake_abs_exit | 210,137 | +5.07% | 1 | 100% | 260 |
| snake_abs | 207,307 | +3.65% | 1 | 100% | 255 |
| snake_abs_conv | 207,147 | +3.57% | 1 | 100% | 255 |
| intramonth | 206,599 | +3.30% | 0 | - | 235 |
| oracle | 204,330 | +2.17% | 0 | - | 233 |
| random_hold | 203,934 | +1.97% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,586 | -0.71% | 3 | 33% | 702 |
| snake_anaconda | 197,653 | -1.17% | 3 | 33% | 374 |
| snake_viper_tick | 195,220 | -2.39% | 2 | 0% | 532 |
| benchmark_smallcap | 195,202 | -2.40% | 0 | - | 237 |
| gold | 190,358 | -4.82% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,615 (-6.19%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,025 | +0.48% |
| intraweek | +858 | +0.41% |
| oracle | +258 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -389 | -0.19% |
| unified | -1,086 | -0.50% |
| intramonth | -1,350 | -0.65% |
| benchmark_smallcap | -3,486 | -1.75% |
| gold | -3,863 | -1.99% |
| snake_abs | -4,382 | -2.07% |
| snake_abs_conv | -4,398 | -2.08% |
| snake_abs_exit_conv | -4,430 | -2.06% |
| snake_abs_exit | -4,522 | -2.11% |
| snake_anaconda | -4,826 | -2.38% |
| snake_viper_tick | -5,918 | -2.94% |
| snake_viper_wild | -6,070 | -2.97% |

Average per day so far: unified Rs +514, benchmark Rs +510, snake_abs_exit_conv Rs +399, snake_abs_exit Rs +390, intraweek Rs +354, snake_abs_conv Rs +275, snake_abs Rs +271, intramonth Rs +228, oracle Rs +149, random_hold Rs +136, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -67, snake_anaconda Rs -98, benchmark_smallcap Rs -192, snake_viper_tick Rs -266, gold Rs -332, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.