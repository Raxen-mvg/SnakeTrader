# Paper trading report

Updated 2026-11-17 10:48 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,814 | +10.91% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| snake_abs_exit | 215,593 | +7.80% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,738 | +6.87% | 2 | 50% | 345 |
| intraweek | 213,638 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,363 | +6.18% | 0 | - | 233 |
| intramonth | 211,647 | +5.82% | 0 | - | 235 |
| snake_abs | 210,215 | +5.11% | 1 | 100% | 255 |
| snake_abs_conv | 210,065 | +5.03% | 1 | 100% | 255 |
| random_hold | 208,195 | +4.10% | 10 | 70% | 733 |
| snake_viper_wild | 207,034 | +3.52% | 14 | 50% | 2,496 |
| snake_anaconda | 205,691 | +2.85% | 3 | 33% | 374 |
| snake_viper_tick | 203,495 | +1.75% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,118 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,513 | -9.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,318 (-4.34%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,372 | +1.12% |
| benchmark | +1,446 | +0.66% |
| benchmark_smallcap | +1,289 | +0.64% |
| snake_abs_exit | +1,184 | +0.55% |
| snake_viper_wild | +890 | +0.43% |
| snake_viper_tick | +875 | +0.43% |
| snake_anaconda | +589 | +0.29% |
| gold | +559 | +0.31% |
| snake_abs_exit_conv | +521 | +0.24% |
| random_hold | +402 | +0.19% |
| unified | +376 | +0.17% |
| oracle | +340 | +0.16% |
| snake_abs | +81 | +0.04% |
| snake_abs_conv | +75 | +0.04% |
| intramonth | +28 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +623, benchmark Rs +615, snake_abs_exit Rs +487, snake_abs_exit_conv Rs +429, intraweek Rs +390, oracle Rs +353, intramonth Rs +333, snake_abs_conv Rs +315, snake_abs Rs +310, snake_viper_wild Rs +261, random_hold Rs +234, snake_anaconda Rs +190, snake_viper_tick Rs +146, benchmark_smallcap Rs +68, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -528

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.