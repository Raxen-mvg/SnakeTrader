# Paper trading report

Updated 2026-11-04 13:19 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,170 | +7.08% | 0 | - | 236 |
| snake_abs_exit_conv | 212,905 | +6.45% | 1 | 100% | 255 |
| snake_abs_exit | 212,769 | +6.38% | 1 | 100% | 260 |
| snake_abs | 209,800 | +4.90% | 1 | 100% | 255 |
| snake_abs_conv | 209,646 | +4.82% | 1 | 100% | 255 |
| intraweek | 209,335 | +4.67% | 25 | 48% | 2,757 |
| benchmark | 208,047 | +4.02% | 0 | - | 237 |
| snake_viper_wild | 206,869 | +3.44% | 3 | 33% | 702 |
| intramonth | 206,444 | +3.22% | 0 | - | 235 |
| snake_viper_tick | 203,262 | +1.63% | 2 | 0% | 532 |
| random_hold | 202,576 | +1.29% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,270 | +0.64% | 3 | 33% | 361 |
| oracle | 201,234 | +0.62% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,392 | -2.30% | 0 | - | 237 |
| gold | 191,016 | -4.49% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,301 (-5.35%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,755 | +4.29% |
| snake_abs_exit_conv | +8,567 | +4.19% |
| snake_abs_conv | +8,505 | +4.23% |
| snake_abs | +8,491 | +4.22% |
| snake_anaconda | +7,446 | +3.84% |
| gold | +5,738 | +3.10% |
| intraweek | +4,250 | +2.07% |
| intramonth | +2,473 | +1.21% |
| benchmark_smallcap | +2,455 | +1.27% |
| unified | +2,169 | +1.02% |
| random_hold | +2,108 | +1.05% |
| benchmark | +1,346 | +0.65% |
| oracle | +1,245 | +0.62% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,905 | -1.89% |
| snake_viper_wild | -4,023 | -1.91% |

Average per day so far: snake_abs_exit_conv Rs +538, snake_abs_exit Rs +532, unified Rs +525, snake_abs_conv Rs +402, snake_abs Rs +392, snake_viper_wild Rs +362, intraweek Rs +346, benchmark Rs +298, intramonth Rs +239, snake_viper_tick Rs +204, random_hold Rs +95, nifty_calls Rs +68, snake_anaconda Rs +58, oracle Rs +46, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -200, gold Rs -333, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.