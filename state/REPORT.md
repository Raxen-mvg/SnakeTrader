# Paper trading report

Updated 2026-11-09 12:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,160 | +10.08% | 0 | - | 236 |
| benchmark | 217,166 | +8.58% | 0 | - | 237 |
| intraweek | 215,133 | +7.57% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,064 | +6.03% | 2 | 50% | 330 |
| snake_abs_exit | 211,790 | +5.89% | 2 | 50% | 308 |
| intramonth | 210,208 | +5.10% | 0 | - | 235 |
| oracle | 209,670 | +4.83% | 0 | - | 233 |
| snake_abs | 209,586 | +4.79% | 1 | 100% | 255 |
| snake_abs_conv | 209,407 | +4.70% | 1 | 100% | 255 |
| random_hold | 204,469 | +2.23% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,414 | -0.29% | 7 | 57% | 1,332 |
| snake_anaconda | 199,289 | -0.36% | 3 | 33% | 374 |
| benchmark_smallcap | 198,542 | -0.73% | 0 | - | 237 |
| snake_viper_tick | 196,027 | -1.99% | 6 | 50% | 1,154 |
| gold | 192,413 | -3.79% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,418 (-4.79%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,771 | +2.27% |
| unified | +4,551 | +2.11% |
| snake_abs_conv | +4,180 | +2.04% |
| snake_abs | +4,167 | +2.03% |
| oracle | +3,843 | +1.87% |
| snake_abs_exit_conv | +3,642 | +1.75% |
| snake_abs_exit | +3,478 | +1.67% |
| snake_anaconda | +3,462 | +1.77% |
| snake_viper_wild | +3,376 | +1.72% |
| snake_viper_tick | +3,317 | +1.72% |
| intramonth | +2,605 | +1.25% |
| benchmark_smallcap | +1,749 | +0.89% |
| gold | +1,365 | +0.71% |
| random_hold | +563 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -321 | -0.15% |

Average per day so far: unified Rs +672, benchmark Rs +572, intraweek Rs +504, snake_abs_exit_conv Rs +447, snake_abs_exit Rs +437, snake_abs_conv Rs +348, snake_abs Rs +342, intramonth Rs +340, oracle Rs +322, random_hold Rs +149, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -27, snake_anaconda Rs -28, benchmark_smallcap Rs -56, snake_viper_tick Rs -209, gold Rs -253, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.