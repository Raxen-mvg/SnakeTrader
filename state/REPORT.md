# Paper trading report

Updated 2026-11-09 13:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,665 | +9.83% | 0 | - | 236 |
| benchmark | 216,822 | +8.41% | 0 | - | 237 |
| intraweek | 214,509 | +7.25% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,833 | +6.42% | 2 | 50% | 330 |
| snake_abs_exit | 212,414 | +6.21% | 2 | 50% | 308 |
| intramonth | 209,842 | +4.92% | 0 | - | 235 |
| snake_abs | 209,609 | +4.80% | 1 | 100% | 255 |
| snake_abs_conv | 209,444 | +4.72% | 1 | 100% | 255 |
| oracle | 209,417 | +4.71% | 0 | - | 233 |
| random_hold | 204,113 | +2.06% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,910 | -0.04% | 3 | 33% | 374 |
| snake_viper_wild | 199,822 | -0.09% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,329 | -0.83% | 0 | - | 237 |
| snake_viper_tick | 196,428 | -1.79% | 6 | 50% | 1,154 |
| gold | 192,183 | -3.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,152 (-4.92%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,411 | +2.12% |
| snake_abs_conv | +4,217 | +2.06% |
| snake_abs | +4,190 | +2.04% |
| intraweek | +4,147 | +1.97% |
| snake_abs_exit | +4,102 | +1.97% |
| snake_anaconda | +4,083 | +2.08% |
| unified | +4,056 | +1.88% |
| snake_viper_wild | +3,785 | +1.93% |
| snake_viper_tick | +3,718 | +1.93% |
| oracle | +3,590 | +1.74% |
| intramonth | +2,238 | +1.08% |
| benchmark_smallcap | +1,536 | +0.78% |
| gold | +1,134 | +0.59% |
| random_hold | +206 | +0.10% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -666 | -0.31% |

Average per day so far: unified Rs +656, benchmark Rs +561, intraweek Rs +484, snake_abs_exit_conv Rs +475, snake_abs_exit Rs +460, snake_abs_conv Rs +350, snake_abs Rs +343, intramonth Rs +328, oracle Rs +314, random_hold Rs +137, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -4, snake_viper_wild Rs -8, benchmark_smallcap Rs -64, snake_viper_tick Rs -188, gold Rs -261, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.