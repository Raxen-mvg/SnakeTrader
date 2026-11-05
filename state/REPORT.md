# Paper trading report

Updated 2026-11-05 10:50 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,823 | +9.41% | 0 | - | 236 |
| snake_abs_exit_conv | 214,569 | +7.29% | 1 | 100% | 255 |
| snake_abs_exit | 214,265 | +7.13% | 1 | 100% | 260 |
| benchmark | 212,347 | +6.17% | 0 | - | 237 |
| snake_abs | 211,440 | +5.72% | 1 | 100% | 255 |
| snake_abs_conv | 211,307 | +5.65% | 1 | 100% | 255 |
| intraweek | 211,186 | +5.59% | 25 | 48% | 2,757 |
| intramonth | 210,595 | +5.30% | 0 | - | 235 |
| snake_viper_wild | 207,500 | +3.75% | 3 | 33% | 702 |
| random_hold | 207,050 | +3.52% | 8 | 62% | 649 |
| oracle | 204,528 | +2.26% | 0 | - | 233 |
| snake_viper_tick | 203,940 | +1.97% | 2 | 0% | 532 |
| snake_anaconda | 202,680 | +1.34% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,383 | -0.31% | 0 | - | 237 |
| gold | 194,632 | -2.68% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,598 (-4.70%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,384 | +2.04% |
| random_hold | +3,741 | +1.84% |
| benchmark | +3,588 | +1.72% |
| intramonth | +3,579 | +1.73% |
| gold | +3,239 | +1.69% |
| oracle | +2,736 | +1.36% |
| benchmark_smallcap | +2,713 | +1.38% |
| intraweek | +1,488 | +0.71% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -446 | -0.21% |
| snake_abs_conv | -451 | -0.21% |
| snake_abs | -464 | -0.22% |
| snake_abs_exit | -635 | -0.30% |
| snake_anaconda | -1,141 | -0.56% |
| snake_viper_tick | -1,460 | -0.71% |
| snake_viper_wild | -1,530 | -0.73% |

Average per day so far: unified Rs +672, snake_abs_exit_conv Rs +583, snake_abs_exit Rs +571, snake_abs_conv Rs +452, benchmark Rs +441, snake_abs Rs +440, intraweek Rs +399, intramonth Rs +378, snake_viper_wild Rs +375, random_hold Rs +252, snake_viper_tick Rs +232, oracle Rs +162, snake_anaconda Rs +117, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, gold Rs -192, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.