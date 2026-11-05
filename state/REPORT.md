# Paper trading report

Updated 2026-11-05 12:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,682 | +8.84% | 0 | - | 236 |
| snake_abs_exit_conv | 213,817 | +6.91% | 1 | 100% | 255 |
| snake_abs_exit | 213,502 | +6.75% | 1 | 100% | 260 |
| benchmark | 212,890 | +6.45% | 0 | - | 237 |
| intraweek | 210,772 | +5.39% | 25 | 48% | 2,757 |
| snake_abs | 210,704 | +5.35% | 1 | 100% | 255 |
| snake_abs_conv | 210,564 | +5.28% | 1 | 100% | 255 |
| intramonth | 209,417 | +4.71% | 0 | - | 235 |
| snake_viper_wild | 206,439 | +3.22% | 3 | 33% | 702 |
| random_hold | 206,325 | +3.16% | 8 | 62% | 649 |
| oracle | 203,869 | +1.93% | 0 | - | 233 |
| snake_viper_tick | 202,891 | +1.45% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,725 | +0.86% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,901 | -0.55% | 0 | - | 237 |
| gold | 194,156 | -2.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,912 (-5.04%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,131 | +1.98% |
| unified | +3,243 | +1.51% |
| random_hold | +3,016 | +1.48% |
| gold | +2,762 | +1.44% |
| intramonth | +2,401 | +1.16% |
| benchmark_smallcap | +2,231 | +1.13% |
| oracle | +2,077 | +1.03% |
| intraweek | +1,074 | +0.51% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,194 | -0.56% |
| snake_abs_exit_conv | -1,198 | -0.56% |
| snake_abs | -1,199 | -0.57% |
| snake_abs_exit | -1,398 | -0.65% |
| snake_anaconda | -2,095 | -1.03% |
| snake_viper_tick | -2,510 | -1.22% |
| snake_viper_wild | -2,591 | -1.24% |

Average per day so far: unified Rs +632, snake_abs_exit_conv Rs +553, snake_abs_exit Rs +540, benchmark Rs +460, snake_abs_conv Rs +423, snake_abs Rs +412, intraweek Rs +385, intramonth Rs +336, snake_viper_wild Rs +322, random_hold Rs +226, snake_viper_tick Rs +170, oracle Rs +138, snake_anaconda Rs +75, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -46, gold Rs -209, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.