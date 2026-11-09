# Paper trading report

Updated 2026-11-09 12:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,001 | +10.00% | 0 | - | 236 |
| benchmark | 216,998 | +8.50% | 0 | - | 237 |
| intraweek | 214,919 | +7.46% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,312 | +6.16% | 2 | 50% | 330 |
| snake_abs_exit | 212,017 | +6.01% | 2 | 50% | 308 |
| intramonth | 210,075 | +5.04% | 0 | - | 235 |
| snake_abs | 209,807 | +4.90% | 1 | 100% | 255 |
| snake_abs_conv | 209,632 | +4.82% | 1 | 100% | 255 |
| oracle | 209,544 | +4.77% | 0 | - | 233 |
| random_hold | 204,342 | +2.17% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,463 | -0.27% | 3 | 33% | 374 |
| snake_viper_wild | 199,181 | -0.41% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,520 | -0.74% | 0 | - | 237 |
| snake_viper_tick | 195,799 | -2.10% | 6 | 50% | 1,154 |
| gold | 192,364 | -3.82% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,337 (-4.83%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,557 | +2.17% |
| snake_abs_conv | +4,404 | +2.15% |
| unified | +4,391 | +2.04% |
| snake_abs | +4,387 | +2.14% |
| snake_abs_exit_conv | +3,890 | +1.87% |
| oracle | +3,717 | +1.81% |
| snake_abs_exit | +3,705 | +1.78% |
| snake_anaconda | +3,636 | +1.86% |
| snake_viper_wild | +3,144 | +1.60% |
| snake_viper_tick | +3,089 | +1.60% |
| intramonth | +2,472 | +1.19% |
| benchmark_smallcap | +1,726 | +0.88% |
| gold | +1,315 | +0.69% |
| random_hold | +436 | +0.21% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -490 | -0.23% |

Average per day so far: unified Rs +667, benchmark Rs +567, intraweek Rs +497, snake_abs_exit_conv Rs +456, snake_abs_exit Rs +445, snake_abs_conv Rs +357, snake_abs Rs +350, intramonth Rs +336, oracle Rs +318, random_hold Rs +145, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -21, snake_viper_wild Rs -37, benchmark_smallcap Rs -57, snake_viper_tick Rs -221, gold Rs -255, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.