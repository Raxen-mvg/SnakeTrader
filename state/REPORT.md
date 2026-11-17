# Paper trading report

Updated 2026-11-17 10:28 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,949 | +10.97% | 0 | - | 236 |
| benchmark | 221,550 | +10.78% | 0 | - | 237 |
| snake_abs_exit | 215,592 | +7.80% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,172 | +7.09% | 2 | 50% | 345 |
| intraweek | 213,544 | +6.77% | 35 | 54% | 3,851 |
| oracle | 212,659 | +6.33% | 0 | - | 233 |
| intramonth | 211,986 | +5.99% | 0 | - | 235 |
| snake_abs | 210,526 | +5.26% | 1 | 100% | 255 |
| snake_abs_conv | 210,378 | +5.19% | 1 | 100% | 255 |
| random_hold | 208,280 | +4.14% | 10 | 70% | 733 |
| snake_viper_wild | 206,982 | +3.49% | 14 | 50% | 2,496 |
| snake_anaconda | 205,969 | +2.98% | 3 | 33% | 374 |
| snake_viper_tick | 203,443 | +1.72% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,107 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,513 | -9.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,475 (-4.26%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,278 | +1.08% |
| benchmark | +1,469 | +0.67% |
| benchmark_smallcap | +1,278 | +0.64% |
| snake_abs_exit | +1,182 | +0.55% |
| snake_abs_exit_conv | +955 | +0.45% |
| snake_anaconda | +866 | +0.42% |
| snake_viper_wild | +838 | +0.41% |
| snake_viper_tick | +823 | +0.41% |
| oracle | +636 | +0.30% |
| gold | +559 | +0.31% |
| unified | +512 | +0.23% |
| random_hold | +487 | +0.23% |
| snake_abs | +393 | +0.19% |
| snake_abs_conv | +388 | +0.18% |
| intramonth | +367 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +627, benchmark Rs +616, snake_abs_exit Rs +487, snake_abs_exit_conv Rs +443, intraweek Rs +387, oracle Rs +362, intramonth Rs +342, snake_abs_conv Rs +324, snake_abs Rs +319, snake_viper_wild Rs +259, random_hold Rs +237, snake_anaconda Rs +199, snake_viper_tick Rs +143, benchmark_smallcap Rs +68, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -528

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.