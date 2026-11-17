# Paper trading report

Updated 2026-11-17 13:15 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,553 | +10.78% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| snake_abs_exit | 214,056 | +7.03% | 2 | 50% | 345 |
| intraweek | 213,900 | +6.95% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,411 | +6.21% | 2 | 50% | 345 |
| oracle | 212,041 | +6.02% | 0 | - | 233 |
| intramonth | 211,349 | +5.67% | 0 | - | 235 |
| snake_abs | 209,274 | +4.64% | 1 | 100% | 255 |
| snake_abs_conv | 209,133 | +4.57% | 1 | 100% | 255 |
| snake_viper_wild | 208,980 | +4.49% | 14 | 50% | 2,496 |
| random_hold | 207,477 | +3.74% | 10 | 70% | 733 |
| snake_viper_tick | 205,408 | +2.70% | 13 | 46% | 2,299 |
| snake_anaconda | 204,851 | +2.43% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,120 | +0.56% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,283 | -9.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,080 (-4.46%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +2,835 | +1.38% |
| snake_viper_tick | +2,788 | +1.38% |
| intraweek | +2,634 | +1.25% |
| benchmark | +1,446 | +0.66% |
| gold | +329 | +0.18% |
| benchmark_smallcap | +291 | +0.14% |
| unified | +115 | +0.05% |
| oracle | +18 | +0.01% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -252 | -0.12% |
| intramonth | -269 | -0.13% |
| random_hold | -316 | -0.15% |
| snake_abs_exit | -354 | -0.17% |
| snake_abs_exit_conv | -806 | -0.38% |
| snake_abs_conv | -857 | -0.41% |
| snake_abs | -860 | -0.41% |

Average per day so far: unified Rs +616, benchmark Rs +615, snake_abs_exit Rs +439, intraweek Rs +397, snake_abs_exit_conv Rs +388, oracle Rs +344, snake_viper_wild Rs +333, intramonth Rs +324, snake_abs_conv Rs +285, snake_abs Rs +281, snake_viper_tick Rs +225, random_hold Rs +214, snake_anaconda Rs +162, nifty_calls Rs +52, benchmark_smallcap Rs +36, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -535

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.