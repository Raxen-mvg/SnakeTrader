# Paper trading report

Updated 2026-11-23 12:06 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,163 | +12.08% | 0 | - | 236 |
| benchmark | 222,781 | +11.39% | 0 | - | 237 |
| intraweek | 213,044 | +6.52% | 40 | 55% | 4,400 |
| intramonth | 212,196 | +6.10% | 0 | - | 235 |
| oracle | 211,709 | +5.85% | 0 | - | 233 |
| random_hold | 209,815 | +4.91% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,271 | +3.64% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,937 | +2.97% | 2 | 50% | 345 |
| snake_abs | 204,922 | +2.46% | 1 | 100% | 255 |
| snake_abs_conv | 204,753 | +2.38% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,513 | +0.76% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,473 | -0.26% | 0 | - | 237 |
| snake_anaconda | 198,241 | -0.88% | 3 | 33% | 374 |
| snake_viper_tick | 198,073 | -0.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,939 | -15.03% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,425 (-4.79%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,891 | +1.12% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -680 | -0.33% |
| oracle | -770 | -0.36% |
| random_hold | -944 | -0.45% |
| snake_abs | -998 | -0.48% |
| snake_abs_conv | -1,030 | -0.50% |
| snake_abs_exit | -1,291 | -0.62% |
| snake_viper_tick | -1,298 | -0.65% |
| snake_viper_wild | -1,316 | -0.65% |
| benchmark_smallcap | -1,435 | -0.71% |
| snake_anaconda | -1,664 | -0.83% |
| unified | -2,018 | -0.89% |
| benchmark | -2,356 | -1.05% |
| intraweek | -2,668 | -1.24% |
| intramonth | -2,808 | -1.31% |

Average per day so far: unified Rs +620, benchmark Rs +584, intraweek Rs +334, intramonth Rs +313, oracle Rs +300, random_hold Rs +252, snake_abs_exit Rs +202, snake_abs_exit_conv Rs +165, snake_abs Rs +133, snake_abs_conv Rs +132, snake_viper_wild Rs +49, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_anaconda Rs -52, snake_viper_tick Rs -69, snake_nonews Rs -300, snake Rs -320, gold Rs -771

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.