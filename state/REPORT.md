# Paper trading report

Updated 2026-11-11 12:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,639 | +10.32% | 0 | - | 237 |
| unified | 220,579 | +10.29% | 0 | - | 236 |
| snake_abs_exit_conv | 217,586 | +8.79% | 2 | 50% | 345 |
| snake_abs_exit | 216,497 | +8.25% | 2 | 50% | 345 |
| snake_abs | 214,084 | +7.04% | 1 | 100% | 255 |
| snake_abs_conv | 213,929 | +6.96% | 1 | 100% | 255 |
| intraweek | 213,631 | +6.82% | 30 | 53% | 3,302 |
| oracle | 212,045 | +6.02% | 0 | - | 233 |
| intramonth | 211,517 | +5.76% | 0 | - | 235 |
| random_hold | 206,909 | +3.46% | 9 | 67% | 709 |
| snake_anaconda | 204,388 | +2.19% | 3 | 33% | 374 |
| snake_viper_wild | 204,312 | +2.16% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| snake_viper_tick | 200,830 | +0.41% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,144 | -4.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,365 (-4.32%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +6,882 | +3.49% |
| snake_viper_tick | +6,753 | +3.48% |
| snake_abs_exit_conv | +5,677 | +2.68% |
| snake_anaconda | +4,922 | +2.47% |
| snake_abs_exit | +4,513 | +2.13% |
| snake_abs_conv | +4,452 | +2.12% |
| snake_abs | +4,437 | +2.12% |
| benchmark_smallcap | +3,285 | +1.66% |
| benchmark | +2,547 | +1.17% |
| oracle | +2,126 | +1.01% |
| random_hold | +1,949 | +0.95% |
| intramonth | +908 | +0.43% |
| unified | +832 | +0.38% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -910 | -0.42% |
| gold | -1,989 | -1.03% |

Average per day so far: benchmark Rs +666, unified Rs +664, snake_abs_exit_conv Rs +628, snake_abs_exit Rs +589, snake_abs_conv Rs +497, snake_abs Rs +486, intraweek Rs +440, oracle Rs +389, intramonth Rs +372, random_hold Rs +223, snake_viper_wild Rs +187, snake_anaconda Rs +169, nifty_calls Rs +59, benchmark_smallcap Rs +54, snake_viper_tick Rs +41, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -318, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.