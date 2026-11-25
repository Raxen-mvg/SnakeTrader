# Paper trading report

Updated 2026-11-25 14:19 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,855 | +12.43% | 0 | - | 237 |
| unified | 224,534 | +12.27% | 0 | - | 236 |
| oracle | 212,612 | +6.31% | 0 | - | 233 |
| intramonth | 212,135 | +6.07% | 0 | - | 235 |
| random_hold | 209,372 | +4.69% | 12 | 75% | 1,009 |
| intraweek | 206,847 | +3.42% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,511 | +0.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,276 | +0.64% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,864 | -0.07% | 1 | 100% | 255 |
| snake_abs_conv | 199,664 | -0.17% | 1 | 100% | 255 |
| benchmark_smallcap | 198,901 | -0.55% | 0 | - | 237 |
| snake_viper_wild | 197,414 | -1.29% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,050 | -2.98% | 15 | 47% | 2,625 |
| snake_anaconda | 193,332 | -3.33% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,139 | -17.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,890 (-5.56%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,381 | +1.53% |
| random_hold | +945 | +0.45% |
| oracle | +270 | +0.13% |
| unified | +249 | +0.11% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -78 | -0.04% |
| intramonth | -617 | -0.29% |
| snake_viper_tick | -3,643 | -1.84% |
| snake_viper_wild | -3,711 | -1.84% |
| gold | -4,291 | -2.53% |
| intraweek | -4,772 | -2.25% |
| snake_anaconda | -5,371 | -2.70% |
| snake_abs | -5,597 | -2.72% |
| snake_abs_conv | -5,638 | -2.75% |
| snake_abs_exit_conv | -5,770 | -2.79% |
| snake_abs_exit | -5,984 | -2.88% |

Average per day so far: benchmark Rs +621, unified Rs +613, oracle Rs +315, intramonth Rs +303, random_hold Rs +234, intraweek Rs +171, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +34, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -4, snake_abs_conv Rs -9, benchmark_smallcap Rs -31, snake_viper_wild Rs -81, snake_anaconda Rs -191, snake_viper_tick Rs -205, snake_nonews Rs -292, snake Rs -311, gold Rs -872

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.