# Paper trading report

Updated 2026-11-09 12:11 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,231 | +10.12% | 0 | - | 236 |
| benchmark | 217,388 | +8.69% | 0 | - | 237 |
| intraweek | 214,604 | +7.30% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,252 | +6.13% | 2 | 50% | 330 |
| snake_abs_exit | 211,957 | +5.98% | 2 | 50% | 308 |
| intramonth | 210,358 | +5.18% | 0 | - | 235 |
| snake_abs | 209,730 | +4.87% | 1 | 100% | 255 |
| snake_abs_conv | 209,553 | +4.78% | 1 | 100% | 255 |
| oracle | 209,385 | +4.69% | 0 | - | 233 |
| random_hold | 204,393 | +2.20% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,426 | -0.29% | 3 | 33% | 374 |
| snake_viper_wild | 198,881 | -0.56% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,699 | -0.65% | 0 | - | 237 |
| snake_viper_tick | 195,502 | -2.25% | 6 | 50% | 1,154 |
| gold | 192,594 | -3.70% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,329 (-4.84%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,621 | +2.14% |
| snake_abs_conv | +4,326 | +2.11% |
| snake_abs | +4,311 | +2.10% |
| intraweek | +4,242 | +2.02% |
| snake_abs_exit_conv | +3,830 | +1.84% |
| snake_abs_exit | +3,645 | +1.75% |
| snake_anaconda | +3,599 | +1.84% |
| oracle | +3,558 | +1.73% |
| snake_viper_wild | +2,843 | +1.45% |
| snake_viper_tick | +2,792 | +1.45% |
| intramonth | +2,755 | +1.33% |
| benchmark_smallcap | +1,906 | +0.97% |
| gold | +1,545 | +0.81% |
| random_hold | +487 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -99 | -0.05% |

Average per day so far: unified Rs +674, benchmark Rs +580, intraweek Rs +487, snake_abs_exit_conv Rs +454, snake_abs_exit Rs +443, snake_abs_conv Rs +354, snake_abs Rs +348, intramonth Rs +345, oracle Rs +313, random_hold Rs +146, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -23, benchmark_smallcap Rs -50, snake_viper_wild Rs -51, snake_viper_tick Rs -237, gold Rs -247, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.