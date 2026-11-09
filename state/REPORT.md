# Paper trading report

Updated 2026-11-09 14:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,010 | +10.01% | 0 | - | 236 |
| benchmark | 218,054 | +9.03% | 0 | - | 237 |
| intraweek | 214,451 | +7.23% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,461 | +6.23% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,358 | +6.18% | 2 | 50% | 330 |
| intramonth | 210,243 | +5.12% | 0 | - | 235 |
| snake_abs | 209,823 | +4.91% | 1 | 100% | 255 |
| snake_abs_conv | 209,658 | +4.83% | 1 | 100% | 255 |
| oracle | 209,480 | +4.74% | 0 | - | 233 |
| random_hold | 204,529 | +2.26% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,932 | -0.03% | 3 | 33% | 374 |
| snake_viper_wild | 198,323 | -0.84% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,262 | -0.87% | 0 | - | 237 |
| snake_viper_tick | 194,956 | -2.52% | 6 | 50% | 1,154 |
| gold | 191,969 | -4.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,294 (-4.85%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,431 | +2.16% |
| snake_abs | +4,404 | +2.14% |
| unified | +4,401 | +2.04% |
| snake_abs_exit | +4,149 | +1.99% |
| snake_anaconda | +4,105 | +2.10% |
| intraweek | +4,089 | +1.94% |
| snake_abs_exit_conv | +3,936 | +1.89% |
| oracle | +3,653 | +1.77% |
| intramonth | +2,640 | +1.27% |
| snake_viper_wild | +2,286 | +1.17% |
| snake_viper_tick | +2,246 | +1.17% |
| benchmark_smallcap | +1,469 | +0.75% |
| gold | +921 | +0.48% |
| random_hold | +622 | +0.30% |
| benchmark | +566 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +667, benchmark Rs +602, intraweek Rs +482, snake_abs_exit Rs +462, snake_abs_exit_conv Rs +458, snake_abs_conv Rs +358, snake_abs Rs +351, intramonth Rs +341, oracle Rs +316, random_hold Rs +151, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -3, benchmark_smallcap Rs -67, snake_viper_wild Rs -76, snake_viper_tick Rs -265, gold Rs -268, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.