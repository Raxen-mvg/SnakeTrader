# Paper trading report

Updated 2026-11-04 12:31 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,919 | +6.96% | 0 | - | 236 |
| snake_abs_exit_conv | 211,761 | +5.88% | 1 | 100% | 255 |
| snake_abs_exit | 211,596 | +5.80% | 1 | 100% | 260 |
| intraweek | 208,796 | +4.40% | 25 | 48% | 2,757 |
| snake_abs | 208,659 | +4.33% | 1 | 100% | 255 |
| snake_abs_conv | 208,505 | +4.25% | 1 | 100% | 255 |
| benchmark | 207,757 | +3.88% | 0 | - | 237 |
| snake_viper_wild | 207,037 | +3.52% | 3 | 33% | 702 |
| intramonth | 206,219 | +3.11% | 0 | - | 235 |
| snake_viper_tick | 203,429 | +1.71% | 2 | 0% | 532 |
| random_hold | 202,776 | +1.39% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,087 | +0.54% | 0 | - | 233 |
| snake_anaconda | 200,100 | +0.05% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 194,955 | -2.52% | 0 | - | 237 |
| gold | 190,884 | -4.56% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,196 (-5.40%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +7,582 | +3.72% |
| snake_abs_exit_conv | +7,422 | +3.63% |
| snake_abs_conv | +7,364 | +3.66% |
| snake_abs | +7,350 | +3.65% |
| snake_anaconda | +6,276 | +3.24% |
| gold | +5,606 | +3.03% |
| intraweek | +3,711 | +1.81% |
| random_hold | +2,308 | +1.15% |
| intramonth | +2,248 | +1.10% |
| benchmark_smallcap | +2,018 | +1.05% |
| unified | +1,918 | +0.91% |
| oracle | +1,097 | +0.55% |
| benchmark | +1,056 | +0.51% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,738 | -1.80% |
| snake_viper_wild | -3,856 | -1.83% |

Average per day so far: unified Rs +516, snake_abs_exit_conv Rs +490, snake_abs_exit Rs +483, snake_viper_wild Rs +370, snake_abs_conv Rs +354, snake_abs Rs +346, intraweek Rs +326, benchmark Rs +287, intramonth Rs +230, snake_viper_tick Rs +214, random_hold Rs +103, nifty_calls Rs +68, oracle Rs +40, snake_anaconda Rs +5, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -219, gold Rs -338, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.