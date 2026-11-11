# Paper trading report

Updated 2026-11-11 11:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,404 | +10.70% | 0 | - | 237 |
| unified | 220,311 | +10.15% | 0 | - | 236 |
| snake_abs_exit_conv | 216,484 | +8.24% | 2 | 50% | 345 |
| snake_abs_exit | 215,160 | +7.58% | 2 | 50% | 345 |
| intraweek | 214,017 | +7.01% | 30 | 53% | 3,302 |
| snake_abs | 213,334 | +6.67% | 1 | 100% | 255 |
| snake_abs_conv | 213,175 | +6.59% | 1 | 100% | 255 |
| oracle | 211,813 | +5.91% | 0 | - | 233 |
| intramonth | 211,206 | +5.60% | 0 | - | 235 |
| random_hold | 206,926 | +3.46% | 9 | 67% | 709 |
| snake_anaconda | 203,084 | +1.54% | 3 | 33% | 374 |
| benchmark_smallcap | 201,849 | +0.93% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,368 | +0.68% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,946 | -1.03% | 9 | 44% | 1,639 |
| gold | 189,799 | -5.10% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,217 (-4.39%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,576 | +2.16% |
| snake_viper_wild | +3,938 | +1.99% |
| snake_viper_tick | +3,869 | +1.99% |
| snake_abs_conv | +3,698 | +1.76% |
| snake_abs | +3,687 | +1.76% |
| benchmark_smallcap | +3,677 | +1.85% |
| snake_anaconda | +3,618 | +1.81% |
| benchmark | +3,312 | +1.52% |
| snake_abs_exit | +3,177 | +1.50% |
| random_hold | +1,965 | +0.96% |
| oracle | +1,894 | +0.90% |
| intramonth | +597 | +0.28% |
| unified | +564 | +0.26% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -525 | -0.24% |
| gold | -2,334 | -1.22% |

Average per day so far: benchmark Rs +690, unified Rs +655, snake_abs_exit_conv Rs +589, snake_abs_exit Rs +541, snake_abs_conv Rs +471, snake_abs Rs +460, intraweek Rs +452, oracle Rs +381, intramonth Rs +361, random_hold Rs +223, snake_anaconda Rs +119, benchmark_smallcap Rs +68, snake_viper_wild Rs +59, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -103, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.