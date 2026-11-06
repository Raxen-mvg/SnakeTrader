# Paper trading report

Updated 2026-11-06 11:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,751 | +7.38% | 0 | - | 236 |
| benchmark | 214,259 | +7.13% | 0 | - | 237 |
| intraweek | 210,706 | +5.35% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,714 | +4.86% | 1 | 100% | 255 |
| snake_abs_exit | 209,501 | +4.75% | 1 | 100% | 260 |
| snake_abs | 206,669 | +3.33% | 1 | 100% | 255 |
| intramonth | 206,659 | +3.33% | 0 | - | 235 |
| snake_abs_conv | 206,499 | +3.25% | 1 | 100% | 255 |
| oracle | 204,669 | +2.33% | 0 | - | 233 |
| random_hold | 203,279 | +1.64% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,351 | -1.32% | 3 | 33% | 702 |
| snake_anaconda | 196,914 | -1.54% | 3 | 33% | 374 |
| benchmark_smallcap | 194,361 | -2.82% | 0 | - | 237 |
| snake_viper_tick | 194,008 | -3.00% | 2 | 0% | 532 |
| gold | 189,783 | -5.11% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,407 (-6.30%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,288 | +0.61% |
| oracle | +597 | +0.29% |
| benchmark | +490 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,044 | -0.51% |
| unified | -1,232 | -0.57% |
| intramonth | -1,290 | -0.62% |
| benchmark_smallcap | -4,327 | -2.18% |
| gold | -4,439 | -2.29% |
| snake_abs | -5,019 | -2.37% |
| snake_abs_conv | -5,046 | -2.38% |
| snake_abs_exit_conv | -5,090 | -2.37% |
| snake_abs_exit | -5,158 | -2.40% |
| snake_anaconda | -5,565 | -2.75% |
| snake_viper_tick | -7,130 | -3.54% |
| snake_viper_wild | -7,305 | -3.57% |

Average per day so far: unified Rs +509, benchmark Rs +492, snake_abs_exit_conv Rs +374, intraweek Rs +369, snake_abs_exit Rs +365, snake_abs_conv Rs +250, snake_abs Rs +247, intramonth Rs +230, oracle Rs +161, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -126, snake_anaconda Rs -129, benchmark_smallcap Rs -226, snake_viper_tick Rs -333, gold Rs -352, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.