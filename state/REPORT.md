# Paper trading report

Updated 2026-11-26 15:10 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,964 | +12.98% | 0 | - | 237 |
| unified | 223,097 | +11.55% | 0 | - | 236 |
| oracle | 212,489 | +6.25% | 0 | - | 233 |
| intramonth | 210,563 | +5.28% | 0 | - | 235 |
| random_hold | 208,716 | +4.36% | 13 | 69% | 1,037 |
| intraweek | 207,296 | +3.65% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,585 | +0.79% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,896 | +0.45% | 2 | 50% | 345 |
| benchmark_smallcap | 200,807 | +0.40% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,088 | -0.46% | 1 | 100% | 255 |
| snake_abs_conv | 198,905 | -0.55% | 1 | 100% | 255 |
| snake_anaconda | 192,867 | -3.57% | 3 | 33% | 374 |
| snake_viper_wild | 192,652 | -3.67% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,378 | -5.31% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,125 | -16.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,449 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,995 | +1.00% |
| gold | +1,529 | +0.93% |
| benchmark | +941 | +0.42% |
| intraweek | +553 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -671 | -0.33% |
| random_hold | -777 | -0.37% |
| unified | -1,002 | -0.45% |
| snake_abs | -1,062 | -0.53% |
| snake_abs_conv | -1,067 | -0.53% |
| snake_abs_exit_conv | -1,080 | -0.54% |
| intramonth | -1,130 | -0.53% |
| oracle | -1,306 | -0.61% |
| snake_anaconda | -1,686 | -0.87% |
| snake_viper_tick | -4,799 | -2.47% |
| snake_viper_wild | -4,891 | -2.48% |

Average per day so far: benchmark Rs +633, unified Rs +563, oracle Rs +305, intramonth Rs +258, random_hold Rs +213, intraweek Rs +178, nifty_calls Rs +45, snake_abs_exit Rs +42, snake_abs_exit_conv Rs +24, benchmark_smallcap Rs +22, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -23, snake_abs_conv Rs -29, snake_anaconda Rs -198, snake_viper_wild Rs -223, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -354, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.