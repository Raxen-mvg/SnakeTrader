# Paper trading report

Updated 2026-11-19 12:47 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,825 | +11.91% | 0 | - | 236 |
| benchmark | 221,511 | +10.76% | 0 | - | 237 |
| intramonth | 213,488 | +6.74% | 0 | - | 235 |
| snake_abs_exit | 213,042 | +6.52% | 2 | 50% | 345 |
| intraweek | 211,755 | +5.88% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,129 | +5.57% | 2 | 50% | 345 |
| oracle | 211,012 | +5.51% | 0 | - | 233 |
| snake_abs | 208,664 | +4.33% | 1 | 100% | 255 |
| snake_abs_conv | 208,538 | +4.27% | 1 | 100% | 255 |
| random_hold | 207,727 | +3.86% | 10 | 70% | 733 |
| snake_viper_wild | 207,480 | +3.74% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,935 | +1.97% | 15 | 47% | 2,625 |
| snake_anaconda | 203,034 | +1.52% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,728 | +0.36% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,987 | -12.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,248 (-4.38%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,401 | +0.70% |
| benchmark | +1,216 | +0.55% |
| intramonth | +1,214 | +0.57% |
| unified | +1,214 | +0.55% |
| random_hold | +795 | +0.38% |
| snake_viper_wild | +440 | +0.21% |
| snake_viper_tick | +431 | +0.21% |
| oracle | +216 | +0.10% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -84 | -0.04% |
| snake_abs | -773 | -0.37% |
| snake_abs_conv | -787 | -0.38% |
| snake_abs_exit | -990 | -0.46% |
| snake_abs_exit_conv | -1,254 | -0.59% |
| snake_anaconda | -1,367 | -0.67% |
| gold | -2,334 | -1.32% |

Average per day so far: unified Rs +644, benchmark Rs +581, snake_abs_exit Rs +384, intramonth Rs +365, snake_abs_exit_conv Rs +327, intraweek Rs +318, oracle Rs +298, snake_viper_wild Rs +258, snake_abs_conv Rs +251, snake_abs Rs +248, random_hold Rs +209, snake_viper_tick Rs +151, snake_anaconda Rs +95, nifty_calls Rs +50, benchmark_smallcap Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.