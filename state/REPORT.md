# Paper trading report

Updated 2026-11-05 10:21 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,742 | +9.37% | 0 | - | 236 |
| snake_abs_exit_conv | 215,253 | +7.63% | 1 | 100% | 255 |
| snake_abs_exit | 214,978 | +7.49% | 1 | 100% | 260 |
| benchmark | 212,584 | +6.29% | 0 | - | 237 |
| snake_abs | 212,133 | +6.07% | 1 | 100% | 255 |
| snake_abs_conv | 211,984 | +5.99% | 1 | 100% | 255 |
| intraweek | 211,365 | +5.68% | 25 | 48% | 2,757 |
| intramonth | 210,569 | +5.28% | 0 | - | 235 |
| snake_viper_wild | 206,825 | +3.41% | 3 | 33% | 702 |
| random_hold | 206,810 | +3.40% | 8 | 62% | 649 |
| oracle | 204,575 | +2.29% | 0 | - | 233 |
| snake_viper_tick | 203,287 | +1.64% | 2 | 0% | 532 |
| snake_anaconda | 202,695 | +1.35% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,831 | -0.08% | 0 | - | 237 |
| gold | 195,126 | -2.44% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,720 (-4.64%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,302 | +2.01% |
| benchmark | +3,825 | +1.83% |
| gold | +3,732 | +1.95% |
| intramonth | +3,553 | +1.72% |
| random_hold | +3,501 | +1.72% |
| benchmark_smallcap | +3,161 | +1.61% |
| oracle | +2,782 | +1.38% |
| intraweek | +1,667 | +0.80% |
| snake_abs_exit_conv | +238 | +0.11% |
| snake_abs | +230 | +0.11% |
| snake_abs_conv | +226 | +0.11% |
| snake_abs_exit | +78 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -1,125 | -0.55% |
| snake_viper_tick | -2,114 | -1.03% |
| snake_viper_wild | -2,204 | -1.05% |

Average per day so far: unified Rs +669, snake_abs_exit_conv Rs +610, snake_abs_exit Rs +599, snake_abs_conv Rs +479, snake_abs Rs +467, benchmark Rs +449, intraweek Rs +406, intramonth Rs +377, snake_viper_wild Rs +341, random_hold Rs +243, snake_viper_tick Rs +193, oracle Rs +163, snake_anaconda Rs +117, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -7, gold Rs -174, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.