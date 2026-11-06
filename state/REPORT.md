# Paper trading report

Updated 2026-11-06 13:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,248 | +8.12% | 0 | - | 237 |
| unified | 214,736 | +7.37% | 0 | - | 236 |
| snake_abs_exit_conv | 208,630 | +4.32% | 1 | 100% | 255 |
| snake_abs_exit | 208,532 | +4.27% | 1 | 100% | 260 |
| intraweek | 208,007 | +4.00% | 25 | 48% | 2,757 |
| intramonth | 206,989 | +3.50% | 0 | - | 235 |
| snake_abs | 205,615 | +2.81% | 1 | 100% | 255 |
| snake_abs_conv | 205,430 | +2.71% | 1 | 100% | 255 |
| oracle | 205,289 | +2.64% | 0 | - | 233 |
| random_hold | 203,328 | +1.66% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,200 | -1.90% | 3 | 33% | 702 |
| snake_anaconda | 195,966 | -2.02% | 3 | 33% | 374 |
| benchmark_smallcap | 195,179 | -2.41% | 0 | - | 237 |
| snake_viper_tick | 192,873 | -3.56% | 2 | 0% | 532 |
| gold | 190,884 | -4.56% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,860 (-6.57%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,479 | +1.16% |
| oracle | +1,217 | +0.60% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -959 | -0.46% |
| random_hold | -995 | -0.49% |
| unified | -1,248 | -0.58% |
| intraweek | -1,412 | -0.67% |
| gold | -3,337 | -1.72% |
| benchmark_smallcap | -3,509 | -1.77% |
| snake_abs | -6,074 | -2.87% |
| snake_abs_conv | -6,115 | -2.89% |
| snake_abs_exit | -6,126 | -2.85% |
| snake_abs_exit_conv | -6,174 | -2.87% |
| snake_anaconda | -6,514 | -3.22% |
| snake_viper_tick | -8,265 | -4.11% |
| snake_viper_wild | -8,456 | -4.13% |

Average per day so far: benchmark Rs +560, unified Rs +508, snake_abs_exit_conv Rs +332, snake_abs_exit Rs +328, intraweek Rs +276, intramonth Rs +241, snake_abs_conv Rs +209, snake_abs Rs +208, oracle Rs +182, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -168, snake_viper_wild Rs -181, benchmark_smallcap Rs -193, gold Rs -314, snake_viper_tick Rs -396, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.