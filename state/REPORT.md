# Paper trading report

Updated 2026-11-11 10:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,068 | +10.53% | 0 | - | 237 |
| unified | 220,489 | +10.24% | 0 | - | 236 |
| snake_abs_exit_conv | 216,729 | +8.37% | 2 | 50% | 345 |
| intraweek | 215,316 | +7.66% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,774 | +7.39% | 2 | 50% | 345 |
| snake_abs | 213,193 | +6.60% | 1 | 100% | 255 |
| snake_abs_conv | 213,033 | +6.52% | 1 | 100% | 255 |
| oracle | 211,180 | +5.59% | 0 | - | 233 |
| intramonth | 210,993 | +5.50% | 0 | - | 235 |
| random_hold | 206,403 | +3.20% | 9 | 67% | 709 |
| snake_anaconda | 202,660 | +1.33% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,513 | +0.76% | 0 | - | 237 |
| snake_viper_wild | 200,758 | +0.38% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,348 | -1.33% | 9 | 44% | 1,639 |
| gold | 189,207 | -5.40% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,340 (-4.33%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,820 | +2.27% |
| snake_abs_conv | +3,555 | +1.70% |
| snake_abs | +3,546 | +1.69% |
| benchmark_smallcap | +3,341 | +1.69% |
| snake_viper_wild | +3,328 | +1.69% |
| snake_viper_tick | +3,272 | +1.69% |
| snake_anaconda | +3,194 | +1.60% |
| benchmark | +2,976 | +1.36% |
| snake_abs_exit | +2,790 | +1.32% |
| random_hold | +1,442 | +0.70% |
| oracle | +1,261 | +0.60% |
| intraweek | +774 | +0.36% |
| unified | +742 | +0.34% |
| intramonth | +384 | +0.18% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,926 | -1.52% |

Average per day so far: benchmark Rs +680, unified Rs +661, snake_abs_exit_conv Rs +597, snake_abs_exit Rs +528, intraweek Rs +494, snake_abs_conv Rs +465, snake_abs Rs +455, oracle Rs +361, intramonth Rs +355, random_hold Rs +207, snake_anaconda Rs +102, nifty_calls Rs +59, benchmark_smallcap Rs +56, snake_viper_wild Rs +33, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -133, gold Rs -348, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.