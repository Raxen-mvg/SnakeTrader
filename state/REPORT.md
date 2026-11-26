# Paper trading report

Updated 2026-11-26 13:51 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,444 | +12.72% | 0 | - | 237 |
| unified | 223,165 | +11.58% | 0 | - | 236 |
| oracle | 213,038 | +6.52% | 0 | - | 233 |
| intramonth | 210,285 | +5.14% | 0 | - | 235 |
| random_hold | 209,288 | +4.64% | 13 | 69% | 1,037 |
| intraweek | 207,827 | +3.91% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,403 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,820 | -0.09% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,253 | -0.37% | 2 | 50% | 345 |
| snake_abs | 197,616 | -1.19% | 1 | 100% | 255 |
| snake_abs_conv | 197,406 | -1.30% | 1 | 100% | 255 |
| snake_viper_wild | 192,215 | -3.89% | 16 | 50% | 2,827 |
| snake_anaconda | 191,314 | -4.34% | 3 | 33% | 374 |
| snake_viper_tick | 188,951 | -5.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,142 | -16.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,502 (-5.75%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,592 | +0.80% |
| gold | +1,545 | +0.94% |
| intraweek | +1,084 | +0.52% |
| benchmark | +421 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -204 | -0.10% |
| oracle | -757 | -0.35% |
| unified | -935 | -0.42% |
| intramonth | -1,408 | -0.67% |
| snake_abs_exit | -2,436 | -1.20% |
| snake_abs | -2,534 | -1.27% |
| snake_abs_conv | -2,567 | -1.28% |
| snake_abs_exit_conv | -2,723 | -1.35% |
| snake_anaconda | -3,239 | -1.67% |
| snake_viper_tick | -5,226 | -2.69% |
| snake_viper_wild | -5,328 | -2.70% |

Average per day so far: benchmark Rs +621, unified Rs +565, oracle Rs +318, intramonth Rs +251, random_hold Rs +227, intraweek Rs +191, nifty_calls Rs +45, benchmark_smallcap Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -5, snake_abs_exit_conv Rs -20, snake_abs Rs -61, snake_abs_conv Rs -68, snake_viper_wild Rs -236, snake_anaconda Rs -241, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.