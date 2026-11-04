# Paper trading report

Updated 2026-11-04 14:49 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,159 | +7.08% | 0 | - | 236 |
| snake_abs_exit_conv | 213,551 | +6.78% | 1 | 100% | 255 |
| snake_abs_exit | 213,442 | +6.72% | 1 | 100% | 260 |
| snake_abs | 210,436 | +5.22% | 1 | 100% | 255 |
| snake_abs_conv | 210,294 | +5.15% | 1 | 100% | 255 |
| intraweek | 209,384 | +4.69% | 25 | 48% | 2,757 |
| benchmark | 208,552 | +4.28% | 0 | - | 237 |
| snake_viper_wild | 208,372 | +4.19% | 3 | 33% | 702 |
| intramonth | 206,689 | +3.35% | 0 | - | 235 |
| snake_viper_tick | 204,748 | +2.37% | 2 | 0% | 532 |
| random_hold | 202,694 | +1.35% | 8 | 62% | 649 |
| snake_anaconda | 202,375 | +1.19% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,263 | +0.63% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,435 | -1.78% | 0 | - | 237 |
| gold | 191,509 | -4.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,783 (-5.11%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,428 | +4.62% |
| snake_abs_exit_conv | +9,213 | +4.51% |
| snake_abs_conv | +9,153 | +4.55% |
| snake_abs | +9,127 | +4.53% |
| snake_anaconda | +8,550 | +4.41% |
| gold | +6,231 | +3.36% |
| intraweek | +4,299 | +2.10% |
| benchmark_smallcap | +3,498 | +1.81% |
| intramonth | +2,718 | +1.33% |
| random_hold | +2,226 | +1.11% |
| unified | +2,158 | +1.02% |
| benchmark | +1,851 | +0.90% |
| oracle | +1,274 | +0.64% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,419 | -1.17% |
| snake_viper_wild | -2,521 | -1.20% |

Average per day so far: snake_abs_exit_conv Rs +565, snake_abs_exit Rs +560, unified Rs +524, snake_viper_wild Rs +441, snake_abs_conv Rs +429, snake_abs Rs +417, intraweek Rs +348, benchmark Rs +317, snake_viper_tick Rs +297, intramonth Rs +248, snake_anaconda Rs +108, random_hold Rs +100, nifty_calls Rs +68, oracle Rs +47, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -155, gold Rs -314, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.