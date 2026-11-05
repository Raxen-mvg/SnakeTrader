# Paper trading report

Updated 2026-11-05 12:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,175 | +9.09% | 0 | - | 236 |
| snake_abs_exit_conv | 213,571 | +6.79% | 1 | 100% | 255 |
| snake_abs_exit | 213,277 | +6.64% | 1 | 100% | 260 |
| benchmark | 212,722 | +6.36% | 0 | - | 237 |
| intraweek | 210,991 | +5.50% | 25 | 48% | 2,757 |
| snake_abs | 210,457 | +5.23% | 1 | 100% | 255 |
| snake_abs_conv | 210,325 | +5.16% | 1 | 100% | 255 |
| intramonth | 209,973 | +4.99% | 0 | - | 235 |
| snake_viper_wild | 206,807 | +3.40% | 3 | 33% | 702 |
| random_hold | 206,684 | +3.34% | 8 | 62% | 649 |
| oracle | 204,171 | +2.08% | 0 | - | 233 |
| snake_viper_tick | 203,253 | +1.63% | 2 | 0% | 532 |
| snake_anaconda | 202,049 | +1.02% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,159 | -0.42% | 0 | - | 237 |
| gold | 194,008 | -3.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,031 (-4.98%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,963 | +1.90% |
| unified | +3,736 | +1.74% |
| random_hold | +3,375 | +1.66% |
| intramonth | +2,957 | +1.43% |
| gold | +2,614 | +1.37% |
| benchmark_smallcap | +2,489 | +1.26% |
| oracle | +2,379 | +1.18% |
| intraweek | +1,294 | +0.62% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,434 | -0.68% |
| snake_abs_exit_conv | -1,444 | -0.67% |
| snake_abs | -1,446 | -0.68% |
| snake_abs_exit | -1,624 | -0.76% |
| snake_anaconda | -1,771 | -0.87% |
| snake_viper_tick | -2,148 | -1.05% |
| snake_viper_wild | -2,223 | -1.06% |

Average per day so far: unified Rs +649, snake_abs_exit_conv Rs +543, snake_abs_exit Rs +531, benchmark Rs +454, snake_abs_conv Rs +413, snake_abs Rs +402, intraweek Rs +393, intramonth Rs +356, snake_viper_wild Rs +340, random_hold Rs +239, snake_viper_tick Rs +191, oracle Rs +149, snake_anaconda Rs +89, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -35, gold Rs -214, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.