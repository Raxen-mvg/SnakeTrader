# Paper trading report

Updated 2026-11-04 15:01 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,436 | +7.22% | 0 | - | 236 |
| snake_abs_exit_conv | 213,661 | +6.83% | 1 | 100% | 255 |
| snake_abs_exit | 213,549 | +6.77% | 1 | 100% | 260 |
| snake_abs | 210,547 | +5.27% | 1 | 100% | 255 |
| snake_abs_conv | 210,402 | +5.20% | 1 | 100% | 255 |
| intraweek | 209,836 | +4.92% | 25 | 48% | 2,757 |
| benchmark | 208,713 | +4.36% | 0 | - | 237 |
| snake_viper_wild | 208,412 | +4.21% | 3 | 33% | 702 |
| intramonth | 206,936 | +3.47% | 0 | - | 235 |
| snake_viper_tick | 204,786 | +2.39% | 2 | 0% | 532 |
| random_hold | 202,988 | +1.49% | 8 | 62% | 649 |
| snake_anaconda | 202,346 | +1.17% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,474 | +0.74% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,513 | -1.74% | 0 | - | 237 |
| gold | 191,509 | -4.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,952 (-5.02%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,534 | +4.67% |
| snake_abs_exit_conv | +9,323 | +4.56% |
| snake_abs_conv | +9,261 | +4.60% |
| snake_abs | +9,238 | +4.59% |
| snake_anaconda | +8,522 | +4.40% |
| gold | +6,231 | +3.36% |
| intraweek | +4,751 | +2.32% |
| benchmark_smallcap | +3,576 | +1.85% |
| intramonth | +2,965 | +1.45% |
| random_hold | +2,520 | +1.26% |
| unified | +2,435 | +1.15% |
| benchmark | +2,012 | +0.97% |
| oracle | +1,484 | +0.74% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,380 | -1.15% |
| snake_viper_wild | -2,481 | -1.18% |

Average per day so far: snake_abs_exit_conv Rs +569, snake_abs_exit Rs +565, unified Rs +535, snake_viper_wild Rs +443, snake_abs_conv Rs +433, snake_abs Rs +422, intraweek Rs +364, benchmark Rs +323, snake_viper_tick Rs +299, intramonth Rs +257, random_hold Rs +111, snake_anaconda Rs +107, nifty_calls Rs +68, oracle Rs +55, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -152, gold Rs -314, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.