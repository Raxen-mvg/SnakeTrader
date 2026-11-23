# Paper trading report

Updated 2026-11-23 11:31 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,197 | +12.10% | 0 | - | 236 |
| benchmark | 223,577 | +11.79% | 0 | - | 237 |
| intraweek | 212,990 | +6.50% | 40 | 55% | 4,400 |
| intramonth | 212,356 | +6.18% | 0 | - | 235 |
| oracle | 211,567 | +5.78% | 0 | - | 233 |
| random_hold | 210,116 | +5.06% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,185 | +3.59% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,194 | +3.10% | 2 | 50% | 345 |
| snake_abs | 204,671 | +2.34% | 1 | 100% | 255 |
| snake_abs_conv | 204,505 | +2.25% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,556 | +0.78% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,686 | -0.16% | 0 | - | 237 |
| snake_anaconda | 198,329 | -0.84% | 3 | 33% | 374 |
| snake_viper_tick | 198,116 | -0.94% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,726 | -15.14% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,473 (-4.76%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,677 | +1.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -423 | -0.20% |
| random_hold | -643 | -0.30% |
| oracle | -911 | -0.43% |
| benchmark_smallcap | -1,222 | -0.61% |
| snake_abs | -1,248 | -0.61% |
| snake_viper_tick | -1,256 | -0.63% |
| snake_viper_wild | -1,273 | -0.63% |
| snake_abs_conv | -1,278 | -0.62% |
| snake_abs_exit | -1,377 | -0.66% |
| benchmark | -1,561 | -0.69% |
| snake_anaconda | -1,577 | -0.79% |
| unified | -1,985 | -0.88% |
| intramonth | -2,648 | -1.23% |
| intraweek | -2,722 | -1.26% |

Average per day so far: unified Rs +620, benchmark Rs +605, intraweek Rs +333, intramonth Rs +317, oracle Rs +297, random_hold Rs +259, snake_abs_exit Rs +200, snake_abs_exit_conv Rs +172, snake_abs Rs +126, snake_abs_conv Rs +125, snake_viper_wild Rs +50, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -9, snake_anaconda Rs -49, snake_viper_tick Rs -67, snake_nonews Rs -300, snake Rs -320, gold Rs -776

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.