# Paper trading report

Updated 2026-11-06 13:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,621 | +7.81% | 0 | - | 237 |
| unified | 214,632 | +7.32% | 0 | - | 236 |
| intraweek | 208,621 | +4.31% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,548 | +4.27% | 1 | 100% | 255 |
| snake_abs_exit | 208,454 | +4.23% | 1 | 100% | 260 |
| intramonth | 206,920 | +3.46% | 0 | - | 235 |
| snake_abs | 205,532 | +2.77% | 1 | 100% | 255 |
| snake_abs_conv | 205,350 | +2.67% | 1 | 100% | 255 |
| oracle | 205,132 | +2.57% | 0 | - | 233 |
| random_hold | 203,264 | +1.63% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,049 | -1.98% | 3 | 33% | 702 |
| snake_anaconda | 195,960 | -2.02% | 3 | 33% | 374 |
| benchmark_smallcap | 194,921 | -2.54% | 0 | - | 237 |
| snake_viper_tick | 192,728 | -3.64% | 2 | 0% | 532 |
| gold | 190,325 | -4.84% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,863 (-6.57%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,851 | +0.87% |
| oracle | +1,060 | +0.52% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -797 | -0.38% |
| intramonth | -1,029 | -0.49% |
| random_hold | -1,059 | -0.52% |
| unified | -1,352 | -0.63% |
| benchmark_smallcap | -3,767 | -1.90% |
| gold | -3,896 | -2.01% |
| snake_abs | -6,156 | -2.91% |
| snake_abs_conv | -6,195 | -2.93% |
| snake_abs_exit | -6,205 | -2.89% |
| snake_abs_exit_conv | -6,255 | -2.91% |
| snake_anaconda | -6,520 | -3.22% |
| snake_viper_tick | -8,410 | -4.18% |
| snake_viper_wild | -8,607 | -4.21% |

Average per day so far: benchmark Rs +539, unified Rs +505, snake_abs_exit_conv Rs +329, snake_abs_exit Rs +325, intraweek Rs +297, intramonth Rs +239, snake_abs_conv Rs +206, snake_abs Rs +205, oracle Rs +177, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -168, snake_viper_wild Rs -188, benchmark_smallcap Rs -203, gold Rs -334, snake_viper_tick Rs -404, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.