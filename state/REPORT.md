# Paper trading report

Updated 2026-11-20 10:52 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,440 | +12.72% | 0 | - | 236 |
| benchmark | 223,049 | +11.53% | 0 | - | 237 |
| intramonth | 214,343 | +7.17% | 0 | - | 235 |
| intraweek | 213,865 | +6.93% | 35 | 54% | 3,851 |
| oracle | 212,433 | +6.22% | 0 | - | 233 |
| snake_abs_exit | 210,996 | +5.50% | 2 | 50% | 345 |
| random_hold | 209,090 | +4.54% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,570 | +4.29% | 2 | 50% | 345 |
| snake_abs | 207,638 | +3.82% | 1 | 100% | 255 |
| snake_abs_conv | 207,498 | +3.75% | 1 | 100% | 255 |
| snake_viper_wild | 207,035 | +3.52% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,500 | +1.75% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,340 | +0.67% | 3 | 33% | 374 |
| benchmark_smallcap | 200,504 | +0.25% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,761 | -17.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,867 (-4.07%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +976 | +0.46% |
| unified | +825 | +0.37% |
| benchmark | +673 | +0.30% |
| random_hold | +637 | +0.31% |
| oracle | +345 | +0.16% |
| intramonth | +335 | +0.16% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -477 | -0.23% |
| snake_viper_wild | -488 | -0.23% |
| benchmark_smallcap | -964 | -0.48% |
| snake_abs | -1,342 | -0.64% |
| snake_abs_conv | -1,362 | -0.65% |
| snake_anaconda | -2,124 | -1.04% |
| snake_abs_exit | -2,355 | -1.10% |
| snake_abs_exit_conv | -2,495 | -1.18% |
| gold | -10,012 | -5.73% |

Average per day so far: unified Rs +669, benchmark Rs +607, intramonth Rs +377, intraweek Rs +365, oracle Rs +327, snake_abs_exit Rs +314, snake_abs_exit_conv Rs +245, random_hold Rs +239, snake_viper_wild Rs +235, snake_abs_conv Rs +214, snake_abs Rs +212, snake_viper_tick Rs +130, nifty_calls Rs +48, snake_anaconda Rs +41, benchmark_smallcap Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -927

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.