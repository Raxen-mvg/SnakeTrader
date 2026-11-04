# Paper trading report

Updated 2026-11-04 13:58 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,315 | +7.16% | 0 | - | 236 |
| snake_abs_exit_conv | 213,330 | +6.67% | 1 | 100% | 255 |
| snake_abs_exit | 213,177 | +6.59% | 1 | 100% | 260 |
| snake_abs | 210,222 | +5.11% | 1 | 100% | 255 |
| snake_abs_conv | 210,071 | +5.04% | 1 | 100% | 255 |
| intraweek | 209,421 | +4.71% | 25 | 48% | 2,757 |
| benchmark | 208,499 | +4.25% | 0 | - | 237 |
| snake_viper_wild | 207,015 | +3.51% | 3 | 33% | 702 |
| intramonth | 206,578 | +3.29% | 0 | - | 235 |
| snake_viper_tick | 203,403 | +1.70% | 2 | 0% | 532 |
| random_hold | 202,965 | +1.48% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,831 | +0.92% | 3 | 33% | 361 |
| oracle | 201,191 | +0.59% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,121 | -1.94% | 0 | - | 237 |
| gold | 191,131 | -4.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,409 (-5.30%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,163 | +4.49% |
| snake_abs_exit_conv | +8,991 | +4.40% |
| snake_abs_conv | +8,930 | +4.44% |
| snake_abs | +8,913 | +4.43% |
| snake_anaconda | +8,006 | +4.13% |
| gold | +5,853 | +3.16% |
| intraweek | +4,335 | +2.11% |
| benchmark_smallcap | +3,184 | +1.65% |
| intramonth | +2,607 | +1.28% |
| random_hold | +2,497 | +1.25% |
| unified | +2,314 | +1.09% |
| benchmark | +1,798 | +0.87% |
| oracle | +1,201 | +0.60% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,764 | -1.82% |
| snake_viper_wild | -3,878 | -1.84% |

Average per day so far: snake_abs_exit_conv Rs +555, snake_abs_exit Rs +549, unified Rs +530, snake_abs_conv Rs +420, snake_abs Rs +409, snake_viper_wild Rs +369, intraweek Rs +349, benchmark Rs +315, intramonth Rs +244, snake_viper_tick Rs +213, random_hold Rs +110, snake_anaconda Rs +83, nifty_calls Rs +68, oracle Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -169, gold Rs -328, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.