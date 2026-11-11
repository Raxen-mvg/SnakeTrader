# Paper trading report

Updated 2026-11-11 13:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,742 | +10.37% | 0 | - | 236 |
| benchmark | 220,440 | +10.22% | 0 | - | 237 |
| snake_abs_exit_conv | 218,486 | +9.24% | 2 | 50% | 345 |
| snake_abs_exit | 217,450 | +8.72% | 2 | 50% | 345 |
| snake_abs | 215,040 | +7.52% | 1 | 100% | 255 |
| snake_abs_conv | 214,887 | +7.44% | 1 | 100% | 255 |
| intraweek | 213,591 | +6.79% | 30 | 53% | 3,302 |
| oracle | 212,034 | +6.02% | 0 | - | 233 |
| intramonth | 211,697 | +5.85% | 0 | - | 235 |
| random_hold | 207,057 | +3.53% | 9 | 67% | 709 |
| snake_viper_wild | 205,772 | +2.89% | 10 | 50% | 1,825 |
| snake_anaconda | 205,352 | +2.68% | 3 | 33% | 374 |
| snake_viper_tick | 202,258 | +1.13% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,345 | +0.67% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,963 | -5.02% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,520 (-4.24%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,342 | +4.22% |
| snake_viper_tick | +8,182 | +4.22% |
| snake_abs_exit_conv | +6,577 | +3.10% |
| snake_anaconda | +5,886 | +2.95% |
| snake_abs_exit | +5,466 | +2.58% |
| snake_abs_conv | +5,410 | +2.58% |
| snake_abs | +5,393 | +2.57% |
| benchmark_smallcap | +3,172 | +1.60% |
| benchmark | +2,349 | +1.08% |
| oracle | +2,115 | +1.01% |
| random_hold | +2,096 | +1.02% |
| intramonth | +1,087 | +0.52% |
| unified | +995 | +0.45% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -951 | -0.44% |
| gold | -2,170 | -1.13% |

Average per day so far: unified Rs +669, snake_abs_exit_conv Rs +660, benchmark Rs +659, snake_abs_exit Rs +623, snake_abs_conv Rs +532, snake_abs Rs +519, intraweek Rs +438, oracle Rs +388, intramonth Rs +377, snake_viper_wild Rs +251, random_hold Rs +228, snake_anaconda Rs +206, snake_viper_tick Rs +113, nifty_calls Rs +59, benchmark_smallcap Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -324, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.