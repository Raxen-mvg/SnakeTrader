# Paper trading report

Updated 2026-11-06 09:45 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,610 | +7.30% | 0 | - | 236 |
| benchmark | 214,328 | +7.16% | 0 | - | 237 |
| snake_abs_exit_conv | 210,230 | +5.12% | 1 | 100% | 255 |
| snake_abs_exit | 209,995 | +5.00% | 1 | 100% | 260 |
| intraweek | 209,787 | +4.89% | 25 | 48% | 2,757 |
| snake_abs | 207,161 | +3.58% | 1 | 100% | 255 |
| snake_abs_conv | 207,004 | +3.50% | 1 | 100% | 255 |
| intramonth | 206,361 | +3.18% | 0 | - | 235 |
| oracle | 204,116 | +2.06% | 0 | - | 233 |
| random_hold | 203,611 | +1.81% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,486 | -0.76% | 3 | 33% | 702 |
| snake_anaconda | 197,575 | -1.21% | 3 | 33% | 374 |
| snake_viper_tick | 195,120 | -2.44% | 2 | 0% | 532 |
| benchmark_smallcap | 194,787 | -2.61% | 0 | - | 237 |
| gold | 190,309 | -4.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,399 (-6.30%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +558 | +0.26% |
| intraweek | +369 | +0.18% |
| oracle | +44 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -712 | -0.35% |
| unified | -1,374 | -0.64% |
| intramonth | -1,587 | -0.76% |
| benchmark_smallcap | -3,901 | -1.96% |
| gold | -3,913 | -2.02% |
| snake_abs | -4,527 | -2.14% |
| snake_abs_conv | -4,541 | -2.15% |
| snake_abs_exit_conv | -4,574 | -2.13% |
| snake_abs_exit | -4,664 | -2.17% |
| snake_anaconda | -4,905 | -2.42% |
| snake_viper_tick | -6,018 | -2.99% |
| snake_viper_wild | -6,170 | -3.02% |

Average per day so far: unified Rs +504, benchmark Rs +494, snake_abs_exit_conv Rs +393, snake_abs_exit Rs +384, intraweek Rs +337, snake_abs_conv Rs +269, snake_abs Rs +265, intramonth Rs +219, oracle Rs +142, random_hold Rs +125, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -72, snake_anaconda Rs -101, benchmark_smallcap Rs -209, snake_viper_tick Rs -271, gold Rs -334, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.