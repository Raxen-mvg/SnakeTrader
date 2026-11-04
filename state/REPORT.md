# Paper trading report

Updated 2026-11-04 11:12 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,007 | +6.00% | 0 | - | 236 |
| snake_abs_exit_conv | 208,476 | +4.24% | 1 | 100% | 255 |
| snake_abs_exit | 208,341 | +4.17% | 1 | 100% | 260 |
| intraweek | 207,621 | +3.81% | 25 | 48% | 2,757 |
| benchmark | 207,558 | +3.78% | 0 | - | 237 |
| snake_viper_wild | 206,727 | +3.36% | 3 | 33% | 702 |
| snake_abs | 205,389 | +2.69% | 1 | 100% | 255 |
| snake_abs_conv | 205,235 | +2.62% | 1 | 100% | 255 |
| intramonth | 205,194 | +2.60% | 0 | - | 235 |
| snake_viper_tick | 203,125 | +1.56% | 2 | 0% | 532 |
| random_hold | 202,049 | +1.02% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,381 | +0.19% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,234 | -1.38% | 3 | 33% | 361 |
| benchmark_smallcap | 194,551 | -2.72% | 0 | - | 237 |
| gold | 188,993 | -5.50% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,381 (-5.81%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,326 | +2.12% |
| snake_abs_exit_conv | +4,138 | +2.02% |
| snake_abs_conv | +4,093 | +2.04% |
| snake_abs | +4,080 | +2.03% |
| gold | +3,715 | +2.00% |
| snake_anaconda | +3,410 | +1.76% |
| intraweek | +2,536 | +1.24% |
| benchmark_smallcap | +1,614 | +0.84% |
| random_hold | +1,580 | +0.79% |
| intramonth | +1,223 | +0.60% |
| benchmark | +857 | +0.41% |
| oracle | +391 | +0.20% |
| unified | +6 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,042 | -1.95% |
| snake_viper_wild | -4,165 | -1.98% |

Average per day so far: unified Rs +445, snake_viper_wild Rs +354, snake_abs_exit_conv Rs +353, snake_abs_exit Rs +348, intraweek Rs +282, benchmark Rs +280, snake_abs_conv Rs +218, snake_abs Rs +216, snake_viper_tick Rs +195, intramonth Rs +192, random_hold Rs +76, nifty_calls Rs +68, oracle Rs +14, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -126, benchmark_smallcap Rs -237, gold Rs -408, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.