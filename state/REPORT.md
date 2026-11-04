# Paper trading report

Updated 2026-11-04 11:55 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,842 | +6.92% | 0 | - | 236 |
| snake_abs_exit_conv | 208,307 | +4.15% | 1 | 100% | 255 |
| intraweek | 208,245 | +4.12% | 25 | 48% | 2,757 |
| snake_abs_exit | 208,170 | +4.08% | 1 | 100% | 260 |
| benchmark | 207,221 | +3.61% | 0 | - | 237 |
| snake_viper_wild | 206,771 | +3.39% | 3 | 33% | 702 |
| intramonth | 205,795 | +2.90% | 0 | - | 235 |
| snake_abs | 205,220 | +2.61% | 1 | 100% | 255 |
| snake_abs_conv | 205,068 | +2.53% | 1 | 100% | 255 |
| snake_viper_tick | 203,170 | +1.58% | 2 | 0% | 532 |
| random_hold | 202,545 | +1.27% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,824 | +0.41% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,242 | -1.38% | 3 | 33% | 361 |
| benchmark_smallcap | 194,697 | -2.65% | 0 | - | 237 |
| gold | 190,374 | -4.81% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,971 (-5.51%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,096 | +2.75% |
| snake_abs_exit | +4,156 | +2.04% |
| snake_abs_exit_conv | +3,968 | +1.94% |
| snake_abs_conv | +3,927 | +1.95% |
| snake_abs | +3,911 | +1.94% |
| snake_anaconda | +3,417 | +1.76% |
| intraweek | +3,160 | +1.54% |
| random_hold | +2,077 | +1.04% |
| unified | +1,841 | +0.87% |
| intramonth | +1,824 | +0.89% |
| benchmark_smallcap | +1,760 | +0.91% |
| oracle | +835 | +0.42% |
| benchmark | +520 | +0.25% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,997 | -1.93% |
| snake_viper_wild | -4,121 | -1.95% |

Average per day so far: unified Rs +513, snake_viper_wild Rs +356, snake_abs_exit_conv Rs +346, snake_abs_exit Rs +340, intraweek Rs +305, benchmark Rs +267, intramonth Rs +215, snake_abs_conv Rs +211, snake_abs Rs +209, snake_viper_tick Rs +198, random_hold Rs +94, nifty_calls Rs +68, oracle Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -125, benchmark_smallcap Rs -231, gold Rs -357, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.