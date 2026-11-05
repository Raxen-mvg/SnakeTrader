# Paper trading report

Updated 2026-11-05 09:32 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,592 | +8.80% | 0 | - | 236 |
| snake_abs_exit_conv | 216,202 | +8.10% | 1 | 100% | 255 |
| snake_abs_exit | 215,936 | +7.97% | 1 | 100% | 260 |
| snake_abs | 213,075 | +6.54% | 1 | 100% | 255 |
| snake_abs_conv | 212,925 | +6.46% | 1 | 100% | 255 |
| benchmark | 211,964 | +5.98% | 0 | - | 237 |
| intramonth | 209,978 | +4.99% | 0 | - | 235 |
| intraweek | 209,323 | +4.66% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,913 | +3.46% | 3 | 33% | 702 |
| random_hold | 205,190 | +2.60% | 8 | 62% | 649 |
| oracle | 203,990 | +2.00% | 0 | - | 233 |
| snake_viper_tick | 203,379 | +1.69% | 2 | 0% | 532 |
| snake_anaconda | 203,278 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,890 | -0.56% | 0 | - | 237 |
| gold | 195,487 | -2.26% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,509 (-4.75%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +4,094 | +2.14% |
| benchmark | +3,205 | +1.53% |
| unified | +3,153 | +1.47% |
| intramonth | +2,962 | +1.43% |
| benchmark_smallcap | +2,220 | +1.13% |
| oracle | +2,198 | +1.09% |
| random_hold | +1,882 | +0.93% |
| snake_abs_exit_conv | +1,187 | +0.55% |
| snake_abs | +1,172 | +0.55% |
| snake_abs_conv | +1,167 | +0.55% |
| snake_abs_exit | +1,035 | +0.48% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraweek | -375 | -0.18% |
| snake_anaconda | -542 | -0.27% |
| snake_viper_tick | -2,021 | -0.98% |
| snake_viper_wild | -2,117 | -1.01% |

Average per day so far: snake_abs_exit_conv Rs +648, snake_abs_exit Rs +637, unified Rs +628, snake_abs_conv Rs +517, snake_abs Rs +503, benchmark Rs +427, intramonth Rs +356, snake_viper_wild Rs +346, intraweek Rs +333, snake_viper_tick Rs +199, random_hold Rs +185, snake_anaconda Rs +143, oracle Rs +143, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -46, gold Rs -161, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.