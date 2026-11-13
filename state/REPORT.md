# Paper trading report

Updated 2026-11-13 10:49 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,638 | +10.32% | 0 | - | 236 |
| benchmark | 220,150 | +10.07% | 0 | - | 237 |
| snake_abs_exit_conv | 217,262 | +8.63% | 2 | 50% | 345 |
| snake_abs_exit | 217,217 | +8.61% | 2 | 50% | 345 |
| intraweek | 215,997 | +8.00% | 30 | 53% | 3,302 |
| oracle | 213,768 | +6.88% | 0 | - | 233 |
| snake_abs | 213,118 | +6.56% | 1 | 100% | 255 |
| snake_abs_conv | 212,951 | +6.47% | 1 | 100% | 255 |
| intramonth | 211,393 | +5.70% | 0 | - | 235 |
| random_hold | 207,371 | +3.69% | 10 | 70% | 733 |
| snake_viper_wild | 206,619 | +3.31% | 14 | 50% | 2,496 |
| snake_anaconda | 205,092 | +2.55% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 203,085 | +1.54% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,522 | -7.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,173 (-3.91%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,339 | +0.62% |
| snake_viper_wild | +1,326 | +0.65% |
| snake_viper_tick | +1,303 | +0.65% |
| oracle | +653 | +0.31% |
| benchmark_smallcap | +493 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -59 | -0.03% |
| intramonth | -200 | -0.10% |
| snake_abs_exit | -226 | -0.10% |
| benchmark | -398 | -0.18% |
| random_hold | -683 | -0.33% |
| gold | -789 | -0.43% |
| snake_anaconda | -835 | -0.41% |
| snake_abs_exit_conv | -1,412 | -0.65% |
| snake_abs_conv | -2,584 | -1.20% |
| snake_abs | -2,593 | -1.20% |

Average per day so far: unified Rs +625, benchmark Rs +611, snake_abs_exit_conv Rs +575, snake_abs_exit Rs +574, intraweek Rs +485, snake_abs_conv Rs +432, snake_abs Rs +423, oracle Rs +417, intramonth Rs +345, snake_viper_wild Rs +265, random_hold Rs +223, snake_anaconda Rs +182, snake_viper_tick Rs +140, benchmark_smallcap Rs +128, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -469

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.