# Paper trading report

Updated 2026-11-11 15:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,511 | +9.76% | 0 | - | 236 |
| benchmark | 219,109 | +9.55% | 0 | - | 237 |
| snake_abs_exit_conv | 216,886 | +8.44% | 2 | 50% | 345 |
| snake_abs_exit | 215,871 | +7.93% | 2 | 50% | 345 |
| snake_abs | 213,541 | +6.77% | 1 | 100% | 255 |
| snake_abs_conv | 213,371 | +6.69% | 1 | 100% | 255 |
| intraweek | 212,832 | +6.42% | 30 | 53% | 3,302 |
| oracle | 211,557 | +5.78% | 0 | - | 233 |
| intramonth | 210,842 | +5.42% | 0 | - | 235 |
| random_hold | 206,993 | +3.50% | 9 | 67% | 709 |
| snake_viper_wild | 206,400 | +3.20% | 10 | 50% | 1,825 |
| snake_anaconda | 203,883 | +1.94% | 3 | 33% | 374 |
| snake_viper_tick | 202,873 | +1.44% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,076 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,602 | -5.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,795 (-4.60%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,970 | +4.54% |
| snake_viper_tick | +8,797 | +4.53% |
| snake_abs_exit_conv | +4,977 | +2.35% |
| snake_anaconda | +4,416 | +2.21% |
| snake_abs | +3,894 | +1.86% |
| snake_abs_conv | +3,894 | +1.86% |
| snake_abs_exit | +3,887 | +1.83% |
| benchmark_smallcap | +2,903 | +1.47% |
| random_hold | +2,032 | +0.99% |
| oracle | +1,639 | +0.78% |
| benchmark | +1,017 | +0.47% |
| intramonth | +233 | +0.11% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -236 | -0.11% |
| intraweek | -1,710 | -0.80% |
| gold | -2,532 | -1.32% |

Average per day so far: unified Rs +629, benchmark Rs +616, snake_abs_exit_conv Rs +603, snake_abs_exit Rs +567, snake_abs_conv Rs +478, snake_abs Rs +467, intraweek Rs +414, oracle Rs +373, intramonth Rs +350, snake_viper_wild Rs +278, random_hold Rs +226, snake_anaconda Rs +149, snake_viper_tick Rs +144, nifty_calls Rs +59, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -335, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.