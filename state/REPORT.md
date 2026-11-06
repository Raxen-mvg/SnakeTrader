# Paper trading report

Updated 2026-11-06 14:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,264 | +8.13% | 0 | - | 237 |
| unified | 215,045 | +7.52% | 0 | - | 236 |
| snake_abs_exit_conv | 208,410 | +4.21% | 1 | 100% | 255 |
| snake_abs_exit | 208,312 | +4.16% | 1 | 100% | 260 |
| intraweek | 207,896 | +3.95% | 25 | 48% | 2,757 |
| intramonth | 207,312 | +3.66% | 0 | - | 235 |
| oracle | 205,467 | +2.73% | 0 | - | 233 |
| snake_abs | 205,394 | +2.70% | 1 | 100% | 255 |
| snake_abs_conv | 205,210 | +2.60% | 1 | 100% | 255 |
| random_hold | 203,374 | +1.69% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,249 | -1.88% | 3 | 33% | 702 |
| snake_anaconda | 195,756 | -2.12% | 3 | 33% | 374 |
| benchmark_smallcap | 195,280 | -2.36% | 0 | - | 237 |
| snake_viper_tick | 192,923 | -3.54% | 2 | 0% | 532 |
| gold | 190,851 | -4.57% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,892 (-6.55%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,494 | +1.17% |
| oracle | +1,395 | +0.68% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -636 | -0.31% |
| unified | -938 | -0.43% |
| random_hold | -949 | -0.47% |
| intraweek | -1,522 | -0.73% |
| gold | -3,370 | -1.74% |
| benchmark_smallcap | -3,408 | -1.72% |
| snake_abs | -6,294 | -2.97% |
| snake_abs_conv | -6,335 | -3.00% |
| snake_abs_exit | -6,347 | -2.96% |
| snake_abs_exit_conv | -6,394 | -2.98% |
| snake_anaconda | -6,724 | -3.32% |
| snake_viper_tick | -8,215 | -4.08% |
| snake_viper_wild | -8,407 | -4.11% |

Average per day so far: benchmark Rs +561, unified Rs +519, snake_abs_exit_conv Rs +323, snake_abs_exit Rs +320, intraweek Rs +272, intramonth Rs +252, snake_abs_conv Rs +200, snake_abs Rs +200, oracle Rs +189, random_hold Rs +116, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -177, snake_viper_wild Rs -179, benchmark_smallcap Rs -189, gold Rs -315, snake_viper_tick Rs -393, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.