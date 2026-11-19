# Paper trading report

Updated 2026-11-19 14:01 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,969 | +11.98% | 0 | - | 236 |
| benchmark | 221,909 | +10.96% | 0 | - | 237 |
| intramonth | 213,503 | +6.75% | 0 | - | 235 |
| snake_abs_exit | 212,754 | +6.38% | 2 | 50% | 345 |
| oracle | 211,858 | +5.93% | 0 | - | 233 |
| intraweek | 211,836 | +5.92% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,446 | +5.22% | 2 | 50% | 345 |
| snake_abs | 208,408 | +4.20% | 1 | 100% | 255 |
| snake_abs_conv | 208,273 | +4.14% | 1 | 100% | 255 |
| random_hold | 207,826 | +3.91% | 10 | 70% | 733 |
| snake_viper_wild | 207,566 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,019 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 203,066 | +1.53% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,650 | +0.33% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,954 | -12.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,454 (-4.27%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,614 | +0.73% |
| unified | +1,358 | +0.61% |
| benchmark_smallcap | +1,323 | +0.66% |
| intramonth | +1,229 | +0.58% |
| oracle | +1,062 | +0.50% |
| random_hold | +893 | +0.43% |
| snake_viper_wild | +527 | +0.25% |
| snake_viper_tick | +516 | +0.25% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -4 | -0.00% |
| snake_abs | -1,029 | -0.49% |
| snake_abs_conv | -1,052 | -0.50% |
| snake_abs_exit | -1,277 | -0.60% |
| snake_anaconda | -1,335 | -0.65% |
| snake_abs_exit_conv | -1,937 | -0.91% |
| gold | -2,367 | -1.33% |

Average per day so far: unified Rs +648, benchmark Rs +592, snake_abs_exit Rs +375, intramonth Rs +365, oracle Rs +320, intraweek Rs +320, snake_abs_exit_conv Rs +307, snake_viper_wild Rs +261, snake_abs_conv Rs +243, snake_abs Rs +240, random_hold Rs +212, snake_viper_tick Rs +155, snake_anaconda Rs +96, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -677

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.