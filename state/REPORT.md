# Paper trading report

Updated 2026-11-09 10:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,505 | +10.25% | 0 | - | 236 |
| benchmark | 217,465 | +8.73% | 0 | - | 237 |
| intraweek | 215,604 | +7.80% | 30 | 53% | 3,302 |
| snake_abs_exit | 211,105 | +5.55% | 2 | 50% | 308 |
| snake_abs_exit_conv | 211,075 | +5.54% | 2 | 50% | 330 |
| intramonth | 210,535 | +5.27% | 0 | - | 235 |
| oracle | 209,558 | +4.78% | 0 | - | 233 |
| snake_abs | 208,789 | +4.39% | 1 | 100% | 255 |
| snake_abs_conv | 208,607 | +4.30% | 1 | 100% | 255 |
| random_hold | 204,095 | +2.05% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,657 | -0.67% | 3 | 33% | 374 |
| benchmark_smallcap | 198,340 | -0.83% | 0 | - | 237 |
| snake_viper_wild | 198,022 | -0.99% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,659 | -2.67% | 6 | 50% | 1,154 |
| gold | 193,268 | -3.37% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,464 (-4.77%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,241 | +2.49% |
| unified | +4,896 | +2.27% |
| oracle | +3,731 | +1.81% |
| snake_abs_conv | +3,380 | +1.65% |
| snake_abs | +3,369 | +1.64% |
| intramonth | +2,932 | +1.41% |
| snake_anaconda | +2,830 | +1.45% |
| snake_abs_exit | +2,793 | +1.34% |
| snake_abs_exit_conv | +2,653 | +1.27% |
| gold | +2,219 | +1.16% |
| snake_viper_wild | +1,985 | +1.01% |
| snake_viper_tick | +1,949 | +1.01% |
| benchmark_smallcap | +1,547 | +0.79% |
| random_hold | +189 | +0.09% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -23 | -0.01% |

Average per day so far: unified Rs +684, benchmark Rs +582, intraweek Rs +520, snake_abs_exit Rs +411, snake_abs_exit_conv Rs +410, intramonth Rs +351, snake_abs_conv Rs +319, oracle Rs +319, snake_abs Rs +314, random_hold Rs +137, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -54, benchmark_smallcap Rs -64, snake_viper_wild Rs -90, gold Rs -224, snake_viper_tick Rs -281, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.