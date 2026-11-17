# Paper trading report

Updated 2026-11-17 13:48 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,689 | +10.85% | 0 | - | 236 |
| benchmark | 221,634 | +10.82% | 0 | - | 237 |
| snake_abs_exit | 214,697 | +7.35% | 2 | 50% | 345 |
| intraweek | 213,354 | +6.68% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,126 | +6.56% | 2 | 50% | 345 |
| oracle | 212,221 | +6.11% | 0 | - | 233 |
| intramonth | 211,673 | +5.84% | 0 | - | 235 |
| snake_abs | 209,961 | +4.98% | 1 | 100% | 255 |
| snake_abs_conv | 209,822 | +4.91% | 1 | 100% | 255 |
| snake_viper_wild | 209,202 | +4.60% | 14 | 50% | 2,496 |
| random_hold | 207,562 | +3.78% | 10 | 70% | 733 |
| snake_viper_tick | 205,627 | +2.81% | 13 | 46% | 2,299 |
| snake_anaconda | 205,504 | +2.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,907 | +0.45% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,741 | -9.63% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,139 (-4.43%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,058 | +1.48% |
| snake_viper_tick | +3,007 | +1.48% |
| intraweek | +2,088 | +0.99% |
| benchmark | +1,553 | +0.71% |
| snake_anaconda | +402 | +0.20% |
| snake_abs_exit | +288 | +0.13% |
| unified | +252 | +0.11% |
| oracle | +198 | +0.09% |
| benchmark_smallcap | +78 | +0.04% |
| intramonth | +54 | +0.03% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit_conv | -91 | -0.04% |
| snake_abs_conv | -167 | -0.08% |
| snake_abs | -172 | -0.08% |
| gold | -214 | -0.12% |
| random_hold | -231 | -0.11% |

Average per day so far: unified Rs +620, benchmark Rs +618, snake_abs_exit Rs +459, snake_abs_exit_conv Rs +410, intraweek Rs +382, oracle Rs +349, snake_viper_wild Rs +341, intramonth Rs +334, snake_abs_conv Rs +307, snake_abs Rs +302, snake_viper_tick Rs +234, random_hold Rs +216, snake_anaconda Rs +183, nifty_calls Rs +52, benchmark_smallcap Rs +29, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -550

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.