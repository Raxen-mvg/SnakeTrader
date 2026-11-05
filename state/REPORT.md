# Paper trading report

Updated 2026-11-05 13:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,470 | +8.73% | 0 | - | 236 |
| snake_abs_exit_conv | 213,764 | +6.88% | 1 | 100% | 255 |
| snake_abs_exit | 213,462 | +6.73% | 1 | 100% | 260 |
| benchmark | 213,119 | +6.56% | 0 | - | 237 |
| intraweek | 210,757 | +5.38% | 25 | 48% | 2,757 |
| snake_abs | 210,647 | +5.32% | 1 | 100% | 255 |
| snake_abs_conv | 210,513 | +5.26% | 1 | 100% | 255 |
| intramonth | 209,484 | +4.74% | 0 | - | 235 |
| snake_viper_wild | 206,414 | +3.21% | 3 | 33% | 702 |
| random_hold | 205,864 | +2.93% | 8 | 62% | 649 |
| oracle | 203,873 | +1.94% | 0 | - | 233 |
| snake_viper_tick | 202,866 | +1.43% | 2 | 0% | 532 |
| snake_anaconda | 201,970 | +0.98% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,091 | -0.45% | 0 | - | 237 |
| gold | 193,876 | -3.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,869 (-5.07%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,360 | +2.09% |
| unified | +3,031 | +1.41% |
| random_hold | +2,555 | +1.26% |
| gold | +2,482 | +1.30% |
| intramonth | +2,468 | +1.19% |
| benchmark_smallcap | +2,421 | +1.23% |
| oracle | +2,081 | +1.03% |
| intraweek | +1,060 | +0.51% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,245 | -0.59% |
| snake_abs_exit_conv | -1,251 | -0.58% |
| snake_abs | -1,256 | -0.59% |
| snake_abs_exit | -1,438 | -0.67% |
| snake_anaconda | -1,850 | -0.91% |
| snake_viper_tick | -2,535 | -1.23% |
| snake_viper_wild | -2,615 | -1.25% |

Average per day so far: unified Rs +624, snake_abs_exit_conv Rs +551, snake_abs_exit Rs +538, benchmark Rs +469, snake_abs_conv Rs +421, snake_abs Rs +410, intraweek Rs +384, intramonth Rs +339, snake_viper_wild Rs +321, random_hold Rs +209, snake_viper_tick Rs +169, oracle Rs +138, snake_anaconda Rs +86, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -38, gold Rs -219, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.