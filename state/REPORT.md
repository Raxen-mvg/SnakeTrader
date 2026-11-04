# Paper trading report

Updated 2026-11-04 14:55 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,139 | +7.07% | 0 | - | 236 |
| snake_abs_exit_conv | 213,548 | +6.77% | 1 | 100% | 255 |
| snake_abs_exit | 213,419 | +6.71% | 1 | 100% | 260 |
| snake_abs | 210,433 | +5.22% | 1 | 100% | 255 |
| snake_abs_conv | 210,289 | +5.14% | 1 | 100% | 255 |
| intraweek | 209,429 | +4.71% | 25 | 48% | 2,757 |
| benchmark | 208,675 | +4.34% | 0 | - | 237 |
| snake_viper_wild | 208,291 | +4.15% | 3 | 33% | 702 |
| intramonth | 206,606 | +3.30% | 0 | - | 235 |
| snake_viper_tick | 204,667 | +2.33% | 2 | 0% | 532 |
| random_hold | 202,719 | +1.36% | 8 | 62% | 649 |
| snake_anaconda | 202,241 | +1.12% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,132 | +0.57% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,423 | -1.79% | 0 | - | 237 |
| gold | 191,492 | -4.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,751 (-5.12%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,405 | +4.61% |
| snake_abs_exit_conv | +9,209 | +4.51% |
| snake_abs_conv | +9,148 | +4.55% |
| snake_abs | +9,124 | +4.53% |
| snake_anaconda | +8,416 | +4.34% |
| gold | +6,214 | +3.35% |
| intraweek | +4,344 | +2.12% |
| benchmark_smallcap | +3,486 | +1.81% |
| intramonth | +2,635 | +1.29% |
| random_hold | +2,250 | +1.12% |
| unified | +2,138 | +1.01% |
| benchmark | +1,974 | +0.95% |
| oracle | +1,142 | +0.57% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,499 | -1.21% |
| snake_viper_wild | -2,601 | -1.23% |

Average per day so far: snake_abs_exit_conv Rs +564, snake_abs_exit Rs +559, unified Rs +524, snake_viper_wild Rs +436, snake_abs_conv Rs +429, snake_abs Rs +417, intraweek Rs +349, benchmark Rs +321, snake_viper_tick Rs +292, intramonth Rs +245, snake_anaconda Rs +102, random_hold Rs +101, nifty_calls Rs +68, oracle Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -156, gold Rs -315, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.