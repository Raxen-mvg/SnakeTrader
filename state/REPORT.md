# Paper trading report

Updated 2026-11-05 13:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,651 | +8.33% | 0 | - | 236 |
| snake_abs_exit_conv | 214,328 | +7.16% | 1 | 100% | 255 |
| snake_abs_exit | 214,100 | +7.05% | 1 | 100% | 260 |
| benchmark | 213,915 | +6.96% | 0 | - | 237 |
| intraweek | 211,249 | +5.62% | 25 | 48% | 2,757 |
| snake_abs | 211,206 | +5.60% | 1 | 100% | 255 |
| snake_abs_conv | 211,072 | +5.54% | 1 | 100% | 255 |
| intramonth | 208,389 | +4.19% | 0 | - | 235 |
| snake_viper_wild | 206,574 | +3.29% | 3 | 33% | 702 |
| random_hold | 205,415 | +2.71% | 8 | 62% | 649 |
| oracle | 203,652 | +1.83% | 0 | - | 233 |
| snake_viper_tick | 203,025 | +1.51% | 2 | 0% | 532 |
| snake_anaconda | 202,473 | +1.24% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,125 | -0.44% | 0 | - | 237 |
| gold | 194,090 | -2.96% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,983 (-5.01%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,156 | +2.47% |
| gold | +2,696 | +1.41% |
| benchmark_smallcap | +2,455 | +1.25% |
| unified | +2,212 | +1.03% |
| random_hold | +2,106 | +1.04% |
| oracle | +1,859 | +0.92% |
| intraweek | +1,551 | +0.74% |
| intramonth | +1,373 | +0.66% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -686 | -0.32% |
| snake_abs_exit_conv | -687 | -0.32% |
| snake_abs | -698 | -0.33% |
| snake_abs_exit | -800 | -0.37% |
| snake_anaconda | -1,347 | -0.66% |
| snake_viper_tick | -2,376 | -1.16% |
| snake_viper_wild | -2,456 | -1.18% |

Average per day so far: unified Rs +595, snake_abs_exit_conv Rs +573, snake_abs_exit Rs +564, benchmark Rs +497, snake_abs_conv Rs +443, snake_abs Rs +431, intraweek Rs +402, snake_viper_wild Rs +329, intramonth Rs +300, random_hold Rs +193, snake_viper_tick Rs +178, oracle Rs +130, snake_anaconda Rs +108, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -211, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.