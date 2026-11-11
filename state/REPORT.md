# Paper trading report

Updated 2026-11-11 14:24 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,614 | +10.31% | 0 | - | 236 |
| benchmark | 219,913 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 216,826 | +8.41% | 2 | 50% | 345 |
| snake_abs_exit | 216,165 | +8.08% | 2 | 50% | 345 |
| snake_abs | 213,991 | +7.00% | 1 | 100% | 255 |
| snake_abs_conv | 213,824 | +6.91% | 1 | 100% | 255 |
| intraweek | 213,023 | +6.51% | 30 | 53% | 3,302 |
| oracle | 211,870 | +5.93% | 0 | - | 233 |
| intramonth | 211,575 | +5.79% | 0 | - | 235 |
| random_hold | 207,091 | +3.54% | 9 | 67% | 709 |
| snake_viper_wild | 205,535 | +2.77% | 10 | 50% | 1,825 |
| snake_anaconda | 203,973 | +1.99% | 3 | 33% | 374 |
| snake_viper_tick | 202,026 | +1.01% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,120 | +0.56% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,618 | -5.19% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,217 (-4.39%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,105 | +4.11% |
| snake_viper_tick | +7,950 | +4.10% |
| snake_abs_exit_conv | +4,918 | +2.32% |
| snake_anaconda | +4,506 | +2.26% |
| snake_abs_conv | +4,347 | +2.08% |
| snake_abs | +4,344 | +2.07% |
| snake_abs_exit | +4,181 | +1.97% |
| benchmark_smallcap | +2,948 | +1.49% |
| random_hold | +2,130 | +1.04% |
| oracle | +1,952 | +0.93% |
| benchmark | +1,821 | +0.83% |
| intramonth | +966 | +0.46% |
| unified | +867 | +0.40% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,519 | -0.71% |
| gold | -2,515 | -1.31% |

Average per day so far: unified Rs +665, benchmark Rs +642, snake_abs_exit_conv Rs +601, snake_abs_exit Rs +577, snake_abs_conv Rs +494, snake_abs Rs +482, intraweek Rs +420, oracle Rs +383, intramonth Rs +373, snake_viper_wild Rs +241, random_hold Rs +229, snake_anaconda Rs +153, snake_viper_tick Rs +101, nifty_calls Rs +59, benchmark_smallcap Rs +41, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -335, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.