# Paper trading report

Updated 2026-11-17 10:58 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,873 | +10.94% | 0 | - | 236 |
| benchmark | 221,680 | +10.84% | 0 | - | 237 |
| snake_abs_exit | 215,711 | +7.86% | 2 | 50% | 345 |
| intraweek | 214,077 | +7.04% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,797 | +6.90% | 2 | 50% | 345 |
| oracle | 212,731 | +6.37% | 0 | - | 233 |
| intramonth | 211,805 | +5.90% | 0 | - | 235 |
| snake_abs | 210,317 | +5.16% | 1 | 100% | 255 |
| snake_abs_conv | 210,168 | +5.08% | 1 | 100% | 255 |
| random_hold | 208,266 | +4.13% | 10 | 70% | 733 |
| snake_viper_wild | 207,303 | +3.65% | 14 | 50% | 2,496 |
| snake_anaconda | 205,775 | +2.89% | 3 | 33% | 374 |
| snake_viper_tick | 203,758 | +1.88% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,241 | +1.12% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,678 | -9.16% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,522 (-4.24%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,812 | +1.33% |
| benchmark | +1,599 | +0.73% |
| benchmark_smallcap | +1,412 | +0.70% |
| snake_abs_exit | +1,301 | +0.61% |
| snake_viper_wild | +1,158 | +0.56% |
| snake_viper_tick | +1,139 | +0.56% |
| gold | +723 | +0.40% |
| oracle | +708 | +0.33% |
| snake_anaconda | +672 | +0.33% |
| snake_abs_exit_conv | +580 | +0.27% |
| random_hold | +473 | +0.23% |
| unified | +435 | +0.20% |
| intramonth | +186 | +0.09% |
| snake_abs | +183 | +0.09% |
| snake_abs_conv | +178 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +625, benchmark Rs +619, snake_abs_exit Rs +491, snake_abs_exit_conv Rs +431, intraweek Rs +402, oracle Rs +364, intramonth Rs +337, snake_abs_conv Rs +318, snake_abs Rs +313, snake_viper_wild Rs +270, random_hold Rs +236, snake_anaconda Rs +192, snake_viper_tick Rs +157, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -523

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.