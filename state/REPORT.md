# Paper trading report

Updated 2026-11-11 12:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,884 | +10.44% | 0 | - | 237 |
| unified | 220,677 | +10.34% | 0 | - | 236 |
| snake_abs_exit_conv | 216,041 | +8.02% | 2 | 50% | 345 |
| snake_abs_exit | 214,740 | +7.37% | 2 | 50% | 345 |
| intraweek | 214,067 | +7.03% | 30 | 53% | 3,302 |
| snake_abs | 212,523 | +6.26% | 1 | 100% | 255 |
| snake_abs_conv | 212,366 | +6.18% | 1 | 100% | 255 |
| oracle | 211,944 | +5.97% | 0 | - | 233 |
| intramonth | 211,618 | +5.81% | 0 | - | 235 |
| random_hold | 206,857 | +3.43% | 9 | 67% | 709 |
| snake_anaconda | 202,734 | +1.37% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_viper_wild | 201,643 | +0.82% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,215 | -0.89% | 9 | 44% | 1,639 |
| gold | 189,766 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,300 (-4.35%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +4,213 | +2.13% |
| snake_viper_tick | +4,138 | +2.13% |
| snake_abs_exit_conv | +4,132 | +1.95% |
| benchmark_smallcap | +3,509 | +1.77% |
| snake_anaconda | +3,267 | +1.64% |
| snake_abs_conv | +2,888 | +1.38% |
| snake_abs | +2,876 | +1.37% |
| benchmark | +2,792 | +1.28% |
| snake_abs_exit | +2,757 | +1.30% |
| oracle | +2,026 | +0.96% |
| random_hold | +1,896 | +0.93% |
| intramonth | +1,009 | +0.48% |
| unified | +930 | +0.42% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -474 | -0.22% |
| gold | -2,367 | -1.23% |

Average per day so far: benchmark Rs +674, unified Rs +667, snake_abs_exit_conv Rs +573, snake_abs_exit Rs +526, intraweek Rs +454, snake_abs_conv Rs +442, snake_abs Rs +432, oracle Rs +385, intramonth Rs +375, random_hold Rs +221, snake_anaconda Rs +105, snake_viper_wild Rs +71, benchmark_smallcap Rs +62, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -89, gold Rs -330, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.