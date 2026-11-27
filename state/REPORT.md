# Paper trading report

Updated 2026-11-27 13:22 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,998 | +12.00% | 0 | - | 237 |
| unified | 223,251 | +11.62% | 0 | - | 236 |
| oracle | 211,833 | +5.92% | 0 | - | 233 |
| random_hold | 210,859 | +5.43% | 13 | 69% | 1,037 |
| intramonth | 210,840 | +5.42% | 0 | - | 235 |
| intraweek | 208,398 | +4.20% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,316 | +2.66% | 2 | 50% | 345 |
| snake_abs_exit | 204,528 | +2.26% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,333 | +0.67% | 0 | - | 237 |
| snake_abs | 200,228 | +0.11% | 1 | 100% | 255 |
| snake_abs_conv | 200,046 | +0.02% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,598 | -3.20% | 3 | 33% | 374 |
| snake_viper_wild | 191,967 | -4.02% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,708 | -5.65% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,890 | -15.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,850 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,919 | +2.46% |
| gold | +3,896 | +2.35% |
| snake_abs_exit | +3,451 | +1.72% |
| random_hold | +2,265 | +1.09% |
| snake_abs_conv | +1,679 | +0.85% |
| snake_abs | +1,676 | +0.84% |
| intraweek | +1,350 | +0.65% |
| snake_anaconda | +1,301 | +0.68% |
| benchmark_smallcap | +493 | +0.25% |
| intramonth | +306 | +0.15% |
| unified | +172 | +0.08% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -233 | -0.12% |
| snake_viper_wild | -238 | -0.12% |
| oracle | -402 | -0.19% |
| benchmark | -1,989 | -0.88% |

Average per day so far: benchmark Rs +571, unified Rs +554, oracle Rs +282, random_hold Rs +259, intramonth Rs +258, intraweek Rs +200, snake_abs_exit_conv Rs +136, snake_abs_exit Rs +116, nifty_calls Rs +44, benchmark_smallcap Rs +35, snake_abs Rs +6, snake_abs_conv Rs +1, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -173, snake_viper_wild Rs -236, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -364, gold Rs -717

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.