# Paper trading report

Updated 2026-11-04 11:16 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 211,260 | +5.63% | 0 | - | 236 |
| snake_abs_exit_conv | 208,526 | +4.26% | 1 | 100% | 255 |
| snake_abs_exit | 208,373 | +4.19% | 1 | 100% | 260 |
| intraweek | 207,860 | +3.93% | 25 | 48% | 2,757 |
| benchmark | 207,604 | +3.80% | 0 | - | 237 |
| snake_viper_wild | 206,795 | +3.40% | 3 | 33% | 702 |
| snake_abs | 205,437 | +2.72% | 1 | 100% | 255 |
| snake_abs_conv | 205,283 | +2.64% | 1 | 100% | 255 |
| intramonth | 204,588 | +2.29% | 0 | - | 235 |
| snake_viper_tick | 203,191 | +1.60% | 2 | 0% | 532 |
| random_hold | 201,869 | +0.93% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,124 | +0.06% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,281 | -1.36% | 3 | 33% | 361 |
| benchmark_smallcap | 194,585 | -2.71% | 0 | - | 237 |
| gold | 189,240 | -5.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,193 (-5.90%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,358 | +2.14% |
| snake_abs_exit_conv | +4,187 | +2.05% |
| snake_abs_conv | +4,142 | +2.06% |
| snake_abs | +4,128 | +2.05% |
| gold | +3,962 | +2.14% |
| snake_anaconda | +3,456 | +1.78% |
| intraweek | +2,775 | +1.35% |
| benchmark_smallcap | +1,648 | +0.85% |
| random_hold | +1,401 | +0.70% |
| benchmark | +903 | +0.44% |
| intramonth | +617 | +0.30% |
| oracle | +134 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -741 | -0.35% |
| snake_viper_tick | -3,975 | -1.92% |
| snake_viper_wild | -4,098 | -1.94% |

Average per day so far: unified Rs +417, snake_viper_wild Rs +358, snake_abs_exit_conv Rs +355, snake_abs_exit Rs +349, intraweek Rs +291, benchmark Rs +282, snake_abs_conv Rs +220, snake_abs Rs +217, snake_viper_tick Rs +199, intramonth Rs +170, random_hold Rs +69, nifty_calls Rs +68, oracle Rs +5, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -124, benchmark_smallcap Rs -235, gold Rs -399, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.