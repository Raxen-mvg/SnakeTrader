# Paper trading report

Updated 2026-11-04 10:00 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,069 | +6.54% | 0 | - | 236 |
| snake_abs_exit_conv | 209,160 | +4.58% | 1 | 100% | 255 |
| snake_abs_exit | 208,968 | +4.48% | 1 | 100% | 260 |
| intraweek | 208,497 | +4.25% | 25 | 48% | 2,757 |
| benchmark | 208,476 | +4.24% | 0 | - | 237 |
| snake_viper_wild | 206,585 | +3.29% | 3 | 33% | 702 |
| snake_abs | 206,062 | +3.03% | 1 | 100% | 255 |
| snake_abs_conv | 205,909 | +2.96% | 1 | 100% | 255 |
| intramonth | 205,611 | +2.81% | 0 | - | 235 |
| random_hold | 203,074 | +1.54% | 8 | 62% | 649 |
| snake_viper_tick | 202,983 | +1.49% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,252 | +0.13% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,641 | -1.18% | 3 | 33% | 361 |
| benchmark_smallcap | 194,338 | -2.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,988 | -6.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,762 (-5.62%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,953 | +2.43% |
| snake_abs_exit_conv | +4,822 | +2.36% |
| snake_abs_conv | +4,768 | +2.37% |
| snake_abs | +4,753 | +2.36% |
| snake_anaconda | +3,817 | +1.97% |
| intraweek | +3,412 | +1.66% |
| random_hold | +2,605 | +1.30% |
| benchmark | +1,775 | +0.86% |
| gold | +1,710 | +0.92% |
| intramonth | +1,640 | +0.80% |
| benchmark_smallcap | +1,401 | +0.73% |
| unified | +1,068 | +0.50% |
| oracle | +263 | +0.13% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,184 | -2.02% |
| snake_viper_wild | -4,308 | -2.04% |

Average per day so far: unified Rs +484, snake_abs_exit_conv Rs +382, snake_abs_exit Rs +374, snake_viper_wild Rs +347, intraweek Rs +315, benchmark Rs +314, snake_abs_conv Rs +246, snake_abs Rs +242, intramonth Rs +208, snake_viper_tick Rs +186, random_hold Rs +114, nifty_calls Rs +68, oracle Rs +9, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -107, benchmark_smallcap Rs -246, snake_nonews Rs -444, snake Rs -467, gold Rs -482

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.