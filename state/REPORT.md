# Paper trading report

Updated 2026-11-05 14:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,206 | +8.10% | 0 | - | 236 |
| snake_abs_exit_conv | 214,161 | +7.08% | 1 | 100% | 255 |
| benchmark | 214,007 | +7.00% | 0 | - | 237 |
| snake_abs_exit | 213,918 | +6.96% | 1 | 100% | 260 |
| snake_abs | 211,046 | +5.52% | 1 | 100% | 255 |
| snake_abs_conv | 210,909 | +5.45% | 1 | 100% | 255 |
| intraweek | 210,215 | +5.11% | 25 | 48% | 2,757 |
| intramonth | 207,790 | +3.90% | 0 | - | 235 |
| snake_viper_wild | 206,195 | +3.10% | 3 | 33% | 702 |
| random_hold | 205,100 | +2.55% | 8 | 62% | 649 |
| oracle | 203,638 | +1.82% | 0 | - | 233 |
| snake_viper_tick | 202,648 | +1.32% | 2 | 0% | 532 |
| snake_anaconda | 202,318 | +1.16% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| gold | 194,139 | -2.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,604 (-5.20%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,248 | +2.51% |
| gold | +2,745 | +1.43% |
| benchmark_smallcap | +2,545 | +1.29% |
| oracle | +1,846 | +0.92% |
| random_hold | +1,791 | +0.88% |
| unified | +1,767 | +0.82% |
| intramonth | +774 | +0.37% |
| intraweek | +517 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -850 | -0.40% |
| snake_abs_exit_conv | -854 | -0.40% |
| snake_abs | -857 | -0.40% |
| snake_abs_exit | -982 | -0.46% |
| snake_anaconda | -1,502 | -0.74% |
| snake_viper_tick | -2,752 | -1.34% |
| snake_viper_wild | -2,835 | -1.36% |

Average per day so far: unified Rs +579, snake_abs_exit_conv Rs +566, snake_abs_exit Rs +557, benchmark Rs +500, snake_abs_conv Rs +436, snake_abs Rs +425, intraweek Rs +365, snake_viper_wild Rs +310, intramonth Rs +278, random_hold Rs +182, snake_viper_tick Rs +156, oracle Rs +130, snake_anaconda Rs +101, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -209, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.