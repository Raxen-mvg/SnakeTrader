# Paper trading report

Updated 2026-11-05 13:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,373 | +8.69% | 0 | - | 236 |
| snake_abs_exit_conv | 214,443 | +7.22% | 1 | 100% | 255 |
| snake_abs_exit | 214,166 | +7.08% | 1 | 100% | 260 |
| benchmark | 213,487 | +6.74% | 0 | - | 237 |
| snake_abs | 211,323 | +5.66% | 1 | 100% | 255 |
| snake_abs_conv | 211,188 | +5.59% | 1 | 100% | 255 |
| intraweek | 211,166 | +5.58% | 25 | 48% | 2,757 |
| intramonth | 209,333 | +4.67% | 0 | - | 235 |
| snake_viper_wild | 206,942 | +3.47% | 3 | 33% | 702 |
| random_hold | 206,012 | +3.01% | 8 | 62% | 649 |
| oracle | 203,963 | +1.98% | 0 | - | 233 |
| snake_viper_tick | 203,384 | +1.69% | 2 | 0% | 532 |
| snake_anaconda | 202,577 | +1.29% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,979 | -0.51% | 0 | - | 237 |
| gold | 194,139 | -2.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,212 (-4.89%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,728 | +2.27% |
| unified | +2,934 | +1.37% |
| gold | +2,745 | +1.43% |
| random_hold | +2,703 | +1.33% |
| intramonth | +2,317 | +1.12% |
| benchmark_smallcap | +2,309 | +1.17% |
| oracle | +2,171 | +1.08% |
| intraweek | +1,468 | +0.70% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -571 | -0.27% |
| snake_abs_exit_conv | -572 | -0.27% |
| snake_abs | -580 | -0.27% |
| snake_abs_exit | -734 | -0.34% |
| snake_anaconda | -1,244 | -0.61% |
| snake_viper_tick | -2,016 | -0.98% |
| snake_viper_wild | -2,088 | -1.00% |

Average per day so far: unified Rs +620, snake_abs_exit_conv Rs +578, snake_abs_exit Rs +567, benchmark Rs +482, snake_abs_conv Rs +448, snake_abs Rs +436, intraweek Rs +399, snake_viper_wild Rs +347, intramonth Rs +333, random_hold Rs +215, snake_viper_tick Rs +199, oracle Rs +142, snake_anaconda Rs +112, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -43, gold Rs -209, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.