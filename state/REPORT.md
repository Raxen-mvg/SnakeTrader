# Paper trading report

Updated 2026-10-07 12:22 IST. Model picks as of 2026-10-01. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 206,936 | +3.47% | 0 | - | 236 |
| snake_abs_exit_conv | 205,896 | +2.95% | 0 | - | 236 |
| snake_abs_exit | 205,883 | +2.94% | 0 | - | 235 |
| snake_anaconda | 204,320 | +2.16% | 0 | - | 236 |
| random_hold | 203,103 | +1.55% | 2 | 50% | 362 |
| snake_abs | 202,828 | +1.41% | 0 | - | 236 |
| benchmark_smallcap | 202,802 | +1.40% | 0 | - | 237 |
| snake_abs_conv | 202,666 | +1.33% | 0 | - | 236 |
| intramonth | 202,642 | +1.32% | 0 | - | 235 |
| oracle | 202,047 | +1.02% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 199,400 | -0.30% | 0 | - | 237 |
| intraweek | 198,555 | -0.72% | 5 | 40% | 748 |
| benchmark | 197,888 | -1.06% | 0 | - | 237 |
| snake | 193,876 | -3.06% | 0 | - | 234 |
| snake_nonews | 192,931 | -3.54% | 0 | - | 231 |
| nifty_calls | 192,776 | -3.61% | 1 | 0% | 50 |

Combined allocator (virtual): Rs 202,214 (+1.11%).

Profit on 2026-10-07:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +5,684 | +2.82% |
| intramonth | +2,896 | +1.45% |
| random_hold | +2,745 | +1.37% |
| snake_anaconda | +1,638 | +0.81% |
| oracle | +533 | +0.26% |
| snake_abs | +385 | +0.19% |
| snake_abs_exit_conv | +362 | +0.18% |
| snake_abs_exit | +354 | +0.17% |
| snake_abs_conv | +340 | +0.17% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| benchmark_smallcap | -179 | -0.09% |
| benchmark | -222 | -0.11% |
| gold | -296 | -0.15% |
| intraweek | -780 | -0.39% |
| snake | -1,558 | -0.80% |
| snake_nonews | -2,313 | -1.19% |

Average per day so far: snake_abs_exit_conv Rs +1,474, snake_abs_exit Rs +1,471, snake_anaconda Rs +1,440, unified Rs +991, benchmark_smallcap Rs +934, snake_abs_conv Rs +666, snake_abs Rs +566, random_hold Rs +443, intramonth Rs +377, oracle Rs +292, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, gold Rs -86, intraweek Rs -206, benchmark Rs -302, snake Rs -1,021, nifty_calls Rs -1,032, snake_nonews Rs -1,414

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.