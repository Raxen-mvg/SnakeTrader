# Paper trading report

Updated 2026-11-26 14:43 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,964 | +12.98% | 0 | - | 237 |
| unified | 223,111 | +11.56% | 0 | - | 236 |
| oracle | 212,810 | +6.41% | 0 | - | 233 |
| intramonth | 210,539 | +5.27% | 0 | - | 235 |
| random_hold | 208,830 | +4.42% | 13 | 69% | 1,037 |
| intraweek | 207,501 | +3.75% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,851 | +0.43% | 0 | - | 237 |
| snake_abs_exit | 200,179 | +0.09% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,600 | -0.20% | 2 | 50% | 345 |
| snake_abs | 197,909 | -1.04% | 1 | 100% | 255 |
| snake_abs_conv | 197,701 | -1.15% | 1 | 100% | 255 |
| snake_viper_wild | 192,302 | -3.85% | 16 | 50% | 2,827 |
| snake_anaconda | 191,582 | -4.21% | 3 | 33% | 374 |
| snake_viper_tick | 189,035 | -5.48% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,372 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,442 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,040 | +1.03% |
| gold | +1,776 | +1.08% |
| benchmark | +941 | +0.42% |
| intraweek | +757 | +0.37% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -662 | -0.32% |
| oracle | -985 | -0.46% |
| unified | -988 | -0.44% |
| intramonth | -1,154 | -0.55% |
| snake_abs_exit | -2,077 | -1.03% |
| snake_abs | -2,241 | -1.12% |
| snake_abs_conv | -2,271 | -1.14% |
| snake_abs_exit_conv | -2,376 | -1.18% |
| snake_anaconda | -2,971 | -1.53% |
| snake_viper_tick | -5,142 | -2.65% |
| snake_viper_wild | -5,242 | -2.65% |

Average per day so far: benchmark Rs +633, unified Rs +564, oracle Rs +312, intramonth Rs +257, random_hold Rs +215, intraweek Rs +183, nifty_calls Rs +45, benchmark_smallcap Rs +23, snake_abs_exit Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -11, snake_abs Rs -54, snake_abs_conv Rs -61, snake_viper_wild Rs -233, snake_anaconda Rs -234, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -365, gold Rs -820

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.