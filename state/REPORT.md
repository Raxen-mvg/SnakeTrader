# Paper trading report

Updated 2026-11-05 13:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,490 | +8.74% | 0 | - | 236 |
| snake_abs_exit_conv | 214,511 | +7.25% | 1 | 100% | 255 |
| snake_abs_exit | 214,232 | +7.12% | 1 | 100% | 260 |
| benchmark | 213,839 | +6.92% | 0 | - | 237 |
| snake_abs | 211,382 | +5.69% | 1 | 100% | 255 |
| snake_abs_conv | 211,252 | +5.63% | 1 | 100% | 255 |
| intraweek | 210,749 | +5.37% | 25 | 48% | 2,757 |
| intramonth | 209,434 | +4.72% | 0 | - | 235 |
| snake_viper_wild | 207,416 | +3.71% | 3 | 33% | 702 |
| random_hold | 206,219 | +3.11% | 8 | 62% | 649 |
| oracle | 204,065 | +2.03% | 0 | - | 233 |
| snake_viper_tick | 203,851 | +1.93% | 2 | 0% | 532 |
| snake_anaconda | 202,641 | +1.32% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,159 | -0.42% | 0 | - | 237 |
| gold | 194,156 | -2.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,261 (-4.87%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,080 | +2.43% |
| unified | +3,050 | +1.42% |
| random_hold | +2,910 | +1.43% |
| gold | +2,762 | +1.44% |
| benchmark_smallcap | +2,489 | +1.26% |
| intramonth | +2,419 | +1.17% |
| oracle | +2,273 | +1.13% |
| intraweek | +1,051 | +0.50% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -504 | -0.23% |
| snake_abs_conv | -507 | -0.24% |
| snake_abs | -521 | -0.25% |
| snake_abs_exit | -668 | -0.31% |
| snake_anaconda | -1,179 | -0.58% |
| snake_viper_tick | -1,550 | -0.75% |
| snake_viper_wild | -1,613 | -0.77% |

Average per day so far: unified Rs +625, snake_abs_exit_conv Rs +580, snake_abs_exit Rs +569, benchmark Rs +494, snake_abs_conv Rs +450, snake_abs Rs +438, intraweek Rs +384, snake_viper_wild Rs +371, intramonth Rs +337, snake_viper_tick Rs +227, random_hold Rs +222, oracle Rs +145, snake_anaconda Rs +115, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -35, gold Rs -209, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.