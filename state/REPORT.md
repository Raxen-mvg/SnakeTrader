# Paper trading report

Updated 2026-11-09 15:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,196 | +9.60% | 0 | - | 236 |
| benchmark | 218,084 | +9.04% | 0 | - | 237 |
| intraweek | 214,580 | +7.29% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,413 | +6.21% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,340 | +6.17% | 2 | 50% | 330 |
| intramonth | 209,787 | +4.89% | 0 | - | 235 |
| snake_abs | 209,675 | +4.84% | 1 | 100% | 255 |
| snake_abs_conv | 209,509 | +4.75% | 1 | 100% | 255 |
| oracle | 209,360 | +4.68% | 0 | - | 233 |
| random_hold | 204,456 | +2.23% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,911 | -0.04% | 3 | 33% | 374 |
| benchmark_smallcap | 198,307 | -0.85% | 0 | - | 237 |
| snake_viper_wild | 198,066 | -0.97% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,703 | -2.65% | 6 | 50% | 1,154 |
| gold | 191,903 | -4.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,085 (-4.96%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,282 | +2.09% |
| snake_abs | +4,255 | +2.07% |
| intraweek | +4,217 | +2.00% |
| snake_abs_exit | +4,101 | +1.97% |
| snake_anaconda | +4,083 | +2.08% |
| snake_abs_exit_conv | +3,918 | +1.88% |
| unified | +3,587 | +1.66% |
| oracle | +3,533 | +1.72% |
| intramonth | +2,184 | +1.05% |
| snake_viper_wild | +2,029 | +1.03% |
| snake_viper_tick | +1,993 | +1.03% |
| benchmark_smallcap | +1,513 | +0.77% |
| gold | +855 | +0.45% |
| benchmark | +597 | +0.27% |
| random_hold | +550 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +640, benchmark Rs +603, intraweek Rs +486, snake_abs_exit Rs +460, snake_abs_exit_conv Rs +457, snake_abs_conv Rs +352, snake_abs Rs +346, intramonth Rs +326, oracle Rs +312, random_hold Rs +149, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -4, benchmark_smallcap Rs -65, snake_viper_wild Rs -88, gold Rs -270, snake_viper_tick Rs -279, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.