# Paper trading report

Updated 2026-11-11 09:47 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,511 | +10.76% | 0 | - | 237 |
| unified | 220,215 | +10.11% | 0 | - | 236 |
| snake_abs_exit_conv | 216,312 | +8.16% | 2 | 50% | 345 |
| intraweek | 215,159 | +7.58% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,737 | +7.37% | 2 | 50% | 345 |
| snake_abs | 213,283 | +6.64% | 1 | 100% | 255 |
| snake_abs_conv | 213,123 | +6.56% | 1 | 100% | 255 |
| oracle | 211,289 | +5.64% | 0 | - | 233 |
| intramonth | 210,815 | +5.41% | 0 | - | 235 |
| random_hold | 206,035 | +3.02% | 9 | 67% | 709 |
| snake_anaconda | 202,892 | +1.45% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,289 | +0.64% | 0 | - | 237 |
| snake_viper_wild | 200,301 | +0.15% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,901 | -1.55% | 9 | 44% | 1,639 |
| gold | 189,141 | -5.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,218 (-4.39%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,403 | +2.08% |
| snake_abs_conv | +3,646 | +1.74% |
| snake_abs | +3,637 | +1.74% |
| snake_anaconda | +3,425 | +1.72% |
| benchmark | +3,420 | +1.57% |
| benchmark_smallcap | +3,116 | +1.57% |
| snake_viper_wild | +2,871 | +1.45% |
| snake_viper_tick | +2,824 | +1.46% |
| snake_abs_exit | +2,753 | +1.30% |
| oracle | +1,370 | +0.65% |
| random_hold | +1,075 | +0.52% |
| intraweek | +617 | +0.29% |
| unified | +468 | +0.21% |
| intramonth | +206 | +0.10% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,992 | -1.56% |

Average per day so far: benchmark Rs +694, unified Rs +652, snake_abs_exit_conv Rs +583, snake_abs_exit Rs +526, intraweek Rs +489, snake_abs_conv Rs +469, snake_abs Rs +458, oracle Rs +364, intramonth Rs +349, random_hold Rs +195, snake_anaconda Rs +111, nifty_calls Rs +59, benchmark_smallcap Rs +48, snake_viper_wild Rs +13, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -155, gold Rs -350, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.