# Paper trading report

Updated 2026-11-26 14:40 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,665 | +12.83% | 0 | - | 237 |
| unified | 223,179 | +11.59% | 0 | - | 236 |
| oracle | 212,722 | +6.36% | 0 | - | 233 |
| intramonth | 210,517 | +5.26% | 0 | - | 235 |
| random_hold | 209,013 | +4.51% | 13 | 69% | 1,037 |
| intraweek | 207,635 | +3.82% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,795 | +0.40% | 0 | - | 237 |
| snake_abs_exit | 200,322 | +0.16% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,684 | -0.16% | 2 | 50% | 345 |
| snake_abs | 198,014 | -0.99% | 1 | 100% | 255 |
| snake_abs_conv | 197,809 | -1.10% | 1 | 100% | 255 |
| snake_viper_wild | 192,417 | -3.79% | 16 | 50% | 2,827 |
| snake_anaconda | 191,692 | -4.15% | 3 | 33% | 374 |
| snake_viper_tick | 189,148 | -5.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,372 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,481 (-5.76%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,984 | +1.00% |
| gold | +1,776 | +1.08% |
| intraweek | +892 | +0.43% |
| benchmark | +643 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -480 | -0.23% |
| unified | -920 | -0.41% |
| oracle | -1,073 | -0.50% |
| intramonth | -1,176 | -0.56% |
| snake_abs_exit | -1,934 | -0.96% |
| snake_abs | -2,136 | -1.07% |
| snake_abs_conv | -2,163 | -1.08% |
| snake_abs_exit_conv | -2,292 | -1.14% |
| snake_anaconda | -2,861 | -1.47% |
| snake_viper_tick | -5,029 | -2.59% |
| snake_viper_wild | -5,127 | -2.60% |

Average per day so far: benchmark Rs +626, unified Rs +565, oracle Rs +310, intramonth Rs +257, random_hold Rs +220, intraweek Rs +186, nifty_calls Rs +45, benchmark_smallcap Rs +21, snake_abs_exit Rs +8, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -8, snake_abs Rs -51, snake_abs_conv Rs -58, snake_viper_wild Rs -230, snake_anaconda Rs -231, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -362, gold Rs -820

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.