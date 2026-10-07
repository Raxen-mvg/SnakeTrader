# Paper trading report

Updated 2026-10-07 13:31 IST. Model picks as of 2026-10-01. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 207,447 | +3.72% | 0 | - | 236 |
| snake_abs_exit_conv | 206,474 | +3.24% | 0 | - | 236 |
| snake_abs_exit | 206,455 | +3.23% | 0 | - | 235 |
| snake_anaconda | 204,665 | +2.33% | 0 | - | 236 |
| snake_abs | 203,405 | +1.70% | 0 | - | 236 |
| random_hold | 203,348 | +1.67% | 2 | 50% | 362 |
| snake_abs_conv | 203,245 | +1.62% | 0 | - | 236 |
| intramonth | 203,042 | +1.52% | 0 | - | 235 |
| oracle | 202,503 | +1.25% | 0 | - | 233 |
| benchmark_smallcap | 202,376 | +1.19% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 199,466 | -0.27% | 0 | - | 237 |
| intraweek | 198,227 | -0.89% | 5 | 40% | 748 |
| benchmark | 197,139 | -1.43% | 0 | - | 237 |
| snake | 193,631 | -3.19% | 0 | - | 234 |
| snake_nonews | 192,841 | -3.58% | 0 | - | 231 |
| nifty_calls | 192,776 | -3.61% | 1 | 0% | 50 |

Combined allocator (virtual): Rs 202,548 (+1.27%).

Profit on 2026-10-07:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +6,195 | +3.08% |
| intramonth | +3,297 | +1.65% |
| random_hold | +2,990 | +1.49% |
| snake_anaconda | +1,984 | +0.98% |
| oracle | +989 | +0.49% |
| snake_abs | +962 | +0.47% |
| snake_abs_exit_conv | +940 | +0.46% |
| snake_abs_exit | +926 | +0.45% |
| snake_abs_conv | +919 | +0.45% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold | -230 | -0.12% |
| benchmark_smallcap | -605 | -0.30% |
| benchmark | -972 | -0.49% |
| intraweek | -1,108 | -0.56% |
| snake | -1,803 | -0.92% |
| snake_nonews | -2,403 | -1.23% |

Average per day so far: snake_abs_exit_conv Rs +1,619, snake_abs_exit Rs +1,614, snake_anaconda Rs +1,555, unified Rs +1,064, snake_abs_conv Rs +811, benchmark_smallcap Rs +792, snake_abs Rs +681, random_hold Rs +478, intramonth Rs +435, oracle Rs +358, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, gold Rs -76, intraweek Rs -253, benchmark Rs -409, nifty_calls Rs -1,032, snake Rs -1,062, snake_nonews Rs -1,432

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.