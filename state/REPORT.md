# Paper trading report

Updated 2026-11-04 10:04 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,729 | +6.37% | 0 | - | 236 |
| snake_abs_exit_conv | 209,620 | +4.81% | 1 | 100% | 255 |
| snake_abs_exit | 209,471 | +4.74% | 1 | 100% | 260 |
| benchmark | 208,484 | +4.24% | 0 | - | 237 |
| intraweek | 208,228 | +4.11% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,570 | +3.29% | 3 | 33% | 702 |
| snake_abs | 206,511 | +3.25% | 1 | 100% | 255 |
| snake_abs_conv | 206,361 | +3.18% | 1 | 100% | 255 |
| intramonth | 205,264 | +2.63% | 0 | - | 235 |
| snake_viper_tick | 202,968 | +1.48% | 2 | 0% | 532 |
| random_hold | 202,803 | +1.40% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,336 | +0.17% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,989 | -1.00% | 3 | 33% | 361 |
| benchmark_smallcap | 194,226 | -2.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,938 | -6.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,600 (-5.70%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +5,457 | +2.67% |
| snake_abs_exit_conv | +5,282 | +2.58% |
| snake_abs_conv | +5,220 | +2.60% |
| snake_abs | +5,202 | +2.58% |
| snake_anaconda | +4,165 | +2.15% |
| intraweek | +3,143 | +1.53% |
| random_hold | +2,335 | +1.17% |
| benchmark | +1,782 | +0.86% |
| gold | +1,660 | +0.90% |
| intramonth | +1,293 | +0.63% |
| benchmark_smallcap | +1,289 | +0.67% |
| unified | +729 | +0.34% |
| oracle | +346 | +0.17% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,199 | -2.03% |
| snake_viper_wild | -4,322 | -2.05% |

Average per day so far: unified Rs +471, snake_abs_exit_conv Rs +401, snake_abs_exit Rs +395, snake_viper_wild Rs +346, benchmark Rs +314, intraweek Rs +305, snake_abs_conv Rs +265, snake_abs Rs +260, intramonth Rs +195, snake_viper_tick Rs +185, random_hold Rs +104, nifty_calls Rs +68, oracle Rs +12, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -91, benchmark_smallcap Rs -251, snake_nonews Rs -444, snake Rs -467, gold Rs -484

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.