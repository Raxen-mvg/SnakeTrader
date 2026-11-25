# Paper trading report

Updated 2026-11-25 09:45 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,654 | +12.83% | 0 | - | 236 |
| benchmark | 224,564 | +12.28% | 0 | - | 237 |
| intramonth | 213,204 | +6.60% | 0 | - | 235 |
| oracle | 212,877 | +6.44% | 0 | - | 233 |
| intraweek | 211,559 | +5.78% | 40 | 55% | 4,400 |
| random_hold | 209,986 | +4.99% | 12 | 75% | 1,009 |
| snake_abs_exit | 203,057 | +1.53% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,456 | +1.23% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,767 | +0.88% | 1 | 100% | 255 |
| snake_abs_conv | 201,580 | +0.79% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,529 | -0.24% | 0 | - | 237 |
| snake_viper_wild | 199,353 | -0.32% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,958 | -2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 194,782 | -2.61% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,682 | -17.16% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,142 (-4.93%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,091 | +1.40% |
| random_hold | +1,560 | +0.75% |
| unified | +1,369 | +0.61% |
| benchmark_smallcap | +549 | +0.28% |
| oracle | +535 | +0.25% |
| intramonth | +452 | +0.21% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -60 | -0.03% |
| snake_viper_tick | -1,734 | -0.88% |
| snake_viper_wild | -1,771 | -0.88% |
| snake_abs | -3,694 | -1.80% |
| snake_abs_conv | -3,723 | -1.81% |
| gold | -3,748 | -2.21% |
| snake_anaconda | -3,921 | -1.97% |
| snake_abs_exit | -4,438 | -2.14% |
| snake_abs_exit_conv | -4,590 | -2.22% |

Average per day so far: unified Rs +641, benchmark Rs +614, intramonth Rs +330, oracle Rs +322, intraweek Rs +289, random_hold Rs +250, snake_abs_exit Rs +83, snake_abs_exit_conv Rs +66, snake_abs Rs +47, nifty_calls Rs +46, snake_abs_conv Rs +43, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_viper_wild Rs -20, snake_viper_tick Rs -139, snake_anaconda Rs -149, snake_nonews Rs -292, snake Rs -311, gold Rs -858

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.