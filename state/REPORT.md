# Paper trading report

Updated 2026-11-26 11:54 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,002 | +13.00% | 0 | - | 237 |
| unified | 223,209 | +11.60% | 0 | - | 236 |
| oracle | 213,127 | +6.56% | 0 | - | 233 |
| intramonth | 210,404 | +5.20% | 0 | - | 235 |
| random_hold | 209,756 | +4.88% | 13 | 69% | 1,037 |
| intraweek | 208,550 | +4.28% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,130 | +0.56% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,597 | +0.30% | 2 | 50% | 345 |
| benchmark_smallcap | 200,526 | +0.26% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,852 | -0.57% | 1 | 100% | 255 |
| snake_abs_conv | 198,663 | -0.67% | 1 | 100% | 255 |
| snake_anaconda | 192,738 | -3.63% | 3 | 33% | 374 |
| snake_viper_wild | 192,330 | -3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,063 | -5.47% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,684 | -16.66% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,802 (-5.60%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,088 | +1.27% |
| intraweek | +1,806 | +0.87% |
| benchmark_smallcap | +1,715 | +0.86% |
| benchmark | +979 | +0.43% |
| random_hold | +263 | +0.12% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -668 | -0.31% |
| unified | -891 | -0.40% |
| snake_abs_exit | -1,126 | -0.56% |
| intramonth | -1,289 | -0.61% |
| snake_abs | -1,298 | -0.65% |
| snake_abs_conv | -1,309 | -0.66% |
| snake_abs_exit_conv | -1,379 | -0.68% |
| snake_anaconda | -1,815 | -0.93% |
| snake_viper_tick | -5,114 | -2.63% |
| snake_viper_wild | -5,213 | -2.64% |

Average per day so far: benchmark Rs +634, unified Rs +566, oracle Rs +320, intramonth Rs +254, random_hold Rs +238, intraweek Rs +209, nifty_calls Rs +45, snake_abs_exit Rs +30, snake_abs_exit_conv Rs +16, benchmark_smallcap Rs +14, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -29, snake_abs_conv Rs -35, snake_anaconda Rs -202, snake_viper_wild Rs -232, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -365, gold Rs -813

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.