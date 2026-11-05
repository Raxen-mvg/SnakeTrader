# Paper trading report

Updated 2026-11-05 09:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,241 | +9.12% | 0 | - | 236 |
| snake_abs_exit_conv | 216,377 | +8.19% | 1 | 100% | 255 |
| snake_abs_exit | 216,106 | +8.05% | 1 | 100% | 260 |
| snake_abs | 213,248 | +6.62% | 1 | 100% | 255 |
| snake_abs_conv | 213,097 | +6.55% | 1 | 100% | 255 |
| benchmark | 212,798 | +6.40% | 0 | - | 237 |
| intraweek | 210,699 | +5.35% | 25 | 48% | 2,757 |
| intramonth | 210,167 | +5.08% | 0 | - | 235 |
| snake_viper_wild | 206,271 | +3.13% | 3 | 33% | 702 |
| random_hold | 205,658 | +2.83% | 8 | 62% | 649 |
| oracle | 204,199 | +2.10% | 0 | - | 233 |
| snake_anaconda | 203,374 | +1.69% | 3 | 33% | 374 |
| snake_viper_tick | 202,741 | +1.37% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,540 | -0.23% | 0 | - | 237 |
| gold | 195,126 | -2.44% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,773 (-4.61%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,039 | +1.94% |
| unified | +3,801 | +1.77% |
| gold | +3,732 | +1.95% |
| intramonth | +3,152 | +1.52% |
| benchmark_smallcap | +2,870 | +1.46% |
| oracle | +2,407 | +1.19% |
| random_hold | +2,349 | +1.16% |
| snake_abs_exit_conv | +1,362 | +0.63% |
| snake_abs | +1,345 | +0.64% |
| snake_abs_conv | +1,339 | +0.63% |
| snake_abs_exit | +1,205 | +0.56% |
| intraweek | +1,001 | +0.48% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -446 | -0.22% |
| snake_viper_tick | -2,660 | -1.29% |
| snake_viper_wild | -2,759 | -1.32% |

Average per day so far: snake_abs_exit_conv Rs +655, unified Rs +651, snake_abs_exit Rs +644, snake_abs_conv Rs +524, snake_abs Rs +510, benchmark Rs +457, intraweek Rs +382, intramonth Rs +363, snake_viper_wild Rs +314, random_hold Rs +202, snake_viper_tick Rs +161, oracle Rs +150, snake_anaconda Rs +147, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -19, gold Rs -174, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.