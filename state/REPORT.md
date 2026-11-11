# Paper trading report

Updated 2026-11-11 14:38 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,336 | +10.17% | 0 | - | 236 |
| benchmark | 220,066 | +10.03% | 0 | - | 237 |
| snake_abs_exit_conv | 217,357 | +8.68% | 2 | 50% | 345 |
| snake_abs_exit | 216,536 | +8.27% | 2 | 50% | 345 |
| snake_abs | 214,093 | +7.05% | 1 | 100% | 255 |
| snake_abs_conv | 213,929 | +6.96% | 1 | 100% | 255 |
| intraweek | 213,710 | +6.86% | 30 | 53% | 3,302 |
| oracle | 211,841 | +5.92% | 0 | - | 233 |
| intramonth | 211,165 | +5.58% | 0 | - | 235 |
| random_hold | 207,195 | +3.60% | 9 | 67% | 709 |
| snake_viper_wild | 206,657 | +3.33% | 10 | 50% | 1,825 |
| snake_anaconda | 204,267 | +2.13% | 3 | 33% | 374 |
| snake_viper_tick | 203,125 | +1.56% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,289 | +0.64% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,520 | -5.24% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,272 (-4.36%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,227 | +4.67% |
| snake_viper_tick | +9,048 | +4.66% |
| snake_abs_exit_conv | +5,448 | +2.57% |
| snake_anaconda | +4,801 | +2.41% |
| snake_abs_exit | +4,552 | +2.15% |
| snake_abs_conv | +4,451 | +2.12% |
| snake_abs | +4,447 | +2.12% |
| benchmark_smallcap | +3,116 | +1.57% |
| random_hold | +2,235 | +1.09% |
| benchmark | +1,974 | +0.91% |
| oracle | +1,922 | +0.92% |
| unified | +589 | +0.27% |
| intramonth | +556 | +0.26% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -832 | -0.39% |
| gold | -2,614 | -1.36% |

Average per day so far: unified Rs +656, benchmark Rs +647, snake_abs_exit_conv Rs +620, snake_abs_exit Rs +591, snake_abs_conv Rs +497, snake_abs Rs +486, intraweek Rs +442, oracle Rs +382, intramonth Rs +360, snake_viper_wild Rs +289, random_hold Rs +232, snake_anaconda Rs +164, snake_viper_tick Rs +156, nifty_calls Rs +59, benchmark_smallcap Rs +48, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -338, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.