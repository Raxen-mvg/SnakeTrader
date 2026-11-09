# Paper trading report

Updated 2026-11-09 11:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,374 | +10.19% | 0 | - | 236 |
| benchmark | 216,853 | +8.43% | 0 | - | 237 |
| intraweek | 215,512 | +7.76% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 211,889 | +5.95% | 2 | 50% | 330 |
| snake_abs_exit | 211,839 | +5.92% | 2 | 50% | 308 |
| intramonth | 210,631 | +5.32% | 0 | - | 235 |
| snake_abs | 209,619 | +4.81% | 1 | 100% | 255 |
| oracle | 209,568 | +4.78% | 0 | - | 233 |
| snake_abs_conv | 209,444 | +4.72% | 1 | 100% | 255 |
| random_hold | 204,273 | +2.14% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,334 | -0.33% | 3 | 33% | 374 |
| benchmark_smallcap | 198,318 | -0.84% | 0 | - | 237 |
| snake_viper_wild | 198,022 | -0.99% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,658 | -2.67% | 6 | 50% | 1,154 |
| gold | 193,103 | -3.45% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,560 (-4.72%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,149 | +2.45% |
| unified | +4,764 | +2.21% |
| snake_abs_conv | +4,217 | +2.06% |
| snake_abs | +4,200 | +2.04% |
| oracle | +3,741 | +1.82% |
| snake_abs_exit | +3,527 | +1.69% |
| snake_anaconda | +3,507 | +1.79% |
| snake_abs_exit_conv | +3,468 | +1.66% |
| intramonth | +3,028 | +1.46% |
| gold | +2,055 | +1.08% |
| snake_viper_wild | +1,985 | +1.01% |
| snake_viper_tick | +1,949 | +1.01% |
| benchmark_smallcap | +1,525 | +0.78% |
| random_hold | +367 | +0.18% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -635 | -0.29% |

Average per day so far: unified Rs +679, benchmark Rs +562, intraweek Rs +517, snake_abs_exit_conv Rs +440, snake_abs_exit Rs +438, intramonth Rs +354, snake_abs_conv Rs +350, snake_abs Rs +344, oracle Rs +319, random_hold Rs +142, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -27, benchmark_smallcap Rs -65, snake_viper_wild Rs -90, gold Rs -230, snake_viper_tick Rs -281, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.