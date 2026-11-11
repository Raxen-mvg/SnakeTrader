# Paper trading report

Updated 2026-11-11 15:21 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,697 | +9.85% | 0 | - | 236 |
| benchmark | 219,347 | +9.67% | 0 | - | 237 |
| snake_abs_exit_conv | 217,172 | +8.59% | 2 | 50% | 345 |
| snake_abs_exit | 216,084 | +8.04% | 2 | 50% | 345 |
| intraweek | 214,103 | +7.05% | 30 | 53% | 3,302 |
| snake_abs | 213,639 | +6.82% | 1 | 100% | 255 |
| snake_abs_conv | 213,471 | +6.74% | 1 | 100% | 255 |
| oracle | 212,705 | +6.35% | 0 | - | 233 |
| intramonth | 211,041 | +5.52% | 0 | - | 235 |
| random_hold | 207,345 | +3.67% | 9 | 67% | 709 |
| snake_viper_wild | 206,379 | +3.19% | 10 | 50% | 1,825 |
| snake_anaconda | 204,088 | +2.04% | 3 | 33% | 374 |
| snake_viper_tick | 202,853 | +1.43% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,773 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,618 | -5.19% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,307 (-4.35%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,949 | +4.53% |
| snake_viper_tick | +8,777 | +4.52% |
| snake_abs_exit_conv | +5,263 | +2.48% |
| snake_anaconda | +4,621 | +2.32% |
| snake_abs_exit | +4,100 | +1.93% |
| snake_abs_conv | +3,994 | +1.91% |
| snake_abs | +3,992 | +1.90% |
| oracle | +2,787 | +1.33% |
| benchmark_smallcap | +2,601 | +1.31% |
| random_hold | +2,384 | +1.16% |
| benchmark | +1,255 | +0.57% |
| intramonth | +431 | +0.20% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -50 | -0.02% |
| intraweek | -439 | -0.20% |
| gold | -2,515 | -1.31% |

Average per day so far: unified Rs +635, benchmark Rs +624, snake_abs_exit_conv Rs +613, snake_abs_exit Rs +574, snake_abs_conv Rs +481, snake_abs Rs +470, intraweek Rs +455, oracle Rs +410, intramonth Rs +356, snake_viper_wild Rs +277, random_hold Rs +237, snake_anaconda Rs +157, snake_viper_tick Rs +143, nifty_calls Rs +59, benchmark_smallcap Rs +29, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -335, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.