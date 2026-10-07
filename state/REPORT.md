# Paper trading report

Updated 2026-10-07 12:34 IST. Model picks as of 2026-10-01. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 206,556 | +3.28% | 0 | - | 236 |
| snake_abs_exit_conv | 206,102 | +3.05% | 0 | - | 236 |
| snake_abs_exit | 206,088 | +3.04% | 0 | - | 235 |
| snake_anaconda | 204,208 | +2.10% | 0 | - | 236 |
| snake_abs | 203,033 | +1.52% | 0 | - | 236 |
| snake_abs_conv | 202,869 | +1.43% | 0 | - | 236 |
| random_hold | 202,828 | +1.41% | 2 | 50% | 362 |
| benchmark_smallcap | 202,477 | +1.24% | 0 | - | 237 |
| intramonth | 202,443 | +1.22% | 0 | - | 235 |
| oracle | 201,938 | +0.97% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 199,351 | -0.33% | 0 | - | 237 |
| intraweek | 198,690 | -0.66% | 5 | 40% | 748 |
| benchmark | 197,659 | -1.17% | 0 | - | 237 |
| snake | 193,875 | -3.06% | 0 | - | 234 |
| nifty_calls | 192,776 | -3.61% | 1 | 0% | 50 |
| snake_nonews | 192,709 | -3.65% | 0 | - | 231 |

Combined allocator (virtual): Rs 202,153 (+1.08%).

Profit on 2026-10-07:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +5,305 | +2.64% |
| intramonth | +2,698 | +1.35% |
| random_hold | +2,470 | +1.23% |
| snake_anaconda | +1,527 | +0.75% |
| snake_abs | +591 | +0.29% |
| snake_abs_exit_conv | +568 | +0.28% |
| snake_abs_exit | +559 | +0.27% |
| snake_abs_conv | +544 | +0.27% |
| oracle | +425 | +0.21% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold | -345 | -0.17% |
| benchmark | -451 | -0.23% |
| benchmark_smallcap | -504 | -0.25% |
| intraweek | -646 | -0.32% |
| snake | -1,559 | -0.80% |
| snake_nonews | -2,535 | -1.30% |

Average per day so far: snake_abs_exit_conv Rs +1,526, snake_abs_exit Rs +1,522, snake_anaconda Rs +1,403, unified Rs +937, benchmark_smallcap Rs +826, snake_abs_conv Rs +717, snake_abs Rs +607, random_hold Rs +404, intramonth Rs +349, oracle Rs +277, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, gold Rs -93, intraweek Rs -187, benchmark Rs -334, snake Rs -1,021, nifty_calls Rs -1,032, snake_nonews Rs -1,458

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.