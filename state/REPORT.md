# Paper trading report

Updated 2026-11-04 14:04 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,242 | +7.12% | 0 | - | 236 |
| snake_abs_exit_conv | 213,508 | +6.75% | 1 | 100% | 255 |
| snake_abs_exit | 213,385 | +6.69% | 1 | 100% | 260 |
| snake_abs | 210,401 | +5.20% | 1 | 100% | 255 |
| snake_abs_conv | 210,249 | +5.12% | 1 | 100% | 255 |
| intraweek | 209,974 | +4.99% | 25 | 48% | 2,757 |
| benchmark | 208,239 | +4.12% | 0 | - | 237 |
| snake_viper_wild | 207,820 | +3.91% | 3 | 33% | 702 |
| intramonth | 206,437 | +3.22% | 0 | - | 235 |
| snake_viper_tick | 204,192 | +2.10% | 2 | 0% | 532 |
| random_hold | 202,960 | +1.48% | 8 | 62% | 649 |
| snake_anaconda | 202,013 | +1.01% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,072 | +0.54% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,065 | -1.97% | 0 | - | 237 |
| gold | 191,229 | -4.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,692 (-5.15%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,371 | +4.59% |
| snake_abs_exit_conv | +9,169 | +4.49% |
| snake_abs_conv | +9,108 | +4.53% |
| snake_abs | +9,091 | +4.52% |
| snake_anaconda | +8,188 | +4.22% |
| gold | +5,951 | +3.21% |
| intraweek | +4,888 | +2.38% |
| benchmark_smallcap | +3,128 | +1.62% |
| random_hold | +2,492 | +1.24% |
| intramonth | +2,466 | +1.21% |
| unified | +2,241 | +1.06% |
| benchmark | +1,538 | +0.74% |
| oracle | +1,083 | +0.54% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,974 | -1.44% |
| snake_viper_wild | -3,073 | -1.46% |

Average per day so far: snake_abs_exit_conv Rs +563, snake_abs_exit Rs +558, unified Rs +527, snake_abs_conv Rs +427, snake_abs Rs +416, snake_viper_wild Rs +412, intraweek Rs +369, benchmark Rs +305, snake_viper_tick Rs +262, intramonth Rs +238, random_hold Rs +110, snake_anaconda Rs +91, nifty_calls Rs +68, oracle Rs +40, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -171, gold Rs -325, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.