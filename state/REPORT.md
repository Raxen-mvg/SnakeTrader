# Paper trading report

Updated 2026-11-04 12:34 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,798 | +6.90% | 0 | - | 236 |
| snake_abs_exit_conv | 212,735 | +6.37% | 1 | 100% | 255 |
| snake_abs_exit | 212,565 | +6.28% | 1 | 100% | 260 |
| snake_abs | 209,633 | +4.82% | 1 | 100% | 255 |
| snake_abs_conv | 209,479 | +4.74% | 1 | 100% | 255 |
| intraweek | 208,744 | +4.37% | 25 | 48% | 2,757 |
| benchmark | 207,604 | +3.80% | 0 | - | 237 |
| snake_viper_wild | 207,073 | +3.54% | 3 | 33% | 702 |
| intramonth | 206,132 | +3.07% | 0 | - | 235 |
| snake_viper_tick | 203,464 | +1.73% | 2 | 0% | 532 |
| random_hold | 202,728 | +1.36% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,108 | +0.55% | 3 | 33% | 361 |
| oracle | 201,029 | +0.52% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 194,843 | -2.58% | 0 | - | 237 |
| gold | 190,637 | -4.68% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,162 (-5.42%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,551 | +4.19% |
| snake_abs_exit_conv | +8,396 | +4.11% |
| snake_abs_conv | +8,338 | +4.14% |
| snake_abs | +8,324 | +4.13% |
| snake_anaconda | +7,283 | +3.76% |
| gold | +5,359 | +2.89% |
| intraweek | +3,659 | +1.78% |
| random_hold | +2,260 | +1.13% |
| intramonth | +2,161 | +1.06% |
| benchmark_smallcap | +1,906 | +0.99% |
| unified | +1,797 | +0.85% |
| oracle | +1,040 | +0.52% |
| benchmark | +903 | +0.44% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,702 | -1.79% |
| snake_viper_wild | -3,820 | -1.81% |

Average per day so far: snake_abs_exit_conv Rs +531, snake_abs_exit Rs +524, unified Rs +511, snake_abs_conv Rs +395, snake_abs Rs +385, snake_viper_wild Rs +372, intraweek Rs +324, benchmark Rs +282, intramonth Rs +227, snake_viper_tick Rs +217, random_hold Rs +101, nifty_calls Rs +68, snake_anaconda Rs +50, oracle Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -224, gold Rs -347, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.