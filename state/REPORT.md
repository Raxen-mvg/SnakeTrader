# Paper trading report

Updated 2026-11-06 13:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,279 | +8.14% | 0 | - | 237 |
| unified | 214,831 | +7.42% | 0 | - | 236 |
| snake_abs_exit_conv | 208,514 | +4.26% | 1 | 100% | 255 |
| snake_abs_exit | 208,423 | +4.21% | 1 | 100% | 260 |
| intraweek | 208,097 | +4.05% | 25 | 48% | 2,757 |
| intramonth | 207,126 | +3.56% | 0 | - | 235 |
| snake_abs | 205,501 | +2.75% | 1 | 100% | 255 |
| oracle | 205,441 | +2.72% | 0 | - | 233 |
| snake_abs_conv | 205,315 | +2.66% | 1 | 100% | 255 |
| random_hold | 203,455 | +1.73% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,007 | -2.00% | 3 | 33% | 702 |
| snake_anaconda | 195,854 | -2.07% | 3 | 33% | 374 |
| benchmark_smallcap | 195,291 | -2.35% | 0 | - | 237 |
| snake_viper_tick | 192,684 | -3.66% | 2 | 0% | 532 |
| gold | 190,753 | -4.62% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,886 (-6.56%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,509 | +1.17% |
| oracle | +1,369 | +0.67% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -822 | -0.40% |
| random_hold | -868 | -0.42% |
| unified | -1,153 | -0.53% |
| intraweek | -1,322 | -0.63% |
| benchmark_smallcap | -3,397 | -1.71% |
| gold | -3,469 | -1.79% |
| snake_abs | -6,188 | -2.92% |
| snake_abs_conv | -6,230 | -2.94% |
| snake_abs_exit | -6,236 | -2.90% |
| snake_abs_exit_conv | -6,290 | -2.93% |
| snake_anaconda | -6,626 | -3.27% |
| snake_viper_tick | -8,454 | -4.20% |
| snake_viper_wild | -8,649 | -4.23% |

Average per day so far: benchmark Rs +561, unified Rs +511, snake_abs_exit_conv Rs +327, snake_abs_exit Rs +324, intraweek Rs +279, intramonth Rs +246, snake_abs_conv Rs +204, snake_abs Rs +204, oracle Rs +188, random_hold Rs +119, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -173, benchmark_smallcap Rs -188, snake_viper_wild Rs -190, gold Rs -319, snake_viper_tick Rs -406, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.