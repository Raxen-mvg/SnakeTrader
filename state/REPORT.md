# Paper trading report

Updated 2026-11-09 10:32 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,043 | +10.02% | 0 | - | 236 |
| benchmark | 217,319 | +8.66% | 0 | - | 237 |
| intraweek | 216,967 | +8.48% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,138 | +6.07% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,127 | +6.06% | 2 | 50% | 330 |
| snake_abs | 210,061 | +5.03% | 1 | 100% | 255 |
| intramonth | 210,001 | +5.00% | 0 | - | 235 |
| snake_abs_conv | 209,884 | +4.94% | 1 | 100% | 255 |
| oracle | 209,419 | +4.71% | 0 | - | 233 |
| random_hold | 204,010 | +2.00% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,596 | -0.20% | 3 | 33% | 374 |
| benchmark_smallcap | 198,531 | -0.73% | 0 | - | 237 |
| snake_viper_wild | 197,473 | -1.26% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,119 | -2.94% | 6 | 50% | 1,154 |
| gold | 193,005 | -3.50% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,710 (-4.64%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +6,605 | +3.14% |
| snake_abs_conv | +4,657 | +2.27% |
| snake_abs | +4,641 | +2.26% |
| unified | +4,434 | +2.06% |
| snake_abs_exit | +3,826 | +1.84% |
| snake_anaconda | +3,769 | +1.93% |
| snake_abs_exit_conv | +3,705 | +1.78% |
| oracle | +3,592 | +1.75% |
| intramonth | +2,398 | +1.16% |
| gold | +1,956 | +1.02% |
| benchmark_smallcap | +1,738 | +0.88% |
| snake_viper_wild | +1,436 | +0.73% |
| snake_viper_tick | +1,409 | +0.73% |
| random_hold | +103 | +0.05% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -168 | -0.08% |

Average per day so far: unified Rs +668, benchmark Rs +577, intraweek Rs +566, snake_abs_exit Rs +450, snake_abs_exit_conv Rs +449, snake_abs_conv Rs +366, snake_abs Rs +359, intramonth Rs +333, oracle Rs +314, random_hold Rs +134, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -16, benchmark_smallcap Rs -57, snake_viper_wild Rs -115, gold Rs -233, snake_viper_tick Rs -310, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.