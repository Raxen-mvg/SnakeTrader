# Paper trading report

Updated 2026-11-04 14:37 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,086 | +7.04% | 0 | - | 236 |
| snake_abs_exit_conv | 213,543 | +6.77% | 1 | 100% | 255 |
| snake_abs_exit | 213,425 | +6.71% | 1 | 100% | 260 |
| snake_abs | 210,428 | +5.21% | 1 | 100% | 255 |
| snake_abs_conv | 210,285 | +5.14% | 1 | 100% | 255 |
| intraweek | 209,346 | +4.67% | 25 | 48% | 2,757 |
| benchmark | 208,484 | +4.24% | 0 | - | 237 |
| snake_viper_wild | 208,165 | +4.08% | 3 | 33% | 702 |
| intramonth | 206,425 | +3.21% | 0 | - | 235 |
| snake_viper_tick | 204,547 | +2.27% | 2 | 0% | 532 |
| random_hold | 202,675 | +1.34% | 8 | 62% | 649 |
| snake_anaconda | 202,360 | +1.18% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,099 | +0.55% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,300 | -1.85% | 0 | - | 237 |
| gold | 191,229 | -4.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,669 (-5.17%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,411 | +4.61% |
| snake_abs_exit_conv | +9,204 | +4.50% |
| snake_abs_conv | +9,144 | +4.55% |
| snake_abs | +9,119 | +4.53% |
| snake_anaconda | +8,535 | +4.40% |
| gold | +5,951 | +3.21% |
| intraweek | +4,261 | +2.08% |
| benchmark_smallcap | +3,363 | +1.74% |
| intramonth | +2,454 | +1.20% |
| random_hold | +2,207 | +1.10% |
| unified | +2,085 | +0.98% |
| benchmark | +1,782 | +0.86% |
| oracle | +1,110 | +0.56% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,620 | -1.26% |
| snake_viper_wild | -2,728 | -1.29% |

Average per day so far: snake_abs_exit_conv Rs +564, snake_abs_exit Rs +559, unified Rs +522, snake_viper_wild Rs +430, snake_abs_conv Rs +429, snake_abs Rs +417, intraweek Rs +346, benchmark Rs +314, snake_viper_tick Rs +284, intramonth Rs +238, snake_anaconda Rs +107, random_hold Rs +99, nifty_calls Rs +68, oracle Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -161, gold Rs -325, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.