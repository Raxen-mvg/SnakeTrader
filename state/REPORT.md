# Paper trading report

Updated 2026-11-11 09:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,014 | +10.51% | 0 | - | 237 |
| unified | 220,591 | +10.29% | 0 | - | 236 |
| snake_abs_exit_conv | 216,417 | +8.21% | 2 | 50% | 345 |
| intraweek | 214,911 | +7.46% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,814 | +7.41% | 2 | 50% | 345 |
| snake_abs | 213,301 | +6.65% | 1 | 100% | 255 |
| snake_abs_conv | 213,142 | +6.57% | 1 | 100% | 255 |
| oracle | 211,400 | +5.70% | 0 | - | 233 |
| intramonth | 211,066 | +5.53% | 0 | - | 235 |
| random_hold | 206,097 | +3.05% | 9 | 67% | 709 |
| snake_anaconda | 202,973 | +1.49% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,367 | +0.68% | 0 | - | 237 |
| snake_viper_wild | 200,368 | +0.18% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,966 | -1.52% | 9 | 44% | 1,639 |
| gold | 189,191 | -5.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,297 (-4.35%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,509 | +2.13% |
| snake_abs_conv | +3,664 | +1.75% |
| snake_abs | +3,654 | +1.74% |
| snake_anaconda | +3,507 | +1.76% |
| benchmark_smallcap | +3,195 | +1.61% |
| snake_viper_wild | +2,938 | +1.49% |
| benchmark | +2,922 | +1.34% |
| snake_viper_tick | +2,889 | +1.49% |
| snake_abs_exit | +2,830 | +1.33% |
| oracle | +1,482 | +0.71% |
| random_hold | +1,137 | +0.56% |
| unified | +844 | +0.38% |
| intramonth | +457 | +0.22% |
| intraweek | +369 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,943 | -1.53% |

Average per day so far: benchmark Rs +678, unified Rs +664, snake_abs_exit_conv Rs +586, snake_abs_exit Rs +529, intraweek Rs +481, snake_abs_conv Rs +469, snake_abs Rs +459, oracle Rs +368, intramonth Rs +357, random_hold Rs +197, snake_anaconda Rs +114, nifty_calls Rs +59, benchmark_smallcap Rs +51, snake_viper_wild Rs +16, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -152, gold Rs -349, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.