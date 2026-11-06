# Paper trading report

Updated 2026-11-06 11:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,895 | +7.45% | 0 | - | 236 |
| benchmark | 214,619 | +7.31% | 0 | - | 237 |
| intraweek | 211,409 | +5.71% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,811 | +4.91% | 1 | 100% | 255 |
| snake_abs_exit | 209,597 | +4.80% | 1 | 100% | 260 |
| intramonth | 207,044 | +3.52% | 0 | - | 235 |
| snake_abs | 206,760 | +3.38% | 1 | 100% | 255 |
| snake_abs_conv | 206,595 | +3.30% | 1 | 100% | 255 |
| oracle | 204,890 | +2.44% | 0 | - | 233 |
| random_hold | 203,535 | +1.77% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,150 | -1.43% | 3 | 33% | 374 |
| snake_viper_wild | 196,104 | -1.95% | 3 | 33% | 702 |
| benchmark_smallcap | 194,944 | -2.53% | 0 | - | 237 |
| snake_viper_tick | 192,784 | -3.61% | 2 | 0% | 532 |
| gold | 189,947 | -5.03% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,580 (-6.21%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,991 | +0.95% |
| benchmark | +849 | +0.40% |
| oracle | +818 | +0.40% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -788 | -0.39% |
| intramonth | -905 | -0.43% |
| unified | -1,088 | -0.50% |
| benchmark_smallcap | -3,744 | -1.88% |
| gold | -4,274 | -2.20% |
| snake_abs | -4,929 | -2.33% |
| snake_abs_conv | -4,950 | -2.34% |
| snake_abs_exit_conv | -4,993 | -2.32% |
| snake_abs_exit | -5,062 | -2.36% |
| snake_anaconda | -5,329 | -2.63% |
| snake_viper_tick | -8,354 | -4.15% |
| snake_viper_wild | -8,552 | -4.18% |

Average per day so far: unified Rs +514, benchmark Rs +504, intraweek Rs +393, snake_abs_exit_conv Rs +377, snake_abs_exit Rs +369, snake_abs_conv Rs +254, snake_abs Rs +250, intramonth Rs +243, oracle Rs +169, random_hold Rs +122, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -119, snake_viper_wild Rs -186, benchmark_smallcap Rs -202, gold Rs -347, snake_viper_tick Rs -401, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.