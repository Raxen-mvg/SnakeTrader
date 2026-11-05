# Paper trading report

Updated 2026-11-05 13:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,437 | +8.22% | 0 | - | 236 |
| snake_abs_exit_conv | 214,209 | +7.10% | 1 | 100% | 255 |
| benchmark | 214,152 | +7.08% | 0 | - | 237 |
| snake_abs_exit | 213,972 | +6.99% | 1 | 100% | 260 |
| snake_abs | 211,090 | +5.54% | 1 | 100% | 255 |
| snake_abs_conv | 210,954 | +5.48% | 1 | 100% | 255 |
| intraweek | 210,602 | +5.30% | 25 | 48% | 2,757 |
| intramonth | 208,264 | +4.13% | 0 | - | 235 |
| snake_viper_wild | 206,506 | +3.25% | 3 | 33% | 702 |
| random_hold | 205,134 | +2.57% | 8 | 62% | 649 |
| oracle | 203,581 | +1.79% | 0 | - | 233 |
| snake_viper_tick | 202,959 | +1.48% | 2 | 0% | 532 |
| snake_anaconda | 202,355 | +1.18% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,125 | -0.44% | 0 | - | 237 |
| gold | 194,353 | -2.82% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,794 (-5.10%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,393 | +2.58% |
| gold | +2,959 | +1.55% |
| benchmark_smallcap | +2,455 | +1.25% |
| unified | +1,998 | +0.93% |
| random_hold | +1,825 | +0.90% |
| oracle | +1,789 | +0.89% |
| intramonth | +1,249 | +0.60% |
| intraweek | +904 | +0.43% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -804 | -0.38% |
| snake_abs_exit_conv | -806 | -0.38% |
| snake_abs | -813 | -0.38% |
| snake_abs_exit | -928 | -0.43% |
| snake_anaconda | -1,465 | -0.72% |
| snake_viper_tick | -2,441 | -1.19% |
| snake_viper_wild | -2,524 | -1.21% |

Average per day so far: unified Rs +587, snake_abs_exit_conv Rs +568, snake_abs_exit Rs +559, benchmark Rs +505, snake_abs_conv Rs +438, snake_abs Rs +427, intraweek Rs +379, snake_viper_wild Rs +325, intramonth Rs +295, random_hold Rs +183, snake_viper_tick Rs +174, oracle Rs +128, snake_anaconda Rs +102, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -202, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.