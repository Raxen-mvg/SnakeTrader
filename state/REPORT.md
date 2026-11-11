# Paper trading report

Updated 2026-11-11 14:03 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,374 | +10.19% | 0 | - | 236 |
| benchmark | 220,127 | +10.06% | 0 | - | 237 |
| snake_abs_exit_conv | 216,589 | +8.29% | 2 | 50% | 345 |
| snake_abs_exit | 215,814 | +7.91% | 2 | 50% | 345 |
| snake_abs | 213,763 | +6.88% | 1 | 100% | 255 |
| snake_abs_conv | 213,592 | +6.80% | 1 | 100% | 255 |
| intraweek | 213,525 | +6.76% | 30 | 53% | 3,302 |
| oracle | 211,837 | +5.92% | 0 | - | 233 |
| intramonth | 211,372 | +5.69% | 0 | - | 235 |
| random_hold | 207,027 | +3.51% | 9 | 67% | 709 |
| snake_viper_wild | 205,288 | +2.64% | 10 | 50% | 1,825 |
| snake_anaconda | 203,564 | +1.78% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,785 | +0.89% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,120 | +0.56% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,766 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,208 (-4.40%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,858 | +3.98% |
| snake_viper_tick | +7,708 | +3.97% |
| snake_abs_exit_conv | +4,680 | +2.21% |
| snake_abs | +4,117 | +1.96% |
| snake_abs_conv | +4,115 | +1.96% |
| snake_anaconda | +4,097 | +2.05% |
| snake_abs_exit | +3,831 | +1.81% |
| benchmark_smallcap | +2,948 | +1.49% |
| random_hold | +2,066 | +1.01% |
| benchmark | +2,035 | +0.93% |
| oracle | +1,919 | +0.91% |
| intramonth | +763 | +0.36% |
| unified | +628 | +0.29% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,016 | -0.47% |
| gold | -2,367 | -1.23% |

Average per day so far: unified Rs +657, benchmark Rs +649, snake_abs_exit_conv Rs +592, snake_abs_exit Rs +565, snake_abs_conv Rs +485, snake_abs Rs +475, intraweek Rs +436, oracle Rs +382, intramonth Rs +367, snake_viper_wild Rs +230, random_hold Rs +227, snake_anaconda Rs +137, snake_viper_tick Rs +89, nifty_calls Rs +59, benchmark_smallcap Rs +41, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -330, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.