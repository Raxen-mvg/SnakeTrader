# Paper trading report

Updated 2026-11-04 12:55 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,686 | +6.84% | 0 | - | 236 |
| snake_abs_exit_conv | 212,411 | +6.21% | 1 | 100% | 255 |
| snake_abs_exit | 212,280 | +6.14% | 1 | 100% | 260 |
| snake_abs | 209,310 | +4.66% | 1 | 100% | 255 |
| snake_abs_conv | 209,156 | +4.58% | 1 | 100% | 255 |
| intraweek | 208,939 | +4.47% | 25 | 48% | 2,757 |
| benchmark | 207,833 | +3.92% | 0 | - | 237 |
| snake_viper_wild | 207,141 | +3.57% | 3 | 33% | 702 |
| intramonth | 206,110 | +3.06% | 0 | - | 235 |
| snake_viper_tick | 203,531 | +1.76% | 2 | 0% | 532 |
| random_hold | 202,835 | +1.42% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,051 | +0.53% | 0 | - | 233 |
| snake_anaconda | 200,820 | +0.41% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 194,966 | -2.52% | 0 | - | 237 |
| gold | 190,703 | -4.65% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,182 (-5.41%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,265 | +4.05% |
| snake_abs_exit_conv | +8,073 | +3.95% |
| snake_abs_conv | +8,015 | +3.98% |
| snake_abs | +8,001 | +3.97% |
| snake_anaconda | +6,995 | +3.61% |
| gold | +5,425 | +2.93% |
| intraweek | +3,854 | +1.88% |
| random_hold | +2,367 | +1.18% |
| intramonth | +2,139 | +1.05% |
| benchmark_smallcap | +2,029 | +1.05% |
| unified | +1,685 | +0.80% |
| benchmark | +1,132 | +0.55% |
| oracle | +1,062 | +0.53% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,636 | -1.75% |
| snake_viper_wild | -3,752 | -1.78% |

Average per day so far: snake_abs_exit_conv Rs +517, snake_abs_exit Rs +512, unified Rs +507, snake_abs_conv Rs +382, snake_viper_wild Rs +376, snake_abs Rs +372, intraweek Rs +331, benchmark Rs +290, intramonth Rs +226, snake_viper_tick Rs +221, random_hold Rs +105, nifty_calls Rs +68, oracle Rs +39, snake_anaconda Rs +37, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -219, gold Rs -344, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.