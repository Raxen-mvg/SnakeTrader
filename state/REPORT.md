# Paper trading report

Updated 2026-11-05 15:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,529 | +7.76% | 0 | - | 236 |
| snake_abs_exit_conv | 214,531 | +7.26% | 1 | 100% | 255 |
| snake_abs_exit | 214,378 | +7.19% | 1 | 100% | 260 |
| benchmark | 214,022 | +7.01% | 0 | - | 237 |
| snake_abs | 211,417 | +5.71% | 1 | 100% | 255 |
| snake_abs_conv | 211,274 | +5.64% | 1 | 100% | 255 |
| intraweek | 208,479 | +4.24% | 25 | 48% | 2,757 |
| intramonth | 207,563 | +3.78% | 0 | - | 235 |
| snake_viper_wild | 204,413 | +2.21% | 3 | 33% | 702 |
| random_hold | 204,077 | +2.04% | 8 | 62% | 649 |
| oracle | 203,948 | +1.97% | 0 | - | 233 |
| snake_anaconda | 202,264 | +1.13% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,900 | +0.45% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,430 | -0.79% | 0 | - | 237 |
| gold | 194,271 | -2.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,050 (-5.48%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,263 | +2.52% |
| gold | +2,877 | +1.50% |
| oracle | +2,156 | +1.07% |
| benchmark_smallcap | +1,760 | +0.90% |
| unified | +1,089 | +0.51% |
| random_hold | +768 | +0.38% |
| intramonth | +547 | +0.26% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_conv | -484 | -0.23% |
| snake_abs_exit_conv | -484 | -0.23% |
| snake_abs | -486 | -0.23% |
| snake_abs_exit | -522 | -0.24% |
| intraweek | -1,219 | -0.58% |
| snake_anaconda | -1,556 | -0.76% |
| snake_viper_tick | -4,500 | -2.19% |
| snake_viper_wild | -4,617 | -2.21% |

Average per day so far: snake_abs_exit_conv Rs +581, snake_abs_exit Rs +575, unified Rs +555, benchmark Rs +501, snake_abs_conv Rs +451, snake_abs Rs +439, intraweek Rs +303, intramonth Rs +270, snake_viper_wild Rs +221, random_hold Rs +146, oracle Rs +141, snake_anaconda Rs +98, nifty_calls Rs +66, snake_viper_tick Rs +53, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -65, gold Rs -205, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.