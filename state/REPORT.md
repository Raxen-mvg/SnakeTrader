# Paper trading report

Updated 2026-11-05 13:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,562 | +8.28% | 0 | - | 236 |
| snake_abs_exit_conv | 214,309 | +7.16% | 1 | 100% | 255 |
| snake_abs_exit | 214,062 | +7.03% | 1 | 100% | 260 |
| benchmark | 214,030 | +7.01% | 0 | - | 237 |
| snake_abs | 211,187 | +5.59% | 1 | 100% | 255 |
| snake_abs_conv | 211,054 | +5.53% | 1 | 100% | 255 |
| intraweek | 210,324 | +5.16% | 25 | 48% | 2,757 |
| intramonth | 208,413 | +4.21% | 0 | - | 235 |
| snake_viper_wild | 206,387 | +3.19% | 3 | 33% | 702 |
| random_hold | 205,236 | +2.62% | 8 | 62% | 649 |
| oracle | 203,696 | +1.85% | 0 | - | 233 |
| snake_viper_tick | 202,840 | +1.42% | 2 | 0% | 532 |
| snake_anaconda | 202,498 | +1.25% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| gold | 194,221 | -2.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,783 (-5.11%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,271 | +2.52% |
| gold | +2,828 | +1.48% |
| benchmark_smallcap | +2,545 | +1.29% |
| unified | +2,123 | +0.99% |
| random_hold | +1,927 | +0.95% |
| oracle | +1,904 | +0.94% |
| intramonth | +1,397 | +0.68% |
| intraweek | +626 | +0.30% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -704 | -0.33% |
| snake_abs_exit_conv | -706 | -0.33% |
| snake_abs | -716 | -0.34% |
| snake_abs_exit | -838 | -0.39% |
| snake_anaconda | -1,322 | -0.65% |
| snake_viper_tick | -2,561 | -1.25% |
| snake_viper_wild | -2,643 | -1.26% |

Average per day so far: unified Rs +592, snake_abs_exit_conv Rs +572, snake_abs_exit Rs +562, benchmark Rs +501, snake_abs_conv Rs +442, snake_abs Rs +430, intraweek Rs +369, snake_viper_wild Rs +319, intramonth Rs +300, random_hold Rs +187, snake_viper_tick Rs +167, oracle Rs +132, snake_anaconda Rs +109, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -206, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.