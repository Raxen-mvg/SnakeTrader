# Paper trading report

Updated 2026-11-25 12:51 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,988 | +12.49% | 0 | - | 236 |
| benchmark | 224,686 | +12.34% | 0 | - | 237 |
| intramonth | 213,072 | +6.54% | 0 | - | 235 |
| oracle | 212,863 | +6.43% | 0 | - | 233 |
| random_hold | 210,234 | +5.12% | 12 | 75% | 1,009 |
| intraweek | 208,686 | +4.34% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,209 | +1.10% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,953 | +0.98% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,369 | +0.18% | 1 | 100% | 255 |
| snake_abs_conv | 200,190 | +0.10% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,304 | -0.35% | 0 | - | 237 |
| snake_viper_wild | 196,742 | -1.63% | 16 | 50% | 2,827 |
| snake_anaconda | 193,901 | -3.05% | 3 | 33% | 374 |
| snake_viper_tick | 193,392 | -3.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,547 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,540 (-5.23%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,213 | +1.45% |
| random_hold | +1,808 | +0.87% |
| unified | +703 | +0.31% |
| oracle | +521 | +0.24% |
| benchmark_smallcap | +325 | +0.16% |
| intramonth | +321 | +0.15% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -2,933 | -1.39% |
| snake_viper_tick | -4,301 | -2.17% |
| snake_viper_wild | -4,383 | -2.18% |
| snake_anaconda | -4,802 | -2.42% |
| gold | -4,883 | -2.88% |
| snake_abs | -5,091 | -2.48% |
| snake_abs_exit_conv | -5,092 | -2.46% |
| snake_abs_conv | -5,113 | -2.49% |
| snake_abs_exit | -5,286 | -2.55% |

Average per day so far: unified Rs +625, benchmark Rs +617, intramonth Rs +327, oracle Rs +322, random_hold Rs +256, intraweek Rs +217, snake_abs_exit Rs +60, snake_abs_exit_conv Rs +53, nifty_calls Rs +46, snake_abs Rs +10, snake_abs_conv Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -19, snake_viper_wild Rs -102, snake_anaconda Rs -174, snake_viper_tick Rs -228, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.