# Paper trading report

Updated 2026-11-04 13:55 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,236 | +7.12% | 0 | - | 236 |
| snake_abs_exit_conv | 213,390 | +6.70% | 1 | 100% | 255 |
| snake_abs_exit | 213,238 | +6.62% | 1 | 100% | 260 |
| snake_abs | 210,290 | +5.14% | 1 | 100% | 255 |
| snake_abs_conv | 210,135 | +5.07% | 1 | 100% | 255 |
| intraweek | 209,234 | +4.62% | 25 | 48% | 2,757 |
| benchmark | 208,438 | +4.22% | 0 | - | 237 |
| snake_viper_wild | 206,922 | +3.46% | 3 | 33% | 702 |
| intramonth | 206,549 | +3.27% | 0 | - | 235 |
| snake_viper_tick | 203,311 | +1.66% | 2 | 0% | 532 |
| random_hold | 203,009 | +1.50% | 8 | 62% | 649 |
| snake_anaconda | 201,945 | +0.97% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,224 | +0.61% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,054 | -1.97% | 0 | - | 237 |
| gold | 191,229 | -4.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,335 (-5.33%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,223 | +4.52% |
| snake_abs_exit_conv | +9,052 | +4.43% |
| snake_abs_conv | +8,994 | +4.47% |
| snake_abs | +8,981 | +4.46% |
| snake_anaconda | +8,120 | +4.19% |
| gold | +5,951 | +3.21% |
| intraweek | +4,149 | +2.02% |
| benchmark_smallcap | +3,116 | +1.61% |
| intramonth | +2,578 | +1.26% |
| random_hold | +2,541 | +1.27% |
| unified | +2,235 | +1.05% |
| benchmark | +1,737 | +0.84% |
| oracle | +1,235 | +0.62% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,855 | -1.86% |
| snake_viper_wild | -3,971 | -1.88% |

Average per day so far: snake_abs_exit_conv Rs +558, snake_abs_exit Rs +552, unified Rs +527, snake_abs_conv Rs +422, snake_abs Rs +412, snake_viper_wild Rs +364, intraweek Rs +342, benchmark Rs +313, intramonth Rs +243, snake_viper_tick Rs +207, random_hold Rs +111, snake_anaconda Rs +88, nifty_calls Rs +68, oracle Rs +45, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -172, gold Rs -325, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.