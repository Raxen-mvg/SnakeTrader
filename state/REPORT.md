# Paper trading report

Updated 2026-11-12 13:38 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,112 | +10.56% | 0 | - | 236 |
| benchmark | 220,157 | +10.08% | 0 | - | 237 |
| snake_abs_exit_conv | 218,612 | +9.31% | 2 | 50% | 345 |
| snake_abs_exit | 217,555 | +8.78% | 2 | 50% | 345 |
| snake_abs | 215,578 | +7.79% | 1 | 100% | 255 |
| snake_abs_conv | 215,404 | +7.70% | 1 | 100% | 255 |
| intraweek | 214,544 | +7.27% | 30 | 53% | 3,302 |
| oracle | 213,121 | +6.56% | 0 | - | 233 |
| intramonth | 211,682 | +5.84% | 0 | - | 235 |
| random_hold | 208,030 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 207,547 | +3.77% | 10 | 50% | 1,825 |
| snake_anaconda | 206,357 | +3.18% | 3 | 33% | 374 |
| snake_viper_tick | 203,995 | +2.00% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,116 | -6.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,058 (-3.97%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,234 | +1.09% |
| benchmark_smallcap | +2,107 | +1.05% |
| snake_abs | +1,954 | +0.92% |
| snake_abs_conv | +1,946 | +0.91% |
| snake_abs_exit_conv | +1,461 | +0.67% |
| intraweek | +1,411 | +0.66% |
| snake_abs_exit | +1,393 | +0.64% |
| unified | +1,298 | +0.59% |
| oracle | +1,118 | +0.53% |
| random_hold | +919 | +0.44% |
| benchmark | +895 | +0.41% |
| snake_viper_wild | +805 | +0.39% |
| snake_viper_tick | +786 | +0.39% |
| intramonth | +686 | +0.33% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,469 | -1.83% |

Average per day so far: unified Rs +660, snake_abs_exit_conv Rs +642, benchmark Rs +630, snake_abs_exit Rs +605, snake_abs_conv Rs +531, snake_abs Rs +519, intraweek Rs +455, oracle Rs +410, intramonth Rs +365, snake_viper_wild Rs +314, random_hold Rs +251, snake_anaconda Rs +235, snake_viper_tick Rs +190, benchmark_smallcap Rs +104, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.