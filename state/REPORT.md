# Paper trading report

Updated 2026-11-27 13:19 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,082 | +12.04% | 0 | - | 237 |
| unified | 223,355 | +11.68% | 0 | - | 236 |
| oracle | 211,842 | +5.92% | 0 | - | 233 |
| intramonth | 210,931 | +5.47% | 0 | - | 235 |
| random_hold | 210,810 | +5.41% | 13 | 69% | 1,037 |
| intraweek | 208,547 | +4.27% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,217 | +2.61% | 2 | 50% | 345 |
| snake_abs_exit | 204,429 | +2.21% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,333 | +0.67% | 0 | - | 237 |
| snake_abs | 200,175 | +0.09% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,993 | -0.00% | 1 | 100% | 255 |
| snake_anaconda | 193,544 | -3.23% | 3 | 33% | 374 |
| snake_viper_wild | 191,895 | -4.05% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,638 | -5.68% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,676 | -15.16% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,890 (-5.55%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,820 | +2.40% |
| gold | +3,683 | +2.22% |
| snake_abs_exit | +3,352 | +1.67% |
| random_hold | +2,216 | +1.06% |
| snake_abs_conv | +1,626 | +0.82% |
| snake_abs | +1,623 | +0.82% |
| intraweek | +1,499 | +0.72% |
| snake_anaconda | +1,248 | +0.65% |
| benchmark_smallcap | +493 | +0.25% |
| intramonth | +398 | +0.19% |
| unified | +276 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -303 | -0.16% |
| snake_viper_wild | -310 | -0.16% |
| oracle | -394 | -0.19% |
| benchmark | -1,905 | -0.84% |

Average per day so far: benchmark Rs +573, unified Rs +556, oracle Rs +282, intramonth Rs +260, random_hold Rs +257, intraweek Rs +204, snake_abs_exit_conv Rs +134, snake_abs_exit Rs +114, nifty_calls Rs +44, benchmark_smallcap Rs +35, snake_abs Rs +4, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_conv Rs -0, snake_anaconda Rs -174, snake_viper_wild Rs -238, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -367, gold Rs -722

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.