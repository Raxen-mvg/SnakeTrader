# Paper trading report

Updated 2026-11-04 10:58 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,725 | +6.36% | 0 | - | 236 |
| snake_abs_exit_conv | 208,810 | +4.41% | 1 | 100% | 255 |
| snake_abs_exit | 208,667 | +4.33% | 1 | 100% | 260 |
| benchmark | 207,696 | +3.85% | 0 | - | 237 |
| intraweek | 207,474 | +3.74% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,891 | +3.45% | 3 | 33% | 702 |
| snake_abs | 205,715 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,564 | +2.78% | 1 | 100% | 255 |
| intramonth | 205,513 | +2.76% | 0 | - | 235 |
| snake_viper_tick | 203,285 | +1.64% | 2 | 0% | 532 |
| random_hold | 202,337 | +1.17% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,441 | +0.22% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,550 | -1.23% | 3 | 33% | 361 |
| benchmark_smallcap | 194,596 | -2.70% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| gold | 187,859 | -6.07% | 0 | - | 237 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,612 (-5.69%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,652 | +2.28% |
| snake_abs_exit_conv | +4,471 | +2.19% |
| snake_abs_conv | +4,423 | +2.20% |
| snake_abs | +4,406 | +2.19% |
| snake_anaconda | +3,725 | +1.92% |
| gold | +2,581 | +1.39% |
| intraweek | +2,389 | +1.17% |
| random_hold | +1,869 | +0.93% |
| benchmark_smallcap | +1,659 | +0.86% |
| intramonth | +1,542 | +0.76% |
| benchmark | +994 | +0.48% |
| unified | +724 | +0.34% |
| oracle | +452 | +0.23% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,881 | -1.87% |
| snake_viper_wild | -4,002 | -1.90% |

Average per day so far: unified Rs +471, snake_abs_exit_conv Rs +367, snake_viper_wild Rs +363, snake_abs_exit Rs +361, benchmark Rs +285, intraweek Rs +277, snake_abs_conv Rs +232, snake_abs Rs +229, snake_viper_tick Rs +205, intramonth Rs +204, random_hold Rs +87, nifty_calls Rs +68, oracle Rs +16, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -111, benchmark_smallcap Rs -235, snake_nonews Rs -444, gold Rs -450, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.