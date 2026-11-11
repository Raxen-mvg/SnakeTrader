# Paper trading report

Updated 2026-11-11 13:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,662 | +10.33% | 0 | - | 237 |
| unified | 220,509 | +10.26% | 0 | - | 236 |
| snake_abs_exit_conv | 218,041 | +9.02% | 2 | 50% | 345 |
| snake_abs_exit | 216,908 | +8.45% | 2 | 50% | 345 |
| snake_abs | 214,556 | +7.28% | 1 | 100% | 255 |
| snake_abs_conv | 214,402 | +7.20% | 1 | 100% | 255 |
| intraweek | 213,679 | +6.84% | 30 | 53% | 3,302 |
| oracle | 211,970 | +5.99% | 0 | - | 233 |
| intramonth | 211,437 | +5.72% | 0 | - | 235 |
| random_hold | 206,998 | +3.50% | 9 | 67% | 709 |
| snake_anaconda | 204,848 | +2.42% | 3 | 33% | 374 |
| snake_viper_wild | 204,567 | +2.28% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,434 | +0.72% | 0 | - | 237 |
| snake_viper_tick | 201,079 | +0.54% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,062 | -4.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,393 (-4.30%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,137 | +3.62% |
| snake_viper_tick | +7,002 | +3.61% |
| snake_abs_exit_conv | +6,132 | +2.89% |
| snake_anaconda | +5,382 | +2.70% |
| snake_abs_conv | +4,924 | +2.35% |
| snake_abs_exit | +4,924 | +2.32% |
| snake_abs | +4,909 | +2.34% |
| benchmark_smallcap | +3,262 | +1.65% |
| benchmark | +2,570 | +1.18% |
| oracle | +2,051 | +0.98% |
| random_hold | +2,037 | +0.99% |
| intramonth | +828 | +0.39% |
| unified | +762 | +0.35% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -863 | -0.40% |
| gold | -2,071 | -1.08% |

Average per day so far: benchmark Rs +667, unified Rs +662, snake_abs_exit_conv Rs +644, snake_abs_exit Rs +604, snake_abs_conv Rs +514, snake_abs Rs +502, intraweek Rs +441, oracle Rs +386, intramonth Rs +369, random_hold Rs +226, snake_viper_wild Rs +199, snake_anaconda Rs +186, nifty_calls Rs +59, snake_viper_tick Rs +54, benchmark_smallcap Rs +53, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -321, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.