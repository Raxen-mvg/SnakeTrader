# Paper trading report

Updated 2026-11-25 15:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,145 | +12.57% | 0 | - | 237 |
| unified | 223,884 | +11.94% | 0 | - | 236 |
| oracle | 213,094 | +6.55% | 0 | - | 233 |
| intramonth | 211,307 | +5.65% | 0 | - | 235 |
| random_hold | 209,788 | +4.89% | 12 | 75% | 1,009 |
| intraweek | 207,053 | +3.53% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,545 | +1.27% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,252 | +1.13% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,545 | +0.27% | 1 | 100% | 255 |
| snake_abs_conv | 200,369 | +0.18% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,968 | -0.52% | 0 | - | 237 |
| snake_viper_wild | 197,538 | -1.23% | 16 | 50% | 2,827 |
| snake_anaconda | 194,586 | -2.71% | 3 | 33% | 374 |
| snake_viper_tick | 194,172 | -2.91% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,860 | -17.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,004 (-5.50%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,672 | +1.66% |
| random_hold | +1,362 | +0.65% |
| oracle | +752 | +0.35% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| benchmark_smallcap | -11 | -0.01% |
| unified | -402 | -0.18% |
| intramonth | -1,444 | -0.68% |
| snake_viper_tick | -3,520 | -1.78% |
| snake_viper_wild | -3,586 | -1.78% |
| snake_anaconda | -4,117 | -2.07% |
| intraweek | -4,566 | -2.16% |
| gold | -4,570 | -2.70% |
| snake_abs_exit_conv | -4,794 | -2.32% |
| snake_abs | -4,915 | -2.39% |
| snake_abs_conv | -4,934 | -2.40% |
| snake_abs_exit | -4,950 | -2.39% |

Average per day so far: benchmark Rs +629, unified Rs +597, oracle Rs +327, intramonth Rs +283, random_hold Rs +245, intraweek Rs +176, snake_abs_exit Rs +69, snake_abs_exit_conv Rs +61, nifty_calls Rs +46, snake_abs Rs +14, snake_abs_conv Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -29, snake_viper_wild Rs -77, snake_anaconda Rs -155, snake_viper_tick Rs -201, snake_nonews Rs -292, snake Rs -311, gold Rs -879

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.