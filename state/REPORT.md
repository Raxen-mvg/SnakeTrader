# Paper trading report

Updated 2026-11-04 14:43 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,149 | +7.08% | 0 | - | 236 |
| snake_abs_exit_conv | 213,711 | +6.86% | 1 | 100% | 255 |
| snake_abs_exit | 213,591 | +6.80% | 1 | 100% | 260 |
| snake_abs | 210,601 | +5.30% | 1 | 100% | 255 |
| snake_abs_conv | 210,456 | +5.23% | 1 | 100% | 255 |
| intraweek | 209,311 | +4.66% | 25 | 48% | 2,757 |
| benchmark | 208,422 | +4.21% | 0 | - | 237 |
| snake_viper_wild | 208,033 | +4.02% | 3 | 33% | 702 |
| intramonth | 206,577 | +3.29% | 0 | - | 235 |
| snake_viper_tick | 204,414 | +2.21% | 2 | 0% | 532 |
| random_hold | 202,715 | +1.36% | 8 | 62% | 649 |
| snake_anaconda | 202,550 | +1.27% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,093 | +0.55% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,289 | -1.86% | 0 | - | 237 |
| gold | 191,476 | -4.26% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,657 (-5.17%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,577 | +4.69% |
| snake_abs_exit_conv | +9,373 | +4.59% |
| snake_abs_conv | +9,315 | +4.63% |
| snake_abs | +9,292 | +4.62% |
| snake_anaconda | +8,726 | +4.50% |
| gold | +6,198 | +3.35% |
| intraweek | +4,225 | +2.06% |
| benchmark_smallcap | +3,352 | +1.74% |
| intramonth | +2,606 | +1.28% |
| random_hold | +2,247 | +1.12% |
| unified | +2,148 | +1.01% |
| benchmark | +1,721 | +0.83% |
| oracle | +1,104 | +0.55% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,753 | -1.33% |
| snake_viper_wild | -2,860 | -1.36% |

Average per day so far: snake_abs_exit_conv Rs +571, snake_abs_exit Rs +566, unified Rs +524, snake_abs_conv Rs +436, snake_abs Rs +424, snake_viper_wild Rs +423, intraweek Rs +345, benchmark Rs +312, snake_viper_tick Rs +276, intramonth Rs +244, snake_anaconda Rs +116, random_hold Rs +101, nifty_calls Rs +68, oracle Rs +40, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -161, gold Rs -316, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.