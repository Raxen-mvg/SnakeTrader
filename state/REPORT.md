# Paper trading report

Updated 2026-11-26 10:37 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,849 | +12.93% | 0 | - | 237 |
| unified | 223,384 | +11.69% | 0 | - | 236 |
| oracle | 212,924 | +6.46% | 0 | - | 233 |
| intramonth | 210,779 | +5.39% | 0 | - | 235 |
| random_hold | 209,908 | +4.95% | 13 | 69% | 1,037 |
| intraweek | 208,103 | +4.05% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,812 | +0.91% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,307 | +0.65% | 2 | 50% | 345 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,461 | -0.27% | 1 | 100% | 255 |
| snake_abs_conv | 199,276 | -0.36% | 1 | 100% | 255 |
| snake_anaconda | 193,250 | -3.38% | 3 | 33% | 374 |
| snake_viper_wild | 193,228 | -3.39% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,942 | -5.03% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,884 | -16.06% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,883 (-5.56%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,288 | +2.00% |
| benchmark_smallcap | +1,805 | +0.91% |
| intraweek | +1,359 | +0.66% |
| benchmark | +826 | +0.37% |
| random_hold | +416 | +0.20% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -443 | -0.22% |
| snake_abs_exit_conv | -669 | -0.33% |
| snake_abs | -689 | -0.34% |
| snake_abs_conv | -696 | -0.35% |
| unified | -716 | -0.32% |
| oracle | -871 | -0.41% |
| intramonth | -914 | -0.43% |
| snake_anaconda | -1,303 | -0.67% |
| snake_viper_tick | -4,235 | -2.18% |
| snake_viper_wild | -4,315 | -2.18% |

Average per day so far: benchmark Rs +630, unified Rs +570, oracle Rs +315, intramonth Rs +263, random_hold Rs +242, intraweek Rs +198, snake_abs_exit Rs +48, nifty_calls Rs +45, snake_abs_exit_conv Rs +34, benchmark_smallcap Rs +17, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -14, snake_abs_conv Rs -19, snake_anaconda Rs -188, snake_viper_wild Rs -205, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -335, gold Rs -783

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.