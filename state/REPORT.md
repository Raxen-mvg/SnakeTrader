# Paper trading report

Updated 2026-11-04 09:53 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,479 | +6.24% | 0 | - | 236 |
| benchmark | 208,736 | +4.37% | 0 | - | 237 |
| snake_abs_exit_conv | 208,461 | +4.23% | 1 | 100% | 255 |
| snake_abs_exit | 208,238 | +4.12% | 1 | 100% | 260 |
| intraweek | 207,975 | +3.99% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,840 | +3.42% | 3 | 33% | 702 |
| snake_abs | 205,368 | +2.68% | 1 | 100% | 255 |
| intramonth | 205,275 | +2.64% | 0 | - | 235 |
| snake_abs_conv | 205,220 | +2.61% | 1 | 100% | 255 |
| snake_viper_tick | 203,230 | +1.61% | 2 | 0% | 532 |
| random_hold | 203,144 | +1.57% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,011 | +0.01% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,398 | -1.30% | 3 | 33% | 361 |
| benchmark_smallcap | 194,260 | -2.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,152 | -6.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,593 (-5.70%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,224 | +2.07% |
| snake_abs_exit_conv | +4,122 | +2.02% |
| snake_abs_conv | +4,079 | +2.03% |
| snake_abs | +4,059 | +2.02% |
| snake_anaconda | +3,574 | +1.84% |
| intraweek | +2,889 | +1.41% |
| random_hold | +2,676 | +1.33% |
| benchmark | +2,035 | +0.98% |
| gold | +1,874 | +1.01% |
| benchmark_smallcap | +1,323 | +0.69% |
| intramonth | +1,304 | +0.64% |
| unified | +478 | +0.23% |
| oracle | +22 | +0.01% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,937 | -1.90% |
| snake_viper_wild | -4,053 | -1.92% |

Average per day so far: unified Rs +462, snake_viper_wild Rs +360, snake_abs_exit_conv Rs +353, snake_abs_exit Rs +343, benchmark Rs +324, intraweek Rs +295, snake_abs_conv Rs +217, snake_abs Rs +215, snake_viper_tick Rs +202, intramonth Rs +195, random_hold Rs +116, nifty_calls Rs +68, oracle Rs +0, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -118, benchmark_smallcap Rs -250, snake_nonews Rs -444, snake Rs -467, gold Rs -476

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.