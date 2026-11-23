# Paper trading report

Updated 2026-11-23 09:56 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,580 | +12.79% | 0 | - | 236 |
| benchmark | 223,875 | +11.94% | 0 | - | 237 |
| intramonth | 213,420 | +6.71% | 0 | - | 235 |
| intraweek | 213,372 | +6.69% | 40 | 55% | 4,400 |
| oracle | 211,889 | +5.94% | 0 | - | 233 |
| random_hold | 210,400 | +5.20% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,352 | +4.18% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,672 | +3.34% | 2 | 50% | 345 |
| snake_abs | 205,429 | +2.71% | 1 | 100% | 255 |
| snake_abs_conv | 205,285 | +2.64% | 1 | 100% | 255 |
| snake_viper_wild | 203,693 | +1.85% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,218 | +0.11% | 15 | 47% | 2,625 |
| benchmark_smallcap | 200,112 | +0.06% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,529 | -0.24% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,183 | -15.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,148 (-4.43%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,134 | +0.68% |
| snake_viper_wild | +864 | +0.43% |
| snake_viper_tick | +846 | +0.42% |
| snake_abs_exit_conv | +55 | +0.03% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -210 | -0.10% |
| random_hold | -359 | -0.17% |
| snake_anaconda | -377 | -0.19% |
| snake_abs | -490 | -0.24% |
| snake_abs_conv | -498 | -0.24% |
| oracle | -590 | -0.28% |
| unified | -602 | -0.27% |
| benchmark_smallcap | -796 | -0.40% |
| benchmark | -1,262 | -0.56% |
| intramonth | -1,584 | -0.74% |
| intraweek | -2,340 | -1.08% |

Average per day so far: unified Rs +656, benchmark Rs +612, intramonth Rs +344, intraweek Rs +343, oracle Rs +305, random_hold Rs +267, snake_abs_exit Rs +232, snake_abs_exit_conv Rs +185, snake_abs_conv Rs +147, snake_abs Rs +147, snake_viper_wild Rs +119, nifty_calls Rs +47, snake_viper_tick Rs +8, benchmark_smallcap Rs +3, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_anaconda Rs -14, snake_nonews Rs -300, snake Rs -320, gold Rs -790

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.