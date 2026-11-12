# Paper trading report

Updated 2026-11-12 15:19 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,752 | +10.38% | 0 | - | 236 |
| benchmark | 220,571 | +10.29% | 0 | - | 237 |
| snake_abs_exit_conv | 219,387 | +9.69% | 2 | 50% | 345 |
| snake_abs_exit | 218,072 | +9.04% | 2 | 50% | 345 |
| snake_abs | 216,058 | +8.03% | 1 | 100% | 255 |
| snake_abs_conv | 215,892 | +7.95% | 1 | 100% | 255 |
| intraweek | 214,739 | +7.37% | 30 | 53% | 3,302 |
| oracle | 212,989 | +6.49% | 0 | - | 233 |
| intramonth | 211,614 | +5.81% | 0 | - | 235 |
| random_hold | 208,075 | +4.04% | 10 | 70% | 733 |
| snake_anaconda | 207,104 | +3.55% | 3 | 33% | 374 |
| snake_viper_wild | 205,798 | +2.90% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,362 | +1.68% | 0 | - | 237 |
| snake_viper_tick | 202,279 | +1.14% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,426 | -7.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,083 (-3.96%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,982 | +1.46% |
| benchmark_smallcap | +2,556 | +1.27% |
| snake_abs_conv | +2,434 | +1.14% |
| snake_abs | +2,433 | +1.14% |
| snake_abs_exit_conv | +2,235 | +1.03% |
| snake_abs_exit | +1,909 | +0.88% |
| intraweek | +1,606 | +0.75% |
| benchmark | +1,308 | +0.60% |
| oracle | +986 | +0.47% |
| random_hold | +965 | +0.47% |
| unified | +938 | +0.43% |
| intramonth | +618 | +0.29% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -930 | -0.46% |
| snake_viper_wild | -944 | -0.46% |
| gold | -4,159 | -2.19% |

Average per day so far: snake_abs_exit_conv Rs +669, unified Rs +648, benchmark Rs +643, snake_abs_exit Rs +623, snake_abs_conv Rs +548, snake_abs Rs +535, intraweek Rs +461, oracle Rs +406, intramonth Rs +363, snake_anaconda Rs +263, random_hold Rs +252, snake_viper_wild Rs +242, benchmark_smallcap Rs +120, snake_viper_tick Rs +109, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -455

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.