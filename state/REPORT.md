# Paper trading report

Updated 2026-11-04 14:16 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,831 | +7.42% | 0 | - | 236 |
| snake_abs_exit_conv | 214,057 | +7.03% | 1 | 100% | 255 |
| snake_abs_exit | 213,928 | +6.96% | 1 | 100% | 260 |
| snake_abs | 210,942 | +5.47% | 1 | 100% | 255 |
| snake_abs_conv | 210,794 | +5.40% | 1 | 100% | 255 |
| intraweek | 209,773 | +4.89% | 25 | 48% | 2,757 |
| benchmark | 208,223 | +4.11% | 0 | - | 237 |
| snake_viper_wild | 207,664 | +3.83% | 3 | 33% | 702 |
| intramonth | 206,779 | +3.39% | 0 | - | 235 |
| snake_viper_tick | 204,041 | +2.02% | 2 | 0% | 532 |
| random_hold | 203,210 | +1.60% | 8 | 62% | 649 |
| snake_anaconda | 202,517 | +1.26% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,079 | +0.54% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,964 | -2.02% | 0 | - | 237 |
| gold | 191,377 | -4.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,794 (-5.10%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,914 | +4.86% |
| snake_abs_exit_conv | +9,718 | +4.76% |
| snake_abs_conv | +9,653 | +4.80% |
| snake_abs | +9,633 | +4.79% |
| snake_anaconda | +8,692 | +4.49% |
| gold | +6,099 | +3.29% |
| intraweek | +4,687 | +2.29% |
| benchmark_smallcap | +3,027 | +1.57% |
| unified | +2,830 | +1.33% |
| intramonth | +2,808 | +1.38% |
| random_hold | +2,742 | +1.37% |
| benchmark | +1,522 | +0.74% |
| oracle | +1,090 | +0.55% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,126 | -1.51% |
| snake_viper_wild | -3,229 | -1.53% |

Average per day so far: snake_abs_exit_conv Rs +586, snake_abs_exit Rs +580, unified Rs +549, snake_abs_conv Rs +450, snake_abs Rs +438, snake_viper_wild Rs +403, intraweek Rs +362, benchmark Rs +305, snake_viper_tick Rs +253, intramonth Rs +251, random_hold Rs +119, snake_anaconda Rs +114, nifty_calls Rs +68, oracle Rs +40, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -175, gold Rs -319, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.