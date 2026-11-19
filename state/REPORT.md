# Paper trading report

Updated 2026-11-19 13:55 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,831 | +11.92% | 0 | - | 236 |
| benchmark | 221,833 | +10.92% | 0 | - | 237 |
| intramonth | 213,352 | +6.68% | 0 | - | 235 |
| snake_abs_exit | 212,642 | +6.32% | 2 | 50% | 345 |
| intraweek | 211,866 | +5.93% | 35 | 54% | 3,851 |
| oracle | 211,559 | +5.78% | 0 | - | 233 |
| snake_abs_exit_conv | 210,347 | +5.17% | 2 | 50% | 345 |
| snake_abs | 208,341 | +4.17% | 1 | 100% | 255 |
| snake_abs_conv | 208,205 | +4.10% | 1 | 100% | 255 |
| random_hold | 207,751 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 207,566 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,019 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 202,853 | +1.43% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,661 | +0.33% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,085 | -12.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,330 (-4.33%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,538 | +0.70% |
| benchmark_smallcap | +1,334 | +0.67% |
| unified | +1,220 | +0.55% |
| intramonth | +1,078 | +0.51% |
| random_hold | +818 | +0.40% |
| oracle | +763 | +0.36% |
| snake_viper_wild | +527 | +0.25% |
| snake_viper_tick | +516 | +0.25% |
| intraweek | +26 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -1,095 | -0.52% |
| snake_abs_conv | -1,120 | -0.54% |
| snake_abs_exit | -1,390 | -0.65% |
| snake_anaconda | -1,548 | -0.76% |
| snake_abs_exit_conv | -2,036 | -0.96% |
| gold | -2,236 | -1.26% |

Average per day so far: unified Rs +644, benchmark Rs +590, snake_abs_exit Rs +372, intramonth Rs +361, intraweek Rs +321, oracle Rs +312, snake_abs_exit_conv Rs +304, snake_viper_wild Rs +261, snake_abs_conv Rs +241, snake_abs Rs +238, random_hold Rs +209, snake_viper_tick Rs +155, snake_anaconda Rs +89, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -673

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.