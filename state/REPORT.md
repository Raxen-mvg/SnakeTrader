# Paper trading report

Updated 2026-11-26 15:28 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,849 | +12.93% | 0 | - | 237 |
| unified | 223,052 | +11.53% | 0 | - | 236 |
| oracle | 212,039 | +6.02% | 0 | - | 233 |
| intramonth | 210,530 | +5.26% | 0 | - | 235 |
| random_hold | 208,684 | +4.34% | 13 | 69% | 1,037 |
| intraweek | 207,046 | +3.52% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,181 | +0.59% | 2 | 50% | 345 |
| benchmark_smallcap | 200,874 | +0.44% | 0 | - | 237 |
| snake_abs_exit_conv | 200,396 | +0.20% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,598 | -0.70% | 1 | 100% | 255 |
| snake_abs_conv | 198,411 | -0.80% | 1 | 100% | 255 |
| snake_viper_wild | 192,417 | -3.79% | 16 | 50% | 2,827 |
| snake_anaconda | 192,305 | -3.85% | 3 | 33% | 374 |
| snake_viper_tick | 189,148 | -5.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,764 | -17.12% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,291 (-5.85%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,063 | +1.04% |
| gold | +1,167 | +0.71% |
| benchmark | +826 | +0.37% |
| intraweek | +303 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -809 | -0.39% |
| unified | -1,048 | -0.47% |
| snake_abs_exit | -1,075 | -0.53% |
| intramonth | -1,163 | -0.55% |
| snake_abs | -1,551 | -0.78% |
| snake_abs_conv | -1,562 | -0.78% |
| snake_abs_exit_conv | -1,580 | -0.78% |
| oracle | -1,756 | -0.82% |
| snake_anaconda | -2,248 | -1.16% |
| snake_viper_tick | -5,029 | -2.59% |
| snake_viper_wild | -5,127 | -2.60% |

Average per day so far: benchmark Rs +630, unified Rs +562, oracle Rs +294, intramonth Rs +257, random_hold Rs +212, intraweek Rs +172, nifty_calls Rs +45, snake_abs_exit Rs +31, benchmark_smallcap Rs +24, snake_abs_exit_conv Rs +10, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -36, snake_abs_conv Rs -42, snake_anaconda Rs -214, snake_viper_wild Rs -230, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -362, gold Rs -835

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.