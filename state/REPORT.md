# Paper trading report

Updated 2026-11-18 15:30 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,612 | +11.31% | 0 | - | 236 |
| benchmark | 220,295 | +10.15% | 0 | - | 237 |
| snake_abs_exit | 214,032 | +7.02% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,383 | +6.19% | 2 | 50% | 345 |
| intramonth | 212,274 | +6.14% | 0 | - | 235 |
| intraweek | 211,839 | +5.92% | 35 | 54% | 3,851 |
| oracle | 210,796 | +5.40% | 0 | - | 233 |
| snake_abs | 209,436 | +4.72% | 1 | 100% | 255 |
| snake_abs_conv | 209,325 | +4.66% | 1 | 100% | 255 |
| snake_viper_wild | 207,039 | +3.52% | 16 | 50% | 2,827 |
| random_hold | 206,932 | +3.47% | 10 | 70% | 733 |
| snake_anaconda | 204,401 | +2.20% | 3 | 33% | 374 |
| snake_viper_tick | 203,503 | +1.75% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,321 | -11.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,694 (-4.65%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,173 | +0.53% |
| snake_abs_conv | +905 | +0.43% |
| snake_abs_exit | +890 | +0.42% |
| snake_abs | +878 | +0.42% |
| snake_abs_exit_conv | +810 | +0.38% |
| intramonth | +731 | +0.35% |
| snake_anaconda | +346 | +0.17% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -1,244 | -0.62% |
| benchmark | -1,308 | -0.59% |
| intraweek | -1,483 | -0.69% |
| random_hold | -1,500 | -0.72% |
| oracle | -1,690 | -0.80% |
| snake_viper_tick | -2,333 | -1.13% |
| snake_viper_wild | -2,376 | -1.13% |
| gold | -3,403 | -1.88% |

Average per day so far: unified Rs +628, benchmark Rs +564, snake_abs_exit Rs +425, snake_abs_exit_conv Rs +375, intramonth Rs +341, intraweek Rs +329, oracle Rs +300, snake_abs_conv Rs +283, snake_abs Rs +278, snake_viper_wild Rs +251, random_hold Rs +193, snake_anaconda Rs +142, snake_viper_tick Rs +140, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -21, snake_nonews Rs -326, snake Rs -347, gold Rs -630

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.