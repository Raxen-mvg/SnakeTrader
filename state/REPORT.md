# Paper trading report

Updated 2026-11-11 09:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,068 | +10.53% | 0 | - | 237 |
| unified | 219,891 | +9.95% | 0 | - | 236 |
| snake_abs_exit_conv | 216,093 | +8.05% | 2 | 50% | 330 |
| snake_abs_exit | 215,083 | +7.54% | 2 | 50% | 308 |
| intraweek | 214,111 | +7.06% | 30 | 53% | 3,302 |
| snake_abs | 213,665 | +6.83% | 1 | 100% | 255 |
| snake_abs_conv | 213,505 | +6.75% | 1 | 100% | 255 |
| oracle | 211,016 | +5.51% | 0 | - | 233 |
| intramonth | 210,785 | +5.39% | 0 | - | 235 |
| random_hold | 205,956 | +2.98% | 9 | 67% | 709 |
| snake_anaconda | 202,267 | +1.13% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,008 | +0.50% | 0 | - | 237 |
| snake_viper_wild | 200,669 | +0.33% | 7 | 57% | 1,332 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,260 | -1.37% | 6 | 50% | 1,154 |
| gold | 189,700 | -5.15% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,932 (-4.53%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,184 | +1.98% |
| snake_abs_conv | +4,028 | +1.92% |
| snake_abs | +4,019 | +1.92% |
| snake_viper_wild | +3,238 | +1.64% |
| snake_viper_tick | +3,183 | +1.64% |
| snake_abs_exit | +3,099 | +1.46% |
| benchmark | +2,976 | +1.36% |
| benchmark_smallcap | +2,836 | +1.43% |
| snake_anaconda | +2,800 | +1.40% |
| oracle | +1,097 | +0.52% |
| random_hold | +995 | +0.49% |
| intramonth | +176 | +0.08% |
| unified | +144 | +0.07% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -431 | -0.20% |
| gold | -2,433 | -1.27% |

Average per day so far: benchmark Rs +680, unified Rs +642, snake_abs_exit_conv Rs +575, snake_abs_exit Rs +539, snake_abs_conv Rs +482, snake_abs Rs +471, intraweek Rs +455, oracle Rs +355, intramonth Rs +348, random_hold Rs +192, snake_anaconda Rs +87, nifty_calls Rs +59, benchmark_smallcap Rs +37, snake_viper_wild Rs +29, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -137, gold Rs -332, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.