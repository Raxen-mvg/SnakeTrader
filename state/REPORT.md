# Paper trading report

Updated 2026-11-09 15:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,120 | +10.06% | 0 | - | 236 |
| benchmark | 218,084 | +9.04% | 0 | - | 237 |
| intraweek | 214,314 | +7.16% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,167 | +6.08% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,081 | +6.04% | 2 | 50% | 330 |
| intramonth | 210,671 | +5.34% | 0 | - | 235 |
| oracle | 209,743 | +4.87% | 0 | - | 233 |
| snake_abs | 209,626 | +4.81% | 1 | 100% | 255 |
| snake_abs_conv | 209,463 | +4.73% | 1 | 100% | 255 |
| random_hold | 204,734 | +2.37% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,641 | -0.18% | 3 | 33% | 374 |
| benchmark_smallcap | 198,441 | -0.78% | 0 | - | 237 |
| snake_viper_wild | 197,522 | -1.24% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,167 | -2.92% | 6 | 50% | 1,154 |
| gold | 192,133 | -3.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,362 (-4.82%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,511 | +2.09% |
| snake_abs_conv | +4,236 | +2.06% |
| snake_abs | +4,207 | +2.05% |
| intraweek | +3,952 | +1.88% |
| oracle | +3,916 | +1.90% |
| snake_abs_exit | +3,855 | +1.85% |
| snake_anaconda | +3,813 | +1.95% |
| snake_abs_exit_conv | +3,660 | +1.76% |
| intramonth | +3,068 | +1.48% |
| benchmark_smallcap | +1,648 | +0.84% |
| snake_viper_wild | +1,485 | +0.76% |
| snake_viper_tick | +1,458 | +0.76% |
| gold | +1,085 | +0.57% |
| random_hold | +828 | +0.41% |
| benchmark | +597 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +671, benchmark Rs +603, intraweek Rs +477, snake_abs_exit Rs +451, snake_abs_exit_conv Rs +447, intramonth Rs +356, snake_abs_conv Rs +350, snake_abs Rs +344, oracle Rs +325, random_hold Rs +158, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -14, benchmark_smallcap Rs -60, snake_viper_wild Rs -113, gold Rs -262, snake_viper_tick Rs -307, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.