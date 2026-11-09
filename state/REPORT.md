# Paper trading report

Updated 2026-11-09 14:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,061 | +10.03% | 0 | - | 236 |
| benchmark | 217,465 | +8.73% | 0 | - | 237 |
| intraweek | 214,540 | +7.27% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,214 | +6.61% | 2 | 50% | 330 |
| snake_abs_exit | 212,776 | +6.39% | 2 | 50% | 308 |
| intramonth | 210,144 | +5.07% | 0 | - | 235 |
| snake_abs | 210,141 | +5.07% | 1 | 100% | 255 |
| snake_abs_conv | 209,971 | +4.99% | 1 | 100% | 255 |
| oracle | 209,415 | +4.71% | 0 | - | 233 |
| random_hold | 204,418 | +2.21% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,194 | +0.10% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,495 | -0.25% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,094 | -0.95% | 0 | - | 237 |
| snake_viper_tick | 196,107 | -1.95% | 6 | 50% | 1,154 |
| gold | 192,150 | -3.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,350 (-4.83%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,793 | +2.30% |
| snake_abs_conv | +4,744 | +2.31% |
| snake_abs | +4,722 | +2.30% |
| snake_abs_exit | +4,464 | +2.14% |
| unified | +4,452 | +2.06% |
| snake_anaconda | +4,366 | +2.23% |
| intraweek | +4,178 | +1.99% |
| oracle | +3,588 | +1.74% |
| snake_viper_wild | +3,458 | +1.76% |
| snake_viper_tick | +3,397 | +1.76% |
| intramonth | +2,541 | +1.22% |
| benchmark_smallcap | +1,300 | +0.66% |
| gold | +1,101 | +0.58% |
| random_hold | +511 | +0.25% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -23 | -0.01% |

Average per day so far: unified Rs +669, benchmark Rs +582, snake_abs_exit_conv Rs +489, intraweek Rs +485, snake_abs_exit Rs +473, snake_abs_conv Rs +369, snake_abs Rs +362, intramonth Rs +338, oracle Rs +314, random_hold Rs +147, nifty_calls Rs +61, snake_anaconda Rs +8, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -23, benchmark_smallcap Rs -73, snake_viper_tick Rs -205, gold Rs -262, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.