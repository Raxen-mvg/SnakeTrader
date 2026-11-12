# Paper trading report

Updated 2026-11-12 12:35 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,515 | +10.76% | 0 | - | 236 |
| benchmark | 219,928 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 218,739 | +9.37% | 2 | 50% | 345 |
| snake_abs_exit | 217,739 | +8.87% | 2 | 50% | 345 |
| snake_abs | 215,813 | +7.91% | 1 | 100% | 255 |
| snake_abs_conv | 215,645 | +7.82% | 1 | 100% | 255 |
| intraweek | 214,826 | +7.41% | 30 | 53% | 3,302 |
| oracle | 213,274 | +6.64% | 0 | - | 233 |
| intramonth | 211,757 | +5.88% | 0 | - | 235 |
| random_hold | 208,019 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 207,118 | +3.56% | 10 | 50% | 1,825 |
| snake_anaconda | 206,530 | +3.27% | 3 | 33% | 374 |
| snake_viper_tick | 203,575 | +1.79% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,138 | +1.57% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,149 | -6.92% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,226 (-3.89%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,407 | +1.18% |
| benchmark_smallcap | +2,332 | +1.16% |
| snake_abs | +2,188 | +1.02% |
| snake_abs_conv | +2,187 | +1.02% |
| unified | +1,701 | +0.77% |
| intraweek | +1,693 | +0.79% |
| snake_abs_exit_conv | +1,587 | +0.73% |
| snake_abs_exit | +1,577 | +0.73% |
| oracle | +1,271 | +0.60% |
| random_hold | +908 | +0.44% |
| intramonth | +761 | +0.36% |
| benchmark | +666 | +0.30% |
| snake_viper_wild | +376 | +0.18% |
| snake_viper_tick | +366 | +0.18% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,436 | -1.81% |

Average per day so far: unified Rs +672, snake_abs_exit_conv Rs +646, benchmark Rs +623, snake_abs_exit Rs +612, snake_abs_conv Rs +539, snake_abs Rs +527, intraweek Rs +463, oracle Rs +415, intramonth Rs +367, snake_viper_wild Rs +297, random_hold Rs +251, snake_anaconda Rs +242, snake_viper_tick Rs +170, benchmark_smallcap Rs +112, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -433

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.