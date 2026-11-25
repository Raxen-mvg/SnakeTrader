# Paper trading report

Updated 2026-11-25 10:45 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,314 | +12.66% | 0 | - | 237 |
| unified | 225,271 | +12.64% | 0 | - | 236 |
| intramonth | 213,009 | +6.50% | 0 | - | 235 |
| oracle | 212,460 | +6.23% | 0 | - | 233 |
| random_hold | 209,763 | +4.88% | 12 | 75% | 1,009 |
| intraweek | 207,654 | +3.83% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,255 | +1.13% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,694 | +0.85% | 2 | 50% | 345 |
| snake_abs | 201,047 | +0.52% | 1 | 100% | 255 |
| snake_abs_conv | 200,859 | +0.43% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_viper_wild | 195,474 | -2.26% | 16 | 50% | 2,827 |
| snake_anaconda | 193,739 | -3.13% | 3 | 33% | 374 |
| snake_viper_tick | 192,151 | -3.92% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,616 | -17.19% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,372 (-5.31%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,840 | +1.73% |
| random_hold | +1,336 | +0.64% |
| unified | +986 | +0.44% |
| benchmark_smallcap | +460 | +0.23% |
| intramonth | +258 | +0.12% |
| oracle | +118 | +0.06% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,814 | -2.25% |
| intraweek | -3,965 | -1.87% |
| snake_abs | -4,413 | -2.15% |
| snake_abs_conv | -4,444 | -2.17% |
| snake_anaconda | -4,964 | -2.50% |
| snake_abs_exit | -5,240 | -2.52% |
| snake_abs_exit_conv | -5,352 | -2.58% |
| snake_viper_tick | -5,541 | -2.80% |
| snake_viper_wild | -5,650 | -2.81% |

Average per day so far: benchmark Rs +633, unified Rs +632, intramonth Rs +325, oracle Rs +312, random_hold Rs +244, intraweek Rs +191, snake_abs_exit Rs +61, nifty_calls Rs +46, snake_abs_exit_conv Rs +46, snake_abs Rs +28, snake_abs_conv Rs +23, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_viper_wild Rs -141, snake_anaconda Rs -179, snake_viper_tick Rs -271, snake_nonews Rs -292, snake Rs -311, gold Rs -860

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.