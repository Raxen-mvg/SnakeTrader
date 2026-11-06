# Paper trading report

Updated 2026-11-06 11:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,658 | +7.33% | 0 | - | 236 |
| benchmark | 214,405 | +7.20% | 0 | - | 237 |
| intraweek | 211,176 | +5.59% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,934 | +4.47% | 1 | 100% | 255 |
| snake_abs_exit | 208,725 | +4.36% | 1 | 100% | 260 |
| intramonth | 206,728 | +3.36% | 0 | - | 235 |
| snake_abs | 205,893 | +2.95% | 1 | 100% | 255 |
| snake_abs_conv | 205,726 | +2.86% | 1 | 100% | 255 |
| oracle | 204,451 | +2.23% | 0 | - | 233 |
| random_hold | 203,219 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,319 | -1.84% | 3 | 33% | 374 |
| snake_viper_wild | 195,421 | -2.29% | 3 | 33% | 702 |
| benchmark_smallcap | 194,585 | -2.71% | 0 | - | 237 |
| snake_viper_tick | 192,111 | -3.94% | 2 | 0% | 532 |
| gold | 190,210 | -4.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,154 (-6.42%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,758 | +0.84% |
| benchmark | +635 | +0.30% |
| oracle | +379 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,104 | -0.54% |
| intramonth | -1,220 | -0.59% |
| unified | -1,326 | -0.61% |
| gold | -4,011 | -2.06% |
| benchmark_smallcap | -4,103 | -2.06% |
| snake_abs | -5,795 | -2.74% |
| snake_abs_conv | -5,819 | -2.75% |
| snake_abs_exit_conv | -5,870 | -2.73% |
| snake_abs_exit | -5,934 | -2.76% |
| snake_anaconda | -6,160 | -3.04% |
| snake_viper_tick | -9,027 | -4.49% |
| snake_viper_wild | -9,235 | -4.51% |

Average per day so far: unified Rs +505, benchmark Rs +497, intraweek Rs +385, snake_abs_exit_conv Rs +344, snake_abs_exit Rs +336, intramonth Rs +232, snake_abs_conv Rs +220, snake_abs Rs +218, oracle Rs +153, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -153, benchmark_smallcap Rs -217, snake_viper_wild Rs -218, gold Rs -338, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -438

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.