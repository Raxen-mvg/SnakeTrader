# Paper trading report

Updated 2026-10-07 12:31 IST. Model picks as of 2026-10-01. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 206,667 | +3.33% | 0 | - | 236 |
| snake_abs_exit_conv | 205,777 | +2.89% | 0 | - | 236 |
| snake_abs_exit | 205,762 | +2.88% | 0 | - | 235 |
| snake_anaconda | 204,110 | +2.06% | 0 | - | 236 |
| random_hold | 202,852 | +1.43% | 2 | 50% | 362 |
| snake_abs | 202,708 | +1.35% | 0 | - | 236 |
| benchmark_smallcap | 202,555 | +1.28% | 0 | - | 237 |
| snake_abs_conv | 202,548 | +1.27% | 0 | - | 236 |
| intramonth | 202,537 | +1.27% | 0 | - | 235 |
| oracle | 201,903 | +0.95% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 199,268 | -0.37% | 0 | - | 237 |
| intraweek | 198,410 | -0.80% | 5 | 40% | 748 |
| benchmark | 197,659 | -1.17% | 0 | - | 237 |
| snake | 193,906 | -3.05% | 0 | - | 234 |
| nifty_calls | 192,776 | -3.61% | 1 | 0% | 50 |
| snake_nonews | 192,747 | -3.63% | 0 | - | 231 |

Combined allocator (virtual): Rs 202,044 (+1.02%).

Profit on 2026-10-07:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +5,416 | +2.69% |
| intramonth | +2,792 | +1.40% |
| random_hold | +2,494 | +1.25% |
| snake_anaconda | +1,429 | +0.70% |
| oracle | +389 | +0.19% |
| snake_abs | +265 | +0.13% |
| snake_abs_exit_conv | +243 | +0.12% |
| snake_abs_exit | +234 | +0.11% |
| snake_abs_conv | +223 | +0.11% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| benchmark_smallcap | -426 | -0.21% |
| gold | -427 | -0.21% |
| benchmark | -451 | -0.23% |
| intraweek | -925 | -0.46% |
| snake | -1,529 | -0.78% |
| snake_nonews | -2,498 | -1.28% |

Average per day so far: snake_abs_exit_conv Rs +1,444, snake_abs_exit Rs +1,441, snake_anaconda Rs +1,370, unified Rs +952, benchmark_smallcap Rs +852, snake_abs_conv Rs +637, snake_abs Rs +542, random_hold Rs +407, intramonth Rs +362, oracle Rs +272, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, gold Rs -105, intraweek Rs -227, benchmark Rs -334, snake Rs -1,016, nifty_calls Rs -1,032, snake_nonews Rs -1,451

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.