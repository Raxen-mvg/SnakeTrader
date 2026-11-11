# Paper trading report

Updated 2026-11-11 14:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,365 | +10.18% | 0 | - | 236 |
| benchmark | 220,027 | +10.01% | 0 | - | 237 |
| snake_abs_exit_conv | 217,369 | +8.68% | 2 | 50% | 345 |
| snake_abs_exit | 216,594 | +8.30% | 2 | 50% | 345 |
| snake_abs | 214,332 | +7.17% | 1 | 100% | 255 |
| snake_abs_conv | 214,170 | +7.08% | 1 | 100% | 255 |
| intraweek | 213,490 | +6.75% | 30 | 53% | 3,302 |
| oracle | 211,786 | +5.89% | 0 | - | 233 |
| intramonth | 211,371 | +5.68% | 0 | - | 235 |
| random_hold | 207,091 | +3.55% | 9 | 67% | 709 |
| snake_viper_wild | 206,084 | +3.04% | 10 | 50% | 1,825 |
| snake_anaconda | 204,377 | +2.19% | 3 | 33% | 374 |
| snake_viper_tick | 202,564 | +1.28% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,244 | +0.62% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,536 | -5.23% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,266 (-4.37%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,654 | +4.38% |
| snake_viper_tick | +8,487 | +4.37% |
| snake_abs_exit_conv | +5,460 | +2.58% |
| snake_anaconda | +4,911 | +2.46% |
| snake_abs_conv | +4,693 | +2.24% |
| snake_abs | +4,685 | +2.23% |
| snake_abs_exit | +4,610 | +2.17% |
| benchmark_smallcap | +3,072 | +1.55% |
| random_hold | +2,131 | +1.04% |
| benchmark | +1,935 | +0.89% |
| oracle | +1,867 | +0.89% |
| intramonth | +762 | +0.36% |
| unified | +618 | +0.28% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,051 | -0.49% |
| gold | -2,598 | -1.35% |

Average per day so far: unified Rs +657, benchmark Rs +646, snake_abs_exit_conv Rs +620, snake_abs_exit Rs +593, snake_abs_conv Rs +506, snake_abs Rs +494, intraweek Rs +435, oracle Rs +380, intramonth Rs +367, snake_viper_wild Rs +265, random_hold Rs +229, snake_anaconda Rs +168, snake_viper_tick Rs +128, nifty_calls Rs +59, benchmark_smallcap Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -338, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.