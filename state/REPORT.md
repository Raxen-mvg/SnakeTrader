# Paper trading report

Updated 2026-11-20 09:21 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,903 | +12.45% | 0 | - | 236 |
| benchmark | 222,139 | +11.07% | 0 | - | 237 |
| intramonth | 214,216 | +7.11% | 0 | - | 235 |
| intraweek | 212,742 | +6.37% | 35 | 54% | 3,851 |
| oracle | 212,133 | +6.07% | 0 | - | 233 |
| snake_abs_exit | 211,354 | +5.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 209,477 | +4.74% | 2 | 50% | 345 |
| random_hold | 208,445 | +4.22% | 10 | 70% | 733 |
| snake_abs | 207,799 | +3.90% | 1 | 100% | 255 |
| snake_abs_conv | 207,671 | +3.84% | 1 | 100% | 255 |
| snake_viper_wild | 206,515 | +3.26% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,990 | +1.50% | 15 | 47% | 2,625 |
| snake_anaconda | 202,074 | +1.04% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,011 | +0.01% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,684 | -16.66% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,582 (-4.21%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +288 | +0.13% |
| intramonth | +208 | +0.10% |
| oracle | +45 | +0.02% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -8 | -0.00% |
| intraweek | -147 | -0.07% |
| benchmark | -237 | -0.11% |
| snake_viper_tick | -987 | -0.48% |
| snake_viper_wild | -1,008 | -0.49% |
| snake_abs | -1,181 | -0.56% |
| snake_abs_conv | -1,189 | -0.57% |
| snake_anaconda | -1,389 | -0.68% |
| benchmark_smallcap | -1,457 | -0.72% |
| snake_abs_exit_conv | -1,588 | -0.75% |
| snake_abs_exit | -1,997 | -0.94% |
| gold | -8,088 | -4.63% |

Average per day so far: unified Rs +655, benchmark Rs +583, intramonth Rs +374, intraweek Rs +335, snake_abs_exit Rs +324, oracle Rs +319, snake_abs_exit_conv Rs +271, random_hold Rs +222, snake_abs_conv Rs +219, snake_viper_wild Rs +217, snake_abs Rs +217, snake_viper_tick Rs +111, snake_anaconda Rs +63, nifty_calls Rs +48, benchmark_smallcap Rs +0, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -877

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.