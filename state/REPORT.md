# Paper trading report

Updated 2026-11-09 11:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,426 | +10.21% | 0 | - | 236 |
| benchmark | 217,266 | +8.63% | 0 | - | 237 |
| intraweek | 214,643 | +7.32% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,089 | +6.04% | 2 | 50% | 330 |
| snake_abs_exit | 211,922 | +5.96% | 2 | 50% | 308 |
| intramonth | 210,409 | +5.21% | 0 | - | 235 |
| snake_abs | 209,685 | +4.84% | 1 | 100% | 255 |
| snake_abs_conv | 209,510 | +4.75% | 1 | 100% | 255 |
| oracle | 209,207 | +4.60% | 0 | - | 233 |
| random_hold | 204,258 | +2.13% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,362 | -0.32% | 3 | 33% | 374 |
| snake_viper_wild | 198,455 | -0.77% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,329 | -0.83% | 0 | - | 237 |
| snake_viper_tick | 195,084 | -2.46% | 6 | 50% | 1,154 |
| gold | 193,087 | -3.46% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,335 (-4.83%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,816 | +2.23% |
| snake_abs_conv | +4,282 | +2.09% |
| intraweek | +4,280 | +2.04% |
| snake_abs | +4,266 | +2.08% |
| snake_abs_exit_conv | +3,667 | +1.76% |
| snake_abs_exit | +3,610 | +1.73% |
| snake_anaconda | +3,535 | +1.80% |
| oracle | +3,380 | +1.64% |
| intramonth | +2,806 | +1.35% |
| snake_viper_wild | +2,417 | +1.23% |
| snake_viper_tick | +2,374 | +1.23% |
| gold | +2,039 | +1.07% |
| benchmark_smallcap | +1,536 | +0.78% |
| random_hold | +351 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -222 | -0.10% |

Average per day so far: unified Rs +681, benchmark Rs +576, intraweek Rs +488, snake_abs_exit_conv Rs +448, snake_abs_exit Rs +442, snake_abs_conv Rs +352, intramonth Rs +347, snake_abs Rs +346, oracle Rs +307, random_hold Rs +142, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -26, benchmark_smallcap Rs -64, snake_viper_wild Rs -70, gold Rs -230, snake_viper_tick Rs -259, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.