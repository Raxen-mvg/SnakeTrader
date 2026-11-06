# Paper trading report

Updated 2026-11-06 10:09 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,816 | +7.41% | 0 | - | 236 |
| benchmark | 214,718 | +7.36% | 0 | - | 237 |
| intraweek | 211,168 | +5.58% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 210,141 | +5.07% | 1 | 100% | 255 |
| snake_abs_exit | 209,923 | +4.96% | 1 | 100% | 260 |
| snake_abs | 207,086 | +3.54% | 1 | 100% | 255 |
| snake_abs_conv | 206,916 | +3.46% | 1 | 100% | 255 |
| intramonth | 206,880 | +3.44% | 0 | - | 235 |
| oracle | 204,335 | +2.17% | 0 | - | 233 |
| random_hold | 203,690 | +1.84% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,724 | -1.14% | 3 | 33% | 702 |
| snake_anaconda | 197,057 | -1.47% | 3 | 33% | 374 |
| benchmark_smallcap | 194,888 | -2.56% | 0 | - | 237 |
| snake_viper_tick | 194,365 | -2.82% | 2 | 0% | 532 |
| gold | 190,506 | -4.75% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,626 (-6.19%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,750 | +0.84% |
| benchmark | +949 | +0.44% |
| oracle | +263 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -633 | -0.31% |
| intramonth | -1,068 | -0.51% |
| unified | -1,168 | -0.54% |
| gold | -3,715 | -1.91% |
| benchmark_smallcap | -3,800 | -1.91% |
| snake_abs | -4,603 | -2.17% |
| snake_abs_conv | -4,628 | -2.19% |
| snake_abs_exit_conv | -4,663 | -2.17% |
| snake_abs_exit | -4,736 | -2.21% |
| snake_anaconda | -5,422 | -2.68% |
| snake_viper_tick | -6,773 | -3.37% |
| snake_viper_wild | -6,932 | -3.39% |

Average per day so far: unified Rs +511, benchmark Rs +508, snake_abs_exit_conv Rs +390, intraweek Rs +385, snake_abs_exit Rs +382, snake_abs_conv Rs +266, snake_abs Rs +262, intramonth Rs +237, oracle Rs +149, random_hold Rs +127, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -108, snake_anaconda Rs -123, benchmark_smallcap Rs -204, snake_viper_tick Rs -313, gold Rs -327, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.