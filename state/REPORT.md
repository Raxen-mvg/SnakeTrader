# Paper trading report

Updated 2026-11-11 13:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,660 | +10.33% | 0 | - | 236 |
| benchmark | 220,517 | +10.26% | 0 | - | 237 |
| snake_abs_exit_conv | 218,487 | +9.24% | 2 | 50% | 345 |
| snake_abs_exit | 217,430 | +8.71% | 2 | 50% | 345 |
| snake_abs | 215,003 | +7.50% | 1 | 100% | 255 |
| snake_abs_conv | 214,850 | +7.42% | 1 | 100% | 255 |
| intraweek | 213,670 | +6.83% | 30 | 53% | 3,302 |
| oracle | 211,950 | +5.97% | 0 | - | 233 |
| intramonth | 211,605 | +5.80% | 0 | - | 235 |
| random_hold | 207,004 | +3.50% | 9 | 67% | 709 |
| snake_viper_wild | 205,658 | +2.83% | 10 | 50% | 1,825 |
| snake_anaconda | 205,280 | +2.64% | 3 | 33% | 374 |
| snake_viper_tick | 202,147 | +1.07% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,390 | +0.69% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,013 | -4.99% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,490 (-4.26%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,228 | +4.17% |
| snake_viper_tick | +8,070 | +4.16% |
| snake_abs_exit_conv | +6,579 | +3.10% |
| snake_anaconda | +5,814 | +2.92% |
| snake_abs_exit | +5,446 | +2.57% |
| snake_abs_conv | +5,373 | +2.56% |
| snake_abs | +5,356 | +2.56% |
| benchmark_smallcap | +3,217 | +1.62% |
| benchmark | +2,425 | +1.11% |
| random_hold | +2,043 | +1.00% |
| oracle | +2,031 | +0.97% |
| intramonth | +996 | +0.47% |
| unified | +913 | +0.42% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -872 | -0.41% |
| gold | -2,121 | -1.10% |

Average per day so far: unified Rs +666, benchmark Rs +662, snake_abs_exit_conv Rs +660, snake_abs_exit Rs +622, snake_abs_conv Rs +530, snake_abs Rs +517, intraweek Rs +441, oracle Rs +385, intramonth Rs +374, snake_viper_wild Rs +246, random_hold Rs +226, snake_anaconda Rs +203, snake_viper_tick Rs +107, nifty_calls Rs +59, benchmark_smallcap Rs +51, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -322, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.