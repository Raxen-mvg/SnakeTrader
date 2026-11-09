# Paper trading report

Updated 2026-11-09 10:53 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,196 | +10.10% | 0 | - | 236 |
| benchmark | 217,044 | +8.52% | 0 | - | 237 |
| intraweek | 215,893 | +7.95% | 30 | 53% | 3,302 |
| snake_abs_exit | 211,845 | +5.92% | 2 | 50% | 308 |
| snake_abs_exit_conv | 211,839 | +5.92% | 2 | 50% | 330 |
| intramonth | 210,501 | +5.25% | 0 | - | 235 |
| oracle | 209,812 | +4.91% | 0 | - | 233 |
| snake_abs | 209,664 | +4.83% | 1 | 100% | 255 |
| snake_abs_conv | 209,490 | +4.75% | 1 | 100% | 255 |
| random_hold | 204,130 | +2.06% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,384 | -0.31% | 3 | 33% | 374 |
| benchmark_smallcap | 198,307 | -0.85% | 0 | - | 237 |
| snake_viper_wild | 197,157 | -1.42% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,806 | -3.10% | 6 | 50% | 1,154 |
| gold | 193,054 | -3.47% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,608 (-4.70%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,531 | +2.63% |
| unified | +4,587 | +2.13% |
| snake_abs_conv | +4,263 | +2.08% |
| snake_abs | +4,245 | +2.07% |
| oracle | +3,985 | +1.94% |
| snake_anaconda | +3,557 | +1.82% |
| snake_abs_exit | +3,533 | +1.70% |
| snake_abs_exit_conv | +3,417 | +1.64% |
| intramonth | +2,898 | +1.40% |
| gold | +2,006 | +1.05% |
| benchmark_smallcap | +1,513 | +0.77% |
| snake_viper_wild | +1,120 | +0.57% |
| snake_viper_tick | +1,096 | +0.57% |
| random_hold | +224 | +0.11% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -444 | -0.20% |

Average per day so far: unified Rs +673, benchmark Rs +568, intraweek Rs +530, snake_abs_exit Rs +439, snake_abs_exit_conv Rs +438, snake_abs_conv Rs +351, intramonth Rs +350, snake_abs Rs +345, oracle Rs +327, random_hold Rs +138, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -25, benchmark_smallcap Rs -65, snake_viper_wild Rs -129, gold Rs -232, snake_viper_tick Rs -326, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.