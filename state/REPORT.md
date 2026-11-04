# Paper trading report

Updated 2026-11-04 13:13 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,849 | +6.92% | 0 | - | 236 |
| snake_abs_exit_conv | 212,527 | +6.26% | 1 | 100% | 255 |
| snake_abs_exit | 212,355 | +6.18% | 1 | 100% | 260 |
| intraweek | 209,828 | +4.91% | 25 | 48% | 2,757 |
| snake_abs | 209,424 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,273 | +4.64% | 1 | 100% | 255 |
| benchmark | 207,925 | +3.96% | 0 | - | 237 |
| snake_viper_wild | 207,172 | +3.59% | 3 | 33% | 702 |
| intramonth | 206,061 | +3.03% | 0 | - | 235 |
| snake_viper_tick | 203,563 | +1.78% | 2 | 0% | 532 |
| random_hold | 202,654 | +1.33% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,132 | +0.57% | 0 | - | 233 |
| snake_anaconda | 201,083 | +0.54% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,168 | -2.42% | 0 | - | 237 |
| gold | 190,966 | -4.52% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,344 (-5.33%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,341 | +4.09% |
| snake_abs_exit_conv | +8,189 | +4.01% |
| snake_abs_conv | +8,132 | +4.04% |
| snake_abs | +8,115 | +4.03% |
| snake_anaconda | +7,259 | +3.75% |
| gold | +5,688 | +3.07% |
| intraweek | +4,743 | +2.31% |
| benchmark_smallcap | +2,231 | +1.16% |
| random_hold | +2,186 | +1.09% |
| intramonth | +2,090 | +1.02% |
| unified | +1,848 | +0.87% |
| benchmark | +1,224 | +0.59% |
| oracle | +1,143 | +0.57% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,603 | -1.74% |
| snake_viper_wild | -3,721 | -1.76% |

Average per day so far: snake_abs_exit_conv Rs +522, snake_abs_exit Rs +515, unified Rs +513, snake_abs_conv Rs +386, snake_viper_wild Rs +377, snake_abs Rs +377, intraweek Rs +364, benchmark Rs +294, intramonth Rs +224, snake_viper_tick Rs +223, random_hold Rs +98, nifty_calls Rs +68, snake_anaconda Rs +49, oracle Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -210, gold Rs -335, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.