# Paper trading report

Updated 2026-11-19 10:53 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,985 | +11.99% | 0 | - | 236 |
| benchmark | 220,976 | +10.49% | 0 | - | 237 |
| snake_abs_exit | 214,010 | +7.00% | 2 | 50% | 345 |
| intramonth | 213,520 | +6.76% | 0 | - | 235 |
| intraweek | 212,102 | +6.05% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,061 | +6.03% | 2 | 50% | 345 |
| oracle | 211,232 | +5.62% | 0 | - | 233 |
| snake_abs | 209,648 | +4.82% | 1 | 100% | 255 |
| snake_abs_conv | 209,527 | +4.76% | 1 | 100% | 255 |
| random_hold | 207,793 | +3.90% | 10 | 70% | 733 |
| snake_viper_wild | 207,556 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,010 | +2.00% | 15 | 47% | 2,625 |
| snake_anaconda | 203,814 | +1.91% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,403 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,839 | -12.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,406 (-4.30%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,373 | +0.62% |
| intramonth | +1,247 | +0.59% |
| benchmark_smallcap | +1,076 | +0.54% |
| random_hold | +860 | +0.42% |
| benchmark | +681 | +0.31% |
| snake_viper_wild | +517 | +0.25% |
| snake_viper_tick | +507 | +0.25% |
| oracle | +436 | +0.21% |
| intraweek | +262 | +0.12% |
| snake_abs | +212 | +0.10% |
| snake_abs_conv | +202 | +0.10% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -22 | -0.01% |
| snake_abs_exit_conv | -322 | -0.15% |
| snake_anaconda | -587 | -0.29% |
| gold | -2,482 | -1.40% |

Average per day so far: unified Rs +648, benchmark Rs +567, snake_abs_exit Rs +412, intramonth Rs +365, snake_abs_exit_conv Rs +355, intraweek Rs +327, oracle Rs +304, snake_abs_conv Rs +280, snake_abs Rs +276, snake_viper_wild Rs +261, random_hold Rs +211, snake_viper_tick Rs +154, snake_anaconda Rs +119, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.